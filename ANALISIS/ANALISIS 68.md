# VERSION 2.2.2 ANALISIS 68

## 1. Objetivo

Determinar qué **decisiones suaves** puede gobernar razonablemente el selector de régimen ya aceptado como base de investigación, **sin cambiar la lógica base del sistema general long-short**, **sin abrir todavía estrategias distintas por clase** y **sin tocar producción**.

La pregunta no es cómo rediseñar el sistema, sino qué grados de modulación prudente merece estudiar primero el selector en calidad de capa de control. La prioridad explícita es evaluar controles de:

- **modulación de exposición**;
- **tope máximo nominal de entrada**;
- **reducción de tamaño por régimen**;
- **cautela adicional en MIXTO**;
- **restricciones prudentes en PROBLEMATICO**.

El criterio rector de este informe es metodológicamente conservador: antes de introducir nuevas señales, nuevas lógicas o variantes por clase, conviene explorar si el selector ya puede aportar valor gobernando decisiones **más suaves, auditables y reversibles**, centradas en la exposición y en los límites operativos.

---

## 2. Evidencia revisada

Se ha revisado obligatoriamente la cadena:

- `ANALISIS 64.md`;
- `ANALISIS 65.md`;
- `ANALISIS 66.md`;
- `ANALISIS 67.md`.

### 2.1. Señales relevantes heredadas de ANALISIS 64

`ANALISIS 64` deja cinco mensajes especialmente útiles para esta tarea:

1. **El sistema general ya gana en las tres clases**, por lo que el selector no debe usarse todavía como interruptor binario de “permitir/prohibir” toda la operativa.
2. **MIXTO concentra la mayor parte del beneficio total**, pero también el mayor drawdown segmentado. Eso sugiere que el problema allí no es falta de edge, sino necesidad de una gestión más prudente del riesgo y de la intensidad.
3. **FAVORABLE es rentable y descriptivamente sano**, aunque no monopoliza el edge del sistema general.
4. **PROBLEMATICO no equivale a inutilidad operativa**, porque la pata short del general puede monetizarlo razonablemente bien.
5. La evidencia sugiere que, en esta fase, el selector encaja mejor como **modulador** que como motor de sustitución del sistema base.

### 2.2. Señales relevantes heredadas de ANALISIS 65

`ANALISIS 65` aporta una advertencia importante sobre `PROBLEMATICO`:

- el buen comportamiento de `2022` es **real en saldo**, pero **concentrado** en pocos trades y pocos bloques temporales;
- por tanto, no conviene sobrerreaccionar interpretando `PROBLEMATICO` como un régimen ya totalmente resuelto;
- la lectura prudente es que el general **puede absorberlo**, pero esa absorción todavía parece de **robustez media-baja** si se exige dispersión amplia.

Esta evidencia favorece decisiones suaves de **cautela, límites y reducción de intensidad**, antes que decisiones duras o rediseños específicos.

### 2.3. Señales relevantes heredadas de ANALISIS 66

`ANALISIS 66` muestra que `PROBLEMATICO` no es homogéneo: contiene al menos cuatro subpatrones observables (`estrés bajista absorbible`, `transición errática`, `lateralidad hostil`, `reversión violenta`).

De ahí se desprenden tres consecuencias directas para este informe:

1. Las decisiones suaves que mande el selector deben ser **robustas a la heterogeneidad interna** de `PROBLEMATICO`.
2. Cuanto más simple y externa a la señal sea la decisión, **menos riesgo de sobreajuste** habrá frente a subtipos aún inmaduros.
3. Tiene más sentido estudiar **restricciones prudentes de tamaño o exposición** que reglas nuevas dependientes de microestructura interna del régimen.

### 2.4. Señales relevantes heredadas de ANALISIS 67

`ANALISIS 67` concluye que el selector ya tiene madurez **medio-alta para investigación** y que una siguiente fase, si se abre, debe ser **parcial, acotada y no agresiva**. En particular:

- no conviene diseñar aún estrategias nuevas por régimen;
- `MIXTO` debe seguir tratándose como **zona de cautela**;
- `PROBLEMATICO` justifica investigación, pero no una sobrerreacción arquitectónica;
- el valor actual del selector es mayor como **organizador de decisiones prudentes** que como generador de sistemas separados.

### 2.5. Implicación metodológica conjunta

Tomadas en conjunto, las evidencias de `64–67` empujan hacia una conclusión común:

- **sí** parece razonable abrir investigación sobre decisiones suaves gobernadas por régimen;
- **no** parece razonable, todavía, abrir lógica nueva por régimen;
- la primera capa a estudiar debe estar centrada en **exposición, tamaño, topes y cautela operativa**, porque es donde el selector puede añadir disciplina sin contaminar en exceso el edge del general.

---

## 3. Familias de decisiones suaves evaluadas

En esta fase se evalúan **cinco familias** de decisión suave, todas compatibles con la restricción de no alterar la lógica base del sistema general:

| Familia | Qué gobierna | Simplicidad operativa | Riesgo de romper el edge del general | Facilidad de medir impacto histórico | Coherencia con 64–67 | Prioridad relativa |
|---|---|---|---|---|---|---|
| 1. Modulación global de exposición | Ajustar intensidad agregada por régimen sin cambiar señales | Alta | Bajo-medio | Alta | Muy alta | Muy alta |
| 2. Tope máximo nominal de entrada | Limitar capital nominal comprometido por trade según régimen | Muy alta | Bajo | Muy alta | Alta | Alta |
| 3. Reducción de tamaño por régimen | Escalar tamaño unitario o fraccional según clase | Alta | Bajo-medio | Alta | Muy alta | Muy alta |
| 4. Cautela adicional en MIXTO | Introducir disciplina de prudencia específica sin cancelar el régimen | Media-alta | Bajo-medio | Media-alta | Muy alta | Alta |
| 5. Restricciones prudentes en PROBLEMATICO | Limitar agresividad en el régimen más hostil sin anularlo | Media | Medio | Media-alta | Alta | Media-alta |

### 3.1. Familia 1: modulación global de exposición

Consiste en dejar intactas las señales del sistema general, pero permitir que el selector module **cuánta exposición efectiva** se permite cuando una señal ya existe.

Ejemplos conceptuales válidos dentro de esta familia:

- exposición plena en `FAVORABLE`;
- exposición intermedia en `MIXTO`;
- exposición reducida o más defensiva en `PROBLEMATICO`.

No implica inventar una estrategia distinta, sino usar el régimen como una **capa de intensidad**.

### 3.2. Familia 2: tope máximo nominal de entrada

Aquí el selector no decide tanto el porcentaje de intensidad relativa como un **límite duro y simple** sobre el nominal máximo permitido por operación o por lado.

Es una familia aún más austera que la anterior, porque su lógica es casi puramente de control de riesgo operacional:

- en clases sanas se admite un tope más amplio;
- en clases menos limpias se impone un techo más estricto.

### 3.3. Familia 3: reducción de tamaño por régimen

Esta familia es parecida a la modulación de exposición, pero aplicada de forma más directa al **tamaño de entrada** de cada operación.

Su lectura práctica es muy simple:

- el sistema sigue entrando cuando debe entrar;
- pero el selector decide si esa entrada se ejecuta a tamaño completo o reducido.

Es una forma natural de trasladar al sizing la información contextual ya capturada por el selector.

### 3.4. Familia 4: cautela adicional en MIXTO

La evidencia de `64` y `67` sugiere que `MIXTO` no debe tratarse ni como clase vacía ni como clase plenamente confiable. Por eso tiene sentido estudiar una familia propia de decisiones suaves para `MIXTO`, centrada en **prudencia adicional**.

Aquí la idea no es prohibir operar, sino reconocer que:

- `MIXTO` genera mucho resultado;
- pero también concentra más irregularidad y mayor drawdown segmentado;
- por tanto, merece una modulación de intensidad o de límites más disciplinada que `FAVORABLE`.

### 3.5. Familia 5: restricciones prudentes en PROBLEMATICO

Dado que `PROBLEMATICO` no es sinónimo de fracaso, pero tampoco bloque homogéneo ni totalmente resuelto, tiene sentido estudiar si el selector debe imponer **restricciones prudentes** cuando el contexto cae ahí.

Lo importante es que esas restricciones no deben equivaler todavía a “apagar el sistema” ni a “crear otra estrategia”, sino a reconocer que:

- hay heterogeneidad interna;
- hay absorción real, pero no plenamente robusta;
- la operativa en este bloque debe tratarse con más disciplina que en `FAVORABLE`.

---

## 4. Ventajas y riesgos de cada familia

### 4.1. Modulación global de exposición

**Ventajas**

- Es probablemente la familia más **interpretable** de todas: el régimen no cambia la señal, solo la cantidad de riesgo que se deja pasar.
- Tiene **alta compatibilidad con IBKR**, porque se traduce fácilmente a menor exposición efectiva o menor tamaño total permitido.
- Es **auditables** tanto ex ante como ex post: puede reconstruirse fácilmente cuánto riesgo se tomó en cada clase.
- Es una decisión **poco agresiva** sobre el sistema general: conserva el edge potencial y solo actúa sobre su amplitud.

**Riesgos**

- Si se parametriza con demasiados escalones o demasiado detalle, puede derivar en sobreajuste fino de sizing.
- Si la reducción es excesiva, puede recortar justo las zonas donde hoy aparece gran parte del beneficio, especialmente en `MIXTO` y partes de `PROBLEMATICO`.

**Evaluación comparativa**

- **Interpretabilidad:** muy alta.
- **Riesgo de sobreajuste:** bajo si se mantienen pocos escalones; medio si se afina demasiado.
- **Facilidad de auditoría:** muy alta.
- **Compatibilidad con IBKR:** muy alta.
- **Agresividad del cambio:** baja.

### 4.2. Tope máximo nominal de entrada

**Ventajas**

- Es la familia más **simple operacionalmente**.
- Tiene **riesgo de sobreajuste muy bajo**, porque funciona como un límite externo y no como una lógica interna sofisticada.
- Es extremadamente **auditable**: o el nominal supera el tope o no lo supera.
- Encaja muy bien con una infraestructura tipo IBKR, donde los límites nominales son fáciles de entender y vigilar.

**Riesgos**

- Puede ser demasiado tosco para capturar matices de intensidad relativa.
- Si el tope se fija demasiado bajo en clases que aún tienen edge, puede amputar parte del rendimiento sin una mejora proporcional del riesgo.
- Aporta disciplina, pero menos sensibilidad fina que la modulación de exposición o el sizing escalado.

**Evaluación comparativa**

- **Interpretabilidad:** muy alta.
- **Riesgo de sobreajuste:** muy bajo.
- **Facilidad de auditoría:** muy alta.
- **Compatibilidad con IBKR:** muy alta.
- **Agresividad del cambio:** muy baja.

### 4.3. Reducción de tamaño por régimen

**Ventajas**

- Es una forma muy natural de trasladar el selector al plano operativo sin tocar la lógica base.
- Mantiene una **relación intuitiva** entre convicción contextual y tamaño ejecutado.
- Permite medir con claridad el impacto histórico por clase sobre drawdown, volatilidad de equity y contribución de beneficio.
- Tiene implementación conceptual sencilla y buena compatibilidad con IBKR.

**Riesgos**

- Se parece mucho a la modulación de exposición y puede acabar duplicando la misma idea con otro nombre si no se define bien el alcance.
- Si se afinan demasiados porcentajes por clase, aparece riesgo de sobreajuste de tamaño.
- Puede reducir demasiado la captura de episodios buenos dentro de `MIXTO` o `PROBLEMATICO` si la prudencia se vuelve excesiva.

**Evaluación comparativa**

- **Interpretabilidad:** alta.
- **Riesgo de sobreajuste:** bajo-medio.
- **Facilidad de auditoría:** alta.
- **Compatibilidad con IBKR:** alta.
- **Agresividad del cambio:** baja.

### 4.4. Cautela adicional en MIXTO

**Ventajas**

- Es la familia mejor alineada con la evidencia de `64` y `67`: `MIXTO` es útil, pero más tenso e irregular.
- Reconoce algo metodológicamente importante: aquí el problema no es ausencia de edge, sino **menor limpieza contextual**.
- Su lógica es fácil de explicar ante auditoría: “no apagamos MIXTO; simplemente exigimos más prudencia”.
- Puede estudiarse sin tocar señales, solo modulando exposición, tamaño o topes cuando el régimen sea `MIXTO`.

**Riesgos**

- Si la cautela se traduce en demasiadas restricciones simultáneas, puede vaciar injustificadamente la clase más productiva del histórico agregado.
- Existe riesgo de sobrerreaccionar al drawdown de `MIXTO` y castigar una zona que hoy explica gran parte del beneficio del general.
- Requiere disciplina para que la cautela siga siendo “suave” y no se convierta en un filtro encubierto.

**Evaluación comparativa**

- **Interpretabilidad:** alta.
- **Riesgo de sobreajuste:** bajo-medio.
- **Facilidad de auditoría:** alta si se limita a una o dos reglas simples.
- **Compatibilidad con IBKR:** alta.
- **Agresividad del cambio:** baja-media.

### 4.5. Restricciones prudentes en PROBLEMATICO

**Ventajas**

- Encajan con la advertencia de `65` y `66`: `PROBLEMATICO` todavía muestra heterogeneidad y absorción no plenamente robusta.
- Permiten reconocer el carácter hostil del régimen sin afirmar erróneamente que ahí no exista edge.
- Son coherentes con un uso prudente del selector: imponer disciplina extra donde la incertidumbre estructural es mayor.

**Riesgos**

- Son más delicadas que las decisiones sobre `MIXTO`, porque `PROBLEMATICO` incluye episodios muy distintos y algunos han sido muy rentables para el general.
- Si la restricción es demasiado fuerte, puede destruir precisamente la captura de los bloques short más valiosos.
- Tienen más riesgo de equivocarse por heterogeneidad interna que las familias centradas en exposición global o topes simples.

**Evaluación comparativa**

- **Interpretabilidad:** media-alta.
- **Riesgo de sobreajuste:** medio.
- **Facilidad de auditoría:** media-alta.
- **Compatibilidad con IBKR:** alta.
- **Agresividad del cambio:** media.

---

## 5. Qué decisiones encajan mejor con FAVORABLE

`FAVORABLE` no parece exigir grandes correcciones. La evidencia revisada sugiere que esta clase funciona mejor como entorno donde el selector debería, en principio, **dejar respirar al general** con la menor fricción posible.

Las decisiones suaves que mejor encajan aquí son:

1. **Modulación de exposición en banda alta o normal.**  
   Tiene sentido que `FAVORABLE` sea la referencia de exposición menos restringida, precisamente porque es la clase más interpretable como contexto sano para continuidad del baseline.

2. **Topes nominales menos severos.**  
   No implica apalancar más, sino evitar castigar innecesariamente al sistema en el entorno donde el selector transmite mayor limpieza contextual.

3. **Reducción de tamaño mínima o nula frente a la línea base.**  
   Si se investiga un esquema de sizing por régimen, `FAVORABLE` debería ser el ancla a partir de la cual se comparan reducciones en otras clases.

Lo que **no** encaja bien en esta fase es introducir restricciones especiales complejas. Sería un cambio poco coherente con la evidencia disponible y demasiado agresivo para un bloque donde el objetivo principal es preservar continuidad del general.

---

## 6. Qué decisiones encajan mejor con MIXTO

`MIXTO` es la clase donde más claramente encaja abrir investigación inmediata sobre decisiones suaves. La razón es fuerte y consistente con `64–67`:

- aporta gran parte del beneficio;
- también concentra el mayor drawdown segmentado;
- ya ha quedado metodológicamente descrita como **zona de cautela**, no como clase residual.

Las decisiones que mejor encajan aquí son:

1. **Cautela adicional en MIXTO como familia prioritaria.**  
   Esta es la decisión más coherente con la evidencia acumulada. No se trata de apagar `MIXTO`, sino de admitir que su productividad viene acompañada de mayor tensión operativa.

2. **Reducción moderada de tamaño por régimen.**  
   Es probablemente la traducción más limpia de esa cautela: el sistema sigue operando, pero no con la misma intensidad que en `FAVORABLE`.

3. **Modulación intermedia de exposición.**  
   Funciona bien como regla paraguas y puede ser más fácil de auditar que una multiplicidad de restricciones locales.

4. **Topes nominales algo más conservadores que en FAVORABLE.**  
   Tiene sentido como complemento simple y fácilmente medible.

Lo que **debería evitarse** es convertir `MIXTO` en una casi-prohibición operativa. Eso chocaría con la evidencia de `ANALISIS 64`, donde precisamente esta clase concentra el mayor aporte agregado del sistema.

---

## 7. Qué decisiones encajan mejor con PROBLEMATICO

`PROBLEMATICO` exige una prudencia distinta. Aquí la evidencia dice dos cosas a la vez:

- no debe tratarse como sinónimo de fracaso operativo;
- pero tampoco como bloque suficientemente limpio para permitir una confianza alta y uniforme.

Por eso, las decisiones suaves que mejor encajan son:

1. **Restricciones prudentes en PROBLEMATICO.**  
   Tiene sentido abrir esta familia, pero de forma acotada. Debe plantearse como disciplina adicional ante heterogeneidad y fragilidad relativa, no como veto sistemático.

2. **Topes máximos nominales más estrictos.**  
   Esta es probablemente la herramienta más segura para empezar, porque es simple, muy auditable y poco propensa a sobreajuste frente a subpatrones aún inmaduros.

3. **Reducción de tamaño por régimen.**  
   También encaja bien si se mantiene austera. Permite reconocer el aumento de hostilidad sin tocar la señal base ni negar el valor de la pata short.

4. **Modulación de exposición claramente más prudente que en FAVORABLE.**  
   Tiene sentido siempre que no se convierta en una anulación casi total del régimen.

Lo que **todavía no encaja** es abrir reglas especializadas por subtipo interno de `PROBLEMATICO`. `ANALISIS 66` justifica investigar la heterogeneidad, pero no legitima aún una ramificación operativa fina.

---

## 8. Prioridad de investigación propuesta

La prioridad debe ordenarse por cuatro criterios simultáneos:

- máxima interpretabilidad;
- mínimo riesgo de sobreajuste;
- alta facilidad de auditoría histórica y operativa;
- mínimo riesgo de romper el edge del sistema general.

### 8.1. Prioridad 1 — Modulación de exposición y reducción de tamaño por régimen

Estas dos familias merecen abrir investigación inmediata porque son las más equilibradas entre utilidad potencial y prudencia metodológica.

**Razones**

- Son conceptualmente limpias.
- Mantienen intacta la lógica de entrada/salida.
- Permiten estudiar impacto histórico con métricas muy claras: retorno, drawdown, contribución por clase y estabilidad del equity.
- Encajan con el papel actual del selector como **capa moduladora**, no como motor de estrategias separadas.

**Juicio**

- Deben ser el núcleo de la siguiente fase.

### 8.2. Prioridad 2 — Cautela adicional en MIXTO

Merece investigación inmediata también, pero como derivación aplicada de la prioridad 1, no como familia totalmente separada y compleja.

**Razones**

- `MIXTO` es la clase con mejor argumento empírico para introducir prudencia sin cancelación.
- La evidencia ya justifica tratarla como una zona de productividad con tensión.
- Se presta muy bien a pruebas de reducción moderada de intensidad.

**Juicio**

- Debe abrirse en paralelo, pero manteniendo reglas simples.

### 8.3. Prioridad 3 — Topes máximos nominales de entrada

También merece investigación relativamente temprana, aunque algo por detrás de exposición/tamaño.

**Razones**

- Su simplicidad y auditabilidad son excelentes.
- Tiene gran compatibilidad con IBKR.
- Es muy seguro metodológicamente.

**Reserva**

- Puede ser demasiado tosco si se usa como único mecanismo.

**Juicio**

- Conviene abrirlo, pero como complemento o benchmark de simplicidad frente a modulación/sizing, no necesariamente como única vía principal.

### 8.4. Prioridad 4 — Restricciones prudentes específicas en PROBLEMATICO

Merecen abrirse con más cautela que las anteriores.

**Razones**

- La evidencia sí justifica prudencia extra en `PROBLEMATICO`.
- Pero `65` y `66` recuerdan que este bloque es heterogéneo y que parte del edge del general aparece precisamente ahí.

**Juicio**

- Deben estudiarse después de fijar primero una gramática simple de exposición, tamaño y topes.
- Si se investigan demasiado pronto o con demasiada dureza, el riesgo de romper el edge del general aumenta.

### 8.5. Qué debería esperar todavía

Deberían esperar, por ahora, todas las decisiones que crucen la línea entre modulación suave y rediseño amplio, por ejemplo:

- reglas nuevas de señal por clase;
- filtros específicos por subtipo de `PROBLEMATICO`;
- árboles distintos de entrada/salida según régimen;
- estrategias separadas para `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

Estas líneas de trabajo serían demasiado agresivas para el estado actual de la evidencia y mezclarían indebidamente decisiones suaves con rediseños grandes.

---

## 9. Conclusión final

Se han evaluado **cinco familias** de decisiones suaves y la comparación deja un resultado bastante claro.

La evidencia de `ANALISIS 64–67` respalda abrir investigación inmediata sobre decisiones que permitan al selector gobernar **la intensidad del riesgo** sin cambiar la lógica base del sistema general long-short. Dentro de ese marco, las familias con mejor balance entre interpretabilidad, bajo sobreajuste, auditabilidad, compatibilidad con IBKR y baja agresividad son:

- **modulación de exposición**;
- **reducción de tamaño por régimen**;
- **cautela adicional en MIXTO**;
- y, como apoyo muy simple, **topes máximos nominales de entrada**.

En cambio, las **restricciones prudentes en PROBLEMATICO** sí merecen estudio, pero con prioridad algo menor y bajo una disciplina especial, porque el régimen sigue siendo heterogéneo y porque una parte no menor del edge del general puede emerger precisamente en ese bloque por la pata short.

La conclusión metodológica central es esta:

> el selector ya parece suficientemente maduro para gobernar **decisiones suaves de exposición y cautela**, pero **todavía no** para justificar rediseños amplios ni estrategias diferenciadas por régimen.

Dicho de otra forma: la siguiente fase razonable no es “inventar sistemas por clase”, sino comprobar si el selector mejora la relación entre rentabilidad y riesgo cuando solo se le concede autoridad sobre **cuánto exponer, cuánto limitar y cuánta cautela aplicar**.

---

## 10. Recomendación: abrir exposición / abrir cautela / abrir topes / esperar todavía

### Recomendación ejecutiva

- **Abrir exposición:** **sí, primero.**  
  Es la línea más coherente con toda la evidencia revisada y la que menos amenaza la lógica base del general.

- **Abrir cautela:** **sí, especialmente en MIXTO.**  
  Es la familia más justificada por la combinación de alta contribución histórica y mayor drawdown segmentado.

- **Abrir topes:** **sí, como línea simple y muy auditable.**  
  Debe tratarse como complemento prudente y benchmark de simplicidad operativa.

- **Esperar todavía:** **sí, para rediseños amplios y restricciones finas por subtipo.**  
  Deben esperar las estrategias distintas por clase, los filtros de señal específicos y cualquier ramificación fuerte dentro de `PROBLEMATICO`.

### Síntesis final de prioridad

1. **Abrir exposición.**
2. **Abrir cautela.**
3. **Abrir topes.**
4. **Esperar todavía** para cambios más agresivos o arquitecturas nuevas.

Ese orden es el más coherente con la evidencia disponible y con la regla central de esta fase: **modular antes que rediseñar**.
