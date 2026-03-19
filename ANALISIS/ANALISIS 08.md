# ANALISIS 08

## 1. Título

ANALISIS 08

## 2. Objetivo del análisis

Consolidar en un único archivo maestro los resultados ya generados por el análisis 08 sobre falsos negativos del módulo short, sin rehacer el análisis desde cero, dejando trazabilidad de fuentes, metodología realmente usada, resultados, métricas, patrones, limitaciones y conclusión final.

## 3. Archivos fuente localizados

### 3.1 Artefactos del análisis 08 localizados antes de consolidar

| Archivo | Tipo | Estado | Contenido útil | Decisión en la consolidación |
|---|---|---|---|---|
| `VERSION 2.2.1 ANALISIS 08.md` | markdown | localizado | Sí. Contenía el informe completo ya generado con casos, comparativa y conclusión. | Consolidado en este archivo maestro y eliminado como salida separada. |
| `analisis_08.py` | script | localizado | Sí. Documentaba la metodología realmente utilizada para generar el informe previo. | Usado como referencia metodológica y eliminado como salida separada. |

### 3.2 Archivos base del repositorio utilizados por el análisis

| Archivo | Rol real en el análisis |
|---|---|
| `META_BOT.py` | Motor principal usado para reconstruir operaciones, señales y métricas del sistema. |
| `SORT.py` | Lógica efectiva del módulo short, incluidos filtros de entrada y salida. |
| `LONG.py` | Contexto operativo de la pata long para comparar qué ocurría durante las caídas sin short. |
| `datos/QQQ.csv` | Serie de QQQ usada para detectar caídas relevantes y régimen de mercado. |
| `datos/QQQ3.csv` | Serie operativa del instrumento sobre el que se ejecutan las operaciones. |
| `datos/VIX.csv` | Dataset cargado por el motor base, aunque no fue la pieza decisiva de las conclusiones. |

### 3.3 Artefactos no encontrados para el análisis 08

No se localizaron archivos adicionales específicos del análisis 08 en formato `csv`, figuras, logs u outputs auxiliares persistidos en el repositorio. Por tanto, el análisis 08 previo quedó materializado de forma efectiva en un script (`analisis_08.py`) y un informe Markdown (`VERSION 2.2.1 ANALISIS 08.md`), que son los dos artefactos ahora consolidados aquí.

## 4. Metodología realmente utilizada

La metodología no se rehízo desde cero para esta consolidación; se tomó de los artefactos ya generados por el análisis 08.

Metodología usada originalmente:

1. Se ejecutó el motor del sistema para obtener `datos_base` y `operaciones`.
2. Se analizó el tramo común realmente operable con datos de QQQ3: del `2014-01-02` al `2026-03-03`.
3. Se definió como `caída relevante` cualquier drawdown pico-suelo de QQQ igual o peor que `-10%`.
4. Cada caída se clasificó como `falso negativo` cuando entre su pico y su suelo no existió ninguna operación real del módulo `SHORT_TREND`.
5. Para cada caso se revisaron las condiciones previas que el sistema sí había calculado: `senal_short_confirmada`, `meta_regimen`, `retorno_63`, `QQQ vs SMA200`, `SMA50 vs SMA200` y `cruces_sma50_ventana`.
6. Después se compararon los falsos negativos con los trades short reales para identificar qué filtros separaban una corrección rápida de una tendencia bajista ya confirmada.

## 5. Resultados principales

### 5.1 Resumen ejecutivo

- Se detectaron `12` caídas relevantes en el periodo analizado.
- De esas `12`, `9` fueron clasificadas como falsos negativos del módulo short.
- Solo `3` caídas relevantes tuvieron alguna operación short real superpuesta.
- El patrón dominante no fue ausencia de señal de debilidad, sino ausencia de activación final del short por filtros estructurales.

### 5.2 Lista consolidada de casos sin short

| Caso | Pico | Suelo | Caída | Días | Primera `senal_short_confirmada` | Primer `meta_regimen=SHORT_TREND` | Lectura resumida |
|---|---|---|---:|---:|---|---|---|
| 1 | 2015-07-20 | 2015-08-25 | -13.94% | 36 | 2015-08-19 | 2015-08-24 | El sistema detectó debilidad, pero no abrió short porque `SMA50` seguía por encima de `SMA200`. |
| 2 | 2018-01-26 | 2018-02-08 | -10.23% | 13 | 2018-02-05 | No apareció | Corrección rápida dentro de estructura alcista; QQQ siguió sobre `SMA200` y `retorno_63` no cayó lo suficiente. |
| 3 | 2018-03-12 | 2018-04-02 | -10.67% | 21 | 2018-03-22 | No apareció | Misma pauta: señal short táctica, pero sin deterioro estructural suficiente. |
| 4 | 2019-05-03 | 2019-06-03 | -10.98% | 31 | 2019-05-13 | No apareció | Debilidad parcial, pero sin `retorno_63 < -8%` ni cruce bajista `SMA50 < SMA200`. |
| 5 | 2020-02-19 | 2020-03-16 | -28.56% | 26 | 2020-02-25 | 2020-03-16 | Crash claro; aun así el short no llegó dentro de la caída porque `SMA50` no cruzó por debajo de `SMA200` antes del suelo. |
| 6 | 2020-09-02 | 2020-09-23 | -12.75% | 21 | 2020-09-11 | No apareció | Corrección fuerte, pero todavía con sesgo estructural alcista. |
| 7 | 2021-02-12 | 2021-03-08 | -10.85% | 24 | 2021-02-25 | No apareció | El sistema vio debilidad táctica, no cambio confirmado de tendencia. |
| 8 | 2024-07-10 | 2024-08-07 | -13.56% | 28 | 2024-07-24 | No apareció | Señal short de corto plazo, pero régimen global aún alcista. |
| 9 | 2025-02-19 | 2025-04-08 | -22.88% | 48 | 2025-02-24 | 2025-03-10 | El régimen short llegó a activarse tarde, pero siguió faltando el filtro `SMA50 < SMA200` durante la caída. |

### 5.3 Comparativa frente a los trades short reales

- Trades short reales detectados en el análisis previo: `11`.
- Beneficio neto agregado del módulo short: `3528.27 €`.
- Trades short ganadores: `7 de 11`.
- Los trades short reales se concentraron sobre todo en contextos bajistas ya maduros, especialmente `2018-12` y `2022`, no en correcciones rápidas de mercado alcista.

## 6. Métricas clave

| Métrica | Valor |
|---|---:|
| Periodo operativo analizado | 2014-01-02 a 2026-03-03 |
| Caídas relevantes detectadas | 12 |
| Falsos negativos detectados | 9 |
| Caídas relevantes con short real | 3 |
| Trades short reales | 11 |
| Trades short ganadores | 7 |
| Trades short perdedores | 4 |
| Beneficio neto agregado del módulo short | 3528.27 € |
| Mayor falso negativo por profundidad | 2020-02-19 -> 2020-03-16 (-28.56%) |
| Segundo falso negativo por profundidad | 2025-02-19 -> 2025-04-08 (-22.88%) |
| Filtro que más veces bloquea la entrada short | `SMA50 >= SMA200` |

## 7. Patrones detectados

1. **El sistema sí ve debilidad antes de muchas caídas, pero no necesariamente la convierte en trade.**  
   En la mayoría de falsos negativos apareció `senal_short_confirmada` antes o cerca del suelo.

2. **La barrera principal fue la confirmación estructural lenta.**  
   El patrón más repetido es la ausencia de `SMA50 < SMA200`, incluso cuando el precio ya estaba cayendo con fuerza.

3. **Las correcciones rápidas de mercados alcistas quedan fuera por diseño.**  
   En varios casos el sistema evitó ponerse corto porque QQQ aún seguía por encima de `SMA200` o porque `retorno_63` no confirmaba deterioro suficiente.

4. **Existe desacople entre `meta_regimen` y la entrada real del short.**  
   En 2015-08 y 2025-03/04 el `meta_regimen` sí llegó a marcar `SHORT_TREND`, pero el módulo short no entró porque seguía faltando `SMA50 < SMA200`.

5. **Los shorts que mejor funcionaron surgieron en bajadas ya asentadas.**  
   El short aportó valor sobre todo en entornos bajistas persistentes, no en caídas verticales de transición.

## 8. Limitaciones o incidencias

- Esta consolidación reutiliza resultados ya generados; no rehace la investigación original salvo la revisión documental necesaria para unificarlos.
- No se localizaron `csv`, figuras o logs específicos del análisis 08 como artefactos persistidos, por lo que el análisis previo dependía principalmente de un script y un informe Markdown.
- La cifra de `12` caídas relevantes y `9` falsos negativos depende de la definición concreta usada en el análisis previo: drawdown pico-suelo de `-10%` o peor sobre QQQ.
- La consolidación no introduce una nueva hipótesis cuantitativa; resume y ordena la evidencia ya obtenida.
- Para cumplir la instrucción de dejar un único archivo final de salida, los artefactos previos del análisis 08 se eliminan de la raíz del repositorio tras consolidar su contenido aquí.

## 9. Conclusión final breve

El análisis 08 concluye que el módulo short de la versión 2.2.1 falla más por **exceso de filtro estructural** que por falta de detección inicial de debilidad. El bloqueo dominante es `SMA50 < SMA200`: protege frente a cortos prematuros, pero deja fuera varias caídas relevantes, incluidas algunas muy profundas. En resumen, el sistema captura bien mercados bajistas ya confirmados, pero llega tarde o no entra en crashes y correcciones rápidas.

## 10. Lista completa de archivos generados o utilizados

### 10.1 Utilizados como fuente base

- `META_BOT.py`
- `SORT.py`
- `LONG.py`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`

### 10.2 Generados previamente por el análisis 08 y consolidados en este archivo

- `VERSION 2.2.1 ANALISIS 08.md` — consolidado y eliminado como salida separada.
- `analisis_08.py` — consolidado y eliminado como salida separada.

### 10.3 Archivo final entregable

- `/ANALISIS/ANALISIS 08.md`
