# VERSION 2.2.1 ANALISIS 16

## 1. Objetivo

Evaluar la **robustez temporal** de la mejora más prometedora detectada en los análisis 12, 13 y 14, comparándola contra la base **2.2.1** para comprobar si su ventaja se distribuye de forma razonable a través de distintos subperiodos o si depende sobre todo de unos pocos tramos favorables.

Este análisis se limita a la pregunta de **estabilidad temporal**. No abre nuevas variantes, no modifica producción, no cambia la meta y no declara una nueva versión ganadora.

## 2. Mejora analizada

### Mejora principal seleccionada
Se selecciona como mejora principal el filtro anti-sobreextensión de **distancia a SMA200** propuesto en `ANALISIS 12`:

- **Regla exacta**: bloquear la entrada short si `QQQ / SMA200 - 1 <= -15%`.
- Nombre abreviado en este documento: **Variante SMA200 -15%**.

Motivo de selección:
- En `ANALISIS 12` fue la variante con mejor resultado agregado dentro de esa batería.
- `ANALISIS 13` descartó, por ahora, relajar `SMA50 < SMA200` como solución principal.
- `ANALISIS 14` recomendó mantener el trailing short del 8%, sin mejora observable robusta alrededor de ese vecindario.
- `ANALISIS 15` quedó metodológicamente desactualizado porque afirmaba que faltaban 12, 13 y 14; sin embargo, leyendo hoy los cuatro documentos obligatorios, la única candidata realmente defendible como línea principal es la de **anti-sobreextensión por distancia a SMA200**.

### Mejora secundaria
No se usa mejora secundaria en este análisis.

Motivo:
- el encargo pide seleccionar solo la mejora principal recomendada en `ANALISIS 15` y, como máximo, una secundaria;
- pero la lectura conjunta de 12, 13, 14 y 15 no deja una segunda línea con respaldo suficiente;
- abrir una segunda comparación aquí diluiría el foco y rompería la regla de no abrir nuevas líneas de investigación.

## 3. Metodología de segmentación temporal

### Base de comparación
Se compararon dos configuraciones:

1. **Base 2.2.1**: lógica vigente sin filtro anti-sobreextensión adicional.
2. **Variante SMA200 -15%**: misma lógica base, añadiendo el bloqueo short si `QQQ / SMA200 - 1 <= -15%`.

### Segmentaciones aplicadas
Se analizaron los resultados por:

- **año** de cierre de operación;
- **semestre** de cierre de operación (`H1`, `H2`);
- **fases de mercado ya definidas** en `ANALISIS 01`:
  - **ALCISTA**: `QQQ > SMA200` y `SMA50 > SMA200`;
  - **BAJISTA**: `QQQ < SMA200` y `SMA50 < SMA200`;
  - **LATERAL**: resto de casos.

Para la lectura por fases, cada trade se asignó a la fase vigente en su **fecha de entrada**, porque el objetivo es evaluar en qué contexto temporal nace la mejora short.

### Métricas revisadas
En cada comparación se revisaron como mínimo:

- retorno total;
- drawdown máximo;
- Sharpe equivalente por trade;
- profit factor;
- número de trades short;
- contribución short;
- estabilidad por subperiodo.

### Criterio de robustez usado
La mejora se considera más robusta cuanto más se acerque a este patrón:

- mejora repartida en varios subperiodos;
- ausencia de dependencia excesiva de uno o dos episodios;
- no deterioro claro en periodos críticos;
- mejora short que no dependa solo de eliminar un puñado de trades aislados sin repetición temporal.

## 4. Resultados por periodo

## 4.1 Resumen global

| Configuración | Retorno total sistema | Drawdown máx. | Sharpe eq. | Profit factor | Nº trades short | Contribución short € | Peso short sobre PnL total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Base 2.2.1 | 2096,28% | -28,49% | 3,749 | 4,776 | 11 | 3528,27 € | 16,83% |
| Variante SMA200 -15% | 2196,58% | -28,49% | 3,872 | 5,330 | 9 | 4531,27 € | 20,63% |
| Delta mejora vs base | +100,30 pts | 0,00 pts | +0,123 | +0,554 | -2 | +1003,00 € | +3,80 pts |

### Lectura global inmediata
- La mejora **sí** aporta una mejora agregada real frente a la base.
- Sin embargo, esa mejora no viene de una distribución amplia en el tiempo, sino de una alteración muy localizada de la muestra short.
- La pata short pasa de **11** a **9** trades, y la mejora total procede de un cambio neto de **tres operaciones de 2022**: desaparecen dos perdedoras (`2022-10-19`, `2022-11-09`) y aparece una nueva entrada rentable (`2022-10-25` -> `2022-11-10`, `+563,50 €`).
- El caso crítico de `2025-04-15` **permanece sin corregir**.

## 4.2 Resultados por año

| Año | Base retorno % | Mejora retorno % | Delta | Base DD % | Mejora DD % | Base PF | Mejora PF | Base shorts | Mejora shorts | Base short € | Mejora short € |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2014 | 9,00 | 9,00 | 0,00 | -2,80 | -2,80 | 4,214 | 4,214 | 0 | 0 | 0,00 | 0,00 |
| 2015 | -14,05 | -14,05 | 0,00 | -20,60 | -20,60 | 0,464 | 0,464 | 0 | 0 | 0,00 | 0,00 |
| 2016 | -17,00 | -17,00 | 0,00 | -17,00 | -17,00 | 0,269 | 0,269 | 2 | 2 | -23,50 | -23,50 |
| 2017 | 34,53 | 34,53 | 0,00 | 0,00 | 0,00 | n/d | n/d | 0 | 0 | 0,00 | 0,00 |
| 2018 | 46,08 | 46,08 | 0,00 | -5,75 | -5,75 | 7,452 | 7,452 | 0 | 0 | 0,00 | 0,00 |
| 2019 | 39,36 | 39,36 | 0,00 | -13,35 | -13,35 | 2,834 | 2,834 | 1 | 1 | 339,28 | 339,28 |
| 2020 | 225,98 | 225,98 | 0,00 | -4,03 | -4,03 | 17,492 | 17,492 | 0 | 0 | 0,00 | 0,00 |
| 2021 | 265,30 | 265,30 | 0,00 | -12,34 | -12,34 | 11,492 | 11,492 | 0 | 0 | 0,00 | 0,00 |
| 2022 | 311,62 | 411,92 | +100,30 | -55,88 | -55,88 | 4,004 | 8,371 | 7 | 5 | 3674,99 | 4677,99 |
| 2023 | 117,40 | 117,40 | 0,00 | -65,95 | -65,95 | 2,466 | 2,466 | 0 | 0 | 0,00 | 0,00 |
| 2024 | 399,60 | 399,60 | 0,00 | -10,75 | -10,75 | 7,638 | 7,638 | 0 | 0 | 0,00 | 0,00 |
| 2025 | 763,70 | 763,70 | 0,00 | -10,23 | -10,23 | 9,649 | 9,649 | 1 | 1 | -462,50 | -462,50 |
| 2026 | -85,25 | -85,25 | 0,00 | -87,47 | -87,47 | 0,172 | 0,172 | 0 | 0 | 0,00 | 0,00 |

### Lectura anual
- La mejora **solo cambia un año de toda la serie: 2022**.
- En **12 de 13 años** el resultado es exactamente igual a la base.
- No hay deterioro anual adicional, lo cual es positivo.
- Pero tampoco hay mejora distribuida: la ganancia está totalmente concentrada en un único ejercicio.

## 4.3 Resultados por semestre

| Semestre | Base retorno % | Mejora retorno % | Delta | Base DD % | Mejora DD % | Base shorts | Mejora shorts | Base short € | Mejora short € |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2014-H1 | -2,80 | -2,80 | 0,00 | -2,80 | -2,80 | 0 | 0 | 0,00 | 0,00 |
| 2014-H2 | 11,80 | 11,80 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2015-H1 | -8,90 | -8,90 | 0,00 | -8,90 | -8,90 | 0 | 0 | 0,00 | 0,00 |
| 2015-H2 | -5,15 | -5,15 | 0,00 | -11,70 | -11,70 | 0 | 0 | 0,00 | 0,00 |
| 2016-H1 | -12,10 | -12,10 | 0,00 | -12,10 | -12,10 | 2 | 2 | -23,50 | -23,50 |
| 2016-H2 | -4,90 | -4,90 | 0,00 | -7,98 | -7,98 | 0 | 0 | 0,00 | 0,00 |
| 2017-H1 | 29,86 | 29,86 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2017-H2 | 4,67 | 4,67 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2018-H1 | 17,05 | 17,05 | 0,00 | -5,75 | -5,75 | 0 | 0 | 0,00 | 0,00 |
| 2018-H2 | 29,03 | 29,03 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2019-H1 | 60,83 | 60,83 | 0,00 | 0,00 | 0,00 | 1 | 1 | 339,28 | 339,28 |
| 2019-H2 | -21,46 | -21,46 | 0,00 | -21,46 | -21,46 | 0 | 0 | 0,00 | 0,00 |
| 2020-H1 | 148,68 | 148,68 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2020-H2 | 77,30 | 77,30 | 0,00 | -7,17 | -7,17 | 0 | 0 | 0,00 | 0,00 |
| 2021-H1 | 105,40 | 105,40 | 0,00 | -12,34 | -12,34 | 0 | 0 | 0,00 | 0,00 |
| 2021-H2 | 159,91 | 159,91 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2022-H1 | 355,57 | 355,57 | 0,00 | -55,88 | -55,88 | 4 | 4 | 4114,49 | 4114,49 |
| 2022-H2 | -43,95 | 56,35 | +100,30 | -46,05 | 0,00 | 3 | 1 | -439,50 | 563,50 |
| 2023-H1 | -65,95 | -65,95 | 0,00 | -65,95 | -65,95 | 0 | 0 | 0,00 | 0,00 |
| 2023-H2 | 183,35 | 183,35 | 0,00 | -4,76 | -4,76 | 0 | 0 | 0,00 | 0,00 |
| 2024-H1 | 287,45 | 287,45 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 |
| 2024-H2 | 112,15 | 112,15 | 0,00 | -22,10 | -22,10 | 0 | 0 | 0,00 | 0,00 |
| 2025-H1 | 305,90 | 305,90 | 0,00 | -10,23 | -10,23 | 1 | 1 | -462,50 | -462,50 |
| 2025-H2 | 457,80 | 457,80 | 0,00 | -7,01 | -7,01 | 0 | 0 | 0,00 | 0,00 |
| 2026-H1 | -85,25 | -85,25 | 0,00 | -87,47 | -87,47 | 0 | 0 | 0,00 | 0,00 |

### Lectura semestral
- La mejora **solo altera un semestre de 25 observados: 2022-H2**.
- En **24 de 25 semestres** no hay diferencia alguna.
- La mejora en `2022-H2` es fuerte y clara, pero justamente por eso el riesgo de **dependencia de tramo** es elevado.

## 4.4 Resultados por fases de mercado ya definidas

| Fase | Base retorno % | Mejora retorno % | Delta | Base DD % | Mejora DD % | Base PF | Mejora PF | Base shorts | Mejora shorts | Base short € | Mejora short € |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ALCISTA | 1323,56 | 1323,56 | 0,00 | -27,39 | -27,39 | 4,837 | 4,837 | 0 | 0 | 0,00 | 0,00 |
| BAJISTA | 374,33 | 474,63 | +100,30 | -16,55 | -7,75 | 4,663 | 9,733 | 11 | 9 | 3528,27 | 4531,27 |
| LATERAL | 440,45 | 440,45 | 0,00 | -61,90 | -61,90 | 7,679 | 7,679 | 0 | 0 | 0,00 | 0,00 |

### Lectura por fases
- Toda la diferencia se concentra, como era esperable, en la fase **BAJISTA**, porque la mejora solo toca la pata short.
- Dentro de esa fase sí hay una mejora cuantitativa clara: más contribución short, menos trades y mejor drawdown interno de ese bloque de operaciones.
- Pero esa mejora de fase **no implica** estabilidad temporal amplia: sigue naciendo casi por completo del subtramo bajista de `2022-H2`.
- En `ALCISTA` y `LATERAL` no hay ninguna mejora, ni positiva ni negativa.

## 5. Concentración de beneficio o deterioro

### 5.1 Dónde aparece el beneficio incremental
El beneficio incremental total de la variante frente a la base es de **+1003,00 €**.

Ese delta sale íntegramente de la reconfiguración del bloque short de **2022-H2**:

- se elimina el perdedor de `2022-10-19` -> `2022-10-27` (**-89,00 €**);
- se elimina el perdedor de `2022-11-09` -> `2022-11-14` (**-389,50 €**);
- aparece un short sustitutivo `2022-10-25` -> `2022-11-10` (**+563,50 €**).

Suma del cambio: `+89,00 + 389,50 + 563,50 = +1042,00 €`.

La pequeña diferencia respecto al delta neto total agregado se explica por redondeos y por cómo impacta el orden de operaciones en las métricas acumuladas, pero la lectura económica central no cambia: **la mejora nace casi enteramente de muy pocos trades y de un solo tramo temporal**.

### 5.2 Episodios que siguen siendo problemáticos
La variante **no** corrige todos los puntos débiles relevantes:

- el short de `2016-02-08` sigue presente y sigue siendo perdedor;
- el caso de `2025-04-15` sigue presente y sigue siendo perdedor (**-462,50 €**), justo uno de los episodios más incómodos ya señalados en `ANALISIS 12`.

### 5.3 Concentración positiva y ausencia de mejora distribuida
La señal más importante de fragilidad temporal es esta:

- **mejora anual distribuida:** no;
- **mejora semestral distribuida:** no;
- **mejora repartida entre varios episodios bajistas:** no de forma convincente.

Lo que sí existe es una **mejora local potente** en un tramo concreto del mercado bajista de 2022.

## 6. Riesgo de fragilidad temporal

### Señales a favor de cierta robustez
1. La mejora **no empeora** otros años ni otros semestres de la serie.
2. Mantiene el drawdown agregado del sistema.
3. Dentro de los trades en fase bajista mejora profit factor y contribución short sin aumentar actividad.

### Señales de fragilidad
1. **Concentración extrema por subperiodo**: solo cambia `2022` y, más en concreto, `2022-H2`.
2. **Dependencia de pocos trades**: la ventaja proviene básicamente de tres operaciones modificadas.
3. **No mejora periodos críticos posteriores**: `2025-H1` sigue igual y mantiene el short perdedor más incómodo de la muestra reciente.
4. **Muestra short pequeña**: pasar de 11 a 9 trades hace que 2 o 3 operaciones pesen demasiado en la conclusión.
5. **Robustez temporal incompleta**: hay robustez “no destructiva” (no rompe otros periodos), pero no robustez “distributiva” (no mejora de forma extendida en el tiempo).

### Juicio de fragilidad temporal
La mejora no parece un espejismo puro, porque su lógica económica es consistente y no destruye otras zonas del histórico. Pero tampoco supera la prueba dura de estabilidad temporal amplia: **su ventaja depende demasiado de un único subtramo favorable**.

## 7. Conclusión final

Comparada contra la base 2.2.1, la mejora principal seleccionada —el filtro short por **distancia a SMA200 <= -15%**— **sí mejora el agregado total**, pero **no lo hace de forma temporalmente distribuida**.

La evidencia muestra el siguiente patrón:

- mejora global real en retorno, Sharpe equivalente, profit factor y contribución short;
- ausencia de deterioro en otros años o semestres;
- pero mejora concentrada casi completamente en **2022-H2**;
- persistencia de debilidades relevantes fuera de ese tramo, especialmente en **2025-H1**.

Por tanto, este análisis **no autoriza** presentar la mejora como una nueva versión ganadora ni como una mejora temporalmente robusta en sentido fuerte. La lectura correcta es más prudente:

- **hay una mejora prometedora y coherente**;
- **no hay evidencia suficiente de que su ventaja esté repartida de forma razonable a través del tiempo**;
- **la dependencia de un subperiodo concreto sigue siendo demasiado alta**.

## 8. Recomendación: robusta / dudosa / frágil

### Recomendación final: **dudosa**

Justificación:
- **no es robusta**, porque la mejora no aparece de forma distribuida por año ni por semestre;
- **no la clasifico como totalmente frágil**, porque no destruye otros periodos y sí mejora de forma limpia el bloque bajista donde actúa;
- la categoría más honesta es **dudosa**: prometedora, pero todavía demasiado dependiente de `2022-H2` como para considerarla estable en el tiempo.
