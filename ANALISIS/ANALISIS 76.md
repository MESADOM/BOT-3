# VERSION 2.2.2 ANALISIS 76

## 1. Objetivo

Realizar una **validación final corta y compuesta** de la familia de **reducción porcentual de exposición por régimen**, trabajando exclusivamente sobre el **sistema general long-short vigente** y usando como base provisional el **selector de régimen actualmente aceptado**.

El objetivo aquí ya no es abrir una nueva fase amplia de investigación, sino responder una pregunta más estrecha y práctica:

- si dentro de esta familia existe una versión **simple, explicable y preliminarmente estable** que merezca una **implementación de prueba controlada**;
- o si la evidencia sigue siendo demasiado dependiente de episodios concretos como para pasar a esa fase.

Restricciones mantenidas en todo momento:

- **no** se toca producción;
- **no** se diseñan nuevas estrategias por régimen;
- **no** se abre tuning amplio;
- **no** se declaran porcentajes óptimos;
- **sí** se fuerza un dictamen final claro y prudente.

---

## 2. Evidencia previa revisada

Se ha revisado obligatoriamente la cadena:

- `ANALISIS 64.md`
- `ANALISIS 65.md`
- `ANALISIS 66.md`
- `ANALISIS 67.md`
- `ANALISIS 68.md`
- `ANALISIS 69.md`
- `ANALISIS 70.md`
- `ANALISIS 71.md`
- `ANALISIS 72.md`
- `ANALISIS 73.md`
- `ANALISIS 74.md`
- `ANALISIS 75.md`

La evidencia acumulada deja cinco puntos base para esta validación final:

1. El selector sí tiene valor real como **capa de modulación prudente**, no todavía como base para sistemas separados por régimen.
2. `MIXTO` sigue siendo la clase más delicada porque concentra mucho beneficio histórico, pero también más tensión y drawdown.
3. `PROBLEMATICO` no equivale a inutilidad operativa, aunque su absorción sigue siendo **heterogénea** y parcialmente concentrada.
4. La familia porcentual salió mejor parada que la nominal, pero en `ANALISIS 73` quedó claro que funciona sobre todo como **trade-off** entre retorno y drawdown, no como mejora limpia en ambas dimensiones.
5. `ANALISIS 75` dejó implícito que aún faltaba una última validación corta y disciplinada antes de plantear siquiera una prueba controlada.

Por tanto, esta tarea no reabre la comparación con otras familias ni rediseña la hipótesis. Solo intenta cerrar con honestidad la pregunta final: **¿hay ya una variante porcentual suficientemente simple y estable para probarla en entorno controlado?**

---

## 3. Subfase A: variantes porcentuales seleccionadas

Para esta validación final se toma un conjunto **muy corto** de variantes, evitando cualquier rejilla amplia:

1. **Baseline sin reducción**
   - referencia obligatoria;
   - mantiene el sistema tal como está.

2. **Reducción uniforme simple 10%**
   - sirve como prueba mínima de cautela general;
   - es la variante uniforme más suave y fácil de explicar.

3. **Reducción condicionada suave**
   - `FAVORABLE 0%`, `MIXTO 10%`, `PROBLEMATICO 20%`;
   - representa la versión condicionada más simple que conserva casi intacto `FAVORABLE` y añade prudencia fuera de él.

4. **Reducción condicionada prudente**
   - `FAVORABLE 0%`, `MIXTO 20%`, `PROBLEMATICO 30%`;
   - se mantiene solo como contraste cercano para medir sensibilidad básica a un pequeño endurecimiento razonable.

### Por qué se seleccionan estas y no más

- El **baseline** es imprescindible.
- El **uniforme 10%** es el recorte global más simple y menos invasivo.
- La **condicionada suave** es la candidata natural si se quiere respetar la evidencia previa sobre `MIXTO` y `PROBLEMATICO` sin sobrerreaccionar.
- La **condicionada prudente** no se usa para buscar un óptimo, sino para comprobar si la familia se mantiene estable o se deteriora con un endurecimiento cercano y todavía razonable.

No se incluyen más variantes como núcleo de decisión porque esta fase ya no es de exploración amplia, sino de **cierre metodológico corto**.

---

## 4. Subfase B: resultados históricos comparados

### 4.1. Retorno total y drawdown total

| Variante | Beneficio neto total | Retorno total | Drawdown total |
|---|---:|---:|---:|
| Sin reducción | `21.965,83 €` | `+2196,58%` | `-28,49%` |
| Uniforme 10% | `20.467,73 €` | `+2046,77%` | `-28,04%` |
| Condicionada suave | `20.952,03 €` | `+2095,20%` | `-28,14%` |
| Condicionada prudente | `20.060,56 €` | `+2006,06%` | `-27,77%` |

### 4.2. Lectura comparada corta

- El **baseline** sigue siendo el mejor en retorno total.
- La mejora de drawdown de toda la familia existe, pero es **pequeña** en términos absolutos.
- La **condicionada suave** es la que mejor conserva retorno entre las variantes con reducción.
- La **condicionada prudente** compra algo más de contención de drawdown, pero a cambio de un deterioro de retorno ya visible.
- La **uniforme 10%** queda peor que la condicionada suave en retorno y no aporta una ventaja clara suficiente en drawdown como para preferirla.

### 4.3. Coste de oportunidad agregado frente al baseline

| Variante | Coste de oportunidad agregado vs baseline |
|---|---:|
| Uniforme 10% | `-1.498,10 €` |
| Condicionada suave | `-1.013,80 €` |
| Condicionada prudente | `-1.905,27 €` |

Lectura:

- el menor coste de oportunidad lo tiene la **condicionada suave**;
- la **uniforme 10%** ya paga un peaje apreciable sin una mejora diferencial clara;
- la **condicionada prudente** empieza a parecer demasiado cara para la mejora de perfil que compra.

### 4.4. Impacto en 2020–2025

Tomando como bloque favorable principal `2020`, `2021`, `2024` y `2025`, la suma baseline es `16.545,82 €`.

| Variante | Resultado agregado 2020, 2021, 2024 y 2025 | Retención del bloque favorable |
|---|---:|---:|
| Sin reducción | `16.545,82 €` | `100,0%` |
| Uniforme 10% | `15.718,78 €` | `95,0%` |
| Condicionada suave | `16.275,70 €` | `98,4%` |
| Condicionada prudente | `15.759,24 €` | `95,2%` |

Lectura:

- la **condicionada suave** preserva claramente mejor los años favorables recientes;
- la **uniforme 10%** y la **prudente** ya recortan más de lo deseable para una hipótesis que solo pretende ser prudente;
- esto favorece otra vez a la **condicionada suave** como mejor equilibrio simple.

---

## 5. Impacto por régimen

### 5.1. Retorno por clase del selector

| Variante | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|
| Sin reducción | `3.914,95 €` | `13.519,61 €` | `4.531,27 €` |
| Uniforme 10% | `3.461,78 €` | `13.197,91 €` | `3.808,04 €` |
| Condicionada suave | `3.878,69 €` | `13.343,77 €` | `3.729,57 €` |
| Condicionada prudente | `3.773,85 €` | `13.018,02 €` | `3.268,69 €` |

### 5.2. Drawdown por clase del selector

La evidencia previa disponible es mucho más fuerte en **retorno por clase** que en drawdown segmentado por variante. Lo que sí queda claro es la estructura base heredada:

- en el baseline, `MIXTO` es la clase con drawdown segmentado más alto;
- `FAVORABLE` mantiene un perfil sano;
- `PROBLEMATICO` no es el peor bloque en drawdown del sistema general, pese a ser el más hostil en lectura contextual.

Para esta validación final, lo relevante no es forzar una falsa precisión adicional por clase, sino observar **dónde se paga el recorte**:

- **FAVORABLE:** la condicionada suave casi no lo toca; la uniforme 10% sí lo recorta innecesariamente.
- **MIXTO:** la condicionada suave es la que mejor preserva la clase más productiva del histórico.
- **PROBLEMATICO:** todas las variantes recortan captura útil; la prudente lo hace de forma ya bastante visible.

### 5.3. Lectura operativa por régimen

#### FAVORABLE

La mejor señal aquí la da la **condicionada suave**: protege la clase sin vaciar el bloque sano. La uniforme 10% es menos coherente porque castiga también donde menos falta hace.

#### MIXTO

Este es el eje decisivo. `MIXTO` sigue siendo el gran motor del sistema y cualquier variante que lo recorte demasiado se vuelve dudosa rápidamente. La **condicionada suave** vuelve a destacar porque es la que menos daña la zona más productiva sin renunciar a introducir cautela.

#### PROBLEMATICO

La familia sí frena exposición en el bloque hostil, pero el coste no es teórico: se pierde parte del beneficio que el sistema todavía captura ahí. La prudente reduce más, pero no demuestra una compensación suficientemente fuerte fuera de ese recorte.

---

## 6. Impacto en 2022 y en años favorables

### 6.1. Impacto en 2022

| Variante | Resultado 2022 |
|---|---:|
| Sin reducción | `4.119,19 €` |
| Uniforme 10% | `3.587,24 €` |
| Condicionada suave | `3.407,79 €` |
| Condicionada prudente | `3.032,95 €` |

Lectura:

- toda reducción porcentual empeora `2022`;
- ese empeoramiento no invalida por sí solo la familia, pero recuerda que `PROBLEMATICO` no debe tratarse como un bloque donde convenga recortar sin coste;
- la **prudente** muestra una dependencia demasiado fuerte de castigar el año hostil más importante del histórico;
- la **suave** sigue siendo asumible, pero incluso ella paga un precio material en `2022`.

### 6.2. Impacto en años favorables

En los años favorables recientes, la jerarquía es clara:

1. **Sin reducción**
2. **Condicionada suave**
3. **Condicionada prudente ≈ Uniforme 10%**

Además, en `2024–2025` la evidencia previa mostraba algo importante: las variantes suaves y condicionadas prácticamente no dañaban el gran bloque ganador reciente, mientras que los recortes más severos sí empezaban a deteriorarlo de forma notable.

### 6.3. Conclusión del contraste 2022 vs años favorables

La familia porcentual no mejora por repartir pequeños beneficios en muchos periodos. Su efecto sale de un equilibrio delicado:

- en `2022` reduce captura útil;
- en años favorables suaves apenas toca el bloque bueno si el recorte es moderado;
- si el endurecimiento sube un escalón, el daño ya empieza a expandirse a bloques que no conviene tocar.

Eso obliga a una lectura prudente: la mejora de perfil **no viene de muchos periodos independientes**, sino de una contención relativamente pequeña del riesgo agregado combinada con un intento de no dañar demasiado los años buenos.

---

## 7. Coste de oportunidad

El coste de oportunidad agregado confirma el patrón principal de la validación:

- la familia sí compra algo de defensa, pero **siempre pagando retorno**;
- ese pago es tolerable solo mientras siga siendo pequeño y esté bien concentrado;
- cuando la prudencia aumenta un poco, el coste crece más deprisa que la mejora de drawdown.

Resumen práctico:

- **Condicionada suave:** coste de oportunidad **moderado y relativamente defendible**.
- **Uniforme 10%:** coste de oportunidad **material pero conceptualmente menos justificado**, porque castiga también `FAVORABLE`.
- **Condicionada prudente:** coste de oportunidad **ya alto** para una mejora que sigue siendo modesta.

Por tanto, la pregunta no es si la familia tiene coste de oportunidad —lo tiene—, sino si existe una variante cuyo coste siga siendo razonable para una prueba controlada. Solo la **condicionada suave** queda cerca de ese umbral.

---

## 8. Subfase C: robustez preliminar y dependencia de episodios

### 8.1. Sensibilidad a pequeños cambios razonables

La comparación entre **condicionada suave** y **condicionada prudente** es el mejor test corto de sensibilidad:

- el endurecimiento de un escalón razonable empeora el retorno de `20.952,03 €` a `20.060,56 €`;
- el drawdown mejora solo de `-28,14%` a `-27,77%`.

Esto indica que la familia **no es indiferente** a pequeños cambios: hay sensibilidad real y el beneficio marginal defensivo parece menor que el coste marginal en retorno.

### 8.2. Dependencia de un año concreto

La evidencia previa ya mostró que una parte importante del debate está concentrada en pocos bloques grandes, especialmente:

- `2022`, sobre todo en episodios `PROBLEMATICO` relevantes;
- algunos grandes ganadores `MIXTO` de `2020–2025`.

Eso significa que la familia no demuestra todavía una mejora repartida y uniforme a lo largo de muchos años independientes.

### 8.3. Dependencia específica de 2022, 2024 o 2025

#### Dependencia de 2022

Es la dependencia más clara. Toda reducción porcentual relevante poda parte de la captura short útil de `2022`. Por tanto, cualquier juicio favorable a la familia debe aceptar que el caso 2022 sigue siendo central.

#### Dependencia de 2024 y 2025

La señal positiva de la familia, especialmente en su variante suave, depende bastante de **no dañar** los grandes bloques ganadores recientes. Eso es bueno como preservación, pero también recuerda que el argumento a favor no es una mejora activa repetida en `2024–2025`, sino más bien que la variante **no estropea demasiado** esos años.

### 8.4. Concentración del efecto en pocos trades o pocos periodos

La evidencia heredada de `ANALISIS 73` es explícita: el deterioro frente al baseline se concentra en **pocos trades grandes** y en pocos bloques temporales de alto peso. Esa concentración es especialmente visible en las versiones condicionadas.

Esto impide vender la familia como una mejora robusta distribuida. En el mejor de los casos, la lectura correcta es otra:

- la variante suave parece **útil**,
- pero su valor sigue dependiendo bastante de **no deteriorar demasiado unos pocos bloques grandes** y de aceptar pérdidas concretas en `2022`.

### 8.5. Juicio de robustez preliminar

La mejor clasificación para la variante más defendible es:

- **no** parece razonablemente estable en sentido fuerte;
- **sí** parece **útil pero frágil**;
- **no** parece todavía una solución demasiado sólida como para pasar a implementación sin reservas.

---

## 9. Mejor variante porcentual encontrada

La mejor variante porcentual encontrada en esta validación final corta es la **condicionada suave**:

- `FAVORABLE 0%`, `MIXTO 10%`, `PROBLEMATICO 20%`.

Motivos:

1. Es la que mejor equilibra **simplicidad**, **preservación del baseline** y **prudencia real**.
2. Tiene el **menor coste de oportunidad** entre las variantes con reducción seleccionadas.
3. Preserva mejor `FAVORABLE` y, sobre todo, `MIXTO`, que sigue siendo la clase más sensible del sistema.
4. Conserva muy bien los años favorables recientes.
5. Sigue siendo explicable sin necesidad de tuning amplio ni de microajustes.

Pero el matiz decisivo es este: **ser la mejor de la familia no equivale a estar suficientemente validada para implementación con confianza alta**.

---

## 10. Conclusión final

La validación final corta de la familia de **reducción porcentual de exposición por régimen** deja un dictamen más prudente que entusiasta.

Sí existe una variante simple que destaca sobre las demás: la **condicionada suave**. Sin embargo, su mejora histórica no aparece como una ventaja amplia, repetida y robusta a través de muchos periodos independientes. Lo que aparece es algo más limitado:

- una pequeña mejora de perfil agregado;
- una preservación razonable de años favorables;
- a cambio de recortar parte de la captura útil de `2022` y de seguir dependiendo bastante de pocos episodios relevantes.

Por tanto, la familia no está ya en estado de “evidencia bastante para adoptar”, pero tampoco queda descartada por completo. La lectura más honesta es esta:

- **hay una variante útil**;
- **esa utilidad todavía es frágil**;
- y la evidencia sigue siendo **insuficiente para recomendar una implementación con ambición operativa fuerte**.

---

## 11. Recomendación: implementar prueba controlada / mantener en investigación / congelar temporalmente

**Recomendación final: mantener en investigación.**

Dictamen explícito sobre implementación de prueba:

- **No merece todavía implementación de prueba**.
- Tampoco parece necesario **congelar temporalmente** toda la línea, porque la familia sí ha dejado una variante simple con cierto valor relativo.
- La salida prudente es **mantener en investigación**, dejando a la **condicionada suave** como referencia provisional para futuras comprobaciones, pero **sin pasar aún a prueba controlada**.

Justificación final:

1. La mejora de drawdown es demasiado pequeña para sostener por sí sola una prueba.
2. El baseline sigue siendo superior en retorno total.
3. La dependencia de `2022` y de pocos bloques grandes sigue siendo demasiado visible.
4. La robustez preliminar es de tipo **útil pero frágil**, no de tipo estable.
5. Con la evidencia actual, recomendar implementación —aunque fuera controlada— sería adelantarse a lo que realmente muestran los datos.

En síntesis final:

- **mejor variante encontrada:** condicionada suave;
- **estado de la evidencia:** útil pero frágil;
- **decisión:** **mantener en investigación**, sin implementación todavía y sin promoción automática a producción.
