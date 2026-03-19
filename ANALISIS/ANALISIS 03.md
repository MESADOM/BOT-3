# ANALISIS 03

## 1. Título
Consolidado maestro del análisis short ganadores vs perdedores. Este archivo reúne los resultados ya generados previamente para el análisis **03**, pero se guarda con el nombre final solicitado: **`ANALISIS 03.md`**.

## 2. Objetivo del análisis
Consolidar en un único documento maestro los hallazgos ya obtenidos sobre la comparación entre trades **short ganadores** y **short perdedores**, sin rehacer el análisis desde cero. El foco del análisis fue estudiar qué ocurría **antes de la entrada** en variables como:
- `retorno_21`
- `retorno_63`
- `retorno_126`
- distancia a `SMA50`
- distancia a `SMA200`
- pendiente de medias
- volatilidad
- cruces recientes

## 3. Archivos fuente localizados
### Archivos con resultados reales del análisis previo
- `VERSION 2.2.1 ANALISIS 03.md` → contenía el resumen analítico ya generado, con tabla comparativa, detalle por trade y conclusión.

### Archivos auxiliares utilizados para producir esos resultados
- `short_analysis_v221.py` → script auxiliar usado para consolidar y calcular métricas del análisis previo.
- `META_BOT.py` → motor principal usado por el script para extraer `datos_base` y `operaciones`.
- `SORT.py` → lógica short utilizada por el motor.
- `LONG.py` → módulo long cargado por el motor, aunque no fue el foco del análisis.
- `VERSION 2.2.1 BASE SHORT.md` → documento base de reglas del módulo short 2.2.1.
- `datos/QQQ.csv` → serie base de QQQ para retornos, distancias a medias y cruces.
- `datos/QQQ3.csv` → activo operativo usado por el bot para entradas/salidas.
- `datos/VIX.csv` → dataset complementario cargado por el motor.

### Clasificación de lo localizado
**Resultados reales:**
- `VERSION 2.2.1 ANALISIS 03.md`

**Artefactos intermedios o auxiliares:**
- `short_analysis_v221.py`
- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `VERSION 2.2.1 BASE SHORT.md`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`

## 4. Metodología realmente utilizada
No se rehízo el análisis desde cero para esta consolidación. Se reutilizaron los resultados ya generados previamente y se resumieron aquí.

La metodología que se había usado para obtener esos resultados fue la siguiente:
1. Ejecutar el motor del sistema versión 2.2.1 para obtener `datos_base` y `operaciones`.
2. Filtrar exclusivamente operaciones `SHORT_TREND`.
3. Separar esas operaciones en dos grupos:
   - Ganadores
   - Perdedores
4. Tomar como referencia **el día de señal**, es decir, la sesión inmediatamente anterior a la fecha de entrada real, porque la ejecución ocurría en la apertura del día siguiente.
5. Calcular y comparar, para cada trade short, las variables previas a la entrada:
   - `retorno_21`
   - `retorno_63`
   - `retorno_126`
   - distancia a `SMA50`
   - distancia a `SMA200`
   - pendiente de `SMA50` a 5 días
   - pendiente de `SMA200` a 5 días
   - volatilidad 21d anualizada
   - cruces recientes respecto a `SMA50`
6. Resumir los grupos por medias y extraer las diferencias más visibles.

## 5. Resultados principales
### Muestra analizada
- Shorts analizados: **11**
- Ganadores: **7**
- Perdedores: **4**

### Tabla comparativa consolidada
| Variable | Ganadores (media) | Perdedores (media) | Diferencia |
|---|---:|---:|---:|
| Retorno 21d | -0.76% | -4.88% | 4.12% |
| Retorno 63d | -11.35% | -12.98% | 1.62% |
| Retorno 126d | -10.37% | -12.57% | 2.20% |
| Distancia a SMA50 | -2.51% | -7.02% | 4.50% |
| Distancia a SMA200 | -8.02% | -11.41% | 3.39% |
| Pendiente SMA50 (5d) | -1.04% | -1.50% | 0.45% |
| Pendiente SMA200 (5d) | -0.16% | -0.53% | 0.37% |
| Volatilidad 21d anualizada | 32.18% | 36.88% | -4.70% |
| Cruces SMA50 (20d) | 0.29 | 0.00 | 0.29 |
| Días desde último cruce SMA50 | 0.67 | n/a | n/a |

## 6. Métricas clave
Las variables con mayor diferencia práctica entre ganadores y perdedores fueron:
- **Volatilidad 21d anualizada**: ganadores 32.18% vs perdedores 36.88%.
- **Distancia a SMA50**: ganadores -2.51% vs perdedores -7.02%.
- **Distancia a SMA200**: ganadores -8.02% vs perdedores -11.41%.
- **Retorno 21d**: ganadores -0.76% vs perdedores -4.88%.
- **Retorno 63d**: ganadores -11.35% vs perdedores -12.98%.

## 7. Patrones detectados
A partir de los resultados previamente generados, los patrones observados fueron:
- Los shorts ganadores llegaron con **menor volatilidad previa** que los perdedores.
- Los ganadores tendieron a entrar con el precio **menos extendido a la baja** frente a `SMA50` y `SMA200`.
- En esta muestra, los peores shorts aparecieron con mayor frecuencia cuando el mercado ya venía **demasiado estirado** a la baja.
- El sesgo bajista de medio plazo estaba presente en ambos grupos, pero los ganadores no fueron los casos más extremos.
- Los cruces recientes de `SMA50` **no mostraron un patrón suficientemente limpio** como para considerarlos un filtro robusto en esta muestra concreta.

## 8. Limitaciones o incidencias
- La muestra es **pequeña**: solo 11 trades short.
- El análisis consolidado aquí corresponde al análisis previamente generado como **03**, y el archivo maestro final se nombra `ANALISIS 03.md` según la instrucción corregida.
- No se rehizo el análisis desde cero en esta tarea de consolidación.
- Parte de la trazabilidad original dependía de un script auxiliar (`short_analysis_v221.py`) y de un archivo intermedio de resultados (`VERSION 2.2.1 ANALISIS 03.md`), que se identificaron como artefactos previos de trabajo.
- No se localizaron figuras, logs ni outputs gráficos adicionales asociados al análisis 03.
- Si en el futuro se quiere máxima reproducibilidad, convendría conservar una copia del script en otra rama o reconstruirlo si vuelve a ser necesario.

## 9. Conclusión final breve
Sí aparecen patrones moderadamente claros: el short funcionó mejor cuando el contexto era bajista, pero **no** en los puntos más extremos de caída, separación respecto a medias y volatilidad. En esta muestra, vender demasiado tarde un tramo bajista ya muy acelerado empeoró el resultado.

## 10. Lista completa de archivos generados o utilizados
### Generado previamente y consolidado aquí
- `VERSION 2.2.1 ANALISIS 03.md` *(resultado previo; consolidado en este maestro)*

### Utilizados como soporte o fuente
- `short_analysis_v221.py`
- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `VERSION 2.2.1 BASE SHORT.md`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`

### Salida final deseada para esta tarea
- `ANALISIS/ANALISIS 03.md`

## Nota final de consolidación
Siguiendo tu instrucción, la salida final de esta tarea queda concentrada en un único archivo maestro: `ANALISIS/ANALISIS 03.md`. Los artefactos previos del análisis se consideran intermedios y no forman ya parte de la salida final deseada.
