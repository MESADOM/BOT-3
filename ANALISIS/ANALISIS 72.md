# VERSION 2.2.2 ANALISIS 72

## 1. Objetivo

Auditar históricamente la familia de reglas de **tope máximo nominal de entrada condicionado por régimen** para decidir si esta línea de modulación de exposición merece seguir adelante como investigación, **sin alterar la lógica base del sistema general long-short vigente**, **sin diseñar nuevas estrategias por régimen** y **sin tocar producción**.

La pregunta aquí no es cuál es el mejor importe nominal, sino si la familia aporta una mejora históricamente defendible o si, por el contrario, tiende a recortar demasiado el edge ya existente del sistema general.

Para mantener continuidad metodológica, este informe toma como base:

- `ANALISIS 68.md`, donde el tope nominal aparece ya como familia simple y auditable de modulación de exposición.
- `ANALISIS 69.md`, donde se refuerza que debe priorizarse la modulación de exposición antes que abrir variantes completas del sistema.
- `ANALISIS 70.md`, donde se plantea explícitamente la comparación entre ausencia de tope, tope único y tope condicionado por régimen.
- `ANALISIS 71.md`, donde la familia de tope nominal por régimen queda situada como prioridad 1 para la siguiente tanda de auditoría histórica.

Además, el **selector de régimen provisional aceptado** se mantiene exactamente como referencia conceptual ya fijada en la cadena previa:

- **FAVORABLE** si `score >= 2`.
- **MIXTO** si `score = 0 o 1`.
- **PROBLEMATICO** si `score <= -1`.

## 2. Familia de reglas auditada

Se auditan tres familias conceptuales, tal como pedían las instrucciones:

1. **Sin tope nominal**: baseline del sistema general long-short actual, sin límite nominal adicional de entrada.
2. **Tope nominal único para todos los regímenes**: mismo techo para cualquier trade, ignorando la clase del selector.
3. **Tope nominal condicionado por régimen**: el techo depende de la clase `FAVORABLE / MIXTO / PROBLEMATICO`, manteniendo intactas las señales y la lógica base del sistema.

El tope se interpreta como **límite adicional sobre el nominal invertido en la entrada**, aplicado encima del sizing actual del sistema, sin rediseñar entradas, salidas ni módulos long/short.

## 3. Variantes nominales evaluadas

Para evitar tuning fino, se probaron variantes deliberadamente simples.

### 3.1. Baseline

- **Sin tope nominal**.

### 3.2. Topes únicos

- **Tope único 3000 €**.
- **Tope único 5000 €**.
- **Tope único 7000 €**.

### 3.3. Topes condicionados por régimen

Se usaron dos escalones sencillos, solo como referencias de familia:

- **Condicionado 7000/5000/3000**:
  - `FAVORABLE = 7000 €`
  - `MIXTO = 5000 €`
  - `PROBLEMATICO = 3000 €`
- **Condicionado suave sin tope/7000/5000**:
  - `FAVORABLE = sin tope nominal adicional`
  - `MIXTO = 7000 €`
  - `PROBLEMATICO = 5000 €`

Estas dos variantes no pretenden validar una jerarquía final. Solo sirven para ver si la familia gana algo al reservar más libertad a `FAVORABLE` y más cautela a `MIXTO` y `PROBLEMATICO`.

## 4. Resultados históricos comparados

### 4.1. Métricas totales por variante

| Variante | Retorno total | Capital final | Drawdown total | Lectura rápida |
|---|---:|---:|---:|---|
| Sin tope nominal | `+2196,58%` | `22.965,83 €` | `-28,49%` | Baseline más rentable |
| Tope único 3000 € | `+1256,04%` | `13.560,42 €` | `-28,49%` | Recorte severo de retorno |
| Tope único 5000 € | `+1757,19%` | `18.571,94 €` | `-28,49%` | Mejora frente a 3000 €, pero sigue claramente por debajo del baseline |
| Tope único 7000 € | `+2026,75%` | `21.267,52 €` | `-28,49%` | Es la versión menos dañina de los topes únicos |
| Tope por régimen 7000/5000/3000 | `+1626,69%` | `17.266,85 €` | `-28,49%` | Castiga mucho `MIXTO` y `PROBLEMATICO` |
| Tope por régimen sin tope/7000/5000 | `+1965,76%` | `20.657,60 €` | `-28,49%` | Menos destructivo, pero todavía inferior al baseline |

### 4.2. Lectura comparada

La foto agregada es bastante clara:

- **ninguna variante con tope supera históricamente al baseline sin tope**;
- el daño es **muy sensible** a la severidad del tope;
- el drawdown total, medido sobre la curva histórica de capital por operaciones cerradas, **no mejora** en esta auditoría;
- por tanto, el coste principal de la familia aparece como **pérdida de retorno**, no como una reducción históricamente visible del drawdown total.

La primera conclusión provisional es que, bajo esta implementación simple de investigación, la familia no muestra aún una mejora estructural obvia: **recorta más beneficio del que protege**.

## 5. Impacto por régimen

### 5.1. Baseline sin tope: contribución por clase

En el sistema general sin tope adicional, la contribución acumulada por clase del selector es:

- **FAVORABLE:** `3.914,95 €`
- **MIXTO:** `13.519,61 €`
- **PROBLEMATICO:** `4.531,27 €`

La lectura es importante porque condiciona toda la auditoría:

- `MIXTO` no es marginal; es **la principal fuente de beneficio histórico**.
- `PROBLEMATICO` también aporta saldo positivo material; no es un bloque que convenga amputar sin coste.
- `FAVORABLE` suma, pero no concentra todo el edge del sistema general.

### 5.2. Efecto de los topes únicos

#### Tope único 3000 €

Impacto frente al baseline:

- **FAVORABLE:** `-412,69 €`
- **MIXTO:** `-7.261,41 €`
- **PROBLEMATICO:** `-1.731,31 €`

Lectura:

- el daño se concentra abrumadoramente en `MIXTO`;
- `PROBLEMATICO` también pierde bastante;
- el tope de `3000 €` funciona como freno general demasiado agresivo.

#### Tope único 5000 €

Impacto frente al baseline:

- **FAVORABLE:** `+183,70 €`
- **MIXTO:** `-4.091,00 €`
- **PROBLEMATICO:** `-486,59 €`

Lectura:

- sigue dañando de forma fuerte a `MIXTO`;
- el efecto sobre `PROBLEMATICO` ya es mucho menor que con `3000 €`;
- el pequeño cambio positivo en `FAVORABLE` no compensa el deterioro en las otras clases.

#### Tope único 7000 €

Impacto frente al baseline:

- **FAVORABLE:** `+123,33 €`
- **MIXTO:** `-1.821,64 €`
- **PROBLEMATICO:** `0,00 €`

Lectura:

- aquí el daño queda casi totalmente localizado en `MIXTO`;
- `PROBLEMATICO` queda prácticamente intacto;
- es la versión única más razonable de la familia, pero todavía no mejora el sistema general.

### 5.3. Efecto de los topes condicionados por régimen

#### Tope por régimen 7000/5000/3000

Impacto frente al baseline:

- **FAVORABLE:** `+123,33 €`
- **MIXTO:** `-4.091,00 €`
- **PROBLEMATICO:** `-1.731,31 €`

Lectura:

- combinar `7000 €` en `FAVORABLE`, `5000 €` en `MIXTO` y `3000 €` en `PROBLEMATICO` **no preserva bien** los bloques más delicados;
- el supuesto beneficio de reservar libertad a `FAVORABLE` no compensa el recorte simultáneo en `MIXTO` y `PROBLEMATICO`.

#### Tope por régimen sin tope/7000/5000

Impacto frente al baseline:

- **FAVORABLE:** `0,00 €`
- **MIXTO:** `-1.821,64 €`
- **PROBLEMATICO:** `-486,59 €`

Lectura:

- es la variante condicionada menos agresiva;
- preserva completamente `FAVORABLE`;
- reduce poco `PROBLEMATICO` y recorta sobre todo `MIXTO`;
- aun así, **sigue quedando por debajo del baseline**, por lo que no ofrece todavía una señal fuerte de mejora histórica.

### 5.4. Juicio por régimen

La familia “tope nominal por régimen” parece históricamente **más peligrosa para `MIXTO` que útil para protegerlo**.

Eso importa mucho porque los análisis previos ya advertían que:

- `MIXTO` es una zona de cautela, sí;
- pero también es una **gran fuente de beneficio** del general;
- por tanto, si el tope nominal no distingue bien entre expansión excesiva y edge auténtico de transición, termina recortando donde más dinero aporta el sistema.

En `PROBLEMATICO`, el comportamiento también es revelador:

- un recorte demasiado duro sí reduce exposición;
- pero también daña episodios que el general short sí estaba absorbiendo bien;
- por eso la mejora en `PROBLEMATICO` **no aparece como robusta ni limpia**.

## 6. Impacto en 2022 y años favorables

### 6.1. Impacto en 2022

`2022` es el test clave en `PROBLEMATICO`.

Resultado del baseline sin tope:

- **2022 = `4.119,19 €`**.

Impacto incremental frente al baseline:

- **Tope único 3000 €:** `-1.701,19 €`
- **Tope único 5000 €:** `-481,91 €`
- **Tope único 7000 €:** `0,00 €`
- **Tope por régimen 7000/5000/3000:** `-1.989,19 €`
- **Tope por régimen sin tope/7000/5000:** `-597,11 €`

Lectura:

- la familia no mejora `2022`; en general, lo **recorta**;
- el único caso que lo deja intacto es el tope único `7000 €`, precisamente porque no llega a restringir de verdad los trades problemáticos relevantes de ese año;
- cuando el tope sí actúa de forma material en `PROBLEMATICO`, el efecto observado es **deterioro**, no mejora.

Eso encaja con la advertencia heredada de la cadena previa: `2022` era duro, pero el sistema general ya lo absorbía en saldo, aunque de forma concentrada. Aquí el tope nominal no está limpiando esa fragilidad; más bien está amputando parte del beneficio histórico capturado allí.

### 6.2. Preservación de años favorables

Tomando como años favorablemente representativos del sistema general `2017`, `2020`, `2021` y `2024`, la preservación es desigual:

- **2017 y 2018** quedan prácticamente intactos en todas las variantes auditadas.
- **2020** también cambia poco o nada.
- **2021** ya sufre con el tope único `3000 €` y, mucho menos, con `5000 €`.
- **2024** es donde los topes empiezan a mostrar un coste más claro.

Impacto en `2024` frente al baseline:

- **Tope único 3000 €:** `-2.007,51 €`
- **Tope único 5000 €:** `-677,85 €`
- **Tope único 7000 €:** `-96,08 €`
- **Tope por régimen 7000/5000/3000:** `-677,85 €`
- **Tope por régimen sin tope/7000/5000:** `-96,08 €`

Lectura:

- la preservación de años buenos **depende mucho del nominal elegido**;
- `3000 €` deteriora claramente un año favorable como `2024`;
- `7000 €` casi lo preserva, pero no aporta mejora compensatoria en otras zonas.

### 6.3. Impacto en 2024–2025

Este bloque es especialmente importante porque combina continuidad favorable con una parte significativa del beneficio reciente del sistema.

Impacto acumulado frente al baseline:

- **Tope único 3000 €:**
  - `2024: -2.007,51 €`
  - `2025: -5.254,73 €`
- **Tope único 5000 €:**
  - `2024: -677,85 €`
  - `2025: -3.705,65 €`
- **Tope único 7000 €:**
  - `2024: -96,08 €`
  - `2025: -2.030,06 €`
- **Tope por régimen 7000/5000/3000:**
  - `2024: -677,85 €`
  - `2025: -3.616,88 €`
- **Tope por régimen sin tope/7000/5000:**
  - `2024: -96,08 €`
  - `2025: -2.128,79 €`

Lectura:

- la familia **sufre claramente en 2024–2025**;
- el principal daño está en `2025`, no en `2024`;
- y ese daño proviene sobre todo de trades `MIXTO` de gran contribución histórica, no de una limpieza homogénea de muchos episodios pequeños.

## 7. Sensibilidad al valor nominal

La sensibilidad al nominal es alta y queda muy limpia en la comparación de topes únicos:

- **3000 €**: retorno total `+1256,04%`
- **5000 €**: retorno total `+1757,19%`
- **7000 €**: retorno total `+2026,75%`
- **Sin tope**: retorno total `+2196,58%`

La progresión muestra dos cosas a la vez:

1. **cuanto más duro es el tope, más retorno se destruye**;
2. el paso de `3000 €` a `5000 €` y luego a `7000 €` no revela una “zona mágica”, sino más bien un patrón simple: **menos rigidez, menos daño**.

En otras palabras, la auditoría no sugiere un valor nominal óptimo. Lo que sugiere es algo más sobrio:

- `3000 €` parece demasiado agresivo para esta base histórica;
- `5000 €` sigue siendo claramente costoso;
- `7000 €` es menos lesivo, pero ya se acerca a una situación donde el tope aporta poco y, precisamente por eso, tampoco mejora gran cosa.

La versión condicionada repite la misma historia:

- cuando el régimen condiciona con dureza real, el daño aparece;
- cuando se suaviza mucho para no dañar, la familia deja de mostrar una protección histórica visible.

## 8. Dependencia de episodios concretos

Aquí la evidencia es especialmente importante.

### 8.1. Concentración del efecto

El deterioro no se reparte de manera homogénea entre muchos trades pequeños. Al contrario, depende en buena medida de **pocos episodios muy concretos**.

#### Tope único 3000 €

- `31` trades afectados.
- Los **3 trades** con mayor impacto explican aproximadamente el `47,8%` del cambio absoluto.
- Los **5 trades** con mayor impacto explican aproximadamente el `63,7%` del cambio absoluto.

#### Tope único 5000 €

- `18` trades afectados.
- Los **3 trades** con mayor impacto explican aproximadamente el `61,0%` del cambio absoluto.
- Los **5 trades** con mayor impacto explican aproximadamente el `76,6%` del cambio absoluto.

#### Tope único 7000 €

- `8` trades afectados.
- Los **3 trades** con mayor impacto explican aproximadamente el `72,4%` del cambio absoluto.
- Los **5 trades** con mayor impacto explican aproximadamente el `86,4%` del cambio absoluto.

#### Tope por régimen 7000/5000/3000

- `16` trades afectados.
- Los **3 trades** con mayor impacto explican aproximadamente el `57,5%` del cambio absoluto.
- Los **5 trades** con mayor impacto explican aproximadamente el `73,2%` del cambio absoluto.

#### Tope por régimen sin tope/7000/5000

- `10` trades afectados.
- Los **3 trades** con mayor impacto explican aproximadamente el `64,7%` del cambio absoluto.
- Los **5 trades** con mayor impacto explican aproximadamente el `84,2%` del cambio absoluto.

### 8.2. Episodios dominantes

Los episodios que más pesan en el deterioro son recurrentes entre variantes:

1. **Trade MIXTO `2025-05-14 -> 2025-11-11`**.
2. **Trade MIXTO `2024-09-16 -> 2025-01-06`**.
3. **Trade MIXTO `2023-11-08 -> 2024-04-08`** en variantes más duras.
4. **Trade MIXTO `2024-05-08 -> 2024-07-22`**.
5. **Trade PROBLEMATICO `2022-04-13 -> 2022-05-17`** cuando el régimen problemático sí queda capado de forma relevante.

Esto obliga a una lectura prudente:

- **sí**, el efecto de la familia depende bastante de pocos trades o pocos periodos;
- **no** parece una mejora distribuida y robusta a lo largo del histórico;
- el principal “beneficio” de la familia no surge de limpiar muchos errores pequeños, sino de recortar grandes episodios… pero históricamente esos episodios, en la mayoría de variantes probadas, eran **más valiosos que dañinos** para el sistema general.

## 9. Conclusión final

La auditoría histórica de la familia **tope máximo nominal por régimen** no ofrece, por ahora, una evidencia convincente para priorizarla como siguiente gran línea de trabajo.

La síntesis es la siguiente:

- el baseline **sin tope nominal** sigue siendo el mejor resultado agregado;
- los topes más duros (`3000 €`, y en menor medida `5000 €`) destruyen demasiado retorno;
- los topes más suaves (`7000 €` o la versión condicionada sin tope/7000/5000) preservan mejor los años buenos, pero **no muestran una mejora clara** ni en drawdown total ni en el tratamiento de `2022`;
- la mayor parte del deterioro se concentra en **pocos trades grandes**, sobre todo en `MIXTO` y especialmente en `2024–2025`.

Por tanto, la familia sí aporta una enseñanza útil, pero no la que haría falta para abrir ya una lógica operativa más ambiciosa:

- **la exposición nominal es un eje sensible**;
- pero un tope nominal simple parece, en esta base histórica, **más capaz de amputar edge que de protegerlo de forma limpia**.

## 10. Recomendación: familia prometedora / útil con reservas / no priorizar

**Recomendación: no priorizar.**

Matiz importante:

- no significa que la idea quede prohibida para siempre;
- sí significa que, con esta auditoría histórica simple, **no merece convertirse ahora en el eje principal de investigación**;
- y también significa que **no hay base para declarar óptimo ningún nominal** ni para abrir todavía una lógica más compleja de topes.

Si en el futuro se reabre esta línea, debería hacerse solo con una pregunta muy concreta y acotada: si existe alguna forma de limitar expansión en episodios extremos **sin tocar apenas `MIXTO` productivo ni `PROBLEMATICO` absorbible**. Pero esa hipótesis, a la luz de esta auditoría, todavía **no ha quedado demostrada**.
