# TAREA 83 — ANÁLISIS UNIFICADO FINAL (RADIOGRAFÍA DE 15 OPERACIONES)

## Alcance

- Este documento **no cambia estrategia** ni propone variantes nuevas.
- Solo consolida la lectura de las 15 operaciones afectadas por `SALIDA_DINAMICA_TENDENCIA` en Tarea 83.
- Objetivo: decidir si la señal dinámica aporta mejora operativa directa o principalmente trazabilidad diagnóstica.
- **Este archivo es la versión unificada final del análisis de la Tarea 83.**

## Tabla de las 15 operaciones afectadas

| Entrada | Salida | Motivo baseline | Motivo con T83 | Beneficio neto final (€) | Resultado final | max_ganancia_flotante_eur | max_perdida_flotante_eur | Fecha señal dinámica | Flotante en señal (€) | Días señal→salida | Evolución tras señal |
|---|---|---|---|---:|---|---:|---:|---|---:|---:|---|
| 2014-02-27 | 2014-03-26 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -15.00 | Pérdida | 9.00 | -25.00 | 2014-03-24 | -25.00 | 2 | Mejora |
| 2014-11-05 | 2014-12-18 | SELL_TRAILING | SALIDA_DINAMICA_TENDENCIA | 8.50 | Ganancia | 60.00 | -18.50 | 2014-12-16 | -7.00 | 2 | Mejora |
| 2015-01-05 | 2015-01-07 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -23.50 | Pérdida | 2.50 | -7.00 | 2015-01-05 | -7.00 | 2 | Empeora |
| 2015-01-26 | 2015-01-29 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -51.50 | Pérdida | 2.00 | -45.50 | 2015-01-27 | -45.50 | 2 | Empeora |
| 2015-04-10 | 2015-04-21 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | 14.50 | Ganancia | 29.50 | -19.50 | 2015-04-17 | -19.50 | 4 | Mejora |
| 2015-05-20 | 2015-06-10 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -37.00 | Pérdida | 25.00 | -26.00 | 2015-06-08 | -26.00 | 2 | Empeora |
| 2015-06-24 | 2015-07-01 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -46.00 | Pérdida | 0.00 | -49.00 | 2015-06-29 | -49.00 | 2 | Empeora |
| 2016-03-23 | 2016-05-02 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -54.00 | Pérdida | 35.00 | -26.00 | 2016-04-28 | -9.50 | 4 | Empeora |
| 2016-09-27 | 2016-10-17 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -16.50 | Pérdida | 24.00 | -20.50 | 2016-10-13 | -20.50 | 4 | Mejora |
| 2018-04-19 | 2018-04-24 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -71.42 | Pérdida | 1.95 | -79.17 | 2018-04-20 | -79.17 | 4 | Mejora |
| 2022-01-05 | 2022-01-07 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -558.80 | Pérdida | -33.35 | -93.96 | 2022-01-05 | -93.96 | 2 | Empeora |
| 2023-03-08 | 2023-03-14 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -209.50 | Pérdida | 84.00 | -109.50 | 2023-03-10 | -109.50 | 4 | Empeora |
| 2023-10-12 | 2023-10-17 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -112.50 | Pérdida | 37.00 | -215.00 | 2023-10-13 | -215.00 | 4 | Mejora |
| 2026-01-05 | 2026-01-06 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | 177.00 | Ganancia | -150.50 | -150.50 | 2026-01-02 | -150.50 | 4 | Mejora |
| 2026-01-23 | 2026-02-05 | SELL_SIGNAL | SALIDA_DINAMICA_TENDENCIA | -1029.50 | Pérdida | 569.00 | -384.00 | 2026-02-03 | -384.00 | 2 | Empeora |

## Conclusiones de cierre (Tarea 83)

1. **Resultado final de las 15 operaciones:** 3 terminan en ganancia y 12 terminan en pérdida.
2. **Lectura principal:** la señal dinámica detecta mayoritariamente operaciones que acaban mal.
3. **Evolución posterior a la señal:** 8 trades empeoran y 7 trades mejoran antes del cierre efectivo.
4. **Antelación respecto al cierre:** la distancia observada es corta, entre **2 y 4 días** en esta muestra.
5. **Valor práctico de Tarea 83:** en este dataset, su contribución es sobre todo de **diagnóstico/trazabilidad** del deterioro durante el trade, más que de mejora operativa autónoma.

## Nota metodológica

- El documento consolida la comparación entre baseline y Tarea 83 sobre las mismas 15 operaciones afectadas.
- `max_ganancia_flotante_eur`, `max_perdida_flotante_eur` y el flotante en señal se reportan como PnL flotante de la posición LONG en euros durante la vida del trade.
