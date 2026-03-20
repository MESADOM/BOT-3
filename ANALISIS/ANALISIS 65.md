# VERSION 2.2.2 ANALISIS 65

## 1. Objetivo

Determinar si `2022` debe tratarse, dentro de la taxonomía ya vigente, como un año `PROBLEMATICO` que el sistema general **ya absorbe operativamente** o como un año `PROBLEMATICO` que **todavía exige investigación específica**.

El foco de este documento no es reclasificar el contexto, ni rediseñar el selector, ni abrir todavía una variante específica. La pregunta es más precisa:

- mantener separadas la **clasificación de contexto** y la **respuesta operativa** del sistema general;
- estudiar si el buen cierre operativo de `2022` es suficientemente estable;
- comprobar si ese resultado depende en exceso de pocos episodios;
- decidir si la absorción de `2022` parece robusta o más bien accidental.

Limitación documental explícita: en el repositorio actual se han podido leer `ANALISIS 61.md` y `ANALISIS 63.md`, pero **no existe** `ANALISIS 64.md`. Por tanto, este análisis no atribuye a `ANALISIS 64` contenido no verificable y trabaja con la evidencia efectivamente disponible y con el motor vigente en `META_BOT.py`.

## 2. Contexto y sistema evaluados

Se evalúa el **sistema general vigente `VERSION 2.2.2`**, sin tocar producción y sin modificar la clasificación histórica ya obtenida para `2022`.

La clasificación de contexto que se mantiene es la ya auditada previamente:

- `FAVORABLE` si `score >= 2`;
- `MIXTO` si `score = 0 o 1`;
- `PROBLEMATICO` si `score <= -1`.

Ese score sigue dependiendo de tres piezas simples:

- `QQQ > SMA200`;
- `Retorno 63`;
- `Cruces SMA50`.

Además, el sistema operativo general se ejecuta en modo `LONG_SHORT`, con estas dos reglas meta relevantes:

- activa `LONG_TREND` cuando `QQQ > SMA200`, el retorno está en `POSITIVO` o `NEUTRAL` y los cruces no son altos;
- activa `SHORT_TREND` cuando `QQQ < SMA200` y el retorno es `NEGATIVO`.

Por tanto, la pregunta de absorción es legítima: un año puede seguir siendo **contextualmente problemático** y aun así resultar **operativamente utilizable** para el general si la pata short compensa de manera suficientemente amplia, repetida y no excesivamente concentrada.

## 3. Clasificación del año 2022

La clasificación de `2022` **no se cambia**.

`2022` sigue siendo un año de contexto `PROBLEMATICO` con una lectura históricamente creíble y muy marcada:

- `82,5% PROBLEMATICO`;
- `13,5% MIXTO`;
- `4,0% FAVORABLE`.

En número de sesiones de mercado de `2022`, eso equivale aproximadamente a:

- `213` sesiones `PROBLEMATICO`;
- `34` sesiones `MIXTO`;
- `11` sesiones `FAVORABLE`.

Los subtramos de contexto relevantes quedan así:

- `2022-01-03` a `2022-01-17` → `FAVORABLE`;
- `2022-01-18` a `2022-01-21` → `MIXTO`;
- `2022-01-24` a `2022-04-01` → `PROBLEMATICO`;
- `2022-04-04` a `2022-04-08` → `MIXTO`;
- `2022-04-11` a `2022-08-05` → `PROBLEMATICO`;
- `2022-08-08` a `2022-08-26` → `MIXTO`;
- `2022-08-29` a `2022-09-09` → `PROBLEMATICO`;
- `2022-09-12` a `2022-09-23` → `MIXTO`;
- `2022-09-26` a `2022-12-30` → `PROBLEMATICO`.

Esto confirma algo importante para el objetivo de este informe: `2022` no es un año “dudoso” o simplemente mixto. El **contexto** fue hostil de forma dominante, prolongada y repartida en varios bloques. Cualquier conclusión operativa favorable debe leerse **a pesar de** ese contexto, no **contra** ese contexto.

## 4. Comportamiento del general en 2022

### 4.1 Resultado anual agregado del general

Con el sistema general vigente, el resultado operativo de `2022` por operaciones cerradas en ese año fue:

- **beneficio neto total:** `+4.119,19 €`;
- **rentabilidad sobre capital inicial del sistema:** `+411,919%`;
- **nº de trades:** `6`;
- **ganadoras:** `5`;
- **perdedoras:** `1`;
- **win rate:** `83,33%`;
- **capital al inicio del año operativo:** `6.892,14 €`;
- **capital al cierre de 2022:** `11.011,33 €`.

A primera vista, el general **sí cierra muy bien 2022**.

### 4.2 Drawdown del general dentro de 2022

Tomando la secuencia de capital cerrado del propio año, el drawdown máximo interno de `2022` fue aproximadamente:

- **drawdown máximo 2022:** `-8,11%`.

Ese drawdown aparece al inicio del año, tras un trade long perdedor:

- `2022-01-05` → `2022-01-07` → `LONG_TREND` → `-558,80 €`.

Después de ese golpe inicial, la curva anual cerrada ya no vuelve a marcar un drawdown peor dentro de `2022`, porque el resto del año queda dominado por ganancias short.

Esto es favorable operativamente, pero también deja una pista metodológica: el buen año no se reparte de forma homogénea entre módulos, sino que depende casi por completo de la respuesta short en el régimen hostil posterior.

### 4.3 Trades de 2022

Los `6` trades cerrados en `2022` fueron:

1. `2022-01-05` → `2022-01-07` → `LONG_TREND` → `-558,80 €`.
2. `2022-03-03` → `2022-03-11` → `SHORT_TREND` → `+707,71 €`.
3. `2022-03-23` → `2022-03-24` → `SHORT_TREND` → `+119,38 €`.
4. `2022-04-13` → `2022-05-17` → `SHORT_TREND` → `+2.112,40 €`.
5. `2022-06-01` → `2022-06-23` → `SHORT_TREND` → `+1.175,00 €`.
6. `2022-10-25` → `2022-11-10` → `SHORT_TREND` → `+563,50 €`.

Lectura operativa inmediata:

- el único trade long de 2022 fue perdedor;
- las `5` operaciones restantes fueron short y ganadoras;
- el año bueno del general en realidad es casi sinónimo de **captura short neta** dentro de un contexto muy hostil.

### 4.4 Rendimiento por subtramos de 2022

Si se mide la contribución por subtramo de contexto usando las operaciones cerradas dentro de cada bloque:

- `2022-01-18` a `2022-01-21` (`MIXTO`) → `0` trades → `0 €`.
- `2022-01-24` a `2022-04-01` (`PROBLEMATICO`) → `2` trades → `+827,09 €`.
- `2022-04-04` a `2022-04-08` (`MIXTO`) → `0` trades → `0 €`.
- `2022-04-11` a `2022-08-05` (`PROBLEMATICO`) → `2` trades → `+3.287,40 €`.
- `2022-08-08` a `2022-08-26` (`MIXTO`) → `0` trades → `0 €`.
- `2022-08-29` a `2022-09-09` (`PROBLEMATICO`) → `0` trades → `0 €`.
- `2022-09-12` a `2022-09-23` (`MIXTO`) → `0` trades → `0 €`.
- `2022-09-26` a `2022-12-30` (`PROBLEMATICO`) → `1` trade → `+563,50 €`.

Agrupado de forma más gruesa:

- `Q1 2022` → `3` trades → `+268,29 €` netos;
- `Q2 2022` → `2` trades → `+3.287,40 €` netos;
- `Q3 2022` → `0` trades → `0 €`;
- `Q4 2022` → `1` trade → `+563,50 €`.

Y por mitades del año:

- `H1 2022` → `5` trades → `+3.555,69 €`;
- `H2 2022` → `1` trade → `+563,50 €`.

Esto ya introduce una reserva importante: el año no está sostenido por un flujo continuo y repartido de captura, sino por unos pocos bloques con actividad efectiva, especialmente `Q2`.

## 5. Concentración del resultado

Aquí está el punto decisivo del análisis.

### 5.1 Concentración por número de trades

El beneficio de `2022` no está repartido de forma uniforme:

- el mejor trade (`2022-04-13` → `2022-05-17`) aporta `+2.112,40 €`, es decir, **51,28%** de todo el beneficio anual;
- los dos mejores trades (`2022-04-13` y `2022-06-01`) aportan `+3.287,40 €`, es decir, **79,81%** del resultado anual;
- los tres mejores trades explican **96,99%** del beneficio anual.

Eso significa que el año operativo depende materialmente de **muy pocos episodios**.

### 5.2 Concentración por subtramos

La concentración por bloques temporales también es alta:

- el subtramo `2022-04-11` a `2022-08-05` concentra `+3.287,40 €`, es decir, **79,81%** del total anual;
- `Q2 2022` por sí solo explica igualmente **79,81%** del beneficio de todo el año;
- `H2 2022`, pese a seguir siendo mayoritariamente `PROBLEMATICO` como contexto, solo aporta `+563,50 €` y además con un único trade.

Por tanto, el sistema **sí gana en 2022**, pero no de un modo equilibrado a lo largo del año. Gana sobre todo porque captura muy bien un bloque concreto del bear market.

### 5.3 Concentración del daño

El daño también está concentrado:

- el único trade perdedor del año es el long inicial de enero (`-558,80 €`);
- ese trade explica el **100%** de la pérdida bruta de `2022`.

Metodológicamente esto importa porque el año queda descrito por una estructura muy simple:

- un fallo long al principio;
- luego varios aciertos short;
- con la mayor parte del valor concentrada en dos trades del segundo trimestre.

Eso es mejor que un año caótico, pero todavía está lejos de una absorción amplia y distribuida.

## 6. Fragilidad o estabilidad de la absorción

### 6.1 Señales a favor de absorción real

Hay motivos para no despreciar la absorción observada:

- el año termina claramente en positivo;
- el general no solo evita el desastre de `2022`, sino que lo monetiza bien;
- no depende de un único trade aislado, porque hay `5` shorts ganadores;
- la captura aparece en más de un bloque `PROBLEMATICO`, no únicamente en una fecha puntual.

En ese sentido, sería excesivo decir que el resultado es puro accidente.

### 6.2 Señales de fragilidad

Sin embargo, la absorción **todavía no parece plenamente robusta**:

1. **Muestra muy corta.**
   Solo hay `6` trades cerrados en todo el año.

2. **Dominancia extrema del bloque central.**
   Dos trades del segundo trimestre explican casi `80%` del resultado.

3. **Cobertura incompleta del año hostil.**
   Aunque `2022` es `PROBLEMATICO` la mayor parte del tiempo, el sistema no muestra una captura repartida por todos esos tramos. En varios bloques hostiles (`2022-08-29` a `2022-09-09`, por ejemplo) no hay aportación operativa.

4. **Asimetría módulo long / short.**
   El componente long no demuestra resiliencia en `2022`; de hecho, la parte favorable del año se explica casi enteramente por la pata short. Eso no invalida el resultado del general, pero sí revela que la absorción no es “general” en el sentido de ser amplia y equilibrada entre respuestas posibles: es una absorción muy sesgada a la captura bajista.

5. **Dependencia de pocos episodios de alta contribución.**
   Que tres trades expliquen prácticamente todo el beneficio anual obliga a ser prudentes antes de llamar “absorbible” al año de forma cerrada.

### 6.3 Juicio de estabilidad

La mejor formulación prudente es esta:

- la absorción de `2022` por el general es **real en saldo**;
- pero su estabilidad es **media-baja** si se exige dispersión razonable del beneficio dentro del año;
- y su robustez todavía no parece suficiente para afirmar sin reservas que `2022` ya está plenamente “absorbido” como caso resuelto.

## 7. Diferencia entre contexto problemático y resultado operativo

Esta separación es crítica para no deformar la lectura.

### 7.1 El contexto sigue siendo hostil

`2022` debe seguir tratándose como `PROBLEMATICO` porque:

- la dominancia del contexto hostil es muy alta (`82,5%` del año);
- los bloques problemáticos son prolongados y múltiples;
- el selector no está exagerando: está reconociendo un año excepcionalmente adverso y persistente.

### 7.2 El resultado operativo puede ser aceptable sin suavizar el contexto

A la vez, el general obtiene un resultado operativo claramente bueno en ese mismo año.

Eso no obliga a reinterpretar `2022` como favorable ni como mixto. Lo correcto es decir:

- **contextualmente**, `2022` fue un año hostil y sigue siéndolo;
- **operativamente**, el general consiguió aprovechar parte importante de esa hostilidad, sobre todo por la pata short.

### 7.3 Lo que todavía impide una absorción declarada sin reservas

Lo que frena la declaración de “caso absorbible” no es que el año cierre mal. Cierra bien.

Lo que la frena es otra cosa:

- la captura está demasiado concentrada;
- la actividad está poco repartida entre subtramos;
- el resultado descansa sobre muy pocos episodios decisivos;
- y varios bloques `PROBLEMATICO` no muestran una respuesta operativa suficientemente continua como para hablar de absorción robusta del año entero.

## 8. Conclusión final

`2022` **no debe reclasificarse** y sigue siendo un año de contexto `PROBLEMATICO` muy bien identificado por el selector.

El sistema general vigente **sí demuestra capacidad real de ganar dinero en 2022**, con un saldo anual fuerte y un drawdown interno contenido tras el golpe inicial de enero. Por tanto, no estamos ante un caso donde el contexto hostil destruya al general de manera uniforme.

Pero ese buen resultado operativo **no está suficientemente distribuido** dentro del año:

- hay solo `6` trades;
- `Q2` concentra casi `80%` del beneficio;
- dos trades explican casi `80%` del total;
- tres trades explican prácticamente todo el año;
- y varios subtramos hostiles relevantes quedan sin contribución apreciable.

En consecuencia, la absorción observada parece **parcialmente real pero todavía frágil**. No parece una casualidad pura, pero tampoco una evidencia bastante sólida como para cerrar el caso y asumir que `2022` ya está plenamente absorbido por el general de forma robusta.

## 9. Recomendación: absorbible por el general / requiere más estudio / todavía ambiguo

### Recomendación final

**PROBLEMATICO que aún justificaría estudio específico.**

### Motivo de la recomendación

La razón no es que el general falle en `2022`; de hecho, en saldo anual funciona bien. La razón es que ese buen funcionamiento:

- depende en exceso de pocos episodios;
- muestra alta concentración temporal y por trade;
- no acredita todavía una absorción amplia y estable del conjunto del año;
- y por tanto no permite declarar con suficiente seguridad que `2022` sea ya un problema “operativamente absorbido” por el sistema general.

### Fórmula prudente de cierre

La lectura más disciplinada es:

- `2022` sigue siendo **contextualmente problemático**;
- el general demuestra que puede **rendir aceptablemente** dentro de ese contexto;
- pero la forma concreta en que lo hace sigue siendo **demasiado concentrada** como para dar por resuelto el caso.

Por ello, `2022` debe mantenerse como **año problemático relevante para investigación**, aunque ahora con un matiz importante: no porque el general no pueda ganar en él, sino porque todavía no está claro que esa absorción sea suficientemente robusta y no demasiado dependiente de unos pocos episodios dominantes.
