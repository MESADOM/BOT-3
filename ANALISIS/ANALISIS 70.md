# VERSION 2.2.2 ANALISIS 70

## 1. Objetivo

Estudiar de forma específica si la familia de reglas basada en un **tope máximo nominal de entrada** merece pasar a una fase posterior de pruebas históricas, manteniéndose todavía dentro del marco del **sistema general vigente**, usando el **selector como segmentación de contexto** y sin tocar producción.

El foco exacto de este documento es más estrecho que el de una validación operativa:

- **no** se implementa nada en producción;
- **no** se fija todavía un tope definitivo;
- **no** se declara óptimo ningún valor nominal concreto;
- **no** se convierte esta hipótesis en regla candidata final;
- se estudia si la familia **“tope máximo nominal por régimen”** tiene suficiente sentido conceptual como para justificar backtest posterior.

Además, debe quedar explícita una distinción metodológica central:

- **estudiar una familia** significa evaluar si la idea tiene lógica, claridad y potencial investigable;
- **validar un parámetro** significaría concluir que un importe concreto —por ejemplo `5000 €`— ya es adecuado para el sistema.

Este documento solo hace lo primero, no lo segundo.

Limitación documental explícita:

- se han leído obligatoriamente `ANALISIS 64.md`, `ANALISIS 65.md`, `ANALISIS 66.md` y `ANALISIS 67.md`, que sí existen en el repositorio actual;
- `ANALISIS 68.md` y `ANALISIS 69.md` **no existen** en el árbol actual, por lo que no han podido ser leídos literalmente;
- por disciplina metodológica, no se inventa contenido ausente y la conclusión se apoya en la evidencia verificable disponible.

## 2. Familia de reglas estudiada

La familia analizada introduce una restricción adicional sobre el tamaño de entrada del sistema: un **tope máximo nominal** expresado en euros que impide que una entrada supere cierto importe absoluto, aunque otras reglas del sistema permitieran un tamaño mayor.

Se estudian tres variantes conceptuales:

### A. Tope máximo nominal igual para todos los regímenes

La misma barrera nominal se aplicaría siempre, con independencia de que el selector clasifique el contexto como:

- `FAVORABLE`;
- `MIXTO`;
- `PROBLEMATICO`.

Ejemplo conceptual:

- ninguna entrada podría superar `5000 €`, sin importar el régimen detectado.

Ventaja conceptual principal:

- es la variante más simple de explicar, auditar e implementar.

Debilidad principal:

- ignora precisamente la información que el selector aporta sobre diferencias de contexto.

### B. Tope máximo nominal condicionado por régimen

La barrera nominal existiría, pero su severidad dependería de la clase del selector. Por ejemplo, en términos puramente conceptuales:

- un régimen `PROBLEMATICO` podría admitir menos tamaño nominal máximo;
- un régimen `MIXTO` podría quedar en una zona intermedia;
- un régimen `FAVORABLE` podría conservar más libertad o incluso no quedar tan constreñido.

Aquí el ejemplo de `5000 €` se usa solo como referencia pedagógica para imaginar cómo funcionaría una barrera nominal, no como propuesta cerrada.

Ventaja conceptual principal:

- intenta alinear la restricción de tamaño con la información contextual del selector.

Debilidad principal:

- añade complejidad y abre la puerta a arbitrariedad doble: no solo el valor nominal, sino también su reparto por régimen.

### C. Ausencia de tope nominal

Se mantiene el sistema sin barrera máxima nominal explícita de entrada.

Ventaja conceptual principal:

- evita introducir rigidez adicional y deja que el motor actual exprese toda su expansión cuando las demás reglas lo permiten.

Debilidad principal:

- si existen contextos donde el sistema escala demasiado en situaciones dudosas, esta opción no ofrece ningún freno específico.

## 3. Qué problema intenta resolver

La familia de reglas estudiada intenta responder a una inquietud muy concreta: si el sistema general vigente puede llegar a **expandir demasiado el tamaño nominal de entrada** en contextos donde esa expansión quizá no esté suficientemente justificada por la calidad del entorno.

A nivel conceptual, esta familia trataría de resolver tres problemas potenciales:

### 3.1. Contener expansión excesiva en contextos dudosos

Los análisis recientes muestran que `MIXTO` no es una clase vacía y que incluso aporta gran parte del beneficio del sistema general, pero también aparece asociada a mayor tensión y mayor irregularidad que `FAVORABLE`. Desde esa lectura, un tope nominal podría actuar como una forma de impedir que el sistema convierta una zona de valor real pero ambigua en una fuente de exposición demasiado agresiva.

### 3.2. Limitar exposición en PROBLEMATICO

La evidencia previa también muestra que `PROBLEMATICO` no equivale a inutilidad operativa, porque la pata short del sistema puede monetizar bien ciertos episodios hostiles. Sin embargo, `PROBLEMATICO` sigue representando un entorno de fricción estructural y no un contexto cómodo. Por eso, la hipótesis de imponer un tope nominal más exigente en esta clase intenta reducir el riesgo de que un episodio hostil pero mal absorbido concentre un tamaño excesivo.

### 3.3. Mantener más libertad en FAVORABLE

Si el selector realmente aporta segmentación útil, no tendría demasiado sentido que una restricción pensada para proteger al sistema en contextos dudosos castigara igual a los tramos `FAVORABLE`. De ahí nace el interés de la variante condicionada por régimen: preservar mayor libertad donde el contexto parece más limpio y reservar la disciplina adicional para `MIXTO` o `PROBLEMATICO`.

## 4. Valor potencial por régimen

El interés de esta familia no es uniforme entre las tres clases del selector.

### FAVORABLE

Valor potencial conceptual: **bajo a moderado**.

Razón:

- `FAVORABLE` representa el bloque donde más sentido tiene dejar respirar al sistema si realmente el contexto es sano;
- imponer un tope nominal duro y uniforme aquí podría recortar innecesariamente la expansión en años fuertes;
- por ello, dentro de esta familia, `FAVORABLE` parece más compatible con libertad alta o con un tope relativamente laxo que con una barrera rígida severa.

La principal advertencia aquí es clara: si se fija un tope nominal demasiado bajo, se corre el riesgo de **capar precisamente los tramos que más justifican dejar correr el sistema**.

### MIXTO

Valor potencial conceptual: **moderado a alto**.

Razón:

- `MIXTO` es útil y productivo, pero no es limpio;
- concentra gran parte del beneficio del sistema general, aunque con mayor tensión y mayor drawdown relativo;
- eso lo convierte en el régimen donde un tope nominal podría tener más sentido como herramienta de disciplina sin necesidad de bloquear totalmente la operativa.

En otras palabras, `MIXTO` parece el principal candidato para estudiar si una restricción nominal ayuda a moderar expansión excesiva sin destruir todo el edge de transición que la clase parece contener.

### PROBLEMATICO

Valor potencial conceptual: **alto, pero con cautela metodológica**.

Razón:

- la clase sí merece tratamiento prudente porque representa contexto hostil;
- además, la evidencia reciente sugiere que dentro de `PROBLEMATICO` conviven subpatrones diferentes: algunos más absorbibles y otros claramente peores;
- eso vuelve razonable la intuición de no permitir la misma libertad nominal que en `FAVORABLE`.

Pero la cautela es imprescindible:

- un tope demasiado estricto podría estropear precisamente los episodios `PROBLEMATICO` donde el sistema general short sí funciona bien;
- por tanto, aquí la familia no debe entenderse como “reducir siempre al máximo”, sino como explorar si existe una forma razonable de **limitar exposición sin anular la captura útil**.

## 5. Riesgos y debilidades

La familia “tope máximo nominal por régimen” no solo ofrece beneficios potenciales; también introduce riesgos conceptuales importantes.

### 5.1. Capar demasiado años fuertes

Este es probablemente el riesgo más claro.

Si el sistema entra en una fase muy favorable y su lógica interna permitiría crecer más, un tope nominal demasiado bajo puede impedir que esa expansión se exprese. El daño sería especialmente serio si se usa un tope uniforme para todos los regímenes, porque convertiría una herramienta defensiva en un freno general permanente.

### 5.2. Introducir rigidez innecesaria

El sistema ya dispone de reglas, filtros y del propio selector como capa de segmentación. Añadir un tope nominal absoluto introduce una rigidez artificial que puede ser útil si corrige un exceso real, pero puede ser redundante si ese exceso no es un problema material. Esta familia solo merece avanzar si el tope aporta disciplina adicional reconocible y no una mera complicación cosmética.

### 5.3. Depender de un valor nominal demasiado arbitrario

Aquí aparece uno de los mayores problemas metodológicos.

Un valor como `5000 €` puede ser útil como ejemplo, pero cualquier importe nominal concreto corre el riesgo de ser arbitrario respecto a:

- el capital acumulado del sistema;
- la fase temporal del backtest;
- la escala histórica de tamaño;
- la interacción con el crecimiento compuesto.

Por tanto, la sensibilidad conceptual al parámetro es alta. Eso obliga a separar con cuidado dos preguntas:

1. si la familia de reglas tiene sentido;
2. qué valor nominal concreto tendría sentido dentro de ella.

Este análisis solo puede apoyar, como mucho, la primera pregunta.

### 5.4. Doble arbitrariedad en la variante por régimen

La versión condicionada por régimen no solo depende de elegir un valor nominal; también depende de decidir:

- qué regímenes llevan tope más duro;
- cuáles conservan más libertad;
- si todos los regímenes deben tener tope o no.

Es decir, esta variante es conceptualmente más prometedora que la uniforme, pero también más expuesta a sobreajuste si se pasa demasiado pronto a calibrarla.

### 5.5. Posible incoherencia con la heterogeneidad interna de PROBLEMATICO

Los análisis previos sugieren que `PROBLEMATICO` no es un bloque homogéneo. Si se usa una sola barrera nominal dura para toda la clase, se corre el riesgo de tratar igual:

- fases de estrés bajista absorbible;
- transiciones erráticas;
- lateralidades hostiles.

Eso puede ser aceptable como primera aproximación de investigación, pero es una debilidad conceptual real que conviene reconocer desde el principio.

### 5.6. Compatibilidad con IBKR: buena en principio, pero no decisiva por sí sola

Desde un punto de vista operativo futuro, un tope máximo nominal es una regla intuitiva y, en principio, compatible con una ejecución vía `IBKR`, porque se traduce fácilmente en límites de tamaño o cantidad antes de enviar la orden.

Sin embargo, esa facilidad no valida por sí misma la idea. Que algo sea fácil de implementar en `IBKR` no significa automáticamente que sea una buena regla de sistema. Solo indica que, si la hipótesis mereciera avanzar, no parece chocar de entrada con la infraestructura prevista.

## 6. Papel del ejemplo 5000 €

El valor `5000 €` debe entenderse en este documento **solo como ejemplo explícito de trabajo**, no como propuesta final ni como cifra validada.

Su función aquí es únicamente hacer visible la lógica de la familia:

- cómo se vería un tope nominal absoluto;
- cómo podría compararse una versión uniforme frente a una condicionada por régimen;
- cómo cambia la discusión cuando existe una barrera concreta en euros en vez de una idea vaga.

Pero debe quedar igual de explícito lo que **no** significa:

- **no** significa que `5000 €` sea el valor correcto;
- **no** significa que `5000 €` sea razonable para todos los momentos del sistema;
- **no** significa que `5000 €` deba convertirse en regla candidata;
- **no** significa que el análisis haya validado ese parámetro.

De hecho, el principal valor metodológico de usar `5000 €` como ejemplo es precisamente mostrar la sensibilidad conceptual del problema: una misma familia puede parecer razonable o torpe según el importe elegido, lo que confirma que **la familia y el parámetro deben evaluarse por separado**.

## 7. Viabilidad futura de prueba histórica

A nivel metodológico, esta familia **sí parece viable para una prueba histórica posterior**, siempre que la siguiente tanda mantenga disciplina y no salte directamente a validaciones prematuras.

### Claridad conceptual de la regla

- **Media-alta** para la variante uniforme.
- **Alta** en intuición pero **media** en detalle para la variante condicionada por régimen.
- La ausencia de tope es trivial de entender, pero no introduce hipótesis nueva.

### Facilidad de implementación futura

- **Alta**.
- La regla es simple de incorporar como restricción previa al tamaño final de entrada.
- La versión por régimen añade algo de lógica condicional, pero sigue siendo técnicamente sencilla.

### Compatibilidad con IBKR

- **Alta en principio**.
- Un tope nominal es conceptualmente compatible con la operativa prevista y no sugiere fricciones especiales de integración.

### Riesgo de capar años favorables

- **Alto** si el tope es uniforme o demasiado bajo.
- **Medio** si la lógica se condiciona por régimen y preserva más libertad en `FAVORABLE`.

### Utilidad potencial en MIXTO y PROBLEMATICO

- **Moderada-alta** como hipótesis de investigación.
- Es especialmente plausible allí donde la intención sea contener expansión excesiva o limitar exposición en contextos dudosos sin apagar completamente la operativa.

### Sensibilidad conceptual al valor nominal elegido

- **Alta**.
- Esta es la principal razón para no convertir todavía la familia en regla candidata final.

### Juicio agregado de viabilidad

La familia merece prueba histórica posterior por tres motivos:

1. la hipótesis es clara y acotada;
2. el selector ofrece una segmentación natural para organizar el experimento;
3. la implementación futura sería fácil y compatible con la infraestructura prevista.

Pero también exige una condición fuerte:

- el backtest futuro debe tratar la familia como **exploración de comportamiento**, no como confirmación encubierta de un valor concreto ni de una solución ya elegida.

## 8. Conclusión final

La familia de reglas basada en un **tope máximo nominal de entrada** sí tiene sentido como línea de investigación futura, especialmente en su variante **condicionada por régimen**, porque intenta resolver una tensión real: contener expansión excesiva en contextos dudosos, limitar exposición en `PROBLEMATICO` y conservar mayor libertad en `FAVORABLE`.

Sin embargo, la evidencia conceptual actual **no autoriza** a validar ningún valor nominal concreto ni a convertir esta idea en regla candidata final. El ejemplo de `5000 €` es útil para estudiar la forma de la hipótesis, pero sigue siendo solo eso: un ejemplo.

La lectura metodológicamente más honesta es esta:

- la **ausencia de tope nominal** mantiene máxima flexibilidad pero deja sin explorar una palanca defensiva potencialmente útil;
- el **tope uniforme** ofrece simplicidad, aunque con riesgo alto de rigidez innecesaria y de capar años fuertes;
- el **tope condicionado por régimen** parece la versión con mejor lógica investigable, porque utiliza la segmentación del selector para reservar la disciplina donde más podría aportar.

Por tanto, lo que aquí queda respaldado no es un parámetro, sino una **familia digna de prueba histórica posterior**.

## 9. Recomendación: merece backtest posterior / mantener como hipótesis / no priorizar todavía

**Recomendación final: merece backtest posterior**, pero con dos reservas explícitas.

### Reserva 1. Mantenerla todavía como hipótesis, no como regla candidata final

El hecho de que merezca backtest no significa que deba promocionarse ya. La familia debe seguir etiquetada como **hipótesis de investigación** hasta que exista evidencia histórica comparativa suficiente.

### Reserva 2. No validar aún el valor 5000 €

Si se abre una siguiente tanda de pruebas, el valor `5000 €` podrá usarse como uno de varios puntos de referencia, pero **no** como cifra ya defendida o preferida.

En resumen:

- **merece backtest posterior** como familia de reglas;
- **mantener como hipótesis** hasta ver resultados históricos;
- **no priorizar como regla final todavía** mientras no se evalúe su sensibilidad al valor nominal y su efecto real por régimen.
