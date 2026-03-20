# VERSION 2.2.2 ANALISIS 71

## 1. Objetivo

Definir una hoja de ruta disciplinada y limitada para la **siguiente tanda de investigación** sobre **modulación de exposición condicionada por régimen**, dejando separadas:

- las **familias de hipótesis** que sí merecen estudio;
- los **criterios de evaluación** que deberán aplicarse a cada familia;
- el **orden de prioridad** recomendado para Codex;
- y qué líneas conviene **posponer** para no convertir todavía esta fase en validación final ni en rediseño de producción.

Este documento:

- **no toca producción**;
- **no implementa** cambios en `META_BOT.py` ni en la lógica vigente;
- **no diseña reglas finales**;
- **no valida definitivamente** ninguna modulación de exposición;
- y **sí prepara** una fase acotada, auditable y metodológicamente prudente.

La pregunta central ya no es si el selector tiene utilidad analítica mínima. La pregunta ahora es otra: **qué tipo de hipótesis de exposición merece probarse primero, con qué disciplina y en qué secuencia, para no abrir demasiados frentes a la vez ni caer en sobreajuste prematuro**.

---

## 2. Evidencia revisada

### 2.1. Lectura obligatoria solicitada

Las instrucciones exigían leer obligatoriamente:

- `ANALISIS 68.md`
- `ANALISIS 69.md`
- `ANALISIS 70.md`

Sin embargo, **esos tres archivos no existen actualmente en el repositorio**. Por tanto:

- no han podido ser leídos literalmente;
- no debe fingirse continuidad documental inexistente;
- y la hoja de ruta debe apoyarse en la **última evidencia verificable disponible**.

### 2.2. Evidencia efectivamente revisada y usada

Sí se han revisado y usado de forma directa:

- `ANALISIS 64.md`;
- `ANALISIS 65.md`;
- `ANALISIS 66.md`;
- `ANALISIS 67.md`.

Además, tal como pedían las instrucciones, se considera la evidencia acumulada que esos documentos arrastran desde `ANALISIS 56–63`, y en particular la base conceptual y metodológica ya consolidada en `64–67`.

### 2.3. Señales principales que deja la cadena 64–67

De la evidencia revisada salen seis señales relevantes para preparar la fase siguiente:

1. **La modulación por régimen no debe arrancar desde una lectura binaria simplista.**
   `FAVORABLE`, `MIXTO` y `PROBLEMATICO` tienen personalidad distinta, y ni `FAVORABLE` monopoliza el edge ni `PROBLEMATICO` equivale automáticamente a mal comportamiento operativo.

2. **`MIXTO` no puede tratarse como residuo sin importancia.**
   La evidencia de `ANALISIS 64` muestra que el sistema general obtiene una parte muy relevante del resultado dentro de `MIXTO`, aunque acompañado de más tensión y drawdown.

3. **`PROBLEMATICO` sí justifica investigación específica, pero no reacción automática.**
   La misma evidencia muestra que puede haber años y subtramos hostiles donde el sistema general, especialmente por la pata short, siga capturando valor real.

4. **Dentro de `PROBLEMATICO` hay heterogeneidad suficiente como para extremar la prudencia.**
   `ANALISIS 66` diferencia entre estrés bajista absorbible, transición errática, lateralidad hostil y reversión violenta. Eso refuerza que la siguiente tanda no debe asumir que toda reducción de exposición en `PROBLEMATICO` será automáticamente correcta.

5. **La siguiente fase debe ser parcial y acotada.**
   `ANALISIS 67` ya concluye que existe base para abrir investigación condicionada por régimen, pero solo de forma limitada, auditada y sin saltar todavía a una batería amplia de variantes finales.

6. **El foco natural de la siguiente tanda es la exposición, no la redefinición completa del selector.**
   La pregunta mejor preparada ahora no es crear nuevas clases ni nuevas estrategias productivas, sino estudiar si conviene modular el tamaño/exposición según régimen de una forma simple, interpretable y robusta.

### 2.4. Implicación metodológica para este documento

La hoja de ruta debe nacer con cuatro restricciones explícitas:

- **pocas familias** y bien separadas;
- **criterios comparables** entre familias;
- **prioridad para hipótesis simples y auditables**;
- y **aplazamiento** de combinaciones complejas hasta que haya evidencia suficiente.

---

## 3. Familias de hipótesis futuras

Para evitar dispersión, la siguiente tanda no debería abrir muchas variantes a la vez. La propuesta prudente es trabajar con **4 familias**, pero **priorizar realmente solo 2 al inicio**.

### 3.1. Familia A: tope máximo nominal por régimen

**Idea base:** mantener la lógica general vigente, pero limitar el tamaño máximo permitido según el régimen de entrada.

Ejemplos conceptuales de futura investigación:

- mismo esquema base para todos los trades;
- techo nominal más alto en `FAVORABLE`;
- techo intermedio en `MIXTO`;
- techo más bajo en `PROBLEMATICO`.

Qué representa esta familia:

- una modulación **directa y fácil de auditar**;
- un cambio de exposición con lectura intuitiva;
- una hipótesis relativamente estable porque toca un solo eje principal: el **máximo tamaño permitido**.

Ventajas metodológicas:

- alta simplicidad;
- trazabilidad clara;
- fácil comparación contra el baseline actual;
- riesgo contenido de construir una lógica demasiado sofisticada.

Riesgo principal:

- puede ser demasiado rígida si `MIXTO` y `PROBLEMATICO` contienen subtexturas muy distintas;
- puede recortar justo donde el general aún mantiene edge útil, especialmente en `MIXTO` y en partes absorbibles de `PROBLEMATICO`.

### 3.2. Familia B: reducción porcentual de exposición por régimen

**Idea base:** en lugar de fijar topes nominales absolutos, aplicar un multiplicador de exposición según régimen.

Ejemplos conceptuales de futura investigación:

- `100%` de exposición base en `FAVORABLE`;
- reducción parcial en `MIXTO`;
- reducción más intensa en `PROBLEMATICO`.

Qué representa esta familia:

- una versión más continua y escalable que la familia A;
- una lectura de “cautela proporcional” en lugar de “límite duro”.

Ventajas metodológicas:

- sigue siendo simple;
- se compara bien con el general;
- puede adaptarse mejor a transiciones sin crear saltos tan bruscos.

Riesgo principal:

- aumenta algo la sensibilidad paramétrica;
- invita más fácilmente a probar muchos porcentajes y, por tanto, a sobreoptimizar si no se restringe el espacio de búsqueda.

### 3.3. Familia C: exposición escalonada entre FAVORABLE, MIXTO y PROBLEMATICO

**Idea base:** establecer una jerarquía explícita y ordinal de exposición entre los tres regímenes, no solo una reducción parcial aislada.

Ejemplos conceptuales de futura investigación:

- `FAVORABLE > MIXTO > PROBLEMATICO`;
- diferencias pequeñas o medias entre escalones;
- estudio de si la separación debe ser suave o marcada.

Qué representa esta familia:

- una formalización más completa del principio de exposición por régimen;
- una hipótesis más estructurada que A o B.

Ventajas metodológicas:

- encaja bien con la taxonomía de tres clases;
- deja una política clara y coherente si luego mostrara valor.

Riesgo principal:

- aunque parece simple, en realidad abre muchas combinaciones de escalones;
- puede convertir demasiado pronto una intuición razonable en una mini-superficie de optimización;
- corre el riesgo de forzar una jerarquía donde la evidencia actual todavía no justifica diferencias demasiado precisas, sobre todo por el papel no trivial de `MIXTO`.

### 3.4. Familia D: combinación de general + cautela de tamaño

**Idea base:** conservar plenamente el sistema general como baseline operativo, añadiendo solo una capa secundaria de cautela de tamaño en contextos concretos.

Ejemplos conceptuales de futura investigación:

- baseline intacto como referencia principal;
- cautela limitada solo en regímenes de mayor duda;
- posible énfasis en `MIXTO`, `PROBLEMATICO` o ambos, según la evidencia futura.

Qué representa esta familia:

- una familia más conservadora conceptualmente;
- prioriza “no dañar años buenos del general” antes que intentar mejorar agresivamente los malos.

Ventajas metodológicas:

- muy alineada con la prudencia de `ANALISIS 67`;
- reduce el riesgo de romper el perfil histórico del general;
- fácil de defender si la pregunta principal es protección sin rediseño.

Riesgo principal:

- puede solaparse parcialmente con A y B si no se define bien;
- si se abre demasiado pronto junto a muchas variantes, puede duplicar familias y generar ruido analítico.

### 3.5. Número de familias priorizadas

Aunque aquí se enumeran **4 familias**, la recomendación no es estudiarlas todas en paralelo.

Propuesta disciplinada:

- **familias listadas:** 4;
- **familias realmente priorizadas para apertura inmediata:** 2;
- **familias a mantener en espera o segunda ronda:** 2.

---

## 4. Criterios de evaluación propuestos

Cada familia debe evaluarse con una plantilla común. La siguiente tanda será sana solo si todas las hipótesis se juzgan con los mismos criterios y no por impresiones aisladas.

### 4.1. Preservación de años favorables

Debe medirse si la hipótesis:

- conserva razonablemente los buenos años del general;
- evita deteriorar de forma innecesaria tramos donde el baseline ya funciona bien;
- no sacrifica demasiado retorno estructural en `FAVORABLE` ni en partes productivas de `MIXTO`.

Pregunta guía:

**¿La cautela propuesta protege sin amputar en exceso la capacidad del sistema para seguir capturando años históricamente favorables?**

### 4.2. Protección en contextos hostiles

Debe medirse si la hipótesis:

- reduce daño en entornos realmente tensos;
- mejora el perfil de drawdown o la estabilidad en contextos adversos;
- aporta defensa sin anular toda la capacidad de captura del general en episodios `PROBLEMATICO` absorbibles.

Pregunta guía:

**¿La modulación propuesta protege mejor cuando el contexto se vuelve hostil, sin borrar por completo la parte del edge que aún puede sobrevivir ahí?**

### 4.3. Simplicidad

Debe evaluarse:

- número de parámetros nuevos;
- facilidad de explicar la regla;
- facilidad de reconstrucción manual y de auditoría posterior;
- grado en que la hipótesis evita depender de excepciones o condiciones encadenadas.

Pregunta guía:

**¿La familia puede sostenerse con una lógica corta, comprensible y replicable?**

### 4.4. Robustez

Debe medirse si el comportamiento observado:

- no depende de uno o dos años extremos;
- no se explica por un pequeño subconjunto de trades;
- se mantiene razonablemente al cambiar ligeramente el valor de los parámetros.

Pregunta guía:

**¿La mejora o el deterioro que produce la hipótesis parece repartido y defendible, o descansa en pocos episodios decisivos?**

### 4.5. Sensibilidad a parámetros

Debe medirse:

- cuánto cambia el resultado al mover modestamente el tamaño de la modulación;
- si existe una meseta razonable o solo un punto “mágico” muy frágil;
- cuántos grados de libertad introduce la familia.

Pregunta guía:

**¿La hipótesis parece estable dentro de un rango corto y razonable, o solo funciona en un ajuste fino sospechoso?**

### 4.6. Riesgo de sobreajuste por familia

Además del resultado observado, cada familia debe clasificarse explícitamente por riesgo de sobreajuste:

- **bajo**: muy pocos parámetros, lectura directa, poca combinatoria;
- **medio**: uno o dos grados de libertad relevantes, pero todavía auditables;
- **alto**: varias combinaciones, escalones múltiples o interacción difícil de interpretar.

### 4.7. Impacto esperado sobre el general

Antes de probar, cada familia debe dejar formulada una expectativa disciplinada:

- impacto esperado sobre retorno general;
- impacto esperado sobre drawdown;
- impacto esperado sobre continuidad del perfil histórico del baseline.

Esto obliga a declarar por adelantado si la familia busca principalmente:

- **proteger**;
- **suavizar**;
- o **reordenar** la exposición del general.

### 4.8. Facilidad de auditoría

Cada familia debe puntuarse también por la facilidad con la que un tercero puede revisar:

- qué hace la regla;
- en qué operaciones actúa;
- y por qué cambia la exposición.

Cuanto más importante sea la modulación propuesta, más alta debe ser la exigencia de auditoría.

### 4.9. Plantilla mínima de evaluación futura

Para cada familia que Codex abra en la siguiente tanda, conviene dejar una ficha mínima con estos campos:

| Campo mínimo | Qué debe responder |
|---|---|
| Objetivo de la familia | Qué intenta mejorar sin rediseñar el sistema |
| Eje de exposición | Tope nominal, multiplicador, escalón o cautela puntual |
| Preservación de años favorables | Alta / Media / Baja |
| Protección en hostiles | Alta / Media / Baja |
| Simplicidad | Alta / Media / Baja |
| Robustez esperada | Alta / Media / Baja |
| Sensibilidad a parámetros | Baja / Media / Alta |
| Riesgo de sobreajuste | Bajo / Medio / Alto |
| Impacto esperado sobre el general | Bajo / Medio / Alto |
| Facilidad de auditoría | Alta / Media / Baja |
| Prioridad recomendada | 1 / 2 / 3 / Espera |

---

## 5. Orden de prioridad

La prioridad recomendada no debe basarse en cuál parece más prometedora en abstracto, sino en cuál permite aprender más con menos complejidad y menos riesgo de engaño analítico.

### 5.1. Prioridad 1: Familia A — tope máximo nominal por régimen

**Motivo de prioridad:**

- es la familia más directa de auditar;
- introduce un solo eje claro;
- permite observar rápido si una restricción simple de tamaño ya cambia de forma significativa el equilibrio entre preservación y protección;
- minimiza el riesgo de abrir una superficie amplia de parámetros.

**Riesgo de sobreajuste:** bajo-medio.

**Impacto esperado sobre el general:** medio.

**Facilidad de auditoría:** alta.

**Juicio:** debe estudiarse primero porque es la prueba más limpia para saber si la exposición por régimen merece realmente más trabajo.

### 5.2. Prioridad 2: Familia B — reducción porcentual de exposición por régimen

**Motivo de prioridad:**

- mantiene simplicidad suficiente;
- ofrece una comparación muy natural con la familia A;
- permite estudiar si una cautela proporcional funciona mejor que un límite duro.

**Riesgo de sobreajuste:** medio.

**Impacto esperado sobre el general:** medio.

**Facilidad de auditoría:** media-alta.

**Juicio:** debe abrirse solo si A deja una señal útil o, alternativamente, como segundo eje comparado muy acotado frente a A.

### 5.3. Prioridad 3: Familia D — combinación de general + cautela de tamaño

**Motivo de prioridad:**

- conceptualmente es prudente;
- pero conviene dejarla detrás de A y B para no duplicar hipótesis antes de tiempo;
- muchas de sus intuiciones pueden quedar parcialmente cubiertas por A o B si estos ya se formulan con disciplina.

**Riesgo de sobreajuste:** medio.

**Impacto esperado sobre el general:** bajo-medio.

**Facilidad de auditoría:** media.

**Juicio:** recomendable como segunda ronda si la primera muestra que la modulación simple tiene valor y que merece un refinamiento conservador.

### 5.4. Prioridad 4: Familia C — exposición escalonada entre FAVORABLE, MIXTO y PROBLEMATICO

**Motivo de prioridad:**

- es la más tentadora narrativamente, pero no la más prudente;
- abre más grados de libertad;
- corre el riesgo de forzar una jerarquía demasiado precisa cuando la evidencia actual sigue diciendo que `MIXTO` y parte de `PROBLEMATICO` contienen edge real del general.

**Riesgo de sobreajuste:** medio-alto / alto.

**Impacto esperado sobre el general:** medio-alto.

**Facilidad de auditoría:** media-baja frente a las familias anteriores.

**Juicio:** debería esperar hasta que una primera ronda simple confirme que realmente existe una señal robusta de mejora al tocar exposición.

### 5.5. Resumen de prioridad recomendada por familia

| Familia | Prioridad recomendada | Riesgo de sobreajuste | Impacto esperado sobre el general | Facilidad de auditoría |
|---|---:|---|---|---|
| A. Tope máximo nominal por régimen | 1 | Bajo-Medio | Medio | Alta |
| B. Reducción porcentual de exposición por régimen | 2 | Medio | Medio | Media-Alta |
| D. General + cautela de tamaño | 3 | Medio | Bajo-Medio | Media |
| C. Exposición escalonada FAVORABLE/MIXTO/PROBLEMATICO | 4 | Medio-Alto / Alto | Medio-Alto | Media-Baja |

---

## 6. Qué estudiar primero

La siguiente tanda debería empezar de forma **estrecha y comparativa**, no amplia.

### 6.1. Hipótesis que deben estudiarse primero

Las dos líneas con mejor relación entre valor informativo y disciplina metodológica son:

1. **tope máximo nominal por régimen**;
2. **reducción porcentual de exposición por régimen**.

### 6.2. Por qué estas dos primero

Porque juntas permiten comparar dos formas simples de responder a la misma pregunta:

- si la exposición por régimen merece tocarse;
- y si, en caso de tocarse, es mejor una lógica de **límite duro** o una lógica de **cautela proporcional**.

Esa comparación ya sería suficientemente informativa sin abrir todavía una arquitectura compleja.

### 6.3. Enfoque recomendado para Codex

Codex debería abrir una tanda **muy limitada** con uno de estos dos formatos:

- **Formato preferido:** un solo eje primero, empezando por la familia A.
- **Formato aceptable si se quiere comparación mínima:** dos ejes comparados, pero solo A vs B y con espacio paramétrico muy restringido.

### 6.4. Decisión recomendada entre un eje, dos ejes o consolidar antes

La conclusión de este documento es la siguiente:

- **no** conviene abrir más de dos ejes comparados;
- **no** conviene consolidar indefinidamente antes de empezar, porque ya existe base suficiente para una apertura parcial;
- la mejor opción es **abrir una tanda muy limitada**, preferiblemente con **un solo eje principal** y, como máximo, **un segundo eje espejo muy controlado** para comparación.

En términos prácticos, la recomendación más prudente es:

**abrir la siguiente tanda centrada en un solo eje principal de exposición, con la opción secundaria de comparar un segundo eje simple si se mantiene un marco extremadamente acotado.**

---

## 7. Qué dejar para más adelante

Para no convertir la hoja de ruta en validación prematura, conviene aplazar explícitamente varias líneas.

### 7.1. Dejar para más adelante la exposición escalonada completa

La familia escalonada `FAVORABLE > MIXTO > PROBLEMATICO` debe esperar porque:

- introduce demasiadas combinaciones de niveles;
- puede esconder sobreajuste detrás de una narrativa muy convincente;
- y todavía no hay base suficiente para fijar una jerarquía fina sin pasar antes por pruebas más austeras.

### 7.2. Dejar para más adelante combinaciones con demasiada lógica adicional

También deben esperar:

- combinaciones de exposición con filtros internos adicionales;
- reglas distintas por subpatrón dentro de `PROBLEMATICO`;
- modulaciones simultáneas por régimen y por módulo long/short;
- cualquier estructura con demasiados parámetros o excepciones.

### 7.3. Dejar para más adelante reglas finales de producción

Aunque una familia simple mostrara señal interesante, todavía no correspondería:

- fijar reglas finales;
- integrar nada en producción;
- ni tratar la siguiente tanda como validación definitiva.

### 7.4. Dejar para más adelante lecturas demasiado agresivas sobre PROBLEMATICO

Dado que `ANALISIS 64–66` deja claro que `PROBLEMATICO` no es homogéneo y no siempre destruye al general, debe esperar cualquier hipótesis de tipo:

- “recorte fuerte automático en todo `PROBLEMATICO`”; 
- “anulación casi total de exposición en contexto hostil”; 
- o “respuesta severa por defecto” sin una primera ronda simple que lo justifique.

---

## 8. Conclusión final

La evidencia acumulada ya justifica preparar una fase posterior sobre **exposición condicionada por régimen**, pero solo si esa fase nace con disciplina fuerte y alcance deliberadamente corto.

La hoja de ruta más sana no es abrir muchas familias, sino organizar pocas y muy claras.

### Síntesis central

1. **La siguiente tanda debe centrarse en exposición, no en rediseño general.**
2. **Las familias iniciales deben ser pocas, simples y auditables.**
3. **La primera comparación útil es entre límite duro y cautela proporcional.**
4. **La exposición escalonada completa debe esperar.**
5. **El objetivo inmediato no es validar reglas finales, sino aprender si tocar exposición aporta valor robusto sin dañar en exceso al general.**

### Dictamen metodológico final

La siguiente fase **sí debe abrirse**, pero **de forma muy limitada** y con prioridad para hipótesis que:

- tengan pocos grados de libertad;
- preserven la capacidad de auditoría;
- y permitan decidir pronto si merece la pena seguir investigando o si conviene volver a consolidar antes de ampliar el árbol de pruebas.

---

## 9. Recomendación: abrir siguiente tanda de exposición / abrir muy limitada / consolidar antes de seguir

**Recomendación final: abrir muy limitada.**

### Traducción práctica de la recomendación

- **No** abrir muchas familias a la vez.
- **Sí** abrir una investigación pequeña y disciplinada sobre exposición.
- **Prioridad principal:** familia A.
- **Prioridad secundaria opcional y comparativa:** familia B.
- **En espera:** familias D y C, en ese orden.

### Respuesta final a la decisión pedida

Entre las tres opciones solicitadas:

- **un solo eje de exposición**;
- **dos ejes comparados**;
- **o más consolidación previa**;

la recomendación es:

**abrir un solo eje principal de exposición**, con posibilidad de **comparar un segundo eje simple solo de forma muy controlada**, y **sin pasar todavía a una batería amplia ni a validación final**.

### Cierre

Por tanto, la siguiente tanda debe abrirse, pero **muy limitada**, priorizando **pocas hipótesis, muy claras y auditables**, y dejando explícitamente para después cualquier familia más compleja o escalonada.
