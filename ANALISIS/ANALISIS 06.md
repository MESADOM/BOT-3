# ANALISIS 06

## 1. Título
Consolidación final del análisis 06 sobre clustering de trades short de la versión 2.2.1.

## 2. Objetivo del análisis
Reunir en un único archivo maestro los resultados ya generados para el análisis 06, sin rehacer el análisis desde cero, con foco en clasificar los trades `SHORT_TREND` en cuatro familias operativas: `Tendenciales`, `Laterales (whipsaw)`, `Rebotes` y `Falsas rupturas`.

## 3. Archivos fuente localizados
### Fuentes con resultados reales previos
- `VERSION 2.2.1 ANALISIS 06.md`: informe previo con la descripción de clusters, métricas y conclusión ya obtenidas.
- `analysis_short_clusters.py`: script usado previamente para construir el dataset de shorts, aplicar k-means simple (`k=4`) y escribir el informe previo.

### Fuentes de datos y soporte usadas por el análisis previo
- `META_BOT.py`: motor que genera las operaciones y expone los campos usados en el análisis short.
- `SORT.py`: lógica del módulo short de la versión 2.2.1.
- `datos/QQQ.csv`, `datos/QQQ3.csv`, `datos/VIX.csv`: series base consumidas por el motor.
- `VERSION 2.2.1 BASE SHORT.md`: documento base funcional de la versión short 2.2.1.

### Artefactos intermedios o auxiliares detectados
- No se localizaron `csv`, `figuras`, `logs` u otros outputs auxiliares persistidos específicamente por el análisis 06 dentro del repositorio.
- El script previo generaba un markdown de salida, pero no dejó otros artefactos persistentes en el árbol del repo.

## 4. Metodología realmente utilizada
Este archivo **no rehace** el análisis desde cero. Consolida lo ya producido por el análisis 06 anterior.

La metodología realmente utilizada en ese análisis fue:
- extracción de las operaciones `SHORT_TREND` generadas por `META_BOT.py`;
- construcción de variables por trade: `retorno_63`, `cruces_sma50_ventana`, duración en días, retorno bruto del short, excursión adversa máxima (MAE) y excursión favorable máxima (MFE);
- estandarización de variables con z-score;
- aplicación de clustering simple tipo k-means con `k=4` y semilla fija `42`;
- renombrado interpretativo de clusters según comportamiento observado para mapearlos a: `Tendenciales`, `Laterales (whipsaw)`, `Rebotes` y `Falsas rupturas`.

## 5. Resultados principales
Los resultados ya generados por el análisis 06 identificaron estos cuatro grupos:

### Tendenciales
- Capturan desplazamientos bajistas prolongados.
- Son los trades más rentables y con mayor excursión favorable.
- Operaciones incluidas: `2018-12-12`, `2022-04-13`, `2022-06-01`.

### Laterales (whipsaw)
- Presentan poco follow-through.
- El precio se mueve parcialmente a favor, pero sin desarrollar una tendencia bajista limpia.
- Operaciones incluidas: `2016-02-08`, `2022-03-03`, `2022-10-19`.

### Rebotes
- Corresponden a shorts castigados por un rebote en contra tras la entrada.
- Son el grupo más débil del análisis.
- Operaciones incluidas: `2022-07-07`, `2022-11-09`, `2025-04-15`.

### Falsas rupturas
- Son entradas bajistas muy breves que pierden continuidad y se invalidan rápido.
- Se asocian especialmente a cierres por pérdida de señal.
- Operaciones incluidas: `2016-03-02`, `2022-03-23`.

## 6. Métricas clave
| Cluster | N trades | Win rate % | Beneficio medio € | Beneficio total € | Retorno medio % | Días medios | MAE medio % | MFE medio % | retorno_63 medio | Cruces SMA50 medios |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Tendenciales | 3 | 100.0 | 1208.89 | 3626.68 | 27.77 | 26.33 | 4.36 | 34.96 | -0.1126 | 0.67 |
| Laterales (whipsaw) | 3 | 33.33 | 197.24 | 591.71 | 1.23 | 8.33 | 8.60 | 13.04 | -0.0978 | 0.00 |
| Rebotes | 3 | 33.33 | -271.00 | -813.00 | -6.59 | 6.67 | 9.78 | 8.19 | -0.1820 | 0.00 |
| Falsas rupturas | 2 | 100.0 | 61.44 | 122.88 | 1.49 | 1.00 | 0.46 | 3.44 | -0.0969 | 0.00 |

## 7. Patrones detectados
- **Mejor comportamiento:** los `Tendenciales` dominan claramente en beneficio medio, beneficio total y MFE.
- **Patrón de mayor fragilidad:** los `Rebotes` muestran la peor combinación de MAE elevado y beneficio medio negativo.
- **Whipsaw / lateralidad:** el grupo `Laterales (whipsaw)` tiene rentabilidad media casi plana y baja calidad de continuidad.
- **Invalidación rápida:** `Falsas rupturas` agrupa entradas muy cortas, normalmente con pérdida rápida de la tesis bajista y salidas tempranas.

## 8. Limitaciones o incidencias
- El análisis consolidado se apoya en resultados ya generados; no se recalculó el clustering en esta tarea porque la instrucción fue **no rehacer el análisis salvo necesidad imprescindible**.
- La muestra short consolidada es pequeña: `11` operaciones `SHORT_TREND`.
- No se localizaron figuras, logs ni csv específicos del análisis 06; por tanto, la consolidación depende del informe previo y del script que lo generó.
- Para cumplir la instrucción de dejar **un único archivo de salida**, los artefactos de salida previos del análisis 06 se eliminan del repositorio en esta actualización.

## 9. Conclusión final breve
El tipo de trade short que mejor funciona en la versión 2.2.1 es el **Tendencial**: combina la mayor rentabilidad media, la mayor excursión favorable y el mejor beneficio agregado. El tipo más débil es **Rebotes**, lo que sugiere que entrar short demasiado tarde, tras caídas ya extendidas, expone al sistema a recuperaciones bruscas en contra.

## 10. Lista completa de archivos generados o utilizados
### Archivo final generado
- `ANALISIS/ANALISIS 06.md`

### Archivos utilizados como fuente o referencia de consolidación
- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`
- `VERSION 2.2.1 BASE SHORT.md`
- `VERSION 2.2.1 ANALISIS 06.md` *(resultado previo consolidado y retirado como salida final en esta tarea)*
- `analysis_short_clusters.py` *(script previo consolidado y retirado como salida final en esta tarea)*
