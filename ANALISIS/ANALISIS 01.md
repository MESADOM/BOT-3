# ANALISIS 01

## 1. Objetivo del análisis
Consolidar en un único documento maestro los resultados ya generados para el análisis 01 de la versión 2.2.1, sin rehacer el backtest ni recalcular el estudio salvo lectura y verificación de los artefactos existentes.

## 2. Archivos fuente localizados

### 2.1 Scripts / lógica usada
- `analisis_regimen_221.py` — script que generó los CSV y el reporte original del análisis 01.
- `META_BOT.py` — motor del backtest 2.2.1 utilizado por el script para obtener `datos_base`, operaciones y resumen anual.
- `LONG.py` — lógica de entradas/salidas del módulo long.
- `SORT.py` — lógica de entradas/salidas del módulo short.

### 2.2 Resultados reales consolidados
- `ANALISIS/ANALISIS 01.md` — único entregable final conservado en el repositorio, autosuficiente y con todos los resultados relevantes volcados aquí.

### 2.3 Artefactos intermedios detectados en el trabajo previo
- `datos/resultados_2_2_1_regimen_resumen.csv` — usado anteriormente como resumen final por régimen.
- `datos/resultados_2_2_1_operaciones.csv` — usado anteriormente para agregar PnL, profit factor y contribución long/short.
- `datos/resultados_2_2_1_resumen_anual.csv` — usado anteriormente como resumen anual exportado.
- `datos/resultados_2_2_1_base.csv` — usado anteriormente como serie diaria auxiliar de clasificación de régimen.
- `VERSION 2.2.1 ANALISIS 01.md` — usado anteriormente como reporte narrativo secundario.
- `analisis_regimen_221.py` — script auxiliar previo para generar esos artefactos.

### 2.4 Estado actual de esos artefactos auxiliares
- Todos los artefactos auxiliares anteriores fueron retirados como salida final para cumplir la nueva restricción: **el único archivo de salida que debe existir es `ANALISIS/ANALISIS 01.md`**.
- Figuras: no se localizaron imágenes, gráficos ni capturas asociados al análisis 01.
- Logs: no se localizaron logs persistidos del análisis 01.

## 3. Metodología realmente utilizada
La metodología consolidada aquí es la que ya quedó implementada y ejecutada en `analisis_regimen_221.py`:

1. Se ejecutó `META_BOT.ejecutar_bot()` para obtener la base diaria, las operaciones y el resumen anual.
2. En el trabajo previo se habían exportado artefactos CSV auxiliares; en esta versión se consolidan sus resultados dentro de este único markdown y ya no se conservan como salida final.
3. Cada fecha se clasificó como:
   - **ALCISTA**: `QQQ > SMA200` y `SMA50 > SMA200`
   - **BAJISTA**: `QQQ < SMA200` y `SMA50 < SMA200`
   - **LATERAL**: resto de casos
4. Las métricas de trades (`rentabilidad total`, `profit factor`, `nº trades` y `contribución long vs short`) se agregaron por **régimen de entrada** de cada operación.
5. El `% tiempo invertido` se calculó como **días con posición abierta dentro de un régimen / días totales de ese régimen**.
6. El `drawdown máximo` por régimen se calculó sobre la curva acumulada de resultados de los trades asignados a ese régimen.

## 4. Resultados principales
Los resultados finales ya generados y consolidados son los siguientes:

| Régimen | Días del régimen | Días invertido | % tiempo invertido | Nº trades | Rentabilidad total % | Drawdown máx % | Profit factor | Contribución long € | Contribución short € |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ALCISTA | 3223 | 1564 | 48.53 | 51 | 1323.56 | -27.39 | 4.84 | 13235.56 | 0.00 |
| BAJISTA | 428 | 96 | 22.43 | 13 | 374.33 | -16.55 | 4.66 | 215.00 | 3528.27 |
| LATERAL | 668 | 117 | 17.51 | 5 | 398.40 | -61.90 | 4.69 | 3984.00 | 0.00 |

## 5. Métricas clave
- **Mejor régimen por rentabilidad total**: `ALCISTA` con `1323.56%`.
- **Mejor drawdown relativo**: `BAJISTA` con `-16.55%`.
- **Peor drawdown**: `LATERAL` con `-61.90%`.
- **Mayor exposición**: `ALCISTA` con `48.53%` del tiempo de ese régimen.
- **Mayor aportación short**: `BAJISTA` con `3528.27 €`.
- **Distribución de trades**: 51 alcistas, 13 bajistas y 5 laterales.

## 6. Patrones detectados
- El grueso del rendimiento acumulado proviene de contextos **alcistas**, dominados por la pata long.
- La pata **short** solo aporta de forma material en régimen **bajista**.
- El régimen **lateral** genera pocos trades, pero concentra el drawdown relativo más severo del análisis.
- La exposición del sistema cae de forma clara fuera del régimen alcista.
- Incluso en régimen bajista existe una contribución residual long, señal de que algunas entradas se clasificaron bajistas por contexto de mercado aunque no todas las ganancias provinieron del módulo short.

## 7. Limitaciones o incidencias
- Este archivo **no rehace** el análisis: consolida exclusivamente artefactos ya generados por el análisis 01.
- No se localizaron figuras ni logs persistidos; por tanto, la trazabilidad visual y de ejecución depende de los CSV y markdown existentes.
- La atribución por régimen se hace por **régimen de entrada del trade**, de modo que un trade que atraviesa varios regímenes no reparte su PnL entre ellos.
- La muestra short sigue siendo relativamente pequeña frente a la long, por lo que la lectura del bloque bajista es más sensible a pocos trades.
- El `drawdown máximo` por régimen depende de la secuencia de trades atribuida a ese régimen, no de una curva mark-to-market diaria segmentada.

## 8. Conclusión final breve
El análisis 01 ya generado muestra que la versión 2.2.1 obtiene su mayor creación de valor en régimen alcista, que el short aporta de verdad en régimen bajista, y que el mayor foco de fragilidad aparece en fases laterales por su drawdown relativo. La consolidación queda completa con los artefactos existentes; no se detectaron piezas imprescindibles faltantes, salvo la ausencia de figuras y logs persistidos.

## 9. Lista completa de archivos generados o utilizados

### Entregable final conservado
- `/ANALISIS/ANALISIS 01.md`

### Artefactos auxiliares del trabajo previo (ya no conservados como salida)
- `/VERSION 2.2.1 ANALISIS 01.md`
- `/analisis_regimen_221.py`
- `/datos/resultados_2_2_1_base.csv`
- `/datos/resultados_2_2_1_operaciones.csv`
- `/datos/resultados_2_2_1_regimen_resumen.csv`
- `/datos/resultados_2_2_1_resumen_anual.csv`

### Archivos base utilizados para el análisis original
- `/META_BOT.py`
- `/LONG.py`
- `/SORT.py`
- `/datos/QQQ.csv`
- `/datos/QQQ3.csv`
- `/datos/VIX.csv`

## 10. Estado de completitud
La tarea solicitada queda completada porque existe el archivo maestro requerido en la ruta estable `/ANALISIS/ANALISIS 01.md`, y el resto de salidas auxiliares fueron retiradas para que este sea el único archivo final de salida.
