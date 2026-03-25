# TAREA 81 — Comparativa cerrada adicional (81m vs 81n) sobre núcleo 81l

## Contexto y objetivo

Se parte del consenso del hilo: **81l** es la mejor versión actual de la familia 81.
Este análisis compara **solo** dos variantes adicionales pedidas, sin barridos ni optimización libre:

- **81m**: activar `max_ganancia_flotante_eur >= 250`, salir `ganancia_flotante_eur <= 0`, y `ret20 < 0`.
- **81n**: activar `max_ganancia_flotante_eur >= 300`, salir `ganancia_flotante_eur <= 50`, y `ret20 < 0`.

Referencias:

- **Baseline actual**: regla 81 en producción (`>=300`, `<=0`, sin filtro `ret20`).
- **81l**: (`>=300`, `<=0`, y `ret20 < 0`).

## Métricas de referencia

- Baseline: neto **21,924.83 €**, drawdown máx **-28.4862%**, salidas efectivas BE **2**.
- 81l: neto **21,965.83 €**, drawdown máx **-28.4862%**, salidas efectivas BE **1**.

---

## Variante 81m

### Resultado principal

- Activaciones técnicas: **26**
- Salidas efectivas (`BREAK_EVEN_TRAS_300`): **1**
- Beneficio neto total: **21,965.83 €**
- Drawdown máximo global: **-28.4862%**

### Diferencias

- vs **81l**:
  - Neto: **0.00 €**
  - Drawdown: **0.0000 pp**
  - Trades cambiados: **ninguno**

- vs **baseline**:
  - Neto: **+41.00 €**
  - Drawdown: **0.0000 pp**
  - Trades que cambian (2):
    - `2025-11-27`: `BREAK_EVEN_TRAS_300` -> `SELL_SIGNAL` (`-855.00` -> `-420.50`)
    - `2026-01-23`: mantiene `BREAK_EVEN_TRAS_300`, salida posterior (`-636.00` -> `-1029.50`)

### Impactos solicitados

- Impacto en ganadoras grandes `>= 300 €`: **0 operaciones afectadas** (impacto total **0.00 €**)
- Perdedoras que pasan a no-pérdida: **0**

### Conclusión 81m

- No mejora ni empeora frente a 81l en este histórico.
- Se comporta como equivalente práctico de 81l para los trades observados.

---

## Variante 81n

### Resultado principal

- Activaciones técnicas: **25**
- Salidas efectivas (`BREAK_EVEN_TRAS_300`): **1**
- Beneficio neto total: **21,965.83 €**
- Drawdown máximo global: **-28.4862%**

### Diferencias

- vs **81l**:
  - Neto: **0.00 €**
  - Drawdown: **0.0000 pp**
  - Trades cambiados: **ninguno**

- vs **baseline**:
  - Neto: **+41.00 €**
  - Drawdown: **0.0000 pp**
  - Trades que cambian (2):
    - `2025-11-27`: `BREAK_EVEN_TRAS_300` -> `SELL_SIGNAL` (`-855.00` -> `-420.50`)
    - `2026-01-23`: mantiene `BREAK_EVEN_TRAS_300`, salida posterior (`-636.00` -> `-1029.50`)

### Impactos solicitados

- Impacto en ganadoras grandes `>= 300 €`: **0 operaciones afectadas** (impacto total **0.00 €**)
- Perdedoras que pasan a no-pérdida: **0**

### Conclusión 81n

- Tampoco aporta mejora adicional frente a 81l en este histórico.
- Queda en empate efectivo con 81l en neto, drawdown y trades.

---

## Conclusión final (objetivo del hilo)

Para confirmar si 81l ya es punto razonable o existe una mejora cercana y estable:

- **Sí: 81l ya parece un punto razonable.**
- Ni 81m ni 81n mejoran los resultados de 81l en este backtest.
- 81m/81n quedan como variantes equivalentes (sin ventaja observable) frente a 81l.
