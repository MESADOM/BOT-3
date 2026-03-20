# VERSION 2.2.2 ANALISIS 69

## 1. Objetivo

Auditar, con continuidad metodológica respecto a `ANALISIS 64–68`, si la siguiente línea de investigación debe priorizar la **modulación de exposición por régimen** o la apertura de **variantes completas del sistema** según las clases `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

Este documento mantiene explícitamente las restricciones de la secuencia reciente:

- **no** toca producción;
- **no** abre todavía variantes completas por régimen;
- **no** rediseña señales;
- **no** declara una línea ganadora por intuición;
- busca decidir **qué camino merece ser explorado primero**, no cerrar todavía un diseño operativo final.

Limitación documental que debe quedar escrita con honestidad metodológica:

- se han leído obligatoriamente `ANALISIS 64.md`, `ANALISIS 65.md`, `ANALISIS 66.md` y `ANALISIS 67.md`;
- `ANALISIS 68.md` **no está presente** en el repositorio actual, por lo que no puede usarse como evidencia literal;
- por tanto, la continuidad real de este informe descansa en la cadena verificable `64–67` y en sus conclusiones explícitas.

La pregunta central es esta: **dado el estado actual del selector y la evidencia acumulada, qué es metodológicamente más sano explorar primero: ajustar cuánto se expone el sistema según el régimen o abrir ya sistemas/reglas diferenciadas por régimen**.

---

## 2. Caminos comparados

### 2.1. Modulación de exposición

Se entiende aquí como una línea de investigación donde el **sistema general sigue siendo el mismo**, pero su intensidad de uso cambia según la clase del selector.

Eso implica, conceptualmente:

- preservar la arquitectura actual del general;
- preservar las señales ya existentes;
- usar el selector como capa de **dosificación** y no como disparador de un sistema distinto;
- investigar diferencias de tamaño, participación o agresividad según `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

Es un cambio de **exposición**, no de identidad del sistema.

### 2.2. Variantes completas del sistema

Se entiende aquí como una línea donde cada régimen podría acabar teniendo una respuesta operativa propia, por ejemplo:

- reglas distintas;
- filtros distintos;
- lógica distinta de entrada/salida;
- módulos separados o semi-separados por clase.

Aunque todavía no se diseñen esas variantes, metodológicamente esta vía ya supone un paso más agresivo:

- el selector deja de ser solo una capa de lectura o modulación;
- pasa a ser una pieza que justificaría **ramificar** el sistema en comportamientos distintos.

### 2.3. Diferencia metodológica esencial

La diferencia no es menor.

- **Modular exposición** pregunta: “si el selector ya aporta información útil, ¿podemos capturar parte de ese valor sin romper el sistema general?”.
- **Abrir variantes completas** pregunta: “si los regímenes son distintos, ¿debemos tratarlos ya como si necesitaran sistemas diferentes?”.

A la luz de `ANALISIS 64`, `65`, `66` y `67`, la primera pregunta parece de continuidad; la segunda ya es una pregunta de **ramificación estructural**.

---

## 3. Ventajas de la modulación de exposición

### 3.1. Menor agresividad sobre el sistema

La modulación de exposición es el cambio menos invasivo de los dos. Conserva:

- el sistema general como baseline;
- la lógica de señales actual;
- la interpretación ya validada de `FAVORABLE`, `MIXTO` y `PROBLEMATICO` como capas analíticas.

Por eso su **agresividad del cambio sobre el sistema** es **baja-media**, mientras que en variantes completas sería **alta**.

### 3.2. Mejor preservación del general

La evidencia reciente no sugiere que el sistema general esté roto por clase de forma tan clara como para exigir separación inmediata. Al contrario:

- `ANALISIS 64` muestra que el general gana en las tres clases, incluso en `PROBLEMATICO`;
- `MIXTO` aporta gran parte del beneficio total, aunque con más drawdown;
- `PROBLEMATICO` no equivale a inutilidad operativa, porque la pata short captura valor real;
- `ANALISIS 65` muestra que incluso un año muy hostil como `2022` fue absorbido en saldo por el general, aunque de forma concentrada y no totalmente robusta.

Eso favorece una línea que **preserve mejor el general** antes de concluir que debe fragmentarse.

### 3.3. Menor riesgo de crear demasiadas ramas del sistema

La modulación de exposición reduce el riesgo de proliferación de ramas metodológicas porque:

- no obliga a una estrategia distinta por cada clase;
- no convierte automáticamente `MIXTO` o `PROBLEMATICO` en familias completas de reglas;
- evita que cada matiz del selector termine pidiendo un módulo propio.

Esto es especialmente importante tras `ANALISIS 66`, donde `PROBLEMATICO` ya aparece como clase **no homogénea** y con subpatrones internos. Si ya dentro de `PROBLEMATICO` hay texturas distintas, abrir variantes completas demasiado pronto podría disparar una cascada de nuevas subdivisiones.

### 3.4. Mayor facilidad de auditoría

La exposición modulada es más fácil de auditar que una familia de variantes completas porque mantiene fija la identidad base del sistema. Eso ayuda a responder preguntas simples:

- qué parte del cambio viene del selector;
- qué parte viene solo de reducir o aumentar intensidad;
- si la mejora observada es estructural o simplemente efecto de poda selectiva.

En cambio, con variantes completas se mezclan varios cambios a la vez:

- cambio de régimen;
- cambio de reglas;
- cambio de cobertura;
- posible cambio de perfil de riesgo.

Por tanto, la **facilidad de auditoría** es claramente mejor en la modulación de exposición.

### 3.5. Menor riesgo de sobreajuste

La modulación de exposición suele requerir menos grados de libertad que abrir sistemas distintos por régimen. Eso importa mucho aquí porque:

- la muestra por clase no es enorme;
- `PROBLEMATICO` tiene pocos trades en la evidencia agregada de `ANALISIS 64`;
- `2022`, según `ANALISIS 65`, sale bien pero con fuerte concentración en pocos trades y bloques;
- `ANALISIS 66` deja claro que algunos subpatrones internos tienen evidencia muy limitada.

Con este estado de evidencia, abrir variantes completas eleva mucho el **riesgo de sobreajuste**, mientras que modular exposición permite investigar valor adicional con una carga paramétrica menor.

### 3.6. Puede capturar parte del valor del selector sin rediseñar señales

Esta es probablemente su mayor ventaja conceptual.

Si el selector ya parece informar sobre:

- calidad del contexto;
- estabilidad o tensión del entorno;
- asimetrías entre continuidad y fragilidad;

entonces una primera forma sana de explotar esa información no es rediseñar entradas y salidas, sino verificar si basta con **dosificar mejor** la exposición del sistema general.

Eso permite capturar parte del valor del selector **sin rediseñar señales**, lo cual encaja directamente con el momento metodológico descrito en `ANALISIS 67`: el selector ya tiene valor real para investigación, pero todavía no está totalmente maduro como base dura para una familia amplia de variantes.

### 3.7. Mejor claridad de implementación futura

Aunque aquí no se implementa nada, la claridad futura también importa.

Una línea basada en exposición:

- tiene fronteras conceptuales más limpias;
- permite iteración gradual;
- facilita pruebas escalonadas;
- deja reversible cualquier paso posterior.

Por ello, su **claridad de implementación futura** es superior a la de una ramificación completa prematura.

---

## 4. Ventajas de abrir variantes completas

### 4.1. Mayor capacidad teórica para capturar diferencias reales entre regímenes

La principal ventaja de las variantes completas es que, si los regímenes fueran realmente muy distintos entre sí, un solo sistema modulado podría quedarse corto.

Esta vía tendría sentido si la evidencia mostrara de forma clara que:

- `FAVORABLE`, `MIXTO` y `PROBLEMATICO` no solo difieren en calidad de contexto;
- sino que requieren respuestas operativas cualitativamente diferentes.

En ese caso, una variante completa podría capturar una parte del edge que la mera modulación no captura.

### 4.2. Potencial de adaptación más profunda

Frente a la exposición modulada, una variante completa ofrece más libertad para adaptar:

- timing;
- filtros;
- selección de setups;
- gestión de entradas y salidas.

Eso podría ser valioso si en el futuro se demostrara que ciertos regímenes contienen oportunidades persistentes de una naturaleza muy distinta.

### 4.3. Posible mejor ajuste a subpatrones internos complejos

`ANALISIS 66` sugiere que dentro de `PROBLEMATICO` hay bloques que no son iguales, por ejemplo:

- estrés bajista absorbible;
- transición errática;
- lateralidad hostil;
- reversión violenta.

Si esa lectura se consolidara con más evidencia, una variante completa podría ser el vehículo para tratar entornos donde el general no solo debería exponerse menos, sino comportarse **de otro modo**.

### 4.4. Posibilidad de capturar valor adicional más allá del tamaño

La exposición modulada actúa sobre intensidad. Las variantes completas, en cambio, podrían capturar valor adicional derivado de:

- evitar ciertos errores estructurales del general en contextos concretos;
- reforzar respuestas específicas donde el general solo absorbe parcialmente;
- separar mejor continuidad y ruptura cuando el selector ya tenga suficiente madurez práctica.

### 4.5. Pero sus ventajas son todavía más potenciales que demostradas

El problema es que, hoy por hoy, estas ventajas son **prospectivas**. La evidencia leída no demuestra todavía que esa mayor profundidad de adaptación deba explorarse antes que una solución más simple.

---

## 5. Riesgos de cada camino

### 5.1. Riesgos de la modulación de exposición

La modulación de exposición también tiene límites y riesgos:

1. **Puede quedarse corta.**  
   Si las diferencias entre regímenes fueran realmente estructurales, modular tamaño podría no capturar suficiente valor.

2. **Puede dar una falsa sensación de avance.**  
   Reducir o aumentar exposición puede mejorar métricas sin resolver de fondo la posible inadecuación del sistema en ciertos entornos.

3. **Puede simplificar demasiado a MIXTO.**  
   Dado que `MIXTO` aporta mucho beneficio pero también mucho drawdown en `ANALISIS 64`, un tratamiento solo por intensidad podría ocultar texturas internas relevantes.

4. **Requiere evidencia adicional, aunque menos intensa.**  
   Incluso una modulación simple necesita demostrar que hay consistencia suficiente por clase y que la señal no es puro ruido estadístico.

Aun así, su **riesgo de complejidad añadida** es claramente menor.

### 5.2. Riesgos de abrir variantes completas

Aquí los riesgos son mucho mayores en el estado actual.

1. **Riesgo alto de sobreajuste.**  
   La muestra disponible por clase y por subpatrón sigue siendo limitada para justificar sistemas separados.

2. **Complejidad añadida elevada.**  
   Ramificar por régimen multiplica decisiones, hipótesis, validaciones y puntos de fallo.

3. **Pérdida de continuidad con el general.**  
   Se pasa demasiado pronto de “el selector segmenta” a “cada clase merece un sistema”, sin una fase intermedia suficientemente auditada.

4. **Auditoría más difícil.**  
   Cuando cambian varias reglas a la vez, se vuelve más difícil saber qué mejora es real y qué mejora es fruto de mayor libertad de ajuste.

5. **Riesgo de ramificación sin final claro.**  
   Si `PROBLEMATICO` ya no es homogéneo y `MIXTO` tampoco es trivial, abrir variantes completas puede terminar arrastrando nuevas subvariantes y una arquitectura excesivamente fragmentada.

6. **Necesidad de tuning adicional mucho más alta.**  
   Una variante completa por régimen exigiría más tuning, más validación y más evidencia fuera de muestra para ser defendible.

### 5.3. Comparativa directa por métricas mínimas

| Métrica | Modulación de exposición | Variantes completas del sistema | Juicio relativo |
|---|---|---|---|
| Agresividad del cambio sobre el sistema | Baja-media | Alta | Ventaja clara para exposición |
| Riesgo de complejidad añadida | Bajo-medio | Alto | Ventaja clara para exposición |
| Compatibilidad con la evidencia actual | Alta | Media-baja | Ventaja para exposición |
| Necesidad de tuning adicional | Moderada | Alta-muy alta | Ventaja para exposición |
| Claridad de implementación futura | Alta | Media-baja | Ventaja para exposición |
| Facilidad de auditoría | Alta | Baja-media | Ventaja para exposición |
| Riesgo de sobreajuste | Medio-bajo | Alto | Ventaja para exposición |
| Necesidad de evidencia adicional | Sí, pero acotada | Sí, y mucha más | Ventaja para exposición |
| Prioridad metodológica relativa | Primera capa lógica | Capa posterior eventual | Ventaja para exposición |

La tabla no prueba que las variantes completas sean inútiles. Sí muestra que **todavía no parecen el primer paso sano**.

---

## 6. Coherencia con el estado actual del selector

### 6.1. El selector está en fase de utilidad real, no de explotación máxima

`ANALISIS 67` es muy claro en el punto central: el selector ya tiene valor práctico como herramienta de investigación, pero todavía no está plenamente cerrado como base fuerte para lanzar una familia amplia de variantes.

Eso hace que la modulación de exposición sea mucho más coherente con el estado actual del selector, porque:

- usa el valor ya demostrado del selector;
- no exige que el selector resuelva todavía toda la política operativa;
- mantiene continuidad entre segmentación analítica y posible uso operativo gradual.

### 6.2. Coherencia con FAVORABLE, MIXTO y PROBLEMATICO

La evidencia leída sugiere una lectura muy concreta de las tres clases:

- `FAVORABLE` es útil, pero no monopoliza el edge del general;
- `MIXTO` no es una clase residual, porque concentra mucho valor y también más tensión;
- `PROBLEMATICO` no equivale a “apagar sistema”, ya que el general long-short puede extraer valor, aunque con heterogeneidad interna y muestras limitadas.

Ese cuadro no empuja todavía a sistemas totalmente separados. Empuja más bien a una lectura de **dosificación prudente**:

- preservar el general;
- reconocer que las clases no valen lo mismo;
- usar el selector para graduar exposición antes de asumir que cada clase exige señales nuevas.

### 6.3. Coherencia con el caso 2022

`ANALISIS 65` es especialmente relevante aquí.

`2022` demuestra que:

- un año muy `PROBLEMATICO` puede ser absorbido por el general;
- pero esa absorción fue concentrada y no totalmente robusta;
- por tanto, el caso no autoriza a concluir que ya exista una receta estable para construir una variante propia de `PROBLEMATICO`.

Metodológicamente, esto favorece una respuesta prudente:

- primero investigar cuánto y cuándo exponerse;
- después, solo si hiciera falta, investigar si hay que cambiar la naturaleza del sistema.

### 6.4. Coherencia con la heterogeneidad interna de PROBLEMATICO

`ANALISIS 66` añade una cautela decisiva: `PROBLEMATICO` contiene subpatrones reales, pero todavía no lo bastante validados como para oficializar nuevas clases o levantar módulos completos.

Eso vuelve especialmente peligroso abrir ya variantes completas, porque podría confundirse:

- valor exploratorio de los subpatrones;
- con madurez suficiente para diseñar sistemas independientes.

La modulación de exposición es más coherente con esa ambigüedad: permite usar la clase sin exagerar la precisión actual del selector.

---

## 7. Qué camino merece prioridad

### 7.1. Juicio metodológico principal

La línea que merece ser explorada primero es la **modulación de exposición por régimen**.

No porque ya esté demostrada como solución final, sino porque es la siguiente capa metodológica más sana dados los hallazgos de `64–67`:

- preserva el sistema general mejor que una ramificación temprana;
- reduce el riesgo de sobreajuste;
- es más auditable;
- exige menos tuning adicional;
- mantiene continuidad con el grado actual de madurez del selector.

### 7.2. Por qué no deben abrirse todavía variantes completas

No se deben priorizar todavía variantes completas por tres razones acumulativas:

1. **La evidencia actual aún favorece continuidad antes que ruptura.**  
   El general no aparece claramente invalidado por clase.

2. **La heterogeneidad interna aún no está suficientemente estabilizada.**  
   Especialmente en `PROBLEMATICO`, abrir un sistema propio sería precipitar una conclusión que la evidencia todavía no cierra.

3. **La carga metodológica sería excesiva para el punto actual.**  
   Más tuning, más libertad, más riesgo de ramas artificiales y peor trazabilidad causal.

### 7.3. Prioridad metodológica relativa

Si se ordenan las fases lógicas posibles, la secuencia más sana parece ser:

1. **usar el selector para modular exposición**;
2. **auditar si esa modulación aporta valor neto robusto**;
3. **solo después** evaluar si queda una anomalía persistente que justifique variantes completas.

Por eso, la **prioridad metodológica relativa** de la modulación de exposición es **superior** a la de abrir ya variantes completas.

---

## 8. Conclusión final

La comparación metodológica y práctica entre ambos caminos deja un balance bastante nítido.

La **modulación de exposición**:

- es menos agresiva sobre el sistema;
- preserva mejor el general;
- reduce el riesgo de generar demasiadas ramas;
- es más fácil de auditar;
- requiere menos tuning adicional;
- y puede capturar parte del valor del selector sin rediseñar señales.

Las **variantes completas del sistema** conservan interés como línea futura, porque en teoría podrían capturar diferencias profundas entre regímenes o subpatrones. Sin embargo, hoy esa vía aparece más cargada de riesgo que de necesidad demostrada.

La evidencia reciente no dice todavía: “cada régimen necesita ya su propio sistema”. Dice algo más prudente y más útil: **el selector ya parece lo bastante informativo como para investigar primero una dosificación distinta del mismo sistema general**.

Dicho de forma directa: la fase siguiente más sana no es multiplicar sistemas, sino comprobar antes si el valor del selector se expresa suficientemente bien mediante una capa de exposición.

---

## 9. Recomendación: priorizar exposición / priorizar variantes / no abrir todavía ninguna

### Recomendación final

**Priorizar exposición.**

Formulación precisa de la recomendación:

- **sí** merece prioridad investigar primero la **modulación de exposición por régimen**;
- **no** merece prioridad abrir ya **variantes completas del sistema** por régimen;
- **no** parece necesario cerrar por completo toda exploración, porque la evidencia sí justifica una siguiente fase, pero esa fase debe ser la más simple y más auditable.

Por tanto, la recomendación final de `ANALISIS 69` es:

> **priorizar exposición frente a variantes completas**.

Y, en términos metodológicos, la interpretación correcta es esta:

- primero **continuidad controlada**;
- después, solo si la evidencia adicional lo obliga, **ramificación estructural**.
