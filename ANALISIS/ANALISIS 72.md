# VERSION 2.2.2 ANALISIS 72

## 1. Objetivo

Auditar históricamente la familia de reglas de **tope máximo nominal de entrada** condicionada por régimen, trabajando sobre el **sistema general long-short vigente** y sobre el **selector provisional actualmente aceptado como base**, para decidir si esta línea merece seguir adelante como investigación histórica sin alterar todavía la lógica base ni tocar producción.

El foco de este documento es deliberadamente acotado:

- **no** diseña estrategias nuevas por régimen;
- **no** implementa nada en producción;
- **no** declara óptimo ningún valor nominal;
- **sí** compara la familia en tres planos mínimos:
  - sin tope nominal;
  - con tope nominal único para todos los regímenes;
  - con tope nominal condicionado por régimen.

La lectura obligatoria previa ha sido:

- `ANALISIS 68.md`
- `ANALISIS 69.md`
- `ANALISIS 70.md`
- `ANALISIS 71.md`

Además, para mantener continuidad con la taxonomía ya usada en la secuencia anterior, el selector se ha traducido a clases de esta forma:

- **FAVORABLE** si `score_regimen >= 2`;
- **MIXTO** si `score_regimen = 0 o 1`;
- **PROBLEMATICO** si `score_regimen <= -1`.

La prueba histórica se ha hecho como replay del motor actual, introduciendo **solo** un cap nominal adicional en la entrada y dejando intactas las señales long-short, las salidas, el selector y la lógica operativa general.

---

## 2. Familia de reglas auditada

La familia auditada añade un único control externo: un **tope máximo nominal de entrada en euros** aplicado sobre el capital objetivo de cada operación antes de convertirlo en unidades.

Conceptualmente, la familia se ha auditado en tres capas:

1. **Sin tope nominal**
   - baseline del sistema actual.

2. **Tope nominal único para todos los regímenes**
   - mismo techo para `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.

3. **Tope nominal condicionado por régimen**
   - mayor libertad en `FAVORABLE`;
   - cautela intermedia en `MIXTO`;
   - mayor restricción en `PROBLEMATICO`.

La intención de esta auditoría no es validar una política final, sino comprobar si esta familia aporta una mejora histórica defendible o si, por el contrario, tiende sobre todo a **recortar años y episodios ya buenos**.

---

## 3. Variantes nominales evaluadas

Se han usado referencias nominales simples y explícitas, tal como se pedía:

- **3000 €**
- **5000 €**
- **7000 €**

### 3.1. Variantes comparadas

| Variante | Regla |
|---|---|
| Sin tope | Sin límite nominal adicional |
| Uniforme 3000 | `3000 €` para todos los regímenes |
| Uniforme 5000 | `5000 €` para todos los regímenes |
| Uniforme 7000 | `7000 €` para todos los regímenes |
| Condicionada suave | `FAVORABLE` sin tope, `MIXTO 7000 €`, `PROBLEMATICO 5000 €` |
| Condicionada prudente | `FAVORABLE` sin tope, `MIXTO 5000 €`, `PROBLEMATICO 3000 €` |

### 3.2. Criterio metodológico de estas dos variantes condicionadas

Se han elegido dos perfiles condicionados muy simples:

- uno **suave**, que intenta preservar más años fuertes y solo moderar `MIXTO` y `PROBLEMATICO`;
- uno **prudente**, que aprieta claramente más en las dos clases no favorables.

No se han abierto combinaciones más complejas porque la prioridad aquí es auditar **la familia**, no hacer tuning fino.

---

## 4. Resultados históricos comparados

### 4.1. Retorno total y drawdown total por variante

| Variante | Beneficio neto total | Retorno total | Drawdown total |
|---|---:|---:|---:|
| Sin tope | `21.965,83 €` | `+2196,58%` | `-28,49%` |
| Uniforme 3000 | `12.560,42 €` | `+1256,04%` | `-28,49%` |
| Uniforme 5000 | `17.571,94 €` | `+1757,19%` | `-28,49%` |
| Uniforme 7000 | `20.267,52 €` | `+2026,75%` | `-28,49%` |
| Condicionada suave | `19.657,60 €` | `+1965,76%` | `-28,49%` |
| Condicionada prudente | `16.143,52 €` | `+1614,35%` | `-28,49%` |

### 4.2. Lectura principal de la comparación total

La señal histórica más clara es esta:

- **ninguna variante con tope mejora el drawdown total histórico**;
- el drawdown total queda **idéntico** en todas las variantes (`-28,49%`);
- por tanto, toda la discusión práctica de esta familia queda dominada por **cuánto retorno sacrifica** y por **dónde lo sacrifica**.

Eso debilita bastante la tesis de un tope nominal como gran herramienta estructural de protección histórica, al menos en esta muestra y manteniendo intacta la lógica base actual.

### 4.3. Orden histórico observado

En retorno total, el orden queda así:

1. **Sin tope**
2. **Uniforme 7000**
3. **Condicionada suave**
4. **Uniforme 5000**
5. **Condicionada prudente**
6. **Uniforme 3000**

La conclusión comparativa inmediata es sencilla: cuanto más severo es el tope, más se degrada el retorno total, y esa degradación **no viene acompañada de una mejora equivalente del drawdown total**.

---

## 5. Impacto por régimen

### 5.1. Beneficio total por clase del selector

Baseline sin tope:

- **FAVORABLE:** `3.914,95 €`
- **MIXTO:** `13.519,61 €`
- **PROBLEMATICO:** `4.531,27 €`

Esto confirma algo ya anticipado en la secuencia anterior:

- `MIXTO` sigue siendo la principal fuente agregada de beneficio;
- `PROBLEMATICO` aporta valor real, pero claramente menor;
- `FAVORABLE` es sano, aunque no monopoliza el edge total.

### 5.2. Efecto comparado por clase

| Variante | FAVORABLE | MIXTO | PROBLEMATICO |
|---|---:|---:|---:|
| Sin tope | `3.914,95 €` | `13.519,61 €` | `4.531,27 €` |
| Uniforme 3000 | `3.502,26 €` | `6.258,20 €` | `2.799,96 €` |
| Uniforme 5000 | `4.098,65 €` | `9.428,61 €` | `4.044,68 €` |
| Uniforme 7000 | `4.038,28 €` | `11.697,97 €` | `4.531,27 €` |
| Condicionada suave | `3.914,95 €` | `11.697,97 €` | `4.044,68 €` |
| Condicionada prudente | `3.914,95 €` | `9.428,61 €` | `2.799,96 €` |

### 5.3. Lectura por clase

#### FAVORABLE

- El impacto es **bajo** salvo en el uniforme `3000 €`.
- Las variantes condicionadas preservan `FAVORABLE` prácticamente por construcción, porque se deja libre esa clase.
- No aparece aquí el gran problema histórico de la familia.

#### MIXTO

- Aquí se concentra el efecto decisivo de la familia.
- Frente al baseline, `MIXTO` cae:
  - `-7.261,41 €` con uniforme `3000 €`;
  - `-4.091,00 €` con uniforme `5000 €`;
  - `-1.821,64 €` con uniforme `7000 €`;
  - `-1.821,64 €` con condicionada suave;
  - `-4.091,00 €` con condicionada prudente.

**Conclusión sobre MIXTO:** el tope nominal actúa sobre todo como un recorte del principal motor histórico del sistema. La familia puede disciplinar `MIXTO`, sí, pero históricamente lo que hace sobre todo es **capar una parte importante de su edge**.

#### PROBLEMATICO

- El efecto existe, pero es menor que en `MIXTO` salvo en la versión muy prudente.
- Caídas frente al baseline:
  - `-1.731,31 €` con uniforme `3000 €`;
  - `-486,59 €` con uniforme `5000 €`;
  - `0,00 €` con uniforme `7000 €`;
  - `-486,59 €` con condicionada suave;
  - `-1.731,31 €` con condicionada prudente.

**Conclusión sobre PROBLEMATICO:** la familia sí reduce exposición en un bloque hostil, pero no muestra una gran mejora histórica asociada; más bien recorta una parte del valor que el general todavía consigue capturar ahí, especialmente en `2022`.

---

## 6. Impacto en 2022 y años favorables

### 6.1. Impacto en 2022

| Variante | Resultado 2022 |
|---|---:|
| Sin tope | `4.119,19 €` |
| Uniforme 3000 | `2.418,00 €` |
| Uniforme 5000 | `3.637,28 €` |
| Uniforme 7000 | `4.119,19 €` |
| Condicionada suave | `3.522,08 €` |
| Condicionada prudente | `2.130,00 €` |

Lectura histórica de `2022`:

- el uniforme `7000 €` no altera `2022` de forma material;
- el uniforme `5000 €` todavía conserva bastante del año;
- la condicionada suave ya recorta una porción relevante;
- la condicionada prudente y el uniforme `3000 €` recortan mucho más.

Esto es importante porque `2022` era precisamente uno de los argumentos intuitivos a favor de poner prudencia en `PROBLEMATICO`. Sin embargo, en la práctica histórica observada, los topes más restrictivos **no mejoran el drawdown total** y sí reducen una parte visible de la captura de `2022`.

### 6.2. Preservación de años favorables

Para medir preservación de años favorables se ha mirado sobre todo el bloque fuerte reciente del baseline: **2020, 2021, 2024 y 2025**.

Suma baseline en esos años: **`16.545,82 €`**.

Retención aproximada del bloque favorable:

- **Uniforme 3000:** `8.336,46 €` → conserva ~`50,4%`
- **Uniforme 5000:** `12.073,76 €` → conserva ~`73,0%`
- **Uniforme 7000:** `14.419,68 €` → conserva ~`87,1%`
- **Condicionada suave:** `14.320,95 €` → conserva ~`86,6%`
- **Condicionada prudente:** `12.041,84 €` → conserva ~`72,8%`

La lectura es clara:

- las variantes duras (`3000 €` o condicionada prudente) **no preservan bien los años fuertes**;
- las variantes más suaves (`7000 €` uniforme o condicionada suave) preservan bastante mejor, pero aun así recortan retorno agregado;
- la familia no muestra una combinación donde el sacrificio de años buenos venga compensado por una mejora histórica visible del drawdown total.

### 6.3. Impacto en 2024–2025

| Variante | 2024 | 2025 | 2024–2025 combinado |
|---|---:|---:|---:|
| Sin tope | `3.996,00 €` | `7.637,00 €` | `11.633,00 €` |
| Uniforme 3000 | `1.988,49 €` | `2.382,27 €` | `4.370,76 €` |
| Uniforme 5000 | `3.318,15 €` | `3.931,35 €` | `7.249,50 €` |
| Uniforme 7000 | `3.899,92 €` | `5.606,94 €` | `9.506,86 €` |
| Condicionada suave | `3.899,92 €` | `5.508,21 €` | `9.408,13 €` |
| Condicionada prudente | `3.318,15 €` | `3.810,87 €` | `7.129,02 €` |

Aquí aparece la mayor advertencia práctica de toda la auditoría:

- el recorte en `2024–2025` es muy visible en casi todas las variantes con tope;
- la mayor parte del deterioro total de la familia viene precisamente de **capar operaciones muy ganadoras del tramo reciente**, sobre todo en `MIXTO`.

---

## 7. Sensibilidad al valor nominal

La sensibilidad básica al valor nominal es alta y monotónica:

- `3000 €` es claramente demasiado restrictivo para esta familia en histórico;
- `5000 €` mejora frente a `3000 €`, pero sigue recortando demasiado retorno;
- `7000 €` es el menos dañino de los uniformes, pero aun así queda por debajo de no poner tope.

### 7.1. Sensibilidad en la versión uniforme

- pasar de **`3000 €` a `5000 €`** recupera una parte grande del retorno perdido;
- pasar de **`5000 €` a `7000 €`** vuelve a recuperar otra porción relevante;
- eso indica que el resultado depende bastante del umbral nominal elegido.

Dicho de otro modo: la familia **sí es sensible al nominal** y no parece ofrecer una zona robusta evidente donde “casi cualquier valor razonable funcione parecido”.

### 7.2. Sensibilidad en la versión condicionada

Comparando las dos variantes condicionadas simples:

- la **condicionada suave** (`F libre / M7000 / P5000`) cae menos que la prudente;
- la **condicionada prudente** (`F libre / M5000 / P3000`) deteriora mucho más, sobre todo por el recorte simultáneo en `MIXTO` y en `PROBLEMATICO`.

Esto sugiere que, dentro de la familia condicionada, el verdadero problema no es solo `PROBLEMATICO`; el coste histórico aparece sobre todo cuando se aprieta demasiado `MIXTO`.

### 7.3. Lectura metodológica de la sensibilidad

La sensibilidad observada no autoriza a decir que exista ya un valor “correcto”. Lo que sí permite decir es esto:

- la familia **no es inerte**;
- cambia mucho el resultado según el nominal;
- y por tanto sería una familia peligrosa de sobreajustar si se abriese demasiado pronto un tuning fino.

---

## 8. Dependencia de episodios concretos

Sí. La mejora o el deterioro de esta familia depende en buena medida de **pocos episodios concretos**, y esto debe quedar escrito de forma explícita.

### 8.1. Concentración del efecto en pocos trades

Al comparar cada variante contra el baseline, la mayor parte del deterioro aparece concentrada en unas pocas operaciones grandes, especialmente:

- `2025-05-14` a `2025-11-11` (`MIXTO`), gran ganador del baseline;
- `2024-09-16` a `2025-01-06` (`MIXTO`), también muy relevante;
- `2024-05-08` a `2024-07-22` (`MIXTO`);
- `2022-04-13` a `2022-05-17` (`PROBLEMATICO`);
- varios bloques adicionales de `2022` en `PROBLEMATICO`, sobre todo cuando se usa la versión prudente.

Ejemplo claro:

- en el uniforme `5000 €`, el mayor deterioro individual proviene del trade `2025-05-14 → 2025-11-11`, cuyo beneficio baja de `4.998,50 €` a `2.598,26 €`;
- en la condicionada prudente, los mayores recortes vuelven a venir de unos pocos trades `MIXTO` de `2024–2025` y de algunos trades ganadores `PROBLEMATICO` de `2022`.

### 8.2. Compensaciones positivas, pero insuficientes

También aparecen algunos episodios donde el tope ayuda:

- por ejemplo, reduce pérdidas en ciertos trades posteriores de `2026`;
- o suaviza algunos trades perdedores de `2024–2025`.

Pero históricamente esas compensaciones son **demasiado pequeñas** frente al daño provocado por el recorte de pocos trades muy ganadores.

### 8.3. Concentración temporal

La dependencia temporal también es clara:

- el efecto relevante se concentra sobre todo en **2022** y en **2024–2025**;
- fuera de esos bloques, muchas diferencias son pequeñas o nulas;
- por tanto, la lectura de la familia depende bastante de cómo se valore justamente ese puñado de episodios de alta contribución.

Conclusión de este punto:

- **sí**, la mejora o deterioro depende de pocos trades y pocos periodos;
- y en esta muestra la dependencia juega más en contra de la familia, porque los topes tienden a amputar ganancias concentradas sin ofrecer una protección total equivalente.

---

## 9. Conclusión final

La auditoría histórica deja una imagen bastante nítida.

### 9.1. Qué sí muestra la familia

La familia “tope máximo nominal por régimen”:

- es simple;
- es fácil de auditar;
- encaja bien como decisión suave;
- y conceptualmente tiene lógica, sobre todo para imponer cautela sin tocar señales.

### 9.2. Qué no muestra la familia en esta auditoría

Sin embargo, históricamente no aparece una evidencia fuerte de que esta familia merezca prioridad alta ahora mismo, porque:

- **no mejora el drawdown total** de la muestra;
- sí recorta retorno total de forma visible;
- el principal daño aparece en `MIXTO`, que sigue siendo el gran motor del sistema;
- y parte de la poda también afecta a `PROBLEMATICO` justo en episodios donde el general sí conseguía capturar valor.

### 9.3. Lectura global equilibrada

La versión condicionada por régimen es **mejor conceptualmente** que la uniforme, porque al menos preserva `FAVORABLE` y concentra la cautela donde más sentido tenía estudiarla.

Pero incluso así, en esta auditoría histórica:

- la versión condicionada **suave** sigue quedando por debajo del baseline;
- la versión condicionada **prudente** ya degrada de forma clara años y episodios importantes;
- y la familia, tomada en conjunto, parece más útil como **idea de disciplina** que como fuente de mejora histórica ya visible.

---

## 10. Recomendación: familia prometedora / útil con reservas / no priorizar

**Recomendación: útil con reservas.**

Motivo:

1. **No conviene priorizarla como línea principal inmediata**, porque el histórico no muestra mejora estructural suficiente y el drawdown total no mejora.
2. **No conviene descartarla por completo**, porque la variante condicionada suave sí conserva parte importante del perfil del sistema y mantiene una lógica prudente, simple y auditable.
3. **Si se mantiene viva como investigación**, debería hacerse solo como línea secundaria y con disciplina estricta:
   - sin declarar ningún nominal óptimo;
   - sin abrir todavía una lógica compleja de topes;
   - y vigilando especialmente no destruir `MIXTO` en nombre de la prudencia.

### Dictamen final resumido

- **Sin tope nominal:** sigue siendo el mejor baseline histórico de esta auditoría.
- **Tope nominal único:** útil para entender sensibilidad, pero históricamente demasiado tosco y costoso en retorno.
- **Tope nominal condicionado por régimen:** es la subfamilia con mejor lógica para seguir investigando, pero **solo con reservas**, porque hasta ahora parece más una herramienta de contención conceptual que una mejora histórica robusta.
