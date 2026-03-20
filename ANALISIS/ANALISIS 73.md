# VERSION 2.2.2 ANALISIS 73

## 1. Objetivo

Auditar históricamente la familia de reglas de **reducción porcentual de exposición condicionada por régimen**, trabajando sobre el **sistema general long-short vigente** y sobre el **selector provisional actualmente aceptado como base**, para decidir si esta línea merece más prioridad que la familia de **tope nominal** estudiada en `ANALISIS 72` o si introduce demasiada sensibilidad adicional para la mejora que realmente aporta.

El alcance se ha mantenido estrictamente dentro de lo pedido:

- **no** se diseñan estrategias nuevas por régimen;
- **no** se toca producción;
- **no** se modifica la lógica base del sistema general;
- **no** se declara óptimo ningún porcentaje;
- **sí** se audita la familia en tres planos mínimos:
  - sin reducción porcentual;
  - reducción porcentual uniforme simple;
  - reducción porcentual condicionada por régimen.

La lectura obligatoria previa ha sido:

- `ANALISIS 68.md`
- `ANALISIS 69.md`
- `ANALISIS 70.md`
- `ANALISIS 71.md`

Para mantener continuidad con la taxonomía ya fijada en la secuencia reciente, el selector se ha traducido a clases así:

- **FAVORABLE** si `score_regimen >= 2`;
- **MIXTO** si `score_regimen = 0 o 1`;
- **PROBLEMATICO** si `score_regimen <= -1`.

La auditoría histórica se ha hecho como replay del motor actual introduciendo **solo** un multiplicador reductor sobre el **porcentaje objetivo de capital** de cada entrada, sin alterar señales, salidas, selector ni arquitectura general long-short.

---

## 2. Familia de reglas auditada

La familia auditada no introduce un tope duro en euros, sino una **reducción porcentual de exposición** aplicada sobre el sizing base que ya decide el sistema.

Conceptualmente, la familia se ha auditado en tres capas:

1. **Sin reducción porcentual**
   - baseline histórico actual.

2. **Reducción porcentual uniforme simple**
   - el mismo recorte se aplica en `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

3. **Reducción porcentual condicionada por régimen**
   - se preserva más exposición en `FAVORABLE`;
   - se introduce prudencia parcial en `MIXTO`;
   - se aprieta más en `PROBLEMATICO`.

La diferencia frente a la familia nominal es importante:

- el **tope nominal** recorta por una barrera absoluta en euros;
- la **reducción porcentual** recorta de forma proporcional al capital y al sizing base vigente.

En teoría, eso hace a la familia porcentual **más flexible** y más coherente con el crecimiento compuesto. Pero esa misma continuidad también puede volverla **más sensible al tuning del porcentaje elegido**.

---

## 3. Variantes porcentuales evaluadas

Se han usado referencias explícitas, simples y prudentes, tal como se pedía:

- **10%**
- **20%**
- **30%**

### 3.1. Variantes comparadas

| Variante | Regla |
|---|---|
| Sin reducción | Sin multiplicador reductor adicional |
| Uniforme 10% | Reducir `10%` la exposición en todos los regímenes |
| Uniforme 20% | Reducir `20%` la exposición en todos los regímenes |
| Uniforme 30% | Reducir `30%` la exposición en todos los regímenes |
| Condicionada suave | `FAVORABLE 0%`, `MIXTO 10%`, `PROBLEMATICO 20%` |
| Condicionada prudente | `FAVORABLE 0%`, `MIXTO 20%`, `PROBLEMATICO 30%` |

### 3.2. Criterio metodológico de las variantes condicionadas

Se han elegido dos perfiles condicionados deliberadamente simples:

- uno **suave**, para comprobar si basta una cautela ligera fuera de `FAVORABLE`;
- uno **prudente**, para forzar una lectura más defensiva sin llegar todavía a una lógica escalonada compleja.

No se han abierto más combinaciones porque aquí la prioridad sigue siendo auditar **la familia** y su robustez básica, no optimizar una superficie amplia de parámetros.

---

## 4. Resultados históricos comparados

### 4.1. Retorno total y drawdown total por variante

| Variante | Beneficio neto total | Retorno total | Drawdown total |
|---|---:|---:|---:|
| Sin reducción | `21.965,83 €` | `+2196,58%` | `-28,49%` |
| Uniforme 10% | `20.467,73 €` | `+2046,77%` | `-28,04%` |
| Uniforme 20% | `18.776,82 €` | `+1877,68%` | `-27,45%` |
| Uniforme 30% | `14.685,62 €` | `+1468,56%` | `-26,56%` |
| Condicionada suave | `20.952,03 €` | `+2095,20%` | `-28,14%` |
| Condicionada prudente | `20.060,56 €` | `+2006,06%` | `-27,77%` |

### 4.2. Lectura principal del bloque total

La señal histórica principal es bastante distinta de la vista en la familia nominal:

- aquí **sí aparece** una mejora gradual del drawdown total cuando la reducción aumenta;
- pero esa mejora es **modesta**, no transformacional;
- a la vez, el retorno total cae de forma bastante visible conforme el recorte se hace más severo.

Dicho de forma práctica:

- la familia porcentual **protege algo más** que el tope nominal;
- pero lo hace al precio de introducir una sensibilidad más fina al porcentaje escogido;
- y su mejora histórica sigue siendo una mejora de **segundo orden**, no una reconfiguración contundente del perfil del sistema.

### 4.3. Orden comparado observado

En retorno total, el orden queda así:

1. **Sin reducción**
2. **Condicionada suave**
3. **Uniforme 10%**
4. **Condicionada prudente**
5. **Uniforme 20%**
6. **Uniforme 30%**

En drawdown total, el orden se invierte parcialmente:

1. **Uniforme 30%**
2. **Uniforme 20%**
3. **Condicionada prudente**
4. **Condicionada suave**
5. **Uniforme 10%**
6. **Sin reducción**

La lectura conjunta no deja un ganador claro, pero sí una pauta: la familia porcentual funciona como un **trade-off continuo** entre captura de retorno y moderación del drawdown, no como una mejora limpia y robusta en ambas dimensiones a la vez.

---

## 5. Impacto por régimen

### 5.1. Beneficio total por clase en el baseline

Baseline sin reducción:

- **FAVORABLE:** `3.914,95 €`
- **MIXTO:** `13.519,61 €`
- **PROBLEMATICO:** `4.531,27 €`

Esto vuelve a confirmar la lectura heredada de `ANALISIS 64–72`:

- `MIXTO` sigue siendo el gran motor agregado del sistema;
- `PROBLEMATICO` aporta valor real, pero con menor peso;
- `FAVORABLE` es sano, aunque no monopoliza el edge.

### 5.2. Efecto comparado por clase del selector

| Variante | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|
| Sin reducción | `3.914,95 €` | `13.519,61 €` | `4.531,27 €` |
| Uniforme 10% | `3.461,78 €` | `13.197,91 €` | `3.808,04 €` |
| Uniforme 20% | `2.950,30 €` | `12.733,41 €` | `3.093,11 €` |
| Uniforme 30% | `2.537,85 €` | `9.988,27 €` | `2.159,50 €` |
| Condicionada suave | `3.878,69 €` | `13.343,77 €` | `3.729,57 €` |
| Condicionada prudente | `3.773,85 €` | `13.018,02 €` | `3.268,69 €` |

### 5.3. Lectura por clase

#### FAVORABLE

- Las variantes condicionadas preservan bastante bien `FAVORABLE`.
- El deterioro serio en esta clase aparece sobre todo en los uniformes `20%` y `30%`.
- Esto favorece, conceptualmente, la versión condicionada frente a la uniforme cuando se quiere no dañar los tramos más sanos.

#### MIXTO

- `MIXTO` sigue siendo el gran punto sensible de la familia.
- Caídas frente al baseline:
  - `-321,70 €` con uniforme `10%`;
  - `-786,20 €` con uniforme `20%`;
  - `-3.531,34 €` con uniforme `30%`;
  - `-175,84 €` con condicionada suave;
  - `-501,59 €` con condicionada prudente.

**Conclusión sobre MIXTO:** la familia porcentual castiga menos a `MIXTO` que la nominal cuando el recorte es moderado, pero si se sube el porcentaje hasta `30%` el daño vuelve a ser claramente grande. La mayor ventaja histórica de la versión condicionada es precisamente que deja a `MIXTO` bastante más intacto que los uniformes medios-altos.

#### PROBLEMATICO

- Aquí la reducción porcentual sí actúa como freno visible.
- Caídas frente al baseline:
  - `-723,23 €` con uniforme `10%`;
  - `-1.438,16 €` con uniforme `20%`;
  - `-2.371,77 €` con uniforme `30%`;
  - `-801,70 €` con condicionada suave;
  - `-1.262,58 €` con condicionada prudente.

**Conclusión sobre PROBLEMATICO:** la familia porcentual sí contiene la exposición en el bloque hostil, pero la mejora que compra no es gratuita: recorta también parte del beneficio que el sistema todavía extrae ahí, especialmente en episodios buenos de `2022`.

---

## 6. Impacto en 2022 y años favorables

### 6.1. Impacto en 2022

| Variante | Resultado 2022 |
|---|---:|
| Sin reducción | `4.119,19 €` |
| Uniforme 10% | `3.587,24 €` |
| Uniforme 20% | `3.030,17 €` |
| Uniforme 30% | `2.235,22 €` |
| Condicionada suave | `3.407,79 €` |
| Condicionada prudente | `3.032,95 €` |

Lectura de `2022`:

- todas las variantes con reducción recortan parte del año;
- el recorte es **progresivo** y coherente con el porcentaje aplicado;
- la versión condicionada suave conserva mejor `2022` que la prudente y que los uniformes altos;
- la mejora en drawdown total no compensa claramente el deterioro de `2022` cuando el recorte se vuelve severo.

Esto es relevante porque `2022` era una de las zonas donde más tentadora parecía la idea de “ser más prudente en PROBLEMATICO”. Históricamente, la familia porcentual sí suaviza exposición, pero también **poda parte de la captura útil** de ese año.

### 6.2. Preservación de años favorables

Para medir preservación de años favorables se ha mirado sobre todo el bloque fuerte reciente del baseline: **2020, 2021, 2024 y 2025**.

Suma baseline en esos años: **`16.545,82 €`**.

Retención aproximada del bloque favorable:

- **Uniforme 10%:** `15.718,78 €` → conserva ~`95,0%`
- **Uniforme 20%:** `14.729,26 €` → conserva ~`89,0%`
- **Uniforme 30%:** `11.419,25 €` → conserva ~`69,0%`
- **Condicionada suave:** `16.275,70 €` → conserva ~`98,4%`
- **Condicionada prudente:** `15.759,24 €` → conserva ~`95,2%`

La lectura es mejor que la de la familia nominal:

- la **condicionada suave** preserva muy bien los años fuertes;
- la **condicionada prudente** y el **uniforme 10%** siguen siendo razonablemente respetuosos con el bloque favorable;
- el **uniforme 30%** ya deteriora demasiado la parte buena del sistema.

### 6.3. Impacto en 2024–2025

| Variante | 2024 | 2025 | 2024–2025 combinado |
|---|---:|---:|---:|
| Sin reducción | `3.996,00 €` | `7.637,00 €` | `11.633,00 €` |
| Uniforme 10% | `3.996,00 €` | `7.637,00 €` | `11.633,00 €` |
| Uniforme 20% | `3.996,00 €` | `7.626,66 €` | `11.622,66 €` |
| Uniforme 30% | `3.187,09 €` | `5.919,20 €` | `9.106,29 €` |
| Condicionada suave | `3.996,00 €` | `7.637,00 €` | `11.633,00 €` |
| Condicionada prudente | `3.996,00 €` | `7.637,00 €` | `11.633,00 €` |

Aquí aparece una diferencia muy importante frente al tope nominal:

- las variantes porcentuales **suaves o intermedias casi no dañan `2024–2025`**;
- el gran deterioro reciente aparece sobre todo en el uniforme `30%`;
- por tanto, la familia porcentual preserva bastante mejor los grandes ganadores recientes que la nominal.

Esto le da una ventaja real como línea de investigación frente al tope duro en euros.

---

## 7. Sensibilidad al porcentaje elegido

La familia porcentual es **más flexible** que la nominal, pero también **más sensible** al porcentaje concreto elegido.

### 7.1. Sensibilidad en la versión uniforme

- pasar de **`10%` a `20%`** reduce retorno total en `1.690,91 €`, pero mejora drawdown solo de `-28,04%` a `-27,45%`;
- pasar de **`20%` a `30%`** vuelve a recortar mucho retorno (`-4.091,20 €`) y mejora drawdown de forma limitada hasta `-26,56%`;
- esa pendiente muestra que el coste marginal del recorte crece antes que la mejora marginal del drawdown.

La versión uniforme, por tanto, parece **bastante frágil** si el porcentaje sube demasiado: a partir de cierto punto el sistema deja de estar “ligeramente modulando” y empieza a amputar de forma visible el edge agregado.

### 7.2. Sensibilidad en la versión condicionada

- la **condicionada suave** conserva mucho retorno y apenas mejora algo el drawdown;
- la **condicionada prudente** mejora un poco más el drawdown, pero ya pierde casi `900 €` extra frente a la suave;
- el salto entre ambas muestra que la familia condicionada tiene una zona útil, pero no una zona donde “casi cualquier porcentaje razonable dé igual”.

### 7.3. Comparación explícita contra la familia nominal

En comparación con `ANALISIS 72`, la familia porcentual parece:

- **más flexible**, porque no introduce cortes bruscos ni topes absolutos que choquen con el crecimiento del capital;
- **más útil históricamente**, porque sí muestra alguna mejora de drawdown y preserva mucho mejor `2024–2025` cuando los recortes son moderados;
- **más frágil al tuning**, porque pequeños cambios de porcentaje alteran el equilibrio retorno/drawdown de forma sensible.

La familia nominal era más tosca pero más simple; la porcentual es mejor candidata investigativa, aunque exige más disciplina para no sobreparametrizarla.

---

## 8. Dependencia de episodios concretos

La mejora o deterioro de esta familia **sí depende en buena parte de pocos episodios concretos**, y conviene decirlo sin ambigüedad.

### 8.1. Episodios donde más se deteriora el resultado

Los mayores recortes frente al baseline se concentran en pocos trades grandes:

- `2022-04-13 → 2022-05-17` (`PROBLEMATICO`), especialmente relevante en todas las variantes con reducción;
- `2020-11-25 → 2021-02-25` (`MIXTO`), con impacto visible en uniformes y en la condicionada prudente;
- `2022-03-03 → 2022-03-11` (`PROBLEMATICO`), otro bloque importante de `2022`;
- en el **uniforme 30%**, aparecen además recortes severos en grandes ganadores `MIXTO` de `2024–2025`, sobre todo:
  - `2024-09-16 → 2025-01-06`;
  - `2025-05-14 → 2025-11-11`;
  - `2023-11-08 → 2024-04-08`.

### 8.2. Concentración del efecto

La concentración es alta en las versiones condicionadas:

- en la **condicionada suave**, los **3** trades más afectados explican ~`74,4%` del deterioro total frente al baseline y los **5** primeros ~`86,4%`;
- en la **condicionada prudente**, los **3** primeros explican ~`65,1%` y los **5** primeros ~`76,8%`.

En las uniformes la concentración también existe, aunque se diluye algo al extender el recorte a más operaciones:

- **uniforme 10%:** top 3 ~`48,9%`, top 5 ~`64,7%`;
- **uniforme 20%:** top 3 ~`45,5%`, top 5 ~`60,5%`;
- **uniforme 30%:** top 3 ~`34,6%`, top 5 ~`47,1%`.

### 8.3. Lectura metodológica de esta dependencia

Esto significa que:

- la mejora aparente no está completamente repartida por toda la historia;
- buena parte del debate práctico sigue concentrándose en pocos bloques grandes, sobre todo en `2022` y en algunos tramos `MIXTO` de gran tamaño;
- por tanto, la familia porcentual **no debe presentarse como robustez estructural ya demostrada**.

Aun así, su dependencia es menos incómoda que la de la familia nominal porque, en versiones suaves, no destruye tanto los grandes ganadores recientes. El coste histórico se concentra más en ciertos episodios `PROBLEMATICO` y menos en amputar sistemáticamente todo el tramo bueno reciente.

---

## 9. Conclusión final

La familia de **reducción porcentual de exposición por régimen** sale históricamente mejor parada que la familia de **tope nominal** auditada en `ANALISIS 72`, pero no como una solución ya validada sino como una línea con potencial y con reservas claras.

La evidencia principal es esta:

- el baseline sin reducción sigue siendo el mejor en retorno total;
- la familia porcentual **sí compra algo de mejora en drawdown**, cosa que el tope nominal no conseguía de forma visible;
- las variantes condicionadas preservan bastante bien `FAVORABLE` y, en porcentajes moderados, dañan poco `2024–2025`;
- el precio pagado por la prudencia se concentra sobre todo en episodios concretos de `2022` y en algunos bloques grandes de `PROBLEMATICO` y `MIXTO`;
- la sensibilidad al porcentaje elegido es real, así que la familia puede degradarse rápido si se entra en tuning fino sin disciplina.

Dicho de forma sintética:

- **más flexible que la nominal:** sí;
- **más útil históricamente que la nominal:** también sí;
- **más frágil al tuning que la nominal:** igualmente sí.

Por eso, la familia porcentual parece merecer **más prioridad investigativa que el tope nominal**, pero solo si se mantiene un espacio de prueba muy corto y prudente.

---

## 10. Recomendación: familia prometedora / útil con reservas / no priorizar

**Recomendación final: útil con reservas.**

Motivos:

1. **Sí merece más prioridad que la familia nominal.**
   - Históricamente ofrece una mejora de drawdown que la nominal apenas mostraba.
   - Preserva mucho mejor los años favorables recientes cuando se usan recortes moderados.

2. **No debe tratarse todavía como familia prometedora en sentido fuerte.**
   - El baseline sigue siendo superior en retorno total.
   - La mejora depende bastante de pocos episodios y del porcentaje elegido.

3. **No conviene abrir todavía una lógica escalonada compleja.**
   - La familia ya introduce sensibilidad suficiente con solo `10%`, `20%` y `30%`.
   - Añadir más escalones o más grados de libertad aumentaría el riesgo de tuning sin necesidad.

4. **La lectura más sana es esta:**
   - si se prioriza una siguiente ronda, la familia porcentual merece ir **antes** que el tope nominal;
   - pero debe hacerse con **muy pocos perfiles**, preferentemente condicionados y moderados;
   - y sin declarar todavía ningún porcentaje como óptimo ni estable.

En resumen final:

- **tope nominal por régimen:** línea simple pero históricamente floja;
- **reducción porcentual por régimen:** línea más útil y más flexible, aunque todavía demasiado sensible para darle rango de solución final.
