# VERSION 2.2.2 ANALISIS 66

## 1. Objetivo

Estudiar si la clase `PROBLEMATICO` del selector histórico de tres clases funciona como un bloque operativamente homogéneo o si, por el contrario, contiene **subpatrones internos suficientemente reconocibles** como para merecer investigación futura.

El objetivo de este documento es deliberadamente prudente:

- trabajar **solo** sobre periodos ya clasificados como `PROBLEMATICO`;
- **no** cambiar la taxonomía oficial `FAVORABLE / MIXTO / PROBLEMATICO`;
- **no** oficializar nuevas clases;
- **no** abrir estrategias nuevas por subtipo;
- evaluar si los subpatrones observados tienen contenido operativo real o si son todavía solo etiquetas narrativas.

Limitación documental que debe quedar explícita:

- se han leído obligatoriamente `ANALISIS 61.md`, `ANALISIS 62.md` y `ANALISIS 63.md`, que sí existen en el repositorio;
- `ANALISIS 64.md` y `ANALISIS 65.md` **no están presentes** en el árbol actual del repositorio, por lo que no han podido ser leídos literalmente;
- para no inventar evidencia inexistente, este documento se apoya en la cadena verificable `ANALISIS 57–63` y en la reconstrucción directa de periodos `PROBLEMATICO` desde `META_BOT.py`.

## 2. Clase PROBLEMATICO analizada

Se mantiene exactamente la taxonomía auditada en la cadena previa:

- `FAVORABLE` si `score_regimen >= 2`;
- `MIXTO` si `score_regimen = 0 o 1`;
- `PROBLEMATICO` si `score_regimen <= -1`.

La lógica base sigue siendo la ya usada en los análisis previos:

- ancla estructural: `QQQ > SMA200`;
- lectura intermedia: `Retorno 63`;
- componente de ruido: `Cruces SMA50`.

El estudio se ha hecho exclusivamente sobre episodios continuos `PROBLEMATICO` reconstruidos desde el histórico preparado por `META_BOT.py`, restringiendo la lectura principal al tramo `2014–2026-03` para mantener consistencia con la etapa donde ya existen `SMA200` y `Retorno 63` con historial suficiente.

### Peso total observado dentro de PROBLEMATICO

En el tramo útil `2014–2026-03` aparecen `12` episodios continuos `PROBLEMATICO`, con `471` sesiones en total. La separación prudente de patrones internos deja este reparto:

| Subpatrón observado | Episodios | Sesiones | Peso temporal dentro de PROBLEMATICO |
|---|---:|---:|---:|
| Estrés bajista absorbible | 3 | 233 | 49,5% |
| Transición errática | 3 | 142 | 30,1% |
| Lateralidad hostil | 5 | 72 | 15,3% |
| Reversión violenta | 1 | 24 | 5,1% |

Primera lectura:

- `PROBLEMATICO` **no parece perfectamente homogéneo**;
- pero tampoco aparecen diez familias distintas: la evidencia visible se concentra en **pocos patrones repetidos**;
- el bloque dominante no es la lateralidad, sino el **estrés bajista persistente con distintos grados de absorción por el sistema**.

## 3. Patrones internos observados

La separación siguiente **no es una taxonomía nueva oficial**, sino una organización exploratoria de los periodos `PROBLEMATICO` observados.

### 3.1. Estrés bajista absorbible

Definición operativa provisional:

- deterioro prolongado;
- fuerte presencia de `SHORT_TREND` dentro del episodio;
- hostilidad real del mercado, pero con suficiente continuidad como para que el sistema general conserve o incluso mejore su comportamiento por la pata short;
- no es un entorno cómodo, pero sí uno donde la hostilidad es relativamente legible.

Casos observados:

- `2018-10-29` a `2019-02-15`;
- `2022-04-11` a `2022-08-05`;
- `2022-09-26` a `2023-01-13`.

Rasgos comunes:

- episodios largos: `75`, `81` y `77` sesiones;
- predominio alto de `SHORT_TREND`: `80,0%`, `93,8%` y `63,6%`;
- poca o nula dependencia de `NO_TRADE` salvo en la fase final del tercer caso;
- daño de mercado visible, pero con una trayectoria más explotable que caótica.

Juicio:

- este subtipo **sí tiene sentido real**;
- es el candidato más serio a futura investigación, porque no solo describe “mercado malo”, sino “mercado malo pero suficientemente direccional como para que el general no sufra igual que en otros tramos problemáticos”.

### 3.2. Transición errática

Definición operativa provisional:

- episodio `PROBLEMATICO` donde sí hay deterioro relevante, pero combinado con rebotes fuertes, cambios de convicción y textura de mercado poco estable;
- el problema no es solo la caída, sino la **irregularidad del viaje**;
- el selector detecta hostilidad, pero esa hostilidad no es tan lineal ni tan aprovechable como en el patrón anterior.

Casos observados:

- `2016-01-11` a `2016-03-18`;
- `2022-01-24` a `2022-04-01`;
- `2025-03-10` a `2025-05-09`.

Rasgos comunes:

- amplitud elevada y rebotes grandes dentro del mismo episodio;
- predominio de `SHORT_TREND`, pero con resultados del general mucho menos consistentes;
- mezcla entre lectura bajista estructural y secuencias de reversión parcial que complican la absorción operativa.

Juicio:

- este subtipo también **tiene sentido real**;
- pero la evidencia todavía indica una familia **menos estable** que la anterior;
- por ahora conviene tratarlo como una hipótesis de trabajo, no como régimen futuro listo para independizarse.

### 3.3. Lateralidad hostil

Definición operativa provisional:

- episodios `PROBLEMATICO` cortos o de convicción incompleta;
- fuerte peso de `NO_TRADE`;
- roce hostil, ruido o deterioro parcial, pero sin una persistencia bajista suficientemente limpia;
- el entorno es incómodo para el sistema general más por falta de claridad que por tendencia bajista sostenida.

Casos observados:

- `2015-08-24` a `2015-10-16`;
- `2016-03-28` a `2016-04-01`;
- `2016-06-20` a `2016-07-08`;
- `2019-06-03` a `2019-06-07`;
- `2022-08-29` a `2022-09-09`.

Rasgos comunes:

- cinco episodios, pero solo `15,3%` del tiempo total `PROBLEMATICO`;
- dominio claro de `NO_TRADE` en cuatro de los cinco casos;
- escasa continuidad para la pata short;
- episodios más cercanos a “entorno incómodo y poco legible” que a “bear phase plenamente estructurada”.

Juicio:

- este patrón **tiene sentido descriptivo**;
- sí parece algo más que pura narrativa;
- aun así, su valor operativo todavía es **moderado**, porque la muestra es fragmentada y con muy pocas operaciones del general encima.

### 3.4. Reversión violenta

Definición operativa provisional:

- shock rápido con derribo fuerte y rebote igualmente fuerte;
- episodio muy concentrado en pocas semanas;
- el problema no es la persistencia bajista, sino la violencia de ida y vuelta.

Caso observado:

- `2020-03-09` a `2020-04-09`.

Rasgos:

- `24` sesiones;
- drawdown interno alto y rebote posterior muy rápido;
- peso alto de `SHORT_TREND`, pero sin suficiente repetición histórica dentro de esta taxonomía como para afirmar que ya existe un subtipo robusto y estable.

Juicio:

- como patrón visual e histórico, **sí existe**;
- como subtipo operativamente validado dentro de `PROBLEMATICO`, la evidencia es **insuficiente** porque la muestra aquí es prácticamente un caso único.

## 4. Rendimiento del general por subpatrón

El criterio relevante no es solo si el mercado fue distinto, sino si el **sistema general** rindió de manera parecida o muy diferente según el subpatrón.

Para no sobredimensionar la precisión, la lectura se hace con métricas simples y prudentes:

- número de episodios por subpatrón;
- peso temporal;
- nº de operaciones del general solapadas con esos episodios;
- win rate observado en esas operaciones;
- beneficio neto agregado del general dentro de esos periodos.

### Resumen comparativo

| Subpatrón | Episodios | Sesiones | Operaciones del general solapadas | Win rate observado | Beneficio neto agregado € | Lectura operativa |
|---|---:|---:|---:|---:|---:|---|
| Estrés bajista absorbible | 3 | 233 | 4 | 100% | +4.190,18 | Mejor comportamiento relativo del general |
| Transición errática | 3 | 142 | 5 | 60,0% | +341,09 | Comportamiento irregular y mucho menos fiable |
| Lateralidad hostil | 5 | 72 | 1 | 0,0% | -54,00 | Prácticamente sin tracción operativa del general |
| Reversión violenta | 1 | 24 | 0 | n/a | 0,00 | Sin muestra suficiente para juzgar al general |

### Lectura por subpatrón

#### A. Estrés bajista absorbible

Es el caso donde el general sale claramente mejor parado.

- `4` operaciones solapadas;
- `100%` de acierto en la muestra observada;
- `+4.190,18 €` agregados;
- concentra casi la mitad del tiempo `PROBLEMATICO` (`49,5%`).

Interpretación prudente:

- no significa que este entorno sea “bueno” en sentido absoluto;
- sí significa que dentro de `PROBLEMATICO` hay un bloque donde la hostilidad es más **ordenada** y el general parece absorberla razonablemente bien.

#### B. Transición errática

Aquí el comportamiento cambia bastante.

- `5` operaciones solapadas;
- win rate de `60,0%`;
- beneficio agregado de solo `+341,09 €`, muy inferior al subtipo anterior y claramente más frágil;
- además, la dispersión interna es alta: `2016-01/03` y `2025-03/05` salen flojos o negativos, mientras `2022-01/04` sale mejor.

Interpretación prudente:

- este patrón ya no parece solo “mercado hostil”;
- parece un entorno donde el general pierde mucha consistencia y donde la rentabilidad depende más de trayectorias concretas que de una ventaja estable.

#### C. Lateralidad hostil

Es el patrón con peor legibilidad operativa.

- `5` episodios, pero solo `1` operación del general en total;
- esa única operación fue perdedora (`-54,00 €`);
- la mayor parte del tiempo el selector operativo cae en `NO_TRADE`, señal de falta de continuidad exploitable.

Interpretación prudente:

- esto respalda la idea de que no todo `PROBLEMATICO` es lo mismo;
- aquí el problema no es tanto “bear market absorbible” como **fricción y falta de dirección útil**.

#### D. Reversión violenta

- `1` episodio;
- `0` operaciones del general solapadas;
- por tanto, no hay base suficiente para comparar rendimiento real del sistema.

Interpretación prudente:

- el patrón existe históricamente;
- pero todavía no hay evidencia operativa suficiente para concluir cómo se comporta el general de manera repetible en él.

### Juicio comparativo central

La diferencia entre subpatrones **no parece pequeña**:

- el general rinde **mucho mejor** en `estrés bajista absorbible`;
- rinde **de forma mucho menos fiable** en `transición errática`;
- y casi no tiene tracción en `lateralidad hostil`.

Por tanto, la idea de que toda la clase `PROBLEMATICO` se comporta operativamente igual queda **debilitada**.

## 5. Relación de 2022 con esos subpatrones

La pregunta clave no es solo si `2022` fue `PROBLEMATICO`, sino **qué tipo de PROBLEMATICO fue**.

### Descomposición interna de 2022

Dentro de la propia clase `PROBLEMATICO`, `2022` no aparece como un bloque único y homogéneo, sino como una combinación de al menos tres texturas:

1. **Transición errática** (`2022-01-24` a `2022-04-01`)
   - apertura muy inestable del año;
   - caída con rebotes fuertes;
   - hostilidad real, pero todavía cambiante.

2. **Estrés bajista absorbible** (`2022-04-11` a `2022-08-05`)
   - es el corazón más claro del año;
   - alta persistencia de `SHORT_TREND` (`93,8%`);
   - el general rindió especialmente bien aquí.

3. **Lateralidad hostil** (`2022-08-29` a `2022-09-09`)
   - pausa corta, incómoda y poco direccional;
   - más ruido que tendencia aprovechable.

4. **Estrés bajista absorbible** otra vez (`2022-09-26` a `2023-01-13`)
   - reanudación de la presión negativa;
   - menos limpia que la fase primavera-verano, pero aún reconocible dentro del mismo bloque dominante.

### Juicio sobre 2022

`2022` **sí se parece** a otros periodos `PROBLEMATICO`, pero no a todos por igual.

#### Casos parecidos a 2022

Los parecidos más útiles son parciales, no perfectos:

- **`2018-10-29` a `2019-02-15`**: se parece al `2022` más absorbible, porque combina deterioro serio con suficiente persistencia bajista para que el general no quede ciego.
- **`2016-01-11` a `2016-03-18`**: se parece al `2022` inicial más errático, por la mezcla de tensión real y rebotes complicados.
- **`2025-03-10` a `2025-05-09`**: recuerda parcialmente al `2022` de transición errática, aunque con peor saldo para el general y menos peso estructural.

#### Casos claramente distintos de 2022

- **`2015-08-24` a `2015-10-16`**: demasiado dominado por `NO_TRADE` y lateralidad hostil; se parece poco al núcleo direccional de 2022.
- **`2019-06-03` a `2019-06-07`**: episodio demasiado breve y ligero para compararlo con 2022.
- **`2020-03-09` a `2020-04-09`**: se parece en violencia, pero no en persistencia; el shock pandémico fue una reversión extrema mucho más singular.

### Conclusión específica sobre 2022

`2022` no debe tratarse como un subtipo independiente por sí solo, pero tampoco como un `PROBLEMATICO` cualquiera.

La lectura más defendible es esta:

- `2022` es sobre todo un **compuesto** de `transición errática` + `estrés bajista absorbible`, con una pequeña pausa de `lateralidad hostil`;
- por tanto, se parece bastante al subtipo más serio a estudiar en el futuro, pero **no equivale** a todo `PROBLEMATICO`.

## 6. Evidencia a favor de subdividir

La evidencia a favor de investigar subtipos dentro de `PROBLEMATICO` es real, aunque todavía no definitiva.

### A favor

1. **Hay más de un patrón observable y repetido.**  
   No aparecen solo diferencias narrativas vagas: se distinguen al menos `3` familias repetidas con algo de consistencia (`estrés bajista absorbible`, `transición errática`, `lateralidad hostil`), más un caso singular de `reversión violenta`.

2. **El rendimiento del general cambia bastante según el subtipo.**  
   La distancia entre `+4.190,18 €` en `estrés bajista absorbible` y `-54,00 €` en `lateralidad hostil`, con `+341,09 €` muy frágiles en `transición errática`, es demasiado grande como para despacharla como simple ruido menor.

3. **El peso temporal dominante está concentrado en un subtipo específico.**  
   Casi la mitad del tiempo `PROBLEMATICO` (`49,5%`) cae en `estrés bajista absorbible`, lo cual sugiere que una posible investigación futura no dependería solo de casos anecdóticos.

4. **2022 no es homogéneo internamente.**  
   El año crítico de la serie no sale como un bloque único, sino como mezcla de subtexturas. Eso refuerza la idea de que la clase `PROBLEMATICO` actual probablemente está agregando fenómenos distintos.

5. **La diferencia entre `SHORT_TREND` y `NO_TRADE` también cambia por patrón.**  
   Eso sugiere que los subpatrones no solo son psicológicos o narrativos, sino que afectan a la forma concreta en que el sistema termina operando o absteniéndose.

## 7. Evidencia en contra de subdividir

La prudencia sigue siendo necesaria. También hay argumentos fuertes **contra** formalizar demasiado pronto una subdivisión operativa.

### En contra

1. **La muestra sigue siendo pequeña.**  
   Solo hay `12` episodios `PROBLEMATICO` útiles en `2014–2026`, y varios subtipos se apoyan en muy pocos casos.

2. **La parte más singular apenas tiene repetición.**  
   `Reversión violenta` es, de momento, básicamente un caso (`2020`). Eso no basta para elevarla a subtipo operativo futuro sin riesgo alto de sobreinterpretación.

3. **La asignación de subpatrones todavía contiene juicio cualitativo.**  
   La separación usada aquí está razonada con métricas, pero no nace todavía de una regla cerrada, estable y validada fuera de muestra. Eso obliga a evitar cualquier formalización prematura.

4. **La muestra de operaciones del general por subtipo es limitada.**  
   En especial, `lateralidad hostil` y `reversión violenta` tienen muy pocas operaciones o ninguna. La diferencia observada puede ser real, pero aún necesita más evidencia para convertirse en decisión estructural.

5. **Parte de la diferencia puede deberse a duración y no solo a textura.**  
   Los episodios más largos tienden a ofrecer más oportunidades al general. Por tanto, parte de la superioridad del `estrés bajista absorbible` puede venir de mayor persistencia temporal y no exclusivamente de una esencia distinta del patrón.

6. **El selector base sigue siendo una herramienta de investigación, no una frontera cerrada.**  
   `ANALISIS 63` ya advertía que la taxonomía aún no está madura para saltos metodológicos agresivos. Subdividir demasiado pronto podría convertir una buena hipótesis analítica en una falsa taxonomía rígida.

## 8. Conclusión final

La clase `PROBLEMATICO` **no parece operativamente homogénea**.

La evidencia disponible sugiere, al menos, esta estructura interna provisional:

- un bloque dominante de **estrés bajista absorbible**, donde la hostilidad del mercado es real pero relativamente legible para el general;
- un bloque de **transición errática**, donde el mercado sigue siendo hostil pero mucho menos limpio y el general pierde consistencia;
- una **lateralidad hostil** más corta y menos direccional, donde la fricción domina sobre la tendencia;
- y una **reversión violenta** que existe históricamente, pero aún sin evidencia suficiente para tratarla como familia robusta.

Dicho de otra forma:

- la idea de subtipos **no parece mera narrativa**;
- pero todavía **no está suficientemente cerrada** como para convertirla ya en taxonomía formal o en base para nuevas estrategias.

Sobre `2022`, el juicio más prudente es que:

- sí pertenece claramente a `PROBLEMATICO`;
- pero dentro de esa clase es un **caso compuesto**, no un bloque uniforme;
- se parece sobre todo a los tramos de `estrés bajista absorbible`, con una fase inicial de `transición errática` y una pausa breve de `lateralidad hostil`.

## 9. Recomendación: mantener PROBLEMATICO unido / estudiar subtipos en el futuro / evidencia insuficiente todavía

### Recomendación final

**Estudiar subtipos en el futuro.**

### Razón

Es la opción más prudente y mejor alineada con la evidencia actual porque:

- ya hay señales suficientes para decir que `PROBLEMATICO` **probablemente contiene subtipos reales**;
- aún no hay base suficiente para **subdividir oficialmente** la clase ni para diseñar una estrategia por subtipo;
- mantener `PROBLEMATICO` unido en la taxonomía oficial sigue siendo lo correcto hoy;
- pero ignorar estas diferencias internas también sería perder información potencialmente valiosa.

Por tanto, la salida metodológicamente sana es:

1. **mantener la clase oficial `PROBLEMATICO` sin cambios**;
2. **aceptar que no es perfectamente homogénea**;
3. **usar estos subpatrones solo como hipótesis de investigación futura**, especialmente en torno a la diferencia entre:
   - `estrés bajista absorbible`,
   - `transición errática`,
   - y `lateralidad hostil`.

Eso preserva la prudencia, evita crear taxonomía débil y deja abierta una línea de investigación futura con fundamento mejor que puramente narrativo.
