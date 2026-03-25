# TAREA 82 — CIERRE FINAL

## 1) Objetivo de la iteración

Evaluar si la familia 82 de protección por devolución de beneficio puede mantenerse en una versión más selectiva, sin tocar entradas ni la estrategia base del sistema.

## 2) Variantes comparadas

Se compararon seis variantes:

- **82a**: MFE >= 300 y devolución >= 70%
- **82b**: MFE >= 400 y devolución >= 70%
- **82c**: MFE >= 500 y devolución >= 70%
- **82d**: MFE >= 300 y devolución >= 70% y ret20 < 0
- **82e**: MFE >= 400 y devolución >= 70% y ret20 < 0
- **82f**: MFE >= 500 y devolución >= 70% y ret20 < 0

## 3) Baseline de referencia

Referencia sin activar la familia 82:

- **Beneficio neto**: 21.965,83 €
- **Capital final**: 22.965,83 €
- **Drawdown máximo**: -28,4862 %
- **Años malos**: 2015 (-140,50 €), 2016 (-170,00 €), 2026 (-852,50 €)
- **Ganadoras grandes (>= 500 €)**: 15 operaciones, suma 23.546,89 €

## 4) Tabla comparativa de resultados

| Variante | Activaciones | Beneficio neto (€) | Capital final (€) | Drawdown máx (%) | Diferencia vs baseline (€) |
|---|---:|---:|---:|---:|---:|
| 82a | 10 | 17.961,15 | 18.961,15 | -28,4862 | -4.004,68 |
| 82b | 10 | 17.961,15 | 18.961,15 | -28,4862 | -4.004,68 |
| 82c | 7 | 19.935,83 | 20.935,83 | -28,4862 | -2.030,00 |
| 82d | 2 | 21.965,83 | 22.965,83 | -28,4862 | 0,00 |
| 82e | 2 | 21.965,83 | 22.965,83 | -28,4862 | 0,00 |
| 82f | 2 | 21.965,83 | 22.965,83 | -28,4862 | 0,00 |

## 5) Impacto en años malos

- **82a / 82b / 82c**:
  - 2015 y 2016 se mantienen igual que baseline.
  - 2026 mejora de -852,50 € a -459,00 €.
  - No hay mejora del drawdown máximo global.

- **82d / 82e / 82f**:
  - Años malos iguales al baseline.
  - Impacto práctico nulo en PnL agregado.

## 6) Impacto en ganadoras grandes

- Baseline: 15 ganadoras grandes, suma 23.546,89 €.
- 82a/82b: 14 ganadoras grandes, suma 18.954,36 €.
- 82c: 16 ganadoras grandes, suma 21.278,89 €.
- 82d/82e/82f: mismas ganadoras grandes que baseline.

Lectura: las variantes activas sin filtro adicional recortan parte del tramo de mayor edge del sistema.

## 7) Resumen de trades afectados

- **82a y 82b**:
  - Cambian 22 operaciones por efecto en cadena tras salidas tempranas.
  - Son las variantes más intrusivas.

- **82c**:
  - Cambia 8 operaciones.
  - Reduce algunas pérdidas puntuales, pero también recorta ganadoras estructurales importantes.

- **82d, 82e y 82f**:
  - Cambian solo 2 operaciones y en la práctica no alteran resultado agregado.
  - Su efecto operativo es casi equivalente a no tener esta familia activa.

## 8) Conclusión final

- **82a y 82b recortan demasiado edge y empeoran claramente el resultado agregado.**
- **82c es la mejor de las variantes sin filtro adicional, pero sigue siendo inferior al baseline en -2.030,00 €.**
- **82d, 82e y 82f son tan restrictivas que no alteran el resultado práctico; equivalen casi a no tener esta familia activa.**
- **Ninguna variante mejora el drawdown máximo global.**
- **La familia 82 no justifica continuidad en la versión principal del sistema.**

## 9) Veredicto operativo

Se **cierra la Tarea 82** con decisión de **no incorporar** esta familia en la versión principal.

Si se retoma en el futuro, debe ser únicamente en línea experimental separada, con criterios adicionales de contexto y validación fuera de la estrategia principal actual.
