# VERSION 2.2.2 ANALISIS 62

## 1. Objetivo

Auditar si la clase `MIXTO` del selector de contexto aporta valor real como categoría intermedia honesta o si está absorbiendo demasiada ambigüedad, reduciendo así la utilidad práctica de la clasificación `FAVORABLE / MIXTO / PROBLEMATICO`.

La misión de este análisis no es tocar producción, ni rediseñar la taxonomía, ni eliminar `MIXTO` por principio. La pregunta concreta es más disciplinada:

- cuánto peso histórico está capturando `MIXTO`;
- si aparece sobre todo en transiciones razonables y años frontera;
- si ayuda a no forzar clasificaciones demasiado agresivas;
- o si se ha convertido en una bolsa excesiva de incertidumbre.

## 2. Selector auditado

Se toma como mejor especificación verificable la cadena documental disponible en `ANALISIS 57`, `58` y `59`, contrastada con la implementación real de `META_BOT.py`.

Limitación documental explícita:

- en el árbol actual del repositorio sí existen `ANALISIS 57.md`, `ANALISIS 58.md` y `ANALISIS 59.md`;
- `ANALISIS 60.md` y `ANALISIS 61.md` **no existen** en el repositorio actual, por lo que no han podido leerse literalmente.

Para no inventar una especificación nueva, se audita la taxonomía de tres clases ya descrita en `ANALISIS 57`, construida sobre el `score_regimen` derivado de las variables ya presentes en el sistema:

- `+1` si `QQQ > SMA200`;
- `-1` si `QQQ < SMA200`;
- `+1` si `Retorno 63 > 0`;
- `-1` si `Retorno 63 < 0`;
- `-1` adicional si `Cruces SMA50` sale en estado `ALTO`.

Con ello, la etiqueta auditada queda así:

- `FAVORABLE` si `score >= 2`;
- `MIXTO` si `score = 0` o `1`;
- `PROBLEMATICO` si `score <= -1`.

La reconstrucción histórica se ha hecho sobre el histórico preparado por `META_BOT.py`, respetando la revisión semanal del régimen ya usada por el sistema y sin introducir variables nuevas.

## 3. Peso histórico de la clase MIXTO

### Proporción temporal global

Sobre `4.198` sesiones auditables con `SMA200` y `Retorno 63` ya disponibles, el reparto temporal queda así:

| Clase | Sesiones | Proporción temporal |
|---|---:|---:|
| FAVORABLE | 2.419 | 57,6% |
| MIXTO | 1.159 | 27,6% |
| PROBLEMATICO | 620 | 14,8% |

Primera lectura:

- `MIXTO` ocupa algo más de **una cuarta parte** del histórico auditado;
- no es una clase marginal, pero tampoco domina el selector;
- queda claramente por debajo de `FAVORABLE` y claramente por encima de `PROBLEMATICO`.

### Peso por bloques históricos

| Bloque | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|
| 2009-2013 | 58,3% | 29,1% | 12,6% |
| 2014-2019 | 56,9% | 30,5% | 12,6% |
| 2020-2025 | 59,0% | 22,1% | 18,8% |
| 2026 observado* | 16,3% | 83,7% | 0,0% |

`* 2026` está incompleto y solo debe leerse como observación parcial.

Lectura de bloque:

- en `2014-2019`, `MIXTO` sí tiene un peso alto, alrededor del **30%**, coherente con un bloque históricamente menos limpio;
- en `2020-2025`, su peso baja al **22,1%**, lo que sugiere que el selector sí distingue mejor entre tramos favorables y problemáticos en el bloque reciente;
- el `83,7%` de `MIXTO` en `2026` es demasiado alto para extrapolar conclusiones fuertes y apunta más a observación abierta que a régimen ya estabilizado.

## 4. Dónde aparece MIXTO

### Distribución anual de MIXTO

| Año | % MIXTO |
|---|---:|
| 2009 | 9,6% |
| 2010 | 26,6% |
| 2011 | 39,7% |
| 2012 | 32,8% |
| 2013 | 21,4% |
| 2014 | 30,9% |
| 2015 | 53,9% |
| 2016 | 34,4% |
| 2017 | 13,6% |
| 2018 | 23,3% |
| 2019 | 27,1% |
| 2020 | 25,5% |
| 2021 | 19,0% |
| 2022 | 13,2% |
| 2023 | 30,6% |
| 2024 | 26,6% |
| 2025 | 17,8% |
| 2026* | 83,7% |

Años donde `MIXTO` sale especialmente alto:

- `2015` es el caso más claro con **53,9%**, señal de año frontera y lateralidad difícil;
- `2011`, `2012`, `2014`, `2016` y `2023` también superan o rozan el `30%`;
- `2017`, `2021` y `2022` muestran pesos bajos de `MIXTO`, lo que encaja con años más direccionales.

### Transiciones que pasan por MIXTO

Se detectan `180` cambios de clase en total. De ellos:

- `173` transiciones, es decir, el **96,1%**, pasan por `MIXTO`;
- solo `7` transiciones son saltos directos entre `FAVORABLE` y `PROBLEMATICO`.

Desglose de transiciones:

| Transición | Nº |
|---|---:|
| FAVORABLE → MIXTO | 68 |
| MIXTO → FAVORABLE | 66 |
| MIXTO → PROBLEMATICO | 20 |
| PROBLEMATICO → MIXTO | 19 |
| PROBLEMATICO → FAVORABLE | 4 |
| FAVORABLE → PROBLEMATICO | 3 |

Lectura:

- `MIXTO` aparece **sobre todo como puente** entre estados más definidos;
- el selector casi nunca salta directamente de `FAVORABLE` a `PROBLEMATICO` sin una fase intermedia;
- eso favorece una lectura más creíble y menos brusca del régimen.

### Persistencia de MIXTO

`MIXTO` no se comporta como un único bloque continuo gigantesco, sino como una secuencia de episodios relativamente cortos:

- `87` episodios de `MIXTO`;
- duración media de `13,3` sesiones;
- mediana de `10` sesiones;
- duración máxima observada de `63` sesiones.

Los tramos más largos de `MIXTO` aparecen en zonas plausiblemente fronterizas o de reconstrucción del contexto, por ejemplo:

- `2012-05-14` a `2012-08-10` (`63` sesiones);
- `2015-05-18` a `2015-07-17` (`45` sesiones);
- `2023-09-18` a `2023-11-17` (`45` sesiones);
- `2020-04-13` a `2020-05-25` (`31` sesiones);
- `2026-01-20` a `2026-03-03` (`31` sesiones, tramo parcial y todavía abierto).

## 5. Casos en los que MIXTO aporta valor

### 1. Evita forzar binarios artificiales

`MIXTO` ayuda cuando la evidencia no justifica afirmar ni un contexto limpiamente favorable ni uno claramente hostil. Esto se ve especialmente bien en años como:

- `2015`, donde el exceso de lateralidad y los cambios de tono harían poco honesto clasificar casi todo como `FAVORABLE` o casi todo como `PROBLEMATICO`;
- `2016`, donde conviven deterioro, rebote y recomposición;
- `2023`, donde la recuperación existe, pero no todo el año tiene la misma limpieza estructural.

### 2. Ordena transiciones razonables

Que el **96,1%** de los cambios de clase pasen por `MIXTO` es una señal fuerte de utilidad descriptiva. En la práctica, `MIXTO` actúa como:

- zona de desacople parcial;
- estado de observación cuando las variables dejan de alinearse;
- antesala a confirmaciones más sólidas hacia `FAVORABLE` o `PROBLEMATICO`.

Eso mejora la honestidad del selector, porque impide fingir que el mercado siempre cambia de régimen con nitidez instantánea.

### 3. Preserva contenido para las clases extremas

La existencia de `MIXTO` permite que:

- `FAVORABLE` siga significando contexto bastante alineado;
- `PROBLEMATICO` siga significando fricción estructural visible;
- y no haya que meter en una clase extrema casos todavía híbridos.

Sin `MIXTO`, buena parte de los años frontera tenderían a contaminar una de las dos clases extremas y volverlas menos interpretables.

### 4. Tiene cierta utilidad descriptiva frente al selector operativo

Al cruzar la taxonomía auditada con el `meta_regimen` operativo actual:

- `FAVORABLE` cae en `LONG_TREND` el `98,1%` del tiempo;
- `PROBLEMATICO` cae en `SHORT_TREND` el `68,1%` del tiempo y en `NO_TRADE` el `31,9%`;
- `MIXTO` se reparte entre `LONG_TREND` (`74,2%`) y `NO_TRADE` (`25,8%`).

Esto sugiere que `MIXTO` no es puro ruido: está capturando situaciones donde la capa descriptiva ya detecta mezcla, aunque la capa operativa todavía conserve bastante sesgo alcista.

## 6. Casos en los que MIXTO genera ambigüedad

### 1. Su peso no es trivial

Un `27,6%` del tiempo histórico es mucho como para tratarlo como detalle menor. No invalida la clase, pero obliga a vigilarla. Si una de cada cuatro sesiones cae en `MIXTO`, esa clase necesita una justificación clara y no puede ser un mero refugio narrativo.

### 2. En algunos años ocupa demasiado espacio

El caso más delicado es `2015` con `53,9%` del año en `MIXTO`. Ahí la clase mejora la honestidad, sí, pero también reduce capacidad práctica porque deja gran parte del año en un estado poco accionable.

También hay que vigilar:

- `2011` (`39,7%`);
- `2012` (`32,8%`);
- `2016` (`34,4%`);
- `2023` (`30,6%`).

En estos casos, `MIXTO` parece razonable como diagnóstico, pero si siguiera expandiéndose correría el riesgo de vaciar la segmentación.

### 3. Puede heredar parte del sesgo del selector actual

Como la capa operativa real resuelve muchos casos intermedios con sesgo alcista (`LONG_TREND` o `AGRESIVO`), `MIXTO` corre el riesgo de quedarse como una categoría descriptiva correcta pero todavía poco diferenciada en la práctica. Es decir:

- mejora la sinceridad analítica;
- pero no siempre mejora igual de bien la capacidad práctica del selector si las decisiones posteriores no respetan esa ambigüedad.

### 4. El arranque de 2026 alerta sobre posible sobreuso reciente

El `83,7%` de `MIXTO` en `2026` no debe usarse para rediseñar nada todavía, pero sí funciona como aviso: si el selector empieza a quedarse demasiado tiempo en `MIXTO` cuando el contexto reciente no termina de aclararse, la clase puede estar absorbiendo más indecisión de la deseable.

## 7. Comparación con FAVORABLE y PROBLEMATICO

### Frente a FAVORABLE

`FAVORABLE` ocupa `57,6%` del histórico y conserva mejor nitidez semántica:

- domina claramente en años muy limpios como `2013`, `2017`, `2021` y `2024`;
- su duración media por episodio es de `34,1` sesiones;
- está casi perfectamente alineado con `LONG_TREND`.

Comparado con ello, `MIXTO` es más corto, más nervioso y menos concluyente. Eso no es un defecto en sí mismo, siempre que se mantenga como estado intermedio y no como clase dominante permanente.

### Frente a PROBLEMATICO

`PROBLEMATICO` ocupa solo `14,8%` del histórico, pero su señal es más específica:

- se concentra en periodos de deterioro más visibles;
- en `2022` llega al `82,6%` del año;
- su duración media por episodio es de `27,0` sesiones.

Comparado con `PROBLEMATICO`, `MIXTO` cumple otra función: no marca crisis clara, sino fricción o alineación incompleta. En ese sentido, ambas clases no parecen redundantes.

### Juicio comparativo

- `FAVORABLE` aporta claridad positiva.
- `PROBLEMATICO` aporta claridad negativa.
- `MIXTO` aporta honestidad en los tramos donde esa claridad no existe todavía.

El problema no es conceptual, sino de **dosificación**: `MIXTO` es útil mientras siga siendo una capa intermedia reconocible y no pase a ocupar demasiado espacio del histórico.

## 8. Conclusión final

La auditoría sugiere que `MIXTO` **sí es una clase útil** y no solo una bolsa vacía de incertidumbre. La evidencia principal es esta:

- su peso histórico global (`27,6%`) es relevante pero no dominante;
- aparece mayoritariamente en **transiciones razonables**;
- el **96,1%** de los cambios de clase pasan por `MIXTO`;
- sus episodios suelen ser relativamente cortos, no un bloqueo permanente del selector;
- ayuda claramente a no forzar clasificaciones artificiales en años frontera.

Dicho eso, también hay un riesgo real:

- en ciertos años, especialmente `2015`, `MIXTO` ocupa demasiado espacio;
- mejora la honestidad descriptiva, pero en esos tramos reduce capacidad práctica;
- si el selector siguiera desplazando demasiados casos hacia `MIXTO`, la claridad global se resentiría.

Por tanto, el juicio más equilibrado no es eliminar `MIXTO`, pero tampoco dejarlo totalmente sin vigilancia. Hoy por hoy, `MIXTO` **mejora la honestidad del selector, aunque a costa de reducir parte de su capacidad práctica en años muy ambiguos**.

## 9. Recomendación: mantener MIXTO / restringir MIXTO / revisar su papel antes de seguir

**Recomendación final: restringir MIXTO.**

No recomiendo eliminarlo, porque la evidencia histórica no respalda que sea una clase superflua. Al contrario, cumple una función real y evita forzar etiquetas engañosas.

Pero tampoco recomiendo mantenerlo exactamente “tal como está” sin cautelas, porque:

- ocupa más de una cuarta parte del histórico;
- domina en exceso algunos años frontera;
- y puede restar claridad práctica si se usa como destino por defecto de cualquier caso incómodo.

La lectura más prudente es esta:

- `MIXTO` debe mantenerse como clase oficial;
- pero conviene **vigilar y restringir su expansión** para que siga describiendo transiciones y estados híbridos reales;
- si en análisis posteriores su peso siguiera creciendo o se concentrara demasiado en años completos, entonces sí habría que revisar su papel antes de seguir.
