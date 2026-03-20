# VERSION 2.2.2 ANALISIS 74

## 1. Objetivo

Emitir un **dictamen comparativo** entre dos familias de investigación sobre modulación de exposición por régimen:

- la familia de **topes máximos nominales por régimen**;
- la familia de **reducciones porcentuales por régimen**.

El objetivo no es declarar una regla final, ni validar parámetros concretos, ni tocar producción. El objetivo es decidir **qué familia merece ser priorizada en la siguiente fase real de investigación**, comparándolas de forma directa en términos de simplicidad, interpretabilidad, robustez aparente, sensibilidad paramétrica, preservación de años favorables, utilidad en `MIXTO` y `PROBLEMATICO`, y facilidad de futura implementación en `IBKR`.

Limitación documental que debe quedar escrita con total transparencia:

- las instrucciones exigían leer obligatoriamente `ANALISIS 72.md` y `ANALISIS 73.md`;
- esos dos archivos **no existen** en el repositorio actual, por lo que no han podido ser leídos literalmente;
- sí se han revisado `ANALISIS 68.md`, `ANALISIS 69.md`, `ANALISIS 70.md` y `ANALISIS 71.md`, que son la base verificable utilizada aquí;
- por tanto, este dictamen compara ambas familias con apoyo en la evidencia disponible y **sin fingir continuidad documental inexistente**.

---

## 2. Familias comparadas

### A. Familia nominal: topes máximos nominales por régimen

Esta familia introduce un **límite absoluto** al tamaño permitido de entrada. El selector no cambia la señal del sistema, pero sí restringe cuánto nominal puede desplegarse en función del régimen.

Su lógica conceptual es:

- más libertad en `FAVORABLE`;
- disciplina intermedia en `MIXTO`;
- mayor restricción en `PROBLEMATICO`.

Es una familia de tipo **límite duro**, fácil de auditar y muy directa desde el punto de vista operativo.

### B. Familia porcentual: reducciones porcentuales por régimen

Esta familia no fija un techo absoluto, sino un **multiplicador de exposición** según régimen.

Su lógica conceptual es:

- `100%` o cerca del baseline en `FAVORABLE`;
- reducción parcial en `MIXTO`;
- reducción más marcada en `PROBLEMATICO`.

Es una familia de tipo **cautela proporcional**, más continua que la nominal y potencialmente más flexible ante transiciones entre contextos.

### Punto metodológico común

Las dos familias comparten el mismo marco:

- no rediseñan señales;
- no crean estrategias nuevas por régimen;
- intentan proteger al sistema general sin anularlo;
- son, por diseño, hipótesis de investigación y no reglas finales.

---

## 3. Ventajas de la familia nominal

### 3.1. Simplicidad superior

La familia nominal es la más simple de las dos. Su estructura es muy corta:

- existe o no existe un tope;
- ese tope puede ser igual o distinto según régimen;
- la validación histórica es relativamente fácil de reconstruir.

Si el rendimiento entre ambas familias termina siendo parecido, esta simplicidad le da una ventaja metodológica clara.

### 3.2. Interpretabilidad muy alta

La lectura del cambio es extremadamente intuitiva: el sistema mantiene su lógica, pero se le impide sobrepasar cierto nominal en contextos más dudosos. Eso facilita explicar:

- qué se está intentando proteger;
- dónde se está imponiendo la disciplina;
- y qué parte del resultado viene de limitar tamaño y no de reescribir la estrategia.

### 3.3. Robustez aparente razonable por baja complejidad

Aunque un tope nominal puede ser tosco, también introduce menos grados de libertad que una familia basada en múltiples porcentajes. Esa menor libertad sugiere, **a priori**, menor riesgo de sobreajuste fino.

La robustez aparente aquí no viene de una supuesta precisión, sino de su condición de herramienta **externa, gruesa y auditable**.

### 3.4. Menor complejidad futura de implementación en IBKR

Desde el punto de vista operativo, la familia nominal parece la más cómoda para una futura implementación en `IBKR`:

- se traduce de forma directa en límites de tamaño o cantidad;
- se supervisa con facilidad;
- genera menos ambigüedad que una capa porcentual más continua.

### 3.5. Buena herramienta para contener excesos en MIXTO y PROBLEMATICO

La evidencia acumulada sugiere que `MIXTO` concentra una parte importante del beneficio pero también más tensión, y que `PROBLEMATICO` exige prudencia porque no es homogéneo. En ese contexto, un tope nominal tiene una virtud clara: **contiene excesos sin necesidad de apagar el régimen**.

### 3.6. Dependencia relativamente menor de microajustes estructurales

La familia nominal depende de elegir niveles concretos, pero una vez fijado el marco conceptual, evita parte de la tentación de buscar una malla demasiado fina de ajustes continuos. Eso le da una cierta ventaja cuando la prioridad es aprender rápido con una hipótesis austera.

---

## 4. Ventajas de la familia porcentual

### 4.1. Mayor continuidad económica entre regímenes

La principal ventaja de la familia porcentual es que su cautela puede ser más proporcional. En vez de imponer un salto duro, ajusta intensidad.

Eso tiene atractivo conceptual porque:

- deja respirar más al sistema cuando el contexto todavía contiene edge;
- reduce el riesgo de rigidez excesiva;
- y puede adaptarse mejor a zonas ambiguas o transicionales.

### 4.2. Mejor preservación potencial de años favorables

En comparación con la familia nominal, la porcentual parece mejor situada para **proteger sin capar demasiado** si el calibrado se hace con prudencia. La razón es simple:

- un multiplicador parcial puede bajar riesgo sin bloquear por completo la expansión del sistema;
- eso es especialmente importante en `MIXTO`, donde la evidencia acumulada sugiere que existe mucho valor histórico que no conviene amputar por exceso de dureza.

### 4.3. Mejor ajuste conceptual para MIXTO

`MIXTO` no parece un régimen que pida una respuesta binaria. Aporta mucho retorno agregado, pero con mayor drawdown y más irregularidad. En ese tipo de contexto, una reducción porcentual parece más natural que un límite nominal duro, porque permite reconocer que:

- hay edge real;
- hay tensión real;
- y la respuesta correcta podría ser bajar intensidad, no imponer un corte demasiado tosco.

### 4.4. Mejor capacidad para no castigar en exceso PROBLEMATICO absorbible

La evidencia acumulada también sugiere que `PROBLEMATICO` no es homogéneo y que algunos episodios hostiles sí son absorbidos razonablemente bien por el general, en especial por la pata short. La familia porcentual, al no imponer un techo absoluto rígido, podría preservar mejor esa captura parcial de valor.

### 4.5. Más coherencia con la lógica de exposición como siguiente fase natural

`ANALISIS 69.md` y `ANALISIS 71.md` empujan hacia una fase centrada en exposición modulada antes que en variantes estructurales. Dentro de ese marco, la familia porcentual representa la forma más pura de responder a la pregunta: **cuánto riesgo conviene dejar pasar en cada régimen**.

### 4.6. Mayor fineza para equilibrar retorno y drawdown agregados

Si la familia nominal es más tosca, la porcentual ofrece una palanca potencialmente mejor para buscar equilibrio entre:

- retorno agregado;
- drawdown agregado;
- y contribución por régimen.

No significa que vaya a funcionar mejor, pero sí que tiene una capacidad conceptual más alta para afinar el balance entre defensa y preservación del general.

---

## 5. Riesgos y debilidades de cada familia

### 5.1. Riesgos de la familia nominal

#### a) Riesgo alto de depender de un valor arbitrario

Esta es su debilidad central. Un tope nominal concreto puede ser arbitrario respecto a:

- capital acumulado;
- fase histórica del sistema;
- crecimiento compuesto;
- escala efectiva del sizing.

Por eso, aunque la familia es simple, **depende mucho de un valor absoluto** cuya justificación puede ser débil si no se prueba con mucha disciplina.

#### b) Riesgo de capar demasiado años favorables

Es la familia con más probabilidad de cortar justo donde no debería, sobre todo si el tope es uniforme o demasiado severo. Esa debilidad pesa mucho porque la prioridad metodológica actual exige proteger **sin deteriorar en exceso** los años buenos del general.

#### c) Riesgo de rigidez excesiva en MIXTO

`MIXTO` no es un bloque residual. Si concentra gran parte del beneficio histórico, una barrera dura puede penalizar demasiado una zona que justamente debería tratarse con cautela, pero no con amputación brusca.

#### d) Debilidad frente a la heterogeneidad de PROBLEMATICO

Si `PROBLEMATICO` contiene subpatrones distintos, un solo tope nominal puede tratar igual episodios que quizá no merecen la misma severidad. Esa simplificación puede ser útil como primera aproximación, pero no deja de ser una fragilidad conceptual.

### 5.2. Riesgos de la familia porcentual

#### a) Mayor sensibilidad paramétrica

Su principal debilidad es la tentación de probar demasiados porcentajes. Eso abre más espacio de búsqueda y, con ello, más riesgo de sobreoptimización.

#### b) Menor claridad absoluta que el tope nominal

Aunque sigue siendo bastante interpretable, su lectura puede dispersarse más rápidamente:

- un porcentaje para `MIXTO`;
- otro para `PROBLEMATICO`;
- posibles escalones o variantes;
- combinaciones con distintas bases de exposición.

Eso la hace menos austera que la familia nominal.

#### c) Riesgo de complejidad incremental

Si no se controla bien, la familia porcentual puede mutar desde una idea simple hacia una superficie de optimización demasiado amplia. Ese riesgo no es inevitable, pero sí real.

#### d) Riesgo de falsa precisión

Un multiplicador porcentual puede parecer más fino de lo que realmente permite sostener la evidencia actual. Si el soporte histórico por régimen sigue siendo medio o limitado, demasiada precisión porcentual podría ser más estética que robusta.

---

## 6. Comparación operativa e histórica

### 6.1. Comparación de retorno y drawdown agregados

Con la evidencia disponible, no existe todavía un backtest comparativo cerrado entre ambas familias. Por tanto, el juicio debe formularse como **comparación metodológica de impacto esperado**, no como veredicto estadístico definitivo.

Aun así, el marco acumulado permite una inferencia prudente:

- la familia nominal parece más fuerte como herramienta de **contención de drawdown agregado** cuando la prioridad es cortar expansiones excesivas;
- la familia porcentual parece mejor situada para **preservar más retorno agregado** si el sistema todavía mantiene edge en `MIXTO` y en partes de `PROBLEMATICO`.

En consecuencia, la comparación preliminar sugiere:

- **nominal:** más protectora por dureza;
- **porcentual:** más equilibrada para no castigar en exceso el retorno.

### 6.2. Comparación de impacto por régimen

#### FAVORABLE

- **Nominal:** corre más riesgo de imponer una limitación innecesaria si el tope se fija demasiado bajo.
- **Porcentual:** permite preservar mejor la libertad del baseline y parece más compatible con la idea de “dejar respirar al general”.

#### MIXTO

- **Nominal:** útil para frenar expansión excesiva, pero con riesgo alto de cortar una parte demasiado grande de una clase que hoy aporta mucho beneficio.
- **Porcentual:** parece mejor adaptada a la naturaleza ambigua de `MIXTO`, donde la cautela debería ser real pero no binaria.

#### PROBLEMATICO

- **Nominal:** transmite prudencia clara y fácil de auditar, lo que es atractivo en un régimen hostil y heterogéneo.
- **Porcentual:** puede capturar mejor la idea de que `PROBLEMATICO` no siempre debe tratarse con el mismo nivel de severidad, aunque su parametrización sea más delicada.

### 6.3. Comparación de sensibilidad paramétrica

Aquí la diferencia es importante.

- **Familia nominal:** depende mucho del valor absoluto elegido. Eso la hace sensible a un parámetro muy arbitrario, aunque tenga menos parámetros totales.
- **Familia porcentual:** depende de más posibles combinaciones, pero sus parámetros son más orgánicos respecto a la lógica de exposición.

Por tanto, la pregunta no es solo “cuántos parámetros hay”, sino **qué tipo de arbitrariedad introducen**.

Dictamen en este eje:

- la nominal introduce **menos complejidad visible**, pero más dependencia de un umbral absoluto potencialmente artificial;
- la porcentual introduce **más grados de ajuste**, pero con una semántica más coherente con la dosificación del riesgo.

### 6.4. Comparación de dependencia de episodios concretos

Dado que la evidencia acumulada advierte sobre concentración de resultados en algunos tramos hostiles y sobre heterogeneidad en `PROBLEMATICO`, ambas familias deben vigilar dependencia de episodios concretos.

Aun así, la familia nominal parece más expuesta a que su éxito o fracaso dependa mucho de:

- unos pocos episodios donde el tope “llegó justo a tiempo”;
- o, al revés, de unos pocos episodios en los que el tope capó una expansión buena.

La porcentual, por su naturaleza más continua, parece algo mejor situada para evitar que el resultado comparativo descanse tanto en choques puntuales de tipo “entró o no entró el límite”.

### 6.5. Comparación de facilidad operativa

#### Simplicidad

- **Gana la nominal.**
- Es más fácil de describir, auditar, revisar y trasladar a reglas operativas futuras.

#### Interpretabilidad

- **Ligera ventaja para la nominal** en lectura operativa pura.
- **Ligera ventaja para la porcentual** en lectura económica del riesgo.

#### Implementación futura en IBKR

- **Ventaja nominal** por su traducción más directa a límites duros.
- La porcentual sigue siendo perfectamente viable, pero algo menos inmediata.

#### Complejidad global añadida

- **Menor en nominal**.
- **Mayor en porcentual**, aunque todavía moderada si se restringe bien.

---

## 7. Qué familia preserva mejor el general

Si la pregunta principal es **qué familia preserva mejor el perfil histórico del sistema general**, la respuesta preliminar es la familia **porcentual**.

La razón no es que sea más simple, sino que parece mejor preparada para cumplir el criterio central de esta fase:

- **proteger mejor sin capar demasiado**.

Esa ventaja aparece sobre todo en tres frentes:

1. **Preservación de años favorables.**  
   La porcentual permite mantener más continuidad con el baseline en `FAVORABLE`.

2. **Preservación de MIXTO productivo.**  
   Dado que `MIXTO` aporta mucho retorno histórico, una reducción proporcional parece menos destructiva que un corte nominal duro.

3. **Preservación de episodios absorbibles en PROBLEMATICO.**  
   La naturaleza no homogénea de `PROBLEMATICO` hace valioso un enfoque que rebaje intensidad sin convertir la disciplina en una barrera demasiado rígida.

Dicho de forma breve:

- la familia nominal **preserva mejor la simplicidad del marco**;
- la familia porcentual **preserva mejor el comportamiento potencial del general**.

---

## 8. Conclusión final

El contraste entre ambas familias deja un resultado matizado.

### Lo que favorece a la familia nominal

- introduce menos complejidad;
- es la más simple de auditar;
- facilita más la futura implementación en `IBKR`;
- y ofrece una defensa muy clara contra expansiones excesivas.

### Lo que la debilita

- depende en exceso de un valor absoluto potencialmente arbitrario;
- puede capar con demasiada facilidad años favorables o tramos productivos de `MIXTO`;
- y su rigidez encaja peor con la heterogeneidad de `PROBLEMATICO`.

### Lo que favorece a la familia porcentual

- se alinea mejor con la lógica de dosificación de exposición por régimen;
- parece más capaz de proteger sin amputar demasiado;
- preserva mejor el sistema general en `FAVORABLE`, `MIXTO` y partes absorbibles de `PROBLEMATICO`;
- y reduce la probabilidad de que el juicio quede demasiado dominado por un umbral nominal arbitrario.

### Lo que la debilita

- añade más sensibilidad paramétrica;
- obliga a vigilar con más disciplina el riesgo de sobreoptimización;
- y es algo menos austera que la familia nominal.

### Dictamen comparativo

Tomando juntas todas las dimensiones exigidas:

- **simplicidad:** ventaja nominal;
- **interpretabilidad:** empate con leve sesgo nominal en lo operativo y porcentual en lo económico;
- **robustez aparente:** ligera ventaja nominal por austeridad, pero no decisiva;
- **sensibilidad a parámetros:** ambas tienen debilidad, aunque la nominal depende más de un umbral absoluto arbitrario y la porcentual de más combinaciones;
- **preservación de años favorables:** ventaja porcentual;
- **utilidad en MIXTO y PROBLEMATICO:** ventaja porcentual para `MIXTO`, empate prudente en `PROBLEMATICO` con perfiles distintos;
- **facilidad futura en IBKR:** ventaja nominal.

La consecuencia metodológica es clara: si dos familias ofrecieran un rendimiento muy parecido, habría buenas razones para empezar por la nominal por su simplicidad. **Pero con la evidencia conceptual disponible, la familia porcentual parece mejor situada para cumplir el objetivo más importante de esta fase: proteger sin capar demasiado el general.**

---

## 9. Recomendación: priorizar nominal / priorizar porcentual / ninguna claramente prioritaria

**Recomendación final: priorizar porcentual.**

La recomendación no equivale a declarar ganadora definitiva a la familia porcentual ni a descartar la nominal. Significa algo más acotado:

- la familia porcentual merece ser **la prioridad metodológica** de la siguiente tanda real de investigación;
- la familia nominal debe mantenerse como **comparador simple y auditable**;
- no corresponde todavía validar porcentajes concretos ni declarar una regla final.

Razones principales para priorizar la porcentual:

1. parece **preservar mejor el general**;
2. ofrece mejor equilibrio potencial entre **retorno agregado y drawdown agregado**;
3. se adapta mejor a la naturaleza ambigua de `MIXTO`;
4. depende menos de un **valor absoluto arbitrario**;
5. y encaja mejor con la idea de investigar **cautela proporcional** antes que límites duros demasiado rígidos.

Reserva final imprescindible:

- esta prioridad es **metodológica**, no definitiva;
- si una comparación histórica posterior mostrara rendimiento muy parecido entre ambas familias, volvería a ganar peso la ventaja de simplicidad de la familia nominal.
