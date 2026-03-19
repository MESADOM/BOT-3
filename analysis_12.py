import math
import statistics
from dataclasses import dataclass
from typing import Callable, Dict, List, Any

import META_BOT
import SORT


@dataclass
class Variant:
    nombre: str
    regla: str
    objetivo: str
    key: str
    fn: Callable[[Dict[str, Any]], bool]


ORIG_PREPARAR = META_BOT.preparar_datos
ORIG_PERMITE = SORT.permite_entrada


def enrich_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    closes: List[float] = []
    for row in rows:
        close = row.get("qqq_close")
        if close is None:
            row["dist_sma50"] = None
            row["dist_sma200"] = None
            row["retorno_21_extra"] = None
            row["vol21_anual"] = None
            continue

        close = float(close)
        closes.append(close)
        idx = len(closes) - 1

        sma50 = row.get("sma50")
        sma200 = row.get("sma200_referencia")
        row["dist_sma50"] = None if sma50 in (None, 0) else close / float(sma50) - 1.0
        row["dist_sma200"] = None if sma200 in (None, 0) else close / float(sma200) - 1.0
        row["retorno_21_extra"] = None if idx < 21 else close / closes[idx - 21] - 1.0

        if idx < 21:
            row["vol21_anual"] = None
        else:
            rets = [closes[j] / closes[j - 1] - 1.0 for j in range(idx - 20, idx + 1) if j > 0]
            media = sum(rets) / len(rets)
            var = sum((r - media) ** 2 for r in rets) / (len(rets) - 1)
            row["vol21_anual"] = math.sqrt(var) * math.sqrt(252)

    return rows


def run_variant(variant: Variant) -> Dict[str, Any]:
    META_BOT.preparar_datos = lambda *a, **k: enrich_rows(ORIG_PREPARAR(*a, **k))

    def permite(hoy, ultima_fecha_salida_ejecutada, operaciones):
        return ORIG_PERMITE(hoy, ultima_fecha_salida_ejecutada, operaciones) and variant.fn(hoy)

    SORT.permite_entrada = permite
    resultado = META_BOT.ejecutar_bot()
    operaciones = resultado["operaciones"]
    rows = resultado["datos_base"]

    equity = META_BOT.CAPITAL_INICIAL_EUR
    peak = equity
    max_dd = 0.0
    trade_returns: List[float] = []

    for op in operaciones:
        equity = float(op["capital_acumulado_eur"])
        peak = max(peak, equity)
        max_dd = min(max_dd, equity / peak - 1.0)
        capital_antes = float(op.get("capital_antes_eur", 0.0) or 0.0)
        trade_returns.append(0.0 if capital_antes <= 0 else float(op["beneficio_neto_eur"]) / capital_antes)

    sharpe = 0.0
    if len(trade_returns) >= 2:
        sd = statistics.stdev(trade_returns)
        if sd > 0:
            sharpe = statistics.mean(trade_returns) / sd * math.sqrt(len(trade_returns))

    shorts = [op for op in operaciones if op["modulo_activo"] == META_BOT.REGIMEN_SHORT_TREND]
    gross_profit = sum(float(op["beneficio_neto_eur"]) for op in shorts if float(op["beneficio_neto_eur"]) > 0)
    gross_loss = -sum(float(op["beneficio_neto_eur"]) for op in shorts if float(op["beneficio_neto_eur"]) < 0)
    pf = gross_profit / gross_loss if gross_loss > 0 else float("inf")

    rows_by_date = {row["fecha"]: row for row in rows}
    capture_ratios = []
    short_details = []
    fechas = [row["fecha"] for row in rows]
    idx_by_fecha = {fecha: idx for idx, fecha in enumerate(fechas)}

    for op in shorts:
        i0 = idx_by_fecha[op["fecha_entrada"]]
        i1 = idx_by_fecha[op["fecha_salida"]]
        tramo = rows[i0:i1 + 1]
        lows = [float(r["qqq3_close"]) for r in tramo if r.get("qqq3_close") is not None]
        min_close = min(lows) if lows else float(op["precio_salida"])
        entry = float(op["precio_entrada"])
        exit_ = float(op["precio_salida"])
        favorable = max(0.0, (entry - min_close) / entry)
        realized = (entry - exit_) / entry
        capture = None if favorable <= 0 else realized / favorable
        if capture is not None and math.isfinite(capture):
            capture_ratios.append(capture)

        sig_idx = i0 - 1
        sig = rows[sig_idx] if sig_idx >= 0 else rows_by_date[op["fecha_entrada"]]
        short_details.append(
            {
                "fecha_entrada": op["fecha_entrada"].strftime("%Y-%m-%d"),
                "beneficio_neto_eur": float(op["beneficio_neto_eur"]),
                "dist_sma50": sig.get("dist_sma50"),
                "dist_sma200": sig.get("dist_sma200"),
                "retorno_21": sig.get("retorno_21_extra"),
                "vol21": sig.get("vol21_anual"),
                "capture_ratio": capture,
            }
        )

    return {
        "variant": variant.nombre,
        "key": variant.key,
        "rule": variant.regla,
        "objective": variant.objetivo,
        "total_return_pct": (sum(float(op["beneficio_neto_eur"]) for op in operaciones) / META_BOT.CAPITAL_INICIAL_EUR) * 100.0,
        "net_profit_eur": sum(float(op["beneficio_neto_eur"]) for op in operaciones),
        "max_drawdown_pct": max_dd * 100.0,
        "sharpe_trade": sharpe,
        "short_profit_factor": pf,
        "short_trades": len(shorts),
        "short_net_profit_eur": sum(float(op["beneficio_neto_eur"]) for op in shorts),
        "short_win_rate_pct": (sum(1 for op in shorts if float(op["beneficio_neto_eur"]) > 0) / len(shorts) * 100.0) if shorts else 0.0,
        "capture_ratio_mean": statistics.mean(capture_ratios) if capture_ratios else 0.0,
        "short_entry_dates": [d["fecha_entrada"] for d in short_details],
        "short_details": short_details,
    }


def main() -> None:
    variants = [
        Variant(
            nombre="Base 2.2.1",
            key="base",
            regla="Sin filtro anti-sobreextensión adicional; se usa la lógica short 2.2.1 tal como está.",
            objetivo="Punto de comparación.",
            fn=lambda hoy: True,
        ),
        Variant(
            nombre="Filtro A - distancia SMA50",
            key="dist_sma50",
            regla="Bloquear entrada short si la distancia de QQQ a SMA50 en el día de señal es <= -7%.",
            objetivo="Evitar shorts cuando el precio ya llega demasiado separado de la media corta.",
            fn=lambda hoy: hoy.get("dist_sma50") is None or hoy["dist_sma50"] > -0.07,
        ),
        Variant(
            nombre="Filtro B - distancia SMA200",
            key="dist_sma200",
            regla="Bloquear entrada short si la distancia de QQQ a SMA200 en el día de señal es <= -15%.",
            objetivo="Evitar ventas demasiado tarde dentro de mercados ya muy hundidos frente a la tendencia larga.",
            fn=lambda hoy: hoy.get("dist_sma200") is None or hoy["dist_sma200"] > -0.15,
        ),
        Variant(
            nombre="Filtro C - caída reciente 21d",
            key="ret21",
            regla="Bloquear entrada short si el retorno acumulado de 21 sesiones es <= -7%.",
            objetivo="Evitar entrar tras una caída mensual ya muy acelerada.",
            fn=lambda hoy: hoy.get("retorno_21_extra") is None or hoy["retorno_21_extra"] > -0.07,
        ),
        Variant(
            nombre="Filtro D - volatilidad previa",
            key="vol21",
            regla="Bloquear entrada short si la volatilidad realizada de 21 sesiones anualizada es >= 40%.",
            objetivo="Evitar entrar cuando el contexto previo ya es demasiado violento y propenso a rebotes.",
            fn=lambda hoy: hoy.get("vol21_anual") is None or hoy["vol21_anual"] < 0.40,
        ),
        Variant(
            nombre="Filtro E - combinación simple",
            key="combo",
            regla="Bloquear entrada short si dist. a SMA50 <= -7% o si vol. 21d anualizada >= 40%.",
            objetivo="Combinar una medida de extensión y otra de inestabilidad sin complicar demasiado la lógica.",
            fn=lambda hoy: (hoy.get("dist_sma50") is None or hoy["dist_sma50"] > -0.07) and (hoy.get("vol21_anual") is None or hoy["vol21_anual"] < 0.40),
        ),
    ]

    results = [run_variant(v) for v in variants]

    base = results[0]
    base_dates = set(base["short_entry_dates"])
    base_losers = {d["fecha_entrada"] for d in base["short_details"] if d["beneficio_neto_eur"] < 0}
    base_winners = {d["fecha_entrada"] for d in base["short_details"] if d["beneficio_neto_eur"] > 0}

    for result in results[1:]:
        result_dates = set(result["short_entry_dates"])
        result["removed_base_losers"] = sorted(base_losers - result_dates)
        result["removed_base_winners"] = sorted(base_winners - result_dates)

    for result in results:
        print("###", result["variant"])
        print(result["rule"])
        print({
            "retorno_total_pct": round(result["total_return_pct"], 2),
            "drawdown_pct": round(result["max_drawdown_pct"], 2),
            "sharpe_trade": round(result["sharpe_trade"], 3),
            "profit_factor_short": round(result["short_profit_factor"], 3),
            "short_trades": result["short_trades"],
            "capture_ratio_mean": round(result["capture_ratio_mean"], 3),
            "short_entry_dates": result["short_entry_dates"],
        })
        if result["key"] != "base":
            print({
                "removed_base_losers": result["removed_base_losers"],
                "removed_base_winners": result["removed_base_winners"],
            })
        print()

    META_BOT.preparar_datos = ORIG_PREPARAR
    SORT.permite_entrada = ORIG_PERMITE


if __name__ == "__main__":
    main()
