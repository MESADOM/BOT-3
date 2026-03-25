# TAREA 81 — Estudio de variantes cerradas (81a, 81d, 81l)

## Baseline usado

Baseline actual del hilo (versión vigente):

- Activar protección si `max_ganancia_flotante_eur >= 300`
- Salir si `ganancia_flotante_eur <= 0`
- Motivo: `BREAK_EVEN_TRAS_300`

Métricas baseline:

- Beneficio neto total: **21,924.83 €**
- Drawdown máximo global: **-28.4862%**
- Salidas `BREAK_EVEN_TRAS_300`: **2**

---

## Variante 81a

Regla:

- Activar protección si `max_ganancia_flotante_eur >= 200`
- Salir si `ganancia_flotante_eur <= 0`

Resultados:

- Activaciones técnicas (operaciones que alcanzan umbral): **28**
- Salidas efectivas por break-even (`BREAK_EVEN_TRAS_300`): **1**
- Beneficio neto total: **21,718.53 €**
- Drawdown máximo global: **-28.4862%**
- Diferencia vs baseline:
  - Neto: **-206.30 €**
  - Drawdown: **0.0000 pp**
- Impacto en ganadoras grandes (>= 300 €): **4 trades afectados**, impacto agregado **-105.22 €**
- Operaciones perdedoras que pasan a no-pérdida: **1**

Trades que cambian:

- `2021-04-08` (LONG): `SELL_TRAILING` `-252.86 €` -> `BREAK_EVEN_TRAS_300` `+135.64 €`
- Ajustes de PnL (sin cambio de fecha/motivo) en:
  - `2021-06-23` (868.54 -> 842.16)
  - `2021-10-20` (539.88 -> 522.40)
  - `2021-12-20` (190.64 -> 184.62)
  - `2022-01-05` (-558.80 -> -539.60)
  - `2022-03-03` (707.71 -> 690.40)
  - `2022-03-23` (119.38 -> 116.49)
  - `2022-04-13` (2112.40 -> 2068.35)

Conclusión 81a:

- Mejora una perdedora concreta, pero erosiona múltiples tramos posteriores y termina peor que el baseline.

---

## Variante 81d

Regla:

- Activar protección si `max_ganancia_flotante_eur >= 300`
- Salir si `ganancia_flotante_eur <= 100`

Resultados:

- Activaciones técnicas (operaciones que alcanzan umbral): **29**
- Salidas efectivas por break-even (`BREAK_EVEN_TRAS_300`): **4**
- Beneficio neto total: **17,368.65 €**
- Drawdown máximo global: **-28.4862%**
- Diferencia vs baseline:
  - Neto: **-4,556.18 €**
  - Drawdown: **0.0000 pp**
- Impacto en ganadoras grandes (>= 300 €): **7 trades afectados**, impacto agregado **-7,070.96 €**
- Operaciones perdedoras que pasan a no-pérdida: **0**

Trades que cambian (más relevantes):

- `2020-11-25` (LONG): `SELL_TRAILING` `+1000.04 €` -> `BREAK_EVEN_TRAS_300` `+264.09 €`
- `2024-05-08` (LONG): `SELL_TRAILING` `+1723.50 €` -> `BREAK_EVEN_TRAS_300` `+397.50 €`
- `2025-05-14` (LONG): `SELL_TRAILING` `+4998.50 €` -> `BREAK_EVEN_TRAS_300` `+621.00 €`
- `2025-04-15` (SHORT): motivo cambia a `BREAK_EVEN_TRAS_300` con PnL igual (`-462.50 €`)

Conclusión 81d:

- Variante demasiado agresiva: protege antes de tiempo y recorta gran parte de los grandes ganadores; claramente dominada por el baseline.

---

## Variante 81l

Regla:

- Activar protección si `max_ganancia_flotante_eur >= 300`
- Salir si `ganancia_flotante_eur <= 0`
- Y además `ret20 < 0`

Resultados:

- Activaciones técnicas (operaciones que alcanzan umbral): **25**
- Salidas efectivas por break-even (`BREAK_EVEN_TRAS_300`): **1**
- Beneficio neto total: **21,965.83 €**
- Drawdown máximo global: **-28.4862%**
- Diferencia vs baseline:
  - Neto: **+41.00 €**
  - Drawdown: **0.0000 pp**
- Impacto en ganadoras grandes (>= 300 €): **0 trades afectados**
- Operaciones perdedoras que pasan a no-pérdida: **0**

Trades que cambian:

- `2025-11-27` (LONG): deja de salir por `BREAK_EVEN_TRAS_300` y vuelve a `SELL_SIGNAL` (`-855.00 €` -> `-420.50 €`)
- `2026-01-23` (LONG): mantiene `BREAK_EVEN_TRAS_300` pero con salida posterior (`-636.00 €` -> `-1029.50 €`)

Conclusión 81l:

- Es la única variante que mejora el neto frente al baseline (+41 €), sin deteriorar drawdown máximo y sin recortar grandes ganadoras.
- Si se quiere mantener la filosofía de la 81 pero con menos “falsos disparos”, **81l** es la mejor de las tres variantes cerradas analizadas.

---

## Conclusión final global

Entre las tres variantes cerradas:

- **81d**: descartable por sobre-recorte de ganancias grandes.
- **81a**: mejora puntual en una perdedora, pero neto final inferior.
- **81l**: mejor equilibrio en este histórico (mejora neta vs baseline, drawdown igual, sin dañar ganadoras grandes).

No se realizaron barridos amplios ni optimización libre: solo comparación directa de las tres variantes solicitadas contra baseline.
