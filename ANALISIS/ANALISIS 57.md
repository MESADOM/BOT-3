# VERSION 2.2.2 ANALISIS 57

## 1. Objetivo

Etiquetar el histórico disponible con una **primera versión simple del selector de régimen** para comprobar si la clasificación resultante encaja de forma razonable con los años y tramos ya conocidos, sin usar todavía el selector para activar cambios operativos, sin tocar producción y sin forzar un ajuste manual año por año.

El propósito de este documento es estrictamente **descriptivo y de auditoría histórica**:

- generar etiquetas de régimen sobre el histórico disponible;
- medir cómo se reparten en el tiempo;
- comprobar si la taxonomía mínima `FAVORABLE / MIXTO / PROBLEMATICO` resulta creíble;
- detectar dónde la clasificación encaja bien y dónde todavía deja dudas.

Se deja `2026` únicamente como **caso de observación**, no como base de diseño.

---

## 2. Selector usado

### 2.1. Base documental usada

Se han leído obligatoriamente los análisis `50`, `51`, `52`, `53`, `54` y `55`.

Sin embargo, en el árbol actual del repositorio **no existe** `ANALISIS/ANALISIS 56.md`. Por tanto, no ha sido posible leer literalmente esa pieza. Para no inventar una especificación nueva, este documento toma como **mejor aproximación verificable** la primera especificación simple que ya queda respaldada por la cadena `50-55` y además por las variables de régimen ya calculadas en el sistema:

- `QQQ > SMA200`;
- `Retorno 63`;
- `Cruces SMA50`.

Esta inferencia es disciplinada por tres motivos:

1. `ANALISIS 50` fijó **3 meses / 63 sesiones** como lenguaje central más equilibrado para describir contexto.
2. `ANALISIS 51` dejó como bloque mínimo más natural las variables estructurales y de ruido ya visibles en el sistema.
3. `ANALISIS 54` fijó la taxonomía oficial mínima en tres clases: `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

### 2.2. Especificación simple empleada para etiquetar

Se usa una clasificación puramente histórica, no operativa, apoyada en el **score de régimen** ya derivable de esas tres variables:

- `+1` si `QQQ > SMA200`.
- `-1` si `QQQ < SMA200`.
- `+1` si `Retorno 63 > 0`.
- `-1` si `Retorno 63 < 0`.
- `-1` adicional si `Cruces SMA50` es alto.

Con ese score, la etiqueta histórica aplicada es:

- **FAVORABLE** si `score >= 2`.
- **MIXTO** si `score = 0 o 1`.
- **PROBLEMATICO** si `score <= -1`.

### 2.3. Qué significa esta lectura

Esta primera versión es deliberadamente austera:

- exige que `FAVORABLE` represente un contexto realmente limpio o claramente alineado;
- permite que muchas zonas intermedias caigan en `MIXTO` en vez de forzar un binario artificial;
- deja `PROBLEMATICO` para entornos con deterioro estructural o ruido/estrés suficientemente visible.

No se usa esta clasificación para activar reglas reales. Solo se audita si **describe bien el histórico**.

---

## 3. Metodología de etiquetado

### 3.1. Datos y horizonte

Se utilizó el histórico diario disponible de `QQQ`, con las variables de régimen calculadas de forma reproducible a partir del propio código del repositorio.

Como el selector requiere `SMA200` y `Retorno 63`, el etiquetado útil arranca cuando esas variables ya existen de forma completa. En la práctica, el análisis interpretable comienza en **2014** para la comparación principal por bloques.

### 3.2. Frecuencia de actualización

La lectura respeta la lógica simple ya presente en el sistema: el contexto se revisa en cadencia **semanal** y la etiqueta se mantiene entre revisiones, lo que evita una clasificación excesivamente nerviosa.

### 3.3. Métricas auditadas

Se revisaron como mínimo:

- proporción temporal global de cada clase;
- número de cambios de clase por año;
- distribución por año;
- distribución por subperiodos cuando hubo cambios dentro del mismo año;
- distribución agregada en `2020-2025`;
- distribución agregada en `2014-2019`;
- clasificación observada en `2026`;
- coherencia cualitativa con años ya conocidos.

### 3.4. Regla metodológica clave

No se hizo ningún ajuste manual para “hacer encajar” años concretos. Si un año sale ambiguo o poco convincente, se declara así explícitamente.

---

## 4. Etiquetado histórico obtenido

### 4.1. Proporción temporal global

Sobre el periodo etiquetable, la distribución temporal total queda así:

| Clase | Proporción temporal |
|---|---:|
| FAVORABLE | 57,6% |
| MIXTO | 27,7% |
| PROBLEMATICO | 14,7% |

Primera lectura:

- la clasificación **no** convierte casi todo en problemático;
- tampoco regala la etiqueta favorable a cualquier entorno dudoso;
- deja una zona intermedia material, lo cual parece sano para una taxonomía todavía simple.

### 4.2. Distribución por grandes bloques

| Bloque | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|
| 2014-2019 | 57,2% | 30,4% | 12,4% |
| 2020-2025 | 58,8% | 22,4% | 18,8% |
| 2026 observación | 14,6% | 85,4% | 0,0% |

Lectura:

- `2020-2025` sale como bloque **generalmente favorable**, aunque no de forma homogénea;
- `2014-2019` aparece más mezclado y menos limpio, con bastante más `MIXTO`;
- `2026` no sale favorable sostenido, sino predominantemente **de observación mixta**.

### 4.3. Distribución por año y cambios de clase

| Año | FAVORABLE | MIXTO | PROBLEMATICO | Cambios de clase |
|---|---:|---:|---:|---:|
| 2014 | 69,0% | 31,0% | 0,0% | 10 |
| 2015 | 31,0% | 53,6% | 15,5% | 19 |
| 2016 | 38,7% | 34,4% | 26,9% | 14 |
| 2017 | 87,3% | 12,7% | 0,0% | 9 |
| 2018 | 59,4% | 23,5% | 17,1% | 10 |
| 2019 | 57,9% | 27,4% | 14,7% | 14 |
| 2020 | 65,2% | 25,3% | 9,5% | 7 |
| 2021 | 80,6% | 19,4% | 0,0% | 12 |
| 2022 | 4,0% | 13,5% | 82,5% | 8 |
| 2023 | 64,8% | 31,6% | 3,6% | 8 |
| 2024 | 72,6% | 27,4% | 0,0% | 8 |
| 2025 | 65,2% | 17,2% | 17,6% | 6 |
| 2026 | 14,6% | 85,4% | 0,0% | 3 |

### 4.4. Subperiodos observados por año

A continuación se listan los tramos detectados cuando hubo cambios dentro del año.

#### 2014
- 2014-02-03 a 2014-02-07 → MIXTO
- 2014-02-10 a 2014-03-28 → FAVORABLE
- 2014-03-31 a 2014-05-02 → MIXTO
- 2014-05-05 a 2014-05-09 → FAVORABLE
- 2014-05-12 a 2014-06-13 → MIXTO
- 2014-06-16 a 2014-10-03 → FAVORABLE
- 2014-10-06 a 2014-10-31 → MIXTO
- 2014-11-03 a 2014-12-12 → FAVORABLE
- 2014-12-15 a 2014-12-19 → MIXTO
- 2014-12-22 a 2015-01-09 → FAVORABLE

#### 2015
- 2015-01-12 a 2015-01-16 → MIXTO
- 2015-01-20 a 2015-01-30 → FAVORABLE
- 2015-02-02 a 2015-02-20 → MIXTO
- 2015-02-23 a 2015-03-06 → FAVORABLE
- 2015-03-09 a 2015-03-20 → MIXTO
- 2015-03-23 a 2015-03-27 → FAVORABLE
- 2015-03-30 a 2015-05-01 → MIXTO
- 2015-05-04 a 2015-05-15 → FAVORABLE
- 2015-05-18 a 2015-07-17 → MIXTO
- 2015-07-20 a 2015-07-24 → FAVORABLE
- 2015-07-27 a 2015-08-07 → MIXTO
- 2015-08-10 a 2015-08-14 → FAVORABLE
- 2015-08-17 a 2015-08-21 → MIXTO
- 2015-08-24 a 2015-10-16 → PROBLEMATICO
- 2015-10-19 a 2015-11-06 → MIXTO
- 2015-11-09 a 2015-11-13 → FAVORABLE
- 2015-11-16 a 2015-11-20 → MIXTO
- 2015-11-23 a 2015-12-24 → FAVORABLE
- 2015-12-28 a 2016-01-08 → MIXTO

#### 2016
- 2016-01-11 a 2016-03-18 → PROBLEMATICO
- 2016-03-21 a 2016-03-24 → MIXTO
- 2016-03-28 a 2016-04-01 → PROBLEMATICO
- 2016-04-04 a 2016-04-08 → MIXTO
- 2016-04-11 a 2016-04-29 → FAVORABLE
- 2016-05-02 a 2016-05-27 → MIXTO
- 2016-05-31 a 2016-06-10 → FAVORABLE
- 2016-06-13 a 2016-06-17 → MIXTO
- 2016-06-20 a 2016-07-08 → PROBLEMATICO
- 2016-07-11 a 2016-07-22 → MIXTO
- 2016-07-25 a 2016-10-28 → FAVORABLE
- 2016-10-31 a 2016-12-09 → MIXTO
- 2016-12-12 a 2016-12-16 → FAVORABLE
- 2016-12-19 a 2017-01-06 → MIXTO

#### 2017
- 2017-01-09 a 2017-06-30 → FAVORABLE
- 2017-07-03 a 2017-07-07 → MIXTO
- 2017-07-10 a 2017-08-18 → FAVORABLE
- 2017-08-21 a 2017-09-08 → MIXTO
- 2017-09-11 a 2017-09-22 → FAVORABLE
- 2017-09-25 a 2017-09-29 → MIXTO
- 2017-10-02 a 2017-10-20 → FAVORABLE
- 2017-10-23 a 2017-10-27 → MIXTO
- 2017-10-30 a 2018-03-29 → FAVORABLE

#### 2018
- 2018-04-02 a 2018-05-04 → MIXTO
- 2018-05-07 a 2018-05-18 → FAVORABLE
- 2018-05-21 a 2018-06-01 → MIXTO
- 2018-06-04 a 2018-06-08 → FAVORABLE
- 2018-06-11 a 2018-06-15 → MIXTO
- 2018-06-18 a 2018-09-14 → FAVORABLE
- 2018-09-17 a 2018-09-21 → MIXTO
- 2018-09-24 a 2018-10-05 → FAVORABLE
- 2018-10-08 a 2018-10-26 → MIXTO
- 2018-10-29 a 2019-02-15 → PROBLEMATICO

#### 2019
- 2019-02-19 a 2019-05-24 → FAVORABLE
- 2019-05-28 a 2019-05-31 → MIXTO
- 2019-06-03 a 2019-06-07 → PROBLEMATICO
- 2019-06-10 a 2019-06-14 → FAVORABLE
- 2019-06-17 a 2019-06-21 → MIXTO
- 2019-06-24 a 2019-07-05 → FAVORABLE
- 2019-07-08 a 2019-07-12 → MIXTO
- 2019-07-15 a 2019-07-19 → FAVORABLE
- 2019-07-22 a 2019-08-09 → MIXTO
- 2019-08-12 a 2019-08-16 → FAVORABLE
- 2019-08-19 a 2019-08-30 → MIXTO
- 2019-09-03 a 2019-09-20 → FAVORABLE
- 2019-09-23 a 2019-11-01 → MIXTO
- 2019-11-04 a 2020-03-06 → FAVORABLE

#### 2020
- 2020-03-09 a 2020-04-09 → PROBLEMATICO
- 2020-04-13 a 2020-05-22 → MIXTO
- 2020-05-26 a 2020-10-02 → FAVORABLE
- 2020-10-05 a 2020-11-06 → MIXTO
- 2020-11-09 a 2020-11-20 → FAVORABLE
- 2020-11-23 a 2020-12-04 → MIXTO
- 2020-12-07 a 2021-03-05 → FAVORABLE

#### 2021
- 2021-03-08 a 2021-03-12 → MIXTO
- 2021-03-15 a 2021-03-19 → FAVORABLE
- 2021-03-22 a 2021-04-01 → MIXTO
- 2021-04-05 a 2021-05-07 → FAVORABLE
- 2021-05-10 a 2021-05-21 → MIXTO
- 2021-05-24 a 2021-06-04 → FAVORABLE
- 2021-06-07 a 2021-06-18 → MIXTO
- 2021-06-21 a 2021-10-01 → FAVORABLE
- 2021-10-04 a 2021-10-15 → MIXTO
- 2021-10-18 a 2021-12-03 → FAVORABLE
- 2021-12-06 a 2021-12-10 → MIXTO
- 2021-12-13 a 2022-01-14 → FAVORABLE

#### 2022
- 2022-01-18 a 2022-01-21 → MIXTO
- 2022-01-24 a 2022-04-01 → PROBLEMATICO
- 2022-04-04 a 2022-04-08 → MIXTO
- 2022-04-11 a 2022-08-05 → PROBLEMATICO
- 2022-08-08 a 2022-08-26 → MIXTO
- 2022-08-29 a 2022-09-09 → PROBLEMATICO
- 2022-09-12 a 2022-09-23 → MIXTO
- 2022-09-26 a 2023-01-13 → PROBLEMATICO

#### 2023
- 2023-01-17 a 2023-02-03 → MIXTO
- 2023-02-06 a 2023-02-24 → FAVORABLE
- 2023-02-27 a 2023-03-17 → MIXTO
- 2023-03-20 a 2023-09-15 → FAVORABLE
- 2023-09-18 a 2023-11-17 → MIXTO
- 2023-11-20 a 2023-12-01 → FAVORABLE
- 2023-12-04 a 2023-12-08 → MIXTO
- 2023-12-11 a 2024-04-19 → FAVORABLE

#### 2024
- 2024-04-22 a 2024-05-17 → MIXTO
- 2024-05-20 a 2024-05-31 → FAVORABLE
- 2024-06-03 a 2024-06-07 → MIXTO
- 2024-06-10 a 2024-08-02 → FAVORABLE
- 2024-08-05 a 2024-08-16 → MIXTO
- 2024-08-19 a 2024-08-30 → FAVORABLE
- 2024-09-03 a 2024-10-18 → MIXTO
- 2024-10-21 a 2025-01-10 → FAVORABLE

#### 2025
- 2025-01-13 a 2025-02-14 → MIXTO
- 2025-02-18 a 2025-02-28 → FAVORABLE
- 2025-03-03 a 2025-03-07 → MIXTO
- 2025-03-10 a 2025-05-09 → PROBLEMATICO
- 2025-05-12 a 2025-05-30 → MIXTO
- 2025-06-02 a 2026-01-02 → FAVORABLE

#### 2026
- 2026-01-05 a 2026-01-09 → MIXTO
- 2026-01-12 a 2026-01-16 → FAVORABLE
- 2026-01-20 a 2026-03-03 → MIXTO

---

## 5. Encaje con años favorables

### 5.1. Bloque 2020-2025

La clasificación sí encaja **razonablemente bien** con la idea de que `2020-2025` fue, en conjunto, un bloque generalmente favorable:

- `58,8%` del tiempo sale `FAVORABLE`;
- solo `18,8%` sale `PROBLEMATICO`;
- el resto (`22,4%`) queda en `MIXTO`, que es una proporción aceptable para un bloque que contiene shock, transición y correcciones intermedias.

Además, por años:

- `2020`: favorable dominante (`65,2%`) pero con crash bien visible (`9,5% problemático`).
- `2021`: muy limpio (`80,6% favorable`, `0% problemático`).
- `2023`: favorable con bastante transición (`64,8% favorable`, `31,6% mixto`).
- `2024`: favorable claro (`72,6% favorable`, `0% problemático`).
- `2025`: favorable dominante (`65,2%`) pero con un tramo problemático no trivial (`17,6%`).

### 5.2. Lectura cualitativa

Esto sugiere que la clasificación **no blanquea** todo el bloque `2020-2025` como si fuese uniforme, pero sí preserva la intuición central correcta: el sesgo dominante en ese conjunto de años sigue siendo favorable.

Ese comportamiento parece más convincente que una taxonomía que:

- marcase casi todo el bloque como `MIXTO`; o
- convirtiese 2020, 2023 o 2025 en años estructuralmente problemáticos.

### 5.3. Años favorables especialmente bien captados

Los años que mejor encajan con la idea de “favorable claro” son:

- **2017**;
- **2021**;
- **2024**.

En esos casos la lectura es coherente y suficientemente limpia. No parece una clasificación arbitraria.

---

## 6. Encaje con años problemáticos

### 6.1. 2015 y 2016

Aquí aparece una de las zonas más útiles del ejercicio, porque obliga a no exagerar la calidad del selector.

#### 2015

`2015` sale así:

- `31,0% FAVORABLE`
- `53,6% MIXTO`
- `15,5% PROBLEMATICO`
- `19` cambios de clase

Lectura:

- **no** aparece como un año favorable limpio;
- tampoco como un año íntegramente problemático;
- se parece más a un año de **incomodidad persistente y mucha ambigüedad**, lo cual resulta bastante razonable.

Por tanto, para `2015` la clasificación me parece **creíble** precisamente porque no intenta fabricar una dureza artificial: reconoce un núcleo problemático claro en `2015-08` a `2015-10`, pero deja el resto mayoritariamente en `MIXTO`.

#### 2016

`2016` sale así:

- `38,7% FAVORABLE`
- `34,4% MIXTO`
- `26,9% PROBLEMATICO`
- `14` cambios de clase

Lectura:

- es un año más repartido y menos estable que un año claramente favorable;
- muestra un arranque muy débil y todavía bastante oscilación posterior;
- no queda tan nítidamente problemático como `2022`, pero sí bastante más ambiguo y accidentado que `2017`, `2021` o `2024`.

Conclusión para `2015-2016`: la clasificación **sí los identifica como años menos claros**, y eso es un punto a favor. No los romantiza como favorables, pero tampoco los sobredramatiza.

### 6.2. Otros años menos lineales

#### 2018

`2018` combina:

- `59,4% FAVORABLE`
- `23,5% MIXTO`
- `17,1% PROBLEMATICO`

La lectura parece razonable: año globalmente utilizable, pero con deterioro final suficientemente visible.

#### 2019

`2019` combina:

- `57,9% FAVORABLE`
- `27,4% MIXTO`
- `14,7% PROBLEMATICO`

También parece una salida aceptable: favorable en conjunto, aunque no tan limpio como los mejores años del bloque alcista.

### 6.3. Juicio global sobre los años problemáticos o ambiguos

La clasificación pasa una prueba importante:

- **sí distingue** un año excepcionalmente malo (`2022`);
- **sí deja ambiguos** los años realmente ambiguos (`2015`, `2016`);
- **sí reconoce** que algunos años buenos no fueron lineales (`2018`, `2019`, `2025`).

Eso es mejor que una segmentación demasiado binaria.

---

## 7. Caso 2022

### 7.1. Resultado observado

`2022` es el caso más claro de todo el histórico auditado:

- `82,5% PROBLEMATICO`
- `13,5% MIXTO`
- `4,0% FAVORABLE`
- `8` cambios de clase

### 7.2. Interpretación

La clasificación trata `2022` como un **caso especial perfectamente reconocible**.

No hace falta abrir todavía una clase formal nueva “tipo 2022”, pero sí se puede decir que el selector lo reconoce como:

- un año muy mayoritariamente problemático;
- con pequeñas pausas mixtas;
- prácticamente sin tramos realmente favorables.

### 7.3. ¿Hace falta un subtipo informal?

Como hipótesis descriptiva, sí puede decirse que `2022` aparece como un **problemático dominante de estrés direccional sostenido**, distinto de años mixtos o de años con un único episodio puntual.

Es decir:

- no parece un simple “mixto duro”;
- tampoco un problema corto y localizado;
- se comporta como una familia propia dentro de lo problemático.

Pero por disciplina metodológica, todavía lo dejaría como **subtipo informal reconocible**, no como clase oficial nueva.

### 7.4. Valor del caso 2022 para esta auditoría

Que `2022` salga tan claramente destacado es una de las señales más fuertes a favor de que esta primera clasificación **sí capta algo real** del histórico.

---

## 8. Observación preliminar sobre 2026

`2026` no debe usarse como base de diseño y, de hecho, la lectura observada aconseja prudencia:

- `14,6% FAVORABLE`
- `85,4% MIXTO`
- `0,0% PROBLEMATICO`
- `3` cambios de clase

Interpretación preliminar:

- no parece, por ahora, un año favorable limpio;
- tampoco aparece como deterioro estructural comparable a `2022`;
- se parece más a un entorno **indefinido / en observación**, donde el selector prefiere no comprometer una lectura extrema.

Eso es metodológicamente correcto para este punto del trabajo. `2026` debe quedar como seguimiento, no como argumento para rediseñar la taxonomía.

---

## 9. Conclusión final

La primera clasificación histórica simple basada en `QQQ > SMA200`, `Retorno 63` y `Cruces SMA50`, comprimida en la taxonomía mínima `FAVORABLE / MIXTO / PROBLEMATICO`, produce una salida **bastante razonable** para esta fase de investigación.

Puntos fuertes:

- reconoce bien los años claramente favorables (`2017`, `2021`, `2024`);
- mantiene `2020-2025` como bloque generalmente favorable sin volverlo homogéneo por la fuerza;
- separa `2022` como caso especial muy reconocible;
- trata `2015` y `2016` como años verdaderamente ambiguos, no como categorías forzadas;
- deja `2026` en observación mixta, que es justo lo prudente.

Limitaciones reales:

- el selector todavía genera bastante fragmentación en años dudosos;
- algunos años favorables pero no perfectos (`2018`, `2019`, `2025`) siguen mostrando bastantes transiciones;
- la ausencia en el repositorio de `ANALISIS 56` obliga a declarar que la especificación usada aquí es una **reconstrucción disciplinada**, no una lectura literal de ese documento ausente.

Juicio honesto:

- **sí hay señal útil**;
- **no** parece todavía una taxonomía final cerrada;
- pero ya ofrece una base defendible para seguir investigando sin caer en ajuste retrospectivo por año.

---

## 10. Recomendación: clasificación convincente / parcialmente útil / todavía poco convincente

**Recomendación: parcialmente útil.**

Motivo:

- la clasificación es **convincente** en los casos gruesos importantes (`2022`, años muy favorables, observación prudente de `2026`);
- también es **útil** porque no fuerza una lectura artificial de `2015` y `2016`;
- pero todavía **no** la llamaría plenamente convincente como base de diseño final, porque en varios años intermedios sigue habiendo bastante rotación y porque falta confirmar la especificación exacta que supuestamente definía `ANALISIS 56`.

Dicho de forma simple:

- **no es humo**;
- **no es suficiente todavía para gobernar producción**;
- **sí merece seguir viva como primera capa de etiquetado histórico**.
