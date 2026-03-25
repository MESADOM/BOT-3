# TAREA 85 — TOPE DE PERDIDAS DISTINTO SEGUN EL REGIMEN (HILO INDEPENDIENTE)

> Documento unificado: este archivo consolida baseline, variantes 85a–85e y conclusiones finales de la tarea.

## 1) Lógica del estudio

Framework mantenido sin tocar entradas, señales base ni otras salidas.

Baseline de referencia:

- `FAVORABLE=-300`
- `MIXTO=-200`
- `PROBLEMATICO=-150`
- régimen fijo al de entrada (implementación actual)

Variantes comparadas:

- **85a:** `-350 / -200 / -150` (fijo entrada)
- **85b:** `-300 / -175 / -125` (fijo entrada)
- **85c:** `-350 / -225 / -150` (fijo entrada)
- **85d:** `-300 / -200 / -150` + reevaluación intratrade diaria
- **85e:** `-350 / -225 / -125` + reevaluación intratrade diaria

## 2) Resultado global por variante

| Variante | Capital final | Beneficio neto total | Δ vs baseline | Operaciones | DD máx global | Δ DD vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | `23.076,33 €` | `22.076,33 €` | `0,00 €` | `68` | `-28,4862%` | `0,0000 pp` |
| 85a | `23.076,33 €` | `22.076,33 €` | `0,00 €` | `68` | `-28,4862%` | `0,0000 pp` |
| 85b | `23.076,33 €` | `22.076,33 €` | `0,00 €` | `68` | `-28,4862%` | `0,0000 pp` |
| 85c | `23.076,33 €` | `22.076,33 €` | `0,00 €` | `68` | `-28,4862%` | `0,0000 pp` |
| 85d | `23.076,33 €` | `22.076,33 €` | `0,00 €` | `68` | `-28,4862%` | `0,0000 pp` |
| 85e | `22.816,33 €` | `21.816,33 €` | `-260,00 €` | `68` | `-28,4862%` | `0,0000 pp` |

## 3) Activaciones de stop escalonado

| Variante | Activaciones totales | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|---:|
| Baseline | `8` | `3` | `5` | `0` |
| 85a | `8` | `3` | `5` | `0` |
| 85b | `8` | `3` | `5` | `0` |
| 85c | `7` | `3` | `4` | `0` |
| 85d | `8` | `5` | `3` | `0` |
| 85e | `6` | `4` | `2` | `0` |

## 4) Impacto en años malos

En todas las variantes, los años negativos se mantienen en los mismos valores:

- `2015: -140,50 €`
- `2016: -170,00 €`
- `2026: -459,00 €`

No aparece mejora estructural en años malos.

## 5) Impacto en grandes ganadoras (>= 300 €)

En todas las variantes:

- número de ganadoras grandes: `18`
- suma de ganadoras grandes: `24.456,67 €`

No se destruyen las grandes ganadoras principales en `85a/85b/85c/85d`.
En `85e` tampoco cambia ese bloque agregado, pero sí empeora una pérdida intermedia concreta.

## 6) Peor operación individual vs baseline

La peor operación se mantiene idéntica en todas las variantes:

- `2025-11-27 -> 2025-12-16`
- `-855,00 €`
- motivo `STOP_ESCALONADO_REGIMEN`

No mejora el extremo de cola negativa.

## 7) Trades que cambian por variante

- **85a:** sin cambios.
- **85b:** sin cambios.
- **85c:** cambia solo la etiqueta del motivo en un trade (misma fecha y mismo PnL):
  - `2023-10-12 -> 2023-10-17`, `-112,50 €`, pasa de `STOP_ESCALONADO_REGIMEN` a `SELL_SIGNAL`.
- **85d:** sin cambios efectivos en trades ni PnL frente a baseline.
- **85e:** cambios reales en 1 trade (además de 2 cambios de motivo sin efecto monetario):
  - `2024-08-20 -> 2024-08-21`, `-162,00 €` (baseline)
  - pasa a `2024-08-20 -> 2024-08-28`, `-422,00 €`
  - impacto neto: `-260,00 €` en el resultado total.

## 8) Valor de la reevaluación intratrade

- **85d** (reevaluación con escala baseline) no aporta mejora alguna: mismo capital final, mismo DD y mismos trades efectivos.
- **85e** (reevaluación + escala más exigente) introduce complejidad y empeora el resultado (`-260 €`) sin mejorar DD ni años malos.

Conclusión sobre reevaluación:

- en esta muestra aporta **más complejidad que valor real**.

## 9) Conclusión operativa de la familia

- La familia 85 **no queda invalidada**, pero en esta ronda muestra **escaso margen de mejora**: casi todo empata con baseline.
- `85e` es claramente peor por deteriorar resultado sin compra de estabilidad.
- Si el objetivo es robustez y simplicidad, mantener baseline actual (`-300/-200/-150`, fijo entrada) sigue siendo la opción más defendible.
- Como hilo independiente, la familia puede quedar **viva en observación mínima**, pero no justifica expansión amplia inmediata sin nuevas hipótesis más específicas.
