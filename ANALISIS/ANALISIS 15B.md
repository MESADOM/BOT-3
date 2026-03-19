# VERSION 2.2.1 ANALISIS 15b

## 1. Objetivo

Comparar conjuntamente los hallazgos de `ANALISIS 12`, `ANALISIS 13` y `ANALISIS 14` para decidir qué línea de mejora de la versión base **2.2.1** merece pasar a una futura candidata **2.2.2**, **sin modificar producción**, **sin declarar todavía una versión ganadora definitiva** y **sin elevar más de una línea principal como candidata prioritaria**.

Alcance real de lectura en esta tarea:
- `ANALISIS/ANALISIS 12.md`: **presente**.
- `ANALISIS/ANALISIS 13.md`: **presente**.
- `ANALISIS/ANALISIS 14.md`: **presente**.

No faltó ninguno de los tres archivos exigidos.

## 2. Comparación conjunta de las 3 líneas

Las tres líneas analizadas atacan problemas distintos del módulo short actual, y por eso no deben juzgarse solo por “si mejoran algo”, sino por **qué problema resuelven**, **a qué coste** y **con cuánta robustez aparente**.

### A. Filtro anti-sobreextensión

Esta línea parte de una hipótesis bien enfocada: el short de la 2.2.1 no parece fallar principalmente por falta de sesgo bajista, sino por entrar a veces **demasiado tarde en caídas ya muy maduras**. Ese diagnóstico es coherente con el comportamiento observado en falsos positivos concretos.

Lo importante no es solo que esta línea generase variantes “mejores”, sino **cómo** lo hizo:
- la variante por distancia a `SMA200` mejoró retorno total, Sharpe y profit factor short frente a la base;
- además redujo algunos perdedores relevantes sin destruir demasiada captura válida;
- la señal útil apareció justo donde tenía que aparecer: en el **timing** de shorts tardíos, no en una relajación indiscriminada del permiso short.

Ahora bien, la mejora tampoco fue completa ni limpia:
- no resolvió todos los casos problemáticos;
- siguió dejando vivo el caso de `2025-04-15`;
- y parte de la mejora depende de sustituciones de timing dentro del mismo tramo bajista.

Por tanto, esta línea muestra **potencial real**, pero todavía no robustez suficiente como para elevarla a cambio de producción.

### B. Revisión del bloqueo estructural `SMA50 < SMA200`

Esta línea tenía una lógica atractiva sobre el papel: si el short llega tarde, quizá exigir `SMA50 < SMA200` bloquea entradas que deberían activarse antes. Sin embargo, al contrastarla con resultados, la lectura fue bastante clara.

Sí apareció una mejora puntual de captura:
- las variantes lograron abrir antes en algún tramo que la base no capturaba.

Pero el balance conjunto fue desfavorable:
- la mejora de captura fue mínima;
- el coste en ruido fue alto;
- todas las variantes empeoraron el beneficio neto del sistema frente a la base;
- incluso la opción más “defendible” por drawdown redujo demasiado la aportación short y la calidad global.

La conclusión comparativa aquí es importante: esta línea **sí toca un síntoma real** —la tardanza—, pero lo hace por una vía demasiado burda. En vez de mejorar la calidad del timing, en la práctica compra algo de anticipación a costa de muchos más falsos positivos.

### C. Ajustes del trailing short

Esta línea era conceptualmente más conservadora: no intentaba cambiar entradas, sino mejorar eficiencia de salida alrededor del trailing actual del `8%`.

Su problema no fue tanto empeorar de forma masiva, sino algo más decisivo para priorización:
- casi no hubo sensibilidad útil en el vecindario razonable del `8%`;
- `7%`, `8%`, `9%` y la variante adaptativa simple produjeron los mismos resultados en la muestra;
- `6%` empeoró;
- `10%` empeoró claramente.

Eso significa que esta línea no ofrece una mejora candidata clara, ni siquiera en forma exploratoria fuerte. El hallazgo útil del análisis 14 no es “hay una alternativa prometedora”, sino más bien lo contrario: **el 8% actual ya parece un punto de equilibrio suficientemente bueno** dentro del espacio probado.

### Comparación cruzada final

Si se comparan las tres líneas con el mismo criterio estratégico:

- **Filtro anti-sobreextensión**: es la única línea que muestra una mejora plausible alineada con el problema correcto y con resultados agregados favorables en al menos una variante.
- **Revisión de `SMA50 < SMA200`**: identifica un bloqueo real, pero su relajación añade demasiado ruido para la pequeña mejora conseguida.
- **Trailing short**: es la línea más estable, pero precisamente por eso no ofrece señal de mejora material; sirve más para confirmar que el 8% no es el problema principal.

## 3. Mejor línea candidata

La **mejor línea candidata** para estudiar de cara a una futura **2.2.2** es el **filtro anti-sobreextensión**, con foco principal en la familia de filtros basada en **distancia del precio a la `SMA200`**.

Motivos de priorización:
- es la única línea que mostró **potencial real** de mejora del sistema completo, no solo una mejora parcial aislada;
- actúa sobre el problema más convincente de la base short: la **entrada tardía en caídas maduras**;
- lo hace de forma más selectiva que relajar el bloqueo estructural;
- y su coste en robustez aparente, aunque relevante, fue menor que el observado en la revisión de `SMA50 < SMA200`.

Dicho con precisión: no es una línea ganadora definitiva, pero sí la **única candidata prioritaria razonable** entre las tres.

## 4. Línea secundaria opcional

Si hubiera que dejar **una sola línea secundaria opcional**, sería **ninguna como prioridad real de desarrollo**, pero entre las dos restantes la menos problemática para mantener en observación sería la de **ajustes del trailing short**, no para promover cambios inmediatos, sino como línea ya casi cerrada.

La razón es simple:
- el análisis 14 sugiere que el trailing del `8%` ya está bien situado;
- no aparece una variante mejor, pero sí una conclusión útil y relativamente robusta;
- por eso no merece prioridad de investigación, aunque tampoco requiere reabrirse salvo que cambien antes las entradas.

En otras palabras, esta línea puede quedar como **secundaria solo en sentido documental**, no como candidata seria a corto plazo.

## 5. Línea a descartar o aplazar

La línea que debería **descartarse o aplazarse** es la **revisión del bloqueo estructural `SMA50 < SMA200`** como vía principal para mejorar la 2.2.1.

Motivos:
- la mejora de captura lograda fue demasiado pequeña;
- el incremento de falsos positivos fue demasiado alto;
- todas las variantes empeoraron el beneficio neto del sistema;
- y la relajación del filtro parece atacar la tardanza con una herramienta demasiado amplia, empeorando la robustez del módulo short.

La palabra adecuada aquí es **aplazar con sesgo a descarte**: no porque la intuición original sea absurda, sino porque esta ronda ya mostró que, en su forma práctica más razonable, **no compensa**.

## 6. Riesgos de sobreajuste

Los riesgos de sobreajuste existen en las tres líneas, pero no con la misma intensidad ni del mismo tipo.

### Línea con más riesgo de sobreajuste

La línea con **más riesgo de sobreajuste** es el **filtro anti-sobreextensión**.

No porque sea la peor, sino precisamente porque es la más prometedora y la que más fácilmente puede seducir con una mejora que aún descansa sobre una muestra short pequeña.

Riesgos concretos:
- la base short trabaja con muy pocos trades;
- un cambio de uno o dos casos altera mucho las métricas;
- los umbrales de sobreextensión son especialmente sensibles;
- y parte de la mejora observada proviene de desplazar el timing, no solo de eliminar entradas malas.

Es decir: esta es la mejor candidata, pero también la que más disciplina exige para no convertir una señal útil en una falsa victoria por ajuste fino.

### Riesgo intermedio

La revisión de `SMA50 < SMA200` también tiene riesgo de sobreajuste, sobre todo porque podría forzarse una narrativa de “captura más temprana” basada en episodios concretos. Aun así, el análisis 13 ya fue bastante severo con esa tentación: como el resultado global empeora con claridad, el riesgo queda parcialmente contenido por la propia evidencia negativa.

### Riesgo menor en esta ronda

Los ajustes del trailing short presentan el menor riesgo de sobreajuste dentro de esta comparación, porque la evidencia dominante no es una mejora aparente dudosa, sino la ausencia de una mejora observable. Aquí el peligro no es tanto sobreajustar una falsa señal positiva, sino perder tiempo intentando exprimir una zona donde el histórico no mostró sensibilidad útil.

## 7. Recomendación de siguiente paso

El siguiente paso recomendado es **una revisión adicional, breve y muy controlada, solo sobre la línea de filtro anti-sobreextensión**, sin abrir de nuevo las otras dos como frentes principales.

Ese siguiente paso debería centrarse en:
- validar si la mejora alrededor de la **distancia a `SMA200`** se mantiene con una familia muy corta de umbrales cercanos;
- comprobar si la mejora sigue existiendo cuando se penaliza explícitamente la dependencia de sustituciones de timing;
- revisar de forma específica los casos que siguen sin resolverse, en especial el short tardío de `2025-04-15`;
- y confirmar que no se deteriora la captura válida que sí aporta el bloque short en episodios buenos.

Lo importante no es “optimizar más”, sino **intentar refutar** la única señal prometedora encontrada. Si sobrevive a una revisión corta y exigente, entonces sí merecería pasar a discusión seria para una candidata 2.2.2. Si no sobrevive, la lectura correcta sería mantener la base actual sin forzar una mejora artificial.

## 8. Conclusión final clara y breve

De las tres líneas estudiadas, la **única que merece pasar como candidata prioritaria a una futura 2.2.2** es el **filtro anti-sobreextensión**, especialmente en torno a la distancia a `SMA200`; la revisión de `SMA50 < SMA200` debería **aplazarse o descartarse** por exceso de ruido, y los ajustes del trailing short deberían **quedar cerrados por ahora** porque no mostraron una mejora material frente al `8%` actual.
