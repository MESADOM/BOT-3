# VERSION 2.2.2 ANALISIS 56

## 1. Objetivo

Construir una **primera especificación explícita, mínima y auditable** del futuro selector de contexto a partir de la evidencia ya obtenida en `ANALISIS 50` a `ANALISIS 55`, sin convertirlo todavía en un mecanismo operativo de producción, sin fijar umbrales finales optimizados y sin abrir aún estrategias distintas por clase.

La misión de este documento es reducir la ambigüedad acumulada y dejar formulado un diseño conceptual simple que responda a estas preguntas:

- cuántas capas temporales mínimas debe tener el selector;
- qué variables mínimas entran en cada capa;
- por qué esas variables merecen entrar;
- qué salida de clasificación gruesa debe producir;
- qué elementos deben quedar expresamente fuera por ahora para preservar simplicidad, trazabilidad y coherencia con la evidencia ya acumulada.

Este análisis **no implementa** el selector, **no modifica producción** y **no propone** aún una lógica final optimizada por régimen.

## 2. Evidencia previa utilizada

La especificación propuesta se apoya directamente en las conclusiones centrales de los análisis `50–55`.

### 2.1. Horizonte temporal base del contexto

De `ANALISIS 50` se desprenden tres ideas clave:

- `1 mes` es útil como radar táctico, pero demasiado ruidoso para gobernar por sí solo el contexto.
- `3 meses` es la ventana más equilibrada como **lenguaje principal** del contexto.
- `6 meses` es demasiado lenta para ser la única lente, pero tiene valor claro como **capa estructural**.

Esto justifica una arquitectura temporal con tres velocidades:

- una capa **táctica** para no quedar ciegos ante giros recientes;
- una capa **principal** para describir el contexto dominante;
- una capa **estructural** para evitar sobrerreaccionar al ruido.

### 2.2. Variables de mercado con mayor valor descriptivo

De `ANALISIS 51` se desprende que, si se busca austeridad, interpretabilidad y viabilidad real, las variables con mejor perfil conceptual son las que salen del propio mercado principal (`QQQ`), especialmente:

- `QQQ > SMA200` como corte estructural simple;
- `retorno 63` como lectura intermedia clara;
- `distancia a SMA200` como medida de separación/sobreextensión estructural;
- `cruces SMA50` como proxy simple de serrucho o falta de persistencia;
- volatilidad simple (`volatilidad realizada` o `ATR%`) como medida de estrés.

La enseñanza importante no es “usar muchas variables”, sino elegir pocas que cubran dimensiones distintas:

- tendencia;
- persistencia/ruido;
- estrés/sobreextensión.

### 2.3. Jerarquía correcta de fuentes

De `ANALISIS 52` se desprende que la base del selector debe ser **mercado primero** y no operaciones propias.

La razón es temporal y metodológica:

- el mercado aporta información **previa** a la decisión;
- las operaciones propias llegan **después** y son más frágiles como base principal;
- un enfoque sano sería, como mucho, híbrido jerárquico, con mercado como núcleo y lo operativo como vigilancia secundaria.

Para esta primera especificación, eso obliga a dejar fuera las operaciones propias como núcleo del selector.

### 2.4. Papel de confirmadores externos

De `ANALISIS 53` se desprende que los confirmadores externos:

- pueden aportar algo si se usan con extrema parsimonia;
- no justifican todavía una arquitectura amplia;
- solo tendrían sentido, en una fase posterior, como apoyo muy secundario;
- entre los pocos candidatos, `VIX` sería el más distinto, pero incluso así no es necesario para esta primera especificación mínima.

Por tanto, la forma más coherente de empezar es construir el selector **solo con el mercado principal**, dejando los externos fuera de la primera versión conceptual.

### 2.5. Taxonomía mínima de salida

De `ANALISIS 54` se desprende que la taxonomía más robusta y menos narrativa en esta fase es de **3 clases**:

- `FAVORABLE`;
- `MIXTO`;
- `PROBLEMATICO`.

También se desprende que **no conviene abrir aún subclases** como estrés bajista, lateral ruidoso o reversión violenta. Esas etiquetas pueden mantenerse como hipótesis internas, pero no como salida oficial.

### 2.6. Viabilidad operativa real

De `ANALISIS 55` se desprende que la primera especificación debe priorizar:

- variables diarias disponibles y replicables en `IBKR`;
- cálculo simple al cierre;
- bajo coste de mantenimiento;
- máxima continuidad entre backtest e implementación real futura.

Esto refuerza la decisión de usar pocas variables de `QQQ`, evitar dependencias externas innecesarias y no construir aún una lógica compleja con muchos umbrales o confirmaciones cruzadas.

## 3. Arquitectura temporal propuesta

La propuesta mínima y coherente con `50–55` es una arquitectura de **3 capas temporales**.

### 3.1. Capa táctica

**Función:** detectar si el mercado reciente está limpio o se ha deteriorado de forma visible en el corto plazo, sin pretender gobernar por sí sola el régimen.

**Horizonte orientativo:** corto plazo, alrededor de `1–2 meses`.

**Papel conceptual:**

- captar cambios recientes que la capa estructural todavía no refleja;
- detectar serrucho, estrés o pérdida de persistencia;
- servir como capa de alerta temprana, no como juez único del contexto.

### 3.2. Capa principal

**Función:** describir el estado dominante del mercado con la mejor relación entre estabilidad, sensibilidad e interpretabilidad.

**Horizonte orientativo:** plazo intermedio, alrededor de `3 meses`.

**Papel conceptual:**

- actuar como núcleo de la clasificación;
- resumir la dirección útil del mercado;
- servir como lenguaje central del selector por ser la capa mejor alineada con la evidencia del `ANALISIS 50`.

### 3.3. Capa estructural

**Función:** describir el sesgo de fondo y evitar que correcciones tácticas o rebotes breves deformen en exceso la lectura del contexto.

**Horizonte orientativo:** largo plazo, alrededor de `6 meses` y referencias lentas.

**Papel conceptual:**

- estabilizar la clasificación;
- distinguir deterioro táctico de daño estructural real;
- evitar que el selector cambie de personalidad con demasiada facilidad.

### 3.4. Relación entre capas

La relación correcta entre capas no debe ser simétrica.

La lectura propuesta es:

- la **capa principal** lleva el mayor peso conceptual;
- la **capa estructural** actúa como ancla de fondo;
- la **capa táctica** actúa como modulador de corto plazo.

Dicho de otra forma:

- la táctica no debe dominar sola;
- la estructural no debe bloquear todo cambio;
- la principal es la capa que traduce mejor el contexto útil.

## 4. Variables incluidas por capa

La especificación mínima propuesta usa **5 variables en total**, repartidas entre las 3 capas. La idea no es maximizar cobertura, sino cubrir con pocas variables las dimensiones esenciales observadas en `50–55`.

### 4.1. Capa táctica

#### Variable 1. Cruces recientes respecto a `SMA50`

**Qué mide:** grado de serrucho, alternancia y falta de persistencia del precio reciente.

**Por qué está incluida:**

- aporta una dimensión distinta a la tendencia pura;
- ayuda a distinguir mercado limpio de mercado errático;
- fue identificada en `ANALISIS 51` como variable con valor real como descriptor de ruido/persistencia;
- encaja muy bien en la capa táctica porque reacciona antes que las referencias lentas.

**Justificación mínima:** si el selector quiere diferenciar entre entorno favorable y entorno incómodo, no basta con saber si el mercado sube o baja; hace falta saber si el trayecto es operable o serruchoso.

#### Variable 2. Volatilidad realizada corta o `ATR%` corto

**Qué mide:** tensión o expansión reciente del rango.

**Por qué está incluida:**

- introduce la dimensión de estrés que precio y medias no resumen completamente;
- permite distinguir corrección ordenada de contexto más violento o inestable;
- es una variable simple, diaria y viable en `IBKR`;
- complementa bien a los cruces: una mide serrucho, la otra intensidad del movimiento.

**Justificación mínima:** la capa táctica debe poder reflejar que dos mercados con dirección parecida pueden ser muy distintos si uno está en calma y el otro en estrés elevado.

### 4.2. Capa principal

#### Variable 3. Retorno intermedio (`retorno 63` como referencia conceptual)

**Qué mide:** comportamiento del mercado en el último trimestre bursátil aproximado.

**Por qué está incluida:**

- `ANALISIS 50` mostró que el horizonte de `3 meses` es el mejor lenguaje central del contexto;
- `ANALISIS 51` lo destacó como variable intermedia muy interpretable;
- añade gradación donde las variables binarias estructurales solo dan un sí/no;
- permite capturar deterioros o recuperaciones antes de que la capa estructural gire del todo.

**Justificación mínima:** si hay una única variable que encarna la capa principal, debe ser una lectura intermedia simple y comprensible del mercado reciente.

#### Variable 4. Distancia del precio a `SMA200`

**Qué mide:** separación del precio respecto a la referencia estructural lenta.

**Por qué está incluida:**

- añade magnitud, no solo dirección;
- ayuda a distinguir deterioro moderado de sobreextensión o capitulación;
- fue una de las variables con mejor perfil global en `ANALISIS 51`;
- sirve de puente entre la lectura principal y la estructural.

**Justificación mínima:** dos contextos pueden compartir retorno intermedio parecido, pero no significan lo mismo si uno está cerca de su estructura de fondo y otro está muy desplazado respecto a ella.

### 4.3. Capa estructural

#### Variable 5. `QQQ > SMA200`

**Qué mide:** sesgo estructural grueso del mercado principal.

**Por qué está incluida:**

- es la variable estructural más simple, estable e interpretable del inventario;
- encaja con la necesidad de una capa lenta de fondo observada en `ANALISIS 50`;
- tiene alta viabilidad operativa y auditabilidad;
- sirve como ancla conceptual para evitar que el selector dependa demasiado del corto plazo.

**Justificación mínima:** la primera especificación del selector necesita un corte estructural fácil de entender y fácil de auditar; `QQQ > SMA200` cumple esa función mejor que una combinación lenta más compleja.

### 4.4. Resumen de variables por capa

| Capa | Número de variables | Variables mínimas propuestas | Interpretabilidad |
|---|---:|---|---|
| Táctica | 2 | Cruces `SMA50`, volatilidad/`ATR%` corto | Alta |
| Principal | 2 | Retorno intermedio, distancia a `SMA200` | Alta |
| Estructural | 1 | `QQQ > SMA200` | Muy alta |
| **Total** | **5** | Selector mínimo de mercado principal | **Alta** |

## 5. Lógica mínima de clasificación

La salida propuesta debe producir exactamente **3 clases**:

- `FAVORABLE`
- `MIXTO`
- `PROBLEMATICO`

La lógica no debe fijar todavía umbrales finales optimizados. Lo que sí debe quedar explícito es la **regla conceptual de combinación** entre capas.

### 5.1. Principio general de clasificación

La clasificación debe leerse como una agregación simple de señales entre capas:

- la capa **principal** aporta la lectura dominante;
- la capa **estructural** confirma o cuestiona el sesgo de fondo;
- la capa **táctica** modula si el entorno reciente está limpio o está tensionado/errático.

### 5.2. Clase `FAVORABLE`

Debe representar contextos donde:

- la capa principal apunta a un mercado constructivo o utilizable;
- la capa estructural no contradice de forma clara esa lectura;
- la capa táctica no muestra un nivel de ruido o estrés suficientemente grave como para degradar el contexto a mixto.

**Interpretación:** el mercado presenta una estructura razonablemente legible y no hay señales dominantes de deterioro severo o serrucho destructivo.

### 5.3. Clase `PROBLEMATICO`

Debe representar contextos donde:

- la capa principal apunta a deterioro claro o pérdida fuerte de calidad;
- la capa estructural confirma debilidad de fondo o no ofrece apoyo suficiente;
- la capa táctica además muestra ruido alto, estrés alto o desorden persistente.

**Interpretación:** no se trata solo de que el mercado esté flojo, sino de que la combinación entre dirección, estructura y calidad del trayecto sugiere un entorno especialmente hostil o poco fiable para la lógica general.

### 5.4. Clase `MIXTO`

Debe absorber los casos intermedios o contradictorios, por ejemplo cuando:

- la capa principal y la estructural discrepan;
- la estructura de fondo sigue siendo razonable, pero la táctica se ha deteriorado;
- el retorno intermedio mejora, pero la calidad del trayecto sigue siendo mala;
- el contexto no es claramente favorable ni claramente problemático.

**Interpretación:** la clase mixta no es un cajón de sastre arbitrario, sino la forma disciplinada de reconocer ambigüedad real sin forzar una etiqueta extrema.

### 5.5. Regla operativa conceptual mínima

Sin fijar aún umbrales exactos, la regla mínima puede expresarse así:

1. **Primero** se evalúa el sesgo dominante de la capa principal.
2. **Después** se contrasta con la capa estructural para saber si hay apoyo o contradicción de fondo.
3. **Por último** la capa táctica decide si el contexto reciente mantiene la lectura o la degrada por ruido/estrés.

Esto implica una jerarquía clara:

- la estructural evita sobrelecturas de muy corto plazo;
- la principal decide el tono central;
- la táctica ajusta la confianza de esa lectura.

## 6. Qué queda fuera por ahora

Para que esta primera especificación sea coherente con la evidencia acumulada, deben quedar fuera explícitamente estos elementos.

### 6.1. Operaciones propias como núcleo principal

Quedan fuera como base del selector porque:

- llegan tarde respecto al mercado;
- dependen de pocas observaciones;
- son más frágiles para clasificar contexto;
- aumentan el riesgo de sobreajuste.

Eso no niega que más adelante puedan servir como freno local o vigilancia secundaria. Solo significa que **no forman parte del núcleo de esta primera especificación**.

### 6.2. Múltiples confirmadores externos

Quedan fuera en esta fase porque:

- añaden complejidad operativa y conceptual;
- no son necesarios para una primera especificación auditable;
- el mercado principal ya cubre la mayor parte del contexto relevante;
- la evidencia de `ANALISIS 53` recomienda máxima parsimonia.

Si en el futuro se añade uno, la hipótesis más razonable sería un único confirmador simple. Pero eso queda fuera del alcance actual.

### 6.3. Clases excesivamente finas

Quedan fuera subclases como:

- estrés bajista;
- lateral ruidoso;
- reversión violenta;
- variantes por año o episodio.

Quedan fuera porque:

- todavía serían demasiado narrativas;
- elevan el riesgo de sobreajuste retrospectivo;
- no son necesarias para una primera taxonomía útil.

La salida oficial se mantiene, por tanto, en **3 clases y no más**.

### 6.4. Umbrales finales optimizados

También quedan fuera:

- cortes numéricos finales;
- pesos exactos entre variables;
- reglas definitivas de transición entre clases;
- calibraciones optimizadas por periodo histórico.

La meta actual es especificar la arquitectura, no cerrarla paramétricamente.

### 6.5. Estrategias distintas por clase

Queda fuera cualquier decisión del tipo:

- una lógica para `FAVORABLE`;
- otra para `MIXTO`;
- otra para `PROBLEMATICO`.

Ese paso solo tendría sentido cuando la clasificación esté validada como objeto descriptivo. En esta fase todavía no corresponde.

## 7. Ventajas y debilidades de esta primera especificación

### 7.1. Ventajas

#### A. Simplicidad

La arquitectura tiene solo **3 capas** y **5 variables**. Eso reduce complejidad prematura y facilita auditoría.

#### B. Trazabilidad

Cada variable tiene una función concreta:

- estructura;
- dirección intermedia;
- sobreextensión;
- ruido;
- estrés.

No hay una batería opaca de señales sin papel claro.

#### C. Coherencia con `50–55`

La especificación respeta los mensajes principales acumulados:

- `3 meses` como centro del lenguaje contextual;
- `6 meses`/estructura como ancla;
- corto plazo solo como modulador;
- mercado principal como núcleo;
- tres clases como taxonomía oficial;
- parsimonia operativa compatible con `IBKR`.

#### D. Interpretabilidad alta

Cada capa puede explicarse de forma sencilla:

- táctica = calidad reciente del trayecto;
- principal = tono dominante del mercado;
- estructural = sesgo de fondo.

#### E. Viabilidad conceptual en `IBKR`

Todas las variables propuestas pueden calcularse con datos diarios simples del mercado principal, lo que hace viable una futura traducción operativa sin depender de infraestructura compleja.

### 7.2. Debilidades

#### A. Ambigüedad todavía inevitable en la combinación

Aunque la arquitectura queda definida, todavía no se fijan pesos ni umbrales exactos. Por tanto, la especificación ya es auditable, pero aún no completamente operativa.

#### B. Posible redundancia parcial

`retorno intermedio`, `distancia a SMA200` y `QQQ > SMA200` comparten parte de la información direccional. Esa redundancia es aceptable por ahora porque mejora interpretabilidad, pero deberá vigilarse en análisis posteriores.

#### C. Cobertura limitada de entornos especiales

Al no usar todavía confirmadores externos ni subclases, algunos entornos especiales podrían quedar resumidos de forma demasiado gruesa dentro de `MIXTO` o `PROBLEMATICO`.

#### D. No resuelve todavía la transición temporal fina

La especificación define capas y lógica general, pero todavía no responde con precisión cuándo debe cambiar el selector de una clase a otra.

## 8. Conclusión final

La evidencia acumulada en `ANALISIS 50–55` ya permite construir una **primera especificación suficiente, explícita y auditable** del selector de contexto sin necesidad de implementarlo todavía en producción.

La forma más coherente de hacerlo es mediante un selector de **3 capas temporales**:

- **táctica** para ruido y estrés recientes;
- **principal** para la lectura dominante del mercado;
- **estructural** para el sesgo de fondo.

La versión mínima razonable de esa arquitectura puede sostenerse con **5 variables** del mercado principal:

- cruces recientes con `SMA50`;
- volatilidad realizada o `ATR%` corto;
- retorno intermedio;
- distancia a `SMA200`;
- `QQQ > SMA200`.

Su salida oficial debe limitarse a **3 clases**:

- `FAVORABLE`;
- `MIXTO`;
- `PROBLEMATICO`.

Y debe dejar fuera, por ahora:

- operaciones propias como núcleo principal;
- múltiples confirmadores externos;
- taxonomías demasiado finas;
- umbrales finales optimizados;
- estrategias diferentes por clase.

En conjunto, esta propuesta parece el punto de equilibrio más sano entre simplicidad, interpretabilidad, coherencia histórica y viabilidad conceptual futura en `IBKR`.

## 9. Recomendación: especificación suficiente / simplificar más / aún demasiado ambigua

### Métricas mínimas evaluadas

- **Número de capas propuestas:** `3`.
- **Número de variables por capa:** táctica `2`, principal `2`, estructural `1`.
- **Interpretabilidad por capa:** alta en las tres; especialmente alta en la estructural.
- **Coherencia con `50–55`:** alta.
- **Complejidad total del selector:** baja-media; suficientemente austera para esta fase.
- **Viabilidad conceptual en `IBKR`:** alta a nivel de datos y cálculo diario.

### Recomendación final

**Recomendación: especificación suficiente.**

No parece necesario simplificar más en esta fase porque hacerlo probablemente eliminaría alguna dimensión importante del contexto, especialmente ruido/estrés o estructura de fondo.

Tampoco parece correcto decir que siga siendo demasiado ambigua: todavía no es operativa, pero ya es lo bastante concreta como para auditarla, discutirla y usarla como base disciplinada para la siguiente fase de investigación.
