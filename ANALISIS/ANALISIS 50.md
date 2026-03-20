# VERSION 2.2.2 ANALISIS 50

## 1. Objetivo

Determinar qué horizonte temporal describe mejor el **contexto de mercado** para un futuro selector de régimen, comparando ventanas de **1 mes, 2 meses, 3 meses y 6 meses**, sin diseñar todavía el selector operativo final, sin fijar reglas finales de activación y sin tocar producción.

El foco de este análisis no es optimizar un umbral fino, sino estudiar qué escala temporal ofrece mejor equilibrio entre:
- estabilidad;
- sensibilidad al ruido;
- capacidad descriptiva frente a años favorables y problemáticos del sistema general long-short;
- velocidad de reacción ante cambios de entorno;
- interpretabilidad.

La pregunta práctica es simple: **qué ventana sirve mejor como “lenguaje base” para describir el mercado de forma robusta e interpretable**.

---

## 2. Ventanas temporales evaluadas

Se evaluaron cuatro horizontes sobre el mercado principal del sistema (**QQQ**):

- **1 mes** ≈ 21 sesiones.
- **2 meses** ≈ 42 sesiones.
- **3 meses** ≈ 63 sesiones.
- **6 meses** ≈ 126 sesiones.

Estas cuatro ventanas se eligieron porque cubren cuatro escalas naturales de lectura del contexto:
- **1m**: táctica / muy rápida.
- **2m**: táctica-media.
- **3m**: principal / cíclica intermedia.
- **6m**: estructural.

---

## 3. Metodología de comparación

### Datos usados

Se trabajó con:
- el histórico del sistema **VERSION 2.2.2** ya disponible en el repositorio;
- el activo principal de referencia del régimen, **QQQ**.

### Qué se midió

Para cada ventana se calculó el retorno rodante del QQQ en ese horizonte y se estudió su comportamiento como descriptor de contexto.

No se optimizaron umbrales finos. Para mantener el análisis interpretable, se utilizó una lectura básica:
- retorno rodante **positivo** → contexto favorable;
- retorno rodante **negativo** → contexto problemático.

Con esa lectura mínima se compararon estas métricas:

1. **Estabilidad de clasificación por ventana**
   - porcentaje de veces en que el estado seguía igual una semana después.

2. **Frecuencia de cambios de estado por ventana**
   - número de cambios positivo/negativo por año.

3. **Nivel de ruido aparente por ventana**
   - porcentaje de cambios de estado que se revertían en los siguientes 10 días.

4. **Capacidad descriptiva frente a años favorables y problemáticos**
   - cuánto tiempo pasaba cada ventana en positivo en años buenos del sistema;
   - cuánto tiempo pasaba en negativo en años malos del sistema.

5. **Latencia aproximada de detección de cambios**
   - retraso para captar giros relevantes:
     - tramo de giro bajista 2021-2022;
     - rebote desde suelo de 2022;
     - corrección de 2025;
     - 2026 solo como referencia secundaria.

6. **Interpretabilidad cualitativa**
   - facilidad para explicar qué “está viendo” realmente cada horizonte.

### Años y tramos de referencia usados

Para la lectura del sistema general long-short, el histórico del bot sugiere esta segmentación descriptiva:

- **Años favorables claros**: 2017, 2018, 2019, 2020, 2021, 2024 y 2025.
- **Año especial**: **2022**, porque combina una parte muy problemática para el sesgo long y muy favorable para la pata short, por lo que no debe tratarse como un año “normal”.
- **Año transicional**: 2023.
- **Años problemáticos**: 2015, 2016.
- **2026**: referencia secundaria, útil para comprobar latencia reciente, pero **no** base de diseño.

---

## 4. Ventaja y desventaja de cada ventana

### 1 mes

**Ventajas**
- Reacciona muy rápido a giros recientes.
- Detecta pronto cambios de tono tras shocks o rebotes.
- Es útil para lectura táctica de corto plazo.

**Desventajas**
- Cambia demasiado de signo.
- Tiene mucha sensibilidad al serrucho y al rebote técnico.
- Tiende a confundir correcciones dentro de un fondo sano con deterioros reales del entorno.

**Lectura resumida**
- Bueno como radar táctico.
- Débil como descriptor principal del régimen.

### 2 meses

**Ventajas**
- Mantiene una reacción todavía razonablemente rápida.
- Filtra mejor el ruido que 1m.
- Empieza a describir mejor tramos favorables y tramos problemáticos sin volverse demasiado lento.

**Desventajas**
- Sigue siendo algo sensible a vaivenes de mercado en zonas de transición.
- En años mixtos o de rotación rápida puede seguir alternando más de lo deseable.

**Lectura resumida**
- Buen equilibrio táctico-principal.
- Candidato serio si se quisiera una sola ventana relativamente ágil.

### 3 meses

**Ventajas**
- Equilibra bastante bien estabilidad y capacidad descriptiva.
- Distingue mejor que 1m y 2m los grandes tramos realmente problemáticos.
- Mantiene una interpretabilidad muy clara: “qué ha hecho el mercado en el último trimestre”.

**Desventajas**
- Llega más tarde que 1m y 2m a algunos giros.
- En cambios violentos puede tardar unas semanas extra en reconocer el nuevo entorno.

**Lectura resumida**
- Es la ventana más equilibrada como lenguaje central del contexto.
- Muy sólida como horizonte principal si se prioriza robustez sobre reflejo inmediato.

### 6 meses

**Ventajas**
- Es la más estable de todas.
- Tiene muy poca rotación de estado.
- Representa bien el sesgo estructural de fondo.

**Desventajas**
- Reacciona tarde.
- Puede seguir calificando positivamente un mercado que ya se ha deteriorado en la práctica operativa.
- Tiende a “aplanar” episodios intermedios importantes.
- Puede llegar demasiado tarde para separar corrección profunda de régimen aún favorable.

**Lectura resumida**
- Muy útil como capa estructural.
- Demasiado lenta para ser la única lente del selector.

---

## 5. Ruido y estabilidad por horizonte

### Resumen cuantitativo

| Ventana | Estabilidad semanal de clasificación | Cambios de estado totales | Cambios por año | Reversiones rápidas (≤10 días) | Lectura de ruido |
|---|---:|---:|---:|---:|---|
| 1m | 81,0% | 371 | 21,73 | 67,9% | Muy ruidosa |
| 2m | 86,9% | 249 | 14,65 | 67,5% | Ruidosa pero ya filtrada |
| 3m | 90,4% | 178 | 10,52 | 66,9% | Bastante estable |
| 6m | 94,5% | 102 | 6,12 | 66,7% | Muy estable |

### Lectura comparativa

#### 1m
- Es la que más cambia de estado con diferencia.
- Supera los **21 cambios por año**, lo que para un descriptor de contexto es demasiado alto.
- Su estabilidad semanal es la peor del grupo.
- Aunque detecta muy rápido, una parte demasiado grande de lo que detecta es ruido o microcambio.

#### 2m
- Mejora claramente frente a 1m.
- Baja de **21,73** a **14,65** cambios por año.
- La estabilidad sube casi 6 puntos.
- Sigue siendo una ventana viva, pero ya empieza a comportarse como lectura útil del entorno en vez de simple pulso táctico.

#### 3m
- Da un nuevo salto de calidad en estabilidad.
- Reduce los cambios a **10,52** por año.
- Mantiene una lectura todavía suficientemente cercana al mercado real.
- Es el primer horizonte que parece claramente “descriptor de régimen” y no solo “detector de impulso reciente”.

#### 6m
- Es la más estable y la menos ruidosa en cambios.
- Pero esa estabilidad se compra con mucha lentitud.
- Sirve mejor para confirmar fondo estructural que para gobernar por sí sola un selector operativo.

### Conclusión de esta sección

En términos de equilibrio ruido-estabilidad:
- **1m** = exceso de ruido.
- **2m** = razonable si se quiere agilidad.
- **3m** = mejor compromiso global.
- **6m** = excelente estabilidad, pero con demasiada inercia para ser única referencia.

---

## 6. Encaje con años y tramos conocidos

### 6.1 Capacidad descriptiva frente a años favorables y problemáticos

Agrupando de forma cualitativa los años del sistema:
- en **años favorables claros**, interesa que la ventana pase buena parte del tiempo en estado positivo;
- en **años problemáticos**, interesa que la ventana pase una parte relevante del tiempo en negativo;
- en **2022**, interesa que reconozca un entorno excepcionalmente hostil para la pata long y claramente distinto de un año alcista normal.

| Ventana | % tiempo positivo en años favorables claros | % tiempo negativo en años problemáticos | Lectura descriptiva |
|---|---:|---:|---|
| 1m | 68,8% | 45,3% | Capta tono, pero mezcla demasiado ruido |
| 2m | 73,9% | 41,1% | Mejor descripción, aún algo inestable |
| 3m | 76,4% | 30,5% | Muy buena separación de años buenos; menos dura en años grises |
| 6m | 81,5% | 17,2% | Excelente para años buenos, floja para detectar deterioro pronto |

### 6.2 Años favorables al general long-short

#### 2017, 2020, 2021, 2024 y 2025
- **1m** y **2m** los reconocen, pero con interrupciones relativamente frecuentes.
- **3m** ofrece una lectura más limpia de continuidad favorable.
- **6m** los reconoce casi siempre como positivos, pero a costa de ser demasiado indulgente cuando aparecen correcciones intermedias.

Interpretación:
- en años fuertemente alcistas o muy persistentes, **6m** y **3m** describen bien el fondo;
- la diferencia es que **3m** conserva más sensibilidad para no quedar completamente ciego ante deterioros intermedios.

#### 2018 y 2019
- Son años menos lineales que 2020-2021.
- **1m** tiende a serruchar demasiado la lectura.
- **2m** mejora, pero todavía alterna con cierta facilidad.
- **3m** empieza a separar mejor lo principal de lo accesorio.
- **6m** suaviza tanto que corre el riesgo de explicar demasiado tarde la pérdida de tono de algunos tramos.

### 6.3 Años problemáticos

#### 2015 y 2016
Aquí aparece una diferencia importante.

- **1m** y **2m** siguen mostrando demasiados tramos positivos para lo incómodo que fue realmente el contexto del sistema.
- **3m** sigue sin “hundirse” del todo, pero ya refleja mejor el carácter poco limpio del periodo.
- **6m** resulta demasiado complaciente: llega a seguir mayoritariamente en positivo en partes de 2015 y buena parte de 2016, lo que la hace peligrosa como única referencia de contexto.

Interpretación:
- si el objetivo es distinguir de forma robusta entre entorno favorable y entorno problemático, **6m sola no es suficiente**;
- **1m sola tampoco**, porque reacciona pero sobreinterpreta demasiado el ruido;
- el centro útil está entre **2m y 3m**, con ventaja para **3m** por claridad estructural.

### 6.4 2022 como caso especial

2022 es la prueba clave de este análisis.

| Ventana | % tiempo positivo en 2022 | % tiempo negativo en 2022 | Retorno medio rodante en 2022 |
|---|---:|---:|---:|
| 1m | 34,7% | 65,3% | -2,61% |
| 2m | 29,1% | 70,9% | -5,28% |
| 3m | 14,7% | 85,3% | -7,72% |
| 6m | 9,6% | 90,4% | -12,00% |

Lectura:
- **1m** reconoce el problema, pero deja demasiado espacio a rebotes tácticos que pueden ocultar la hostilidad de fondo.
- **2m** ya describe bastante mejor el carácter negativo del año.
- **3m** separa con mucha claridad que 2022 no fue un simple bache, sino un entorno persistentemente adverso.
- **6m** lo describe todavía con más contundencia, pero su lentitud hace que esa claridad llegue tarde en transiciones.

Conclusión sobre 2022:
- para detectar un año excepcionalmente duro sin caer en serrucho, **3m** parece el mejor compromiso;
- **6m** confirma muy bien el deterioro, pero como capa de fondo, no como única señal viva.

### 6.5 2026 como referencia secundaria

En el tramo disponible de **2026**:
- **1m** ya entra en lectura problemática con cierta claridad.
- **2m** queda casi neutral, señal de transición todavía abierta.
- **3m** ya empieza a suavizar demasiado la debilidad.
- **6m** sigue viéndose claramente positiva, lo que confirma que es demasiado lenta para usarla sola.

Esto no debe usarse como base de diseño, pero sí como advertencia metodológica:
- **si la ventana es demasiado larga, tarda tanto en girar que puede llegar tarde a un deterioro reciente relevante**.

---

## 7. Comparación entre ventana única y enfoque multicapa

## Opción A: una sola ventana

### Si fuera 1m
No parece recomendable como ventana única.
- Tiene demasiada sensibilidad al ruido.
- Su clasificación cambia demasiado.
- Puede convertir el selector de contexto en una lectura casi táctica, no de régimen.

### Si fuera 2m
Sería defendible como solución simple y relativamente ágil.
- Mejor que 1m en casi todo.
- Pero todavía puede sobre-reaccionar en fases de transición o serrucho.

### Si fuera 3m
Es la mejor candidata a **ventana única**.
- Tiene el mejor equilibrio entre estabilidad, legibilidad y separación de grandes entornos.
- Reconoce 2022 con claridad.
- No se vuelve tan lenta como 6m.

### Si fuera 6m
No parece suficiente como ventana única.
- Sirve para sesgo de fondo.
- Pero llega tarde y puede mantener demasiado tiempo un diagnóstico desactualizado.

## Opción B: arquitectura multicapa

La evidencia de este análisis sí sugiere que una **arquitectura por capas** tiene más sentido conceptual que una sola ventana aislada.

### Capa táctica
- **1m** o **2m**.
- Función: captar aceleraciones, deterioros rápidos y rebotes recientes.
- No debería dominar por sí sola el diagnóstico global.

### Capa principal
- **3m**.
- Función: actuar como descripción central del contexto.
- Es la ventana más equilibrada y la que mejor combina robustez e interpretabilidad.

### Capa estructural
- **6m**.
- Función: confirmar si el fondo de mercado sigue siendo favorable o adverso.
- Muy útil para evitar sobrerreaccionar a microciclos.

### Lectura global del enfoque multicapa

La arquitectura más coherente a nivel analítico sería:
- **táctica** = 1m o 2m;
- **principal** = 3m;
- **estructural** = 6m.

Importante: esto **no** equivale a proponer reglas finales de activación. Solo significa que, a nivel descriptivo, estas escalas parecen complementarse mejor que una única ventana rígida.

---

## 8. Conclusión final

El análisis del histórico del sistema y del mercado principal sugiere lo siguiente:

1. **1 mes** es demasiado ruidoso para ser el lenguaje central del contexto.
   - Reacciona rápido, pero cambia demasiado y sobreinterpreta rebotes y microcorrecciones.

2. **2 meses** es una mejora clara frente a 1m.
   - Puede ser útil si se desea una lectura relativamente viva.
   - Aun así, no parece tan robusta ni tan limpia como 3m para describir régimen.

3. **3 meses** es el horizonte más equilibrado.
   - Tiene suficiente estabilidad para describir contexto.
   - Sigue siendo interpretable.
   - Distingue bien 2022 del resto.
   - No incurre en la lentitud excesiva de 6m.

4. **6 meses** es muy valioso como lente estructural, pero no como única referencia.
   - Su mayor problema no es el ruido, sino la latencia.
   - Puede mantener demasiado tiempo una lectura positiva cuando el entorno ya se ha deteriorado operativamente.

5. A nivel conceptual, **la evidencia favorece más un enfoque multicapa que una única ventana extrema**.
   - El mercado parece tener una dimensión táctica, una principal y una estructural.
   - Forzar todo el contexto en una sola escala pierde información o introduce demasiado ruido, según la ventana elegida.

En resumen:
- si hubiera que elegir **una sola ventana**, la mejor candidata por robustez e interpretabilidad sería **3 meses**;
- si se prioriza una representación más fiel del mercado real, **un enfoque multicapa tiene más sentido analítico** que una ventana única.

---

## 9. Recomendación: priorizar 1m / 2m / 3m / 6m / enfoque multicapa

### Prioridad recomendada

1. **Enfoque multicapa**.
2. **3m** como horizonte principal si se fuerza una sola ventana.
3. **2m** como alternativa más ágil, pero menos robusta.
4. **6m** como capa estructural, no como ventana única.
5. **1m** solo como capa táctica, no como descriptor central.

### Recomendación final de este análisis

La priorización más sensata, sin declarar todavía un selector final, es:

**enfoque multicapa > 3m > 2m > 6m > 1m**

Traducción práctica de esa recomendación analítica:
- **1m** aporta velocidad, pero demasiado ruido.
- **2m** ya es útil, aunque todavía algo nervioso.
- **3m** es la mejor escala central para describir contexto de forma estable e interpretable.
- **6m** es muy buena referencia estructural, pero demasiado lenta para ir sola.
- **multicapa** encaja mejor con la realidad del mercado porque separa táctica, contexto principal y estructura de fondo.

Este análisis **no** propone todavía reglas finales, **no** define activadores operativos y **no** abre una nueva estrategia. Solo deja fijado qué horizontes temporales parecen más sólidos para construir, en una fase posterior, un selector de contexto robusto e interpretable.
