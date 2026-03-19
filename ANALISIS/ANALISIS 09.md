# ANALISIS 09

## 1. Objetivo del análisis
Consolidar en un único archivo maestro los resultados ya generados para el análisis 09 sobre la versión 2.2.1, manteniendo la meta `LONG_SHORT` y sin rehacer el análisis salvo en lo imprescindible para identificar artefactos realmente utilizados frente a artefactos intermedios.

## 2. Archivos fuente localizados
### Artefactos con resultados reales o contenido fuente relevante
- `ANALISIS/ANALISIS 09.md`: archivo maestro final de consolidación.
- `VERSION 2.2.1 BASE SHORT.md`: documento base que define la configuración de referencia 2.2.1 usada como contexto del análisis.
- `META_BOT.py`: motor principal que ejecuta el backtest y del que salen las métricas agregadas.
- `SORT.py`: módulo short cuyos parámetros fueron sensibilizados en el análisis 09.
- `LONG.py`: módulo long, mantenido sin cambios finales, pero que sigue afectando los resultados totales al compartir la meta `LONG_SHORT`.
- `datos/QQQ.csv`: serie base de QQQ usada para señales, SMA y métricas de régimen.
- `datos/QQQ3.csv`: serie operativa de QQQ3 usada para entradas, salidas y trailing.
- `datos/VIX.csv`: dataset cargado por el motor en la ejecución del bot.

### Artefactos intermedios o no persistidos
- Script ad-hoc de consola usado en la tarea anterior para recorrer escenarios: **no se guardó como archivo dentro del repositorio**; existió solo como ejecución temporal.
- Salida estándar de `python META_BOT.py`: **no persistida** como log versionado.
- CSV de resultados generados (`datos/operaciones_generadas.csv`, `datos/resumen_anual_generado.csv`): **no presentes** en el repositorio porque `GUARDAR_RESULTADOS = False`.
- Figuras, imágenes o gráficos: **no existen** en este análisis.
- Logs adicionales u outputs auxiliares persistidos: **no localizados**.

## 3. Metodología realmente utilizada
La metodología realmente utilizada para el análisis 09 fue la siguiente:
1. Se tomó como base la configuración documentada de la versión 2.2.1 short.
2. Se ejecutó el motor del backtest para la base y para variaciones aisladas de cuatro palancas del módulo short:
   - confirmación 1 vs 2 días
   - umbral de `retorno_63`
   - umbral de `cruces_sma50`
   - trailing stop short 6% / 8% / 10%
3. No se cambió la meta del sistema: se mantuvo `LONG_SHORT`.
4. No se generaron ficheros de resultados persistentes; las métricas comparativas se consolidaron manualmente a partir de la salida obtenida en ejecución.
5. Para esta tarea de consolidación **no se rehízo el análisis desde cero**; solo se reutilizó el contenido ya generado y se reorganizó en este archivo maestro.

## 4. Resultados principales
| Escenario | Confirmación | `retorno_63` | `cruces_sma50` | Trailing short | Operaciones totales | Operaciones short | Beneficio neto € | Delta vs base € | Capital final € | Drawdown máx % | Win rate % | Beneficio short € |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base 2.2.1 | 1 día | -0.08 | `< 4` | 8% | 69 | 11 | 20,962.83 | 0.00 | 21,962.83 | -17.1120% | 56.52% | 3,528.27 |
| Confirmación 2 días | 2 días | -0.08 | `< 4` | 8% | 66 | 11 | 20,639.24 | -323.59 | 21,639.24 | -19.4757% | 53.03% | 3,489.63 |
| `retorno_63 < -0.04` | 1 día | -0.04 | `< 4` | 8% | 74 | 16 | 18,599.20 | -2,363.63 | 19,599.20 | -20.6751% | 54.05% | 2,218.16 |
| `retorno_63 < -0.12` | 1 día | -0.12 | `< 4` | 8% | 66 | 8 | 18,377.66 | -2,585.17 | 19,377.66 | -17.1120% | 54.55% | 1,218.02 |
| `cruces_sma50 < 3` | 1 día | -0.08 | `< 3` | 8% | 69 | 11 | 20,962.83 | 0.00 | 21,962.83 | -17.1120% | 56.52% | 3,528.27 |
| `cruces_sma50 < 2` | 1 día | -0.08 | `< 2` | 8% | 69 | 11 | 19,833.93 | -1,128.90 | 20,833.93 | -17.1120% | 56.52% | 2,399.37 |
| Trailing short 6% | 1 día | -0.08 | `< 4` | 6% | 69 | 11 | 20,807.83 | -155.00 | 21,807.83 | -17.1120% | 55.07% | 3,373.27 |
| Trailing short 10% | 1 día | -0.08 | `< 4` | 10% | 68 | 10 | 20,128.16 | -834.67 | 21,128.16 | -17.1120% | 55.88% | 2,944.08 |

## 5. Métricas clave
- Escenario base consolidado: **69 operaciones**, de las cuales **11** fueron short.
- Beneficio neto total base: **20,962.83 €**.
- Capital final base: **21,962.83 €**.
- Drawdown máximo base: **-17.1120%**.
- Win rate base: **56.52%**.
- Beneficio neto atribuido a operaciones short en la base: **3,528.27 €**.
- Mayor deterioro agregado frente a la base entre los escenarios comparados: `retorno_63 < -0.12` con **-2,585.17 €** de delta.
- Mayor deterioro de drawdown: `retorno_63 < -0.04` con **-20.6751%**.

## 6. Patrones detectados
- **Confirmación**: subir de 1 a 2 días reduce operaciones y beneficio, sin cambiar el conteo short en esta muestra.
- **`retorno_63`**: es la palanca más sensible de las comparadas; tanto relajar como endurecer el filtro reducen la calidad agregada frente a la base.
- **`cruces_sma50`**: pasar de `< 4` a `< 3` no cambia el resultado agregado; bajar a `< 2` sí reduce la contribución short aunque no cambia el número total de operaciones reportadas.
- **Trailing short**: el 8% quedó por encima de 6% y 10% en beneficio total y beneficio short dentro del histórico evaluado.
- **Meta sin cambios**: aunque el análisis toca reglas short, el resultado consolidado siempre refleja el sistema completo bajo `LONG_SHORT`, no un backtest short aislado.

## 7. Limitaciones o incidencias
- No existen scripts persistidos específicos del análisis 09 dentro del repositorio; la comparación de escenarios se obtuvo con una ejecución ad-hoc no guardada como archivo.
- No existen CSV de salida, logs persistidos ni figuras versionadas para este análisis.
- La consolidación actual depende de resultados ya generados en la tarea previa; por instrucción, no se rehízo el análisis completo desde cero.
- Solo hay un markdown final de salida dentro de una ruta estable; el markdown previo de trabajo fue eliminado para evitar dispersión documental.
- En la petición original de consolidación aparece una mezcla entre `01` y `XX`; para mantener consistencia con el análisis realmente realizado, este archivo se consolidó como **ANALISIS 09**.

## 8. Conclusión final breve
El análisis 09 ya generado muestra que, dentro del histórico evaluado y sin modificar la meta `LONG_SHORT`, la sensibilidad más acusada aparece en el umbral de `retorno_63`, mientras que confirmación y trailing producen deterioros más acotados y `cruces_sma50 < 3` no altera el agregado frente a la base. La evidencia consolidada queda reunida en este único archivo maestro, sin abrir una nueva ronda de análisis ni repartir la conclusión en otros documentos.

## 9. Lista completa de archivos generados o utilizados
### Generado como salida final consolidada
- `ANALISIS/ANALISIS 09.md`

### Utilizados como fuente o contexto
- `VERSION 2.2.1 BASE SHORT.md`
- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`

### Localizados como artefactos no persistidos o ausentes
- script temporal ad-hoc de comparación de escenarios (**no versionado**)
- logs de ejecución persistidos (**no localizados**)
- figuras (**no localizadas**)
- outputs CSV generados por el motor (**no presentes en el repositorio**)
