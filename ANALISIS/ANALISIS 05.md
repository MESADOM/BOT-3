# ANALISIS 05

## 1. Título
**VERSION 2.2.1 ANALISIS 05**

## 2. Objetivo del análisis
Consolidar en un único archivo maestro los resultados ya generados para el análisis 05, sin rehacer el análisis desde cero, documentando qué artefactos existían, cuáles aportaban resultados reales y cuál es la conclusión final sobre MAE/MFE y el trailing stop short del 8%.

## 3. Archivos fuente localizados
Se localizaron los siguientes artefactos vinculados al análisis 05 y a las fuentes necesarias para interpretarlo:

### Artefactos específicos del análisis 05
- `VERSION 2.2.1 ANALISIS 05.md` — **resultado real previo** con el informe entregado originalmente.
- `analisis_mae_mfe_short.py` — **artefacto intermedio/reproducible** usado para recalcular el análisis y regenerar el informe, pero no requerido como salida final consolidada.

### Código y datos de soporte usados por el análisis 05
- `META_BOT.py` — lógica del motor y acceso a datos utilizados por el script de análisis.
- `SORT.py` — módulo de soporte del régimen short usado por el proyecto.
- `LONG.py` — módulo complementario del proyecto incluido en la verificación sintáctica original.
- `datos/QQQ3.csv` — serie de precios de `QQQ3` utilizada para medir MAE/MFE intratrade.
- `datos/QQQ.csv` y `datos/VIX.csv` — datasets del repositorio disponibles como soporte del sistema, aunque no fueron el artefacto principal de cálculo del informe consolidado.

### Resultado de la localización por tipo
- **Scripts:** `analisis_mae_mfe_short.py`.
- **CSV:** `datos/QQQ3.csv`, `datos/QQQ.csv`, `datos/VIX.csv`.
- **Figuras:** no se localizaron figuras generadas para este análisis.
- **Markdown:** `VERSION 2.2.1 ANALISIS 05.md`.
- **Logs:** no se localizaron logs persistidos específicos del análisis 05.
- **Outputs auxiliares:** no se localizaron otros outputs persistidos aparte del markdown previo.

## 4. Metodología realmente utilizada
No se rehízo el análisis desde cero para esta consolidación. La metodología realmente utilizada fue la ya implementada y ejecutada en el artefacto previo:

1. Ejecutar `META_BOT.ejecutar_bot()` para obtener las operaciones del backtest.
2. Filtrar únicamente las operaciones short del régimen `REGIMEN_SHORT_TREND`.
3. Recorrer `datos/QQQ3.csv` dentro del intervalo de cada trade short.
4. Calcular para cada operación:
   - **MAE** como la excursión adversa máxima respecto al precio de entrada short.
   - **MFE** como la excursión favorable máxima respecto al precio de entrada short.
   - **PnL final** y **giveback desde MFE**.
5. Comparar los recorridos con el trailing stop short del **8%** y distinguir entre:
   - salidas reales por `COVER_TRAILING`, y
   - activación intradía teórica con mínimo acumulado + rebote del 8%.
6. Volcar los resultados en un markdown resumen.

Para esta tarea, únicamente se consolidó esa información en este archivo maestro y se eliminaron los artefactos redundantes de salida del análisis 05.

## 5. Resultados principales
- Se analizaron **11 trades short**.
- La distribución de **MAE** mostró una **media de 6.28%** y una **mediana de 4.42%**.
- La distribución de **MFE** mostró una **media de 15.95%** y una **mediana de 12.19%**.
- Hubo **9 de 11** salidas reales por `COVER_TRAILING`.
- **6 de 11** trades alcanzaron un **MFE igual o superior al 8%**.
- La activación intradía teórica del trailing del 8% se habría producido en **9 de 11** casos.
- El **PnL medio final** del bloque short fue **6.38%** y el **PnL mediano** fue **1.08%**.
- El **giveback medio desde el mejor MFE hasta la salida final** fue **9.56%**.

## 6. Métricas clave

### Distribución MAE
| Métrica | Valor |
|---|---:|
| Mínimo | 0.00% |
| P25 | 4.06% |
| Mediana | 4.42% |
| P75 | 8.84% |
| P90 | 11.83% |
| Máximo | 14.52% |
| Media | 6.28% |

**Buckets MAE**
- 0-2%: **2** trades
- 2-4%: **1** trade
- 4-6%: **3** trades
- 6-8%: **2** trades
- >=8%: **3** trades

### Distribución MFE
| Métrica | Valor |
|---|---:|
| Mínimo | 2.40% |
| P25 | 5.17% |
| Mediana | 12.19% |
| P75 | 24.63% |
| P90 | 32.99% |
| Máximo | 42.80% |
| Media | 15.95% |

**Buckets MFE**
- 0-2%: **0** trades
- 2-4%: **3** trades
- 4-6%: **0** trades
- 6-8%: **2** trades
- >=8%: **6** trades

### Evaluación del trailing actual (8%)
- Salidas reales por trailing: **9/11**.
- Trades cuyo MFE superó el 8%: **6/11**.
- Activación intradía teórica del trailing 8%: **9/11**.
- Trades con MAE >= 8%: **3/11**.
- PnL medio final del bloque short: **6.38%**.
- PnL mediano del bloque short: **1.08%**.
- Giveback medio desde MFE: **9.56%**.

## 7. Patrones detectados
- El bloque short presenta una **asimetría favorable**: el MFE medio (**15.95%**) supera ampliamente al MAE medio (**6.28%**).
- Aun así, el **giveback medio de 9.56%** indica que una porción relevante del recorrido favorable se devolvió antes del cierre.
- Los casos con peor MAE también muestran que el trailing actual **no evitó pérdidas relevantes** en algunos trades ya activados o próximos al umbral.
- La cercanía entre **9 salidas reales por trailing** y **9 activaciones intradía teóricas** sugiere que el trailing participa de forma importante en la gestión del bloque short, pero no necesariamente captura el tramo óptimo del movimiento.
- Los trades con MFE muy alto (por ejemplo, superiores al 20%) terminaron reteniendo beneficio, aunque con devoluciones todavía visibles frente al máximo favorable.

## 8. Limitaciones o incidencias
- Esta consolidación **no rehízo los cálculos**; resume y centraliza resultados previamente generados.
- No se localizaron **figuras** ni **logs persistidos** específicos del análisis 05.
- El archivo previo mezclaba resultado final y detalle operativo; en esta consolidación se dejó un único archivo maestro para evitar dispersión.
- La instrucción original menciona de forma inconsistente `ANALISIS 01.md` y `ANALISIS XX.md`; para resolver la corrección posterior de numeración, se consolidó el análisis en **`/ANALISIS/ANALISIS 05.md`**.
- Si en el futuro se exige trazabilidad completa de recálculo, sería necesario conservar o regenerar el script auxiliar; en esta entrega se priorizó la regla de dejar **un único archivo de salida** para el análisis.

## 9. Conclusión final breve
El trailing stop short del **8%** está razonablemente alineado con la dinámica favorable de los trades short analizados, pero su **eficiencia es mejorable** porque el sistema deja escapar una parte material del MFE antes de cerrar. En síntesis: el stop actual funciona como mecanismo de protección y salida frecuente, pero no maximiza de forma consistente la captura del recorrido favorable disponible.

## 10. Lista completa de archivos generados o utilizados

### Archivos utilizados como fuente o soporte
- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `datos/QQQ3.csv`
- `datos/QQQ.csv`
- `datos/VIX.csv`

### Archivos generados previamente y consolidados aquí
- `VERSION 2.2.1 ANALISIS 05.md` — consolidado y luego eliminado como salida separada.
- `analisis_mae_mfe_short.py` — artefacto auxiliar/intermedio, eliminado para cumplir la regla de un único archivo de salida del análisis.

### Archivo final entregable
- `/ANALISIS/ANALISIS 05.md`
