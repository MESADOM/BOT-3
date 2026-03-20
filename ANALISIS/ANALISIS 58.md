# VERSION 2.2.2 ANALISIS 58

## 1. Objetivo

Auditar la **sensibilidad y fragilidad básica** de la primera versión del selector de contexto de la línea `2.2.2`, comprobando si **cambios pequeños y razonables** en ventanas, umbrales o parámetros secundarios alteran demasiado la clasificación histórica.

El objetivo de este documento **no** es optimizar el selector, **no** es abrir nuevas familias de variables y **no** es tocar producción. La misión es más austera:

- medir cuánto cambia la clasificación al mover ligeramente piezas ya existentes;
- detectar qué partes parecen estables y cuáles dependen demasiado de elecciones finas;
- decidir si esta primera versión puede considerarse robusta, usable con cautelas o todavía demasiado sensible.

### Nota metodológica importante

En el árbol actual del repositorio **no existen** `ANALISIS 56.md` ni `ANALISIS 57.md`. Por tanto, no es posible leer literalmente esa “primera especificación” pedida. Para no inventar un selector nuevo, esta auditoría toma como **primera versión efectivamente materializada** la que sí está implementada en `META_BOT.py`, porque es la única especificación operativa verificable hoy:

- variables núcleo del mercado principal: `QQQ > SMA200`, `Retorno 63` y `Cruces SMA50`;
- umbrales y ventanas efectivamente codificados;
- clasificación operativa `LONG_TREND / SHORT_TREND / NO_TRADE`.

Esta decisión es más honesta que fabricar una especificación ausente.

## 2. Selector auditado

Se audita la primera versión operativa visible en `META_BOT.py`, que usa exclusivamente variables del mercado principal ya justificadas en la cadena `50–55`:

- **estructura lenta**: `QQQ > SMA200`;
- **momento intermedio**: retorno de `63` sesiones;
- **ruido / serrucho**: número de cruces del precio respecto a `SMA50` en una ventana de `20` sesiones.

### Reglas efectivas auditadas

1. `Retorno 63`:
   - `POSITIVO` si `> +3%`;
   - `NEGATIVO` si `< -5%`;
   - si no, `NEUTRAL`.

2. `Cruces SMA50`:
   - `ALTO` si los cruces en ventana 20 son `> 4`;
   - si no, `NO_ALTO`.

3. Clasificación final del **meta-régimen**:
   - **LONG_TREND** si `QQQ > SMA200` y el retorno está en `POSITIVO` o `NEUTRAL`, con cruces no altos;
   - **SHORT_TREND** si `QQQ < SMA200` y el retorno es `NEGATIVO`;
   - **NO_TRADE** en el resto de casos.

### Muestra auditada

Se usó `datos/QQQ.csv`, con observaciones válidas desde `2009-10-15` hasta `2026-03-03`, una vez disponible `SMA200`.

### Distribución base observada

La clasificación base reparte los `4.120` días auditables así:

- **LONG_TREND**: `3.243` días (`78,7%`);
- **NO_TRADE**: `459` días (`11,1%`);
- **SHORT_TREND**: `418` días (`10,1%`).

Esto ya deja una primera señal estructural: el selector nace con **sesgo claramente alcista**, y su clase intermedia/bajista ocupa una parte mucho menor del histórico.

### Observación crítica adicional

La capa de sizing `AGRESIVO / DEFENSIVO` implementada en el mismo archivo resulta casi degenerada: clasifica prácticamente todo el histórico como `AGRESIVO`. Por eso, la auditoría de robustez útil se centra en el **meta-régimen de tres estados**, que sí ofrece una clasificación histórica con suficiente variedad para ser evaluada seriamente.

## 3. Variaciones razonables evaluadas

Se probaron únicamente variaciones **prudentes** dentro de las mismas familias ya presentes, sin introducir variables nuevas.

### A. Variación de ventana temporal principal

1. **Retorno 63 → 42 sesiones**
   - lectura algo más rápida;
   - variación razonable dentro del rango ya defendido en `ANALISIS 50`.

2. **Retorno 63 → 84 sesiones**
   - lectura algo más lenta;
   - sigue siendo una escala intermedia, no extrema.

### B. Variación de variable secundaria de ruido

3. **Ventana de cruces SMA50: 20 → 15 sesiones**
   - versión algo más táctica.

4. **Ventana de cruces SMA50: 20 → 25 sesiones**
   - versión algo más amortiguada.

### C. Variación de umbral no extremo

5. **Umbral de cruces altos: >4 → >3**
   - endurece ligeramente la detección de serrucho.

6. **Umbral de cruces altos: >4 → >5**
   - la vuelve algo más permisiva.

7. **Umbrales de retorno algo más blandos**
   - `POSITIVO > +2%`;
   - `NEGATIVO < -4%`.

8. **Umbrales de retorno algo más duros**
   - `POSITIVO > +4%`;
   - `NEGATIVO < -6%`.

## 4. Cambios observados en la clasificación

## 4.1 Cambio total de clasificación

| Variación | % de periodos cuya clase cambia | Lectura |
|---|---:|---|
| Retorno 42 | 7,21% | Cambio material, pero no catastrófico |
| Retorno 84 | 6,58% | Cambio material y concentrado en tramos límite |
| Cruces 15 | 1,94% | Bastante estable |
| Cruces 25 | 3,47% | Cambio moderado |
| Umbral cruces >3 | 6,14% | Sensibilidad relevante |
| Umbral cruces >5 | 2,16% | Sensibilidad baja-moderada |
| Retorno blando (+2/-4) | 2,01% | Bastante estable |
| Retorno duro (+4/-6) | 1,55% | Bastante estable |

### Lectura principal

La sensibilidad total del selector **no explota** con cualquier microcambio, lo cual es una buena señal. Sin embargo, tampoco puede llamarse “muy robusto” sin matices, porque:

- mover la ventana de retorno intermedio (`63 → 42/84`) cambia alrededor de **6,6%–7,2%** del histórico;
- endurecer el umbral de serrucho a `>3` también mueve **6,14%** del histórico;
- la mayor fragilidad aparece en las capas que deciden si un tramo dudoso sale de `LONG_TREND` hacia `NO_TRADE`, o si un tramo bajista pasa de `SHORT_TREND` a `NO_TRADE`.

## 4.2 Estabilidad de 2020–2025

| Variación | % de cambio dentro de 2020–2025 | Lectura |
|---|---:|---|
| Retorno 42 | 8,29% | Sensibilidad relevante |
| Retorno 84 | 6,90% | Sensibilidad relevante |
| Cruces 15 | 1,92% | Estable |
| Cruces 25 | 3,05% | Moderadamente estable |
| Umbral cruces >3 | 4,91% | Sensibilidad media |
| Umbral cruces >5 | 1,79% | Estable |
| Retorno blando (+2/-4) | 2,12% | Estable |
| Retorno duro (+4/-6) | 0,99% | Muy estable |

### Lectura de 2020–2025

El bloque `2020–2025` es **bastante estable** frente a cambios suaves de umbral, pero **menos estable** cuando se toca la ventana del retorno intermedio. Es decir:

- la **escala temporal del momentum** pesa más que los pequeños ajustes del umbral del propio momentum;
- la lectura de ruido por cruces también influye, pero menos;
- el selector reciente no parece caótico, aunque sí muestra dependencia apreciable de cómo se mida la persistencia intermedia.

## 4.3 Estabilidad de años ancla

### Base auditada

| Año | LONG_TREND | NO_TRADE | SHORT_TREND | Clase dominante base |
|---|---:|---:|---:|---|
| 2015 | 69,0% | 23,4% | 7,5% | LONG_TREND |
| 2016 | 66,0% | 17,8% | 16,2% | LONG_TREND |
| 2022 | 4,8% | 27,5% | 67,7% | SHORT_TREND |
| 2026* | 100,0% | 0,0% | 0,0% | LONG_TREND |

`* 2026` solo está disponible de forma parcial hasta `2026-03-03`.

### Sensibilidad observada por año ancla

#### 2015

- Con `Cruces 15`, `LONG_TREND` sube a **77,4%**.
- Con `Cruces 25`, `LONG_TREND` baja a **56,7%** y `NO_TRADE` sube a **35,7%**.
- Con `Umbral cruces >3`, `LONG_TREND` cae a **56,3%**.

**Lectura:** `2015` es bastante sensible a la capa de ruido. No suele cambiar a `SHORT_TREND`, pero sí oscila mucho entre `LONG_TREND` y `NO_TRADE`.

#### 2016

- Cambia menos que 2015, pero sigue mostrando sensibilidad en la dimensión de cruces.
- `LONG_TREND` baja a **60,9%** con `Cruces 25` y a **59,3%** con umbral `>3`.

**Lectura:** `2016` también es un año limítrofe, aunque algo menos frágil que `2015`.

#### 2022

- Es muy estable frente a cambios de cruces: prácticamente **no se mueve** con `15/25` sesiones ni con `>3 / >5` cruces.
- Sí es sensible a la ventana de retorno:
  - `Retorno 42`: `SHORT_TREND` baja de **67,7%** a **51,0%** y `NO_TRADE` sube a **44,2%**.
  - `Retorno 84`: `SHORT_TREND` sube a **72,1%**.

**Lectura:** `2022` no depende del filtro de ruido, pero sí bastante de la **longitud del momentum intermedio**. La pregunta no es si fue bajista, sino **cuánto tiempo** merece permanecer en `SHORT_TREND` frente a `NO_TRADE`.

#### 2026

- Base: `100% LONG_TREND`.
- Con `Cruces 25`, baja a **82,9% LONG_TREND** y **17,1% NO_TRADE**.
- Con `Umbral cruces >3`, baja a **70,7% LONG_TREND** y **29,3% NO_TRADE**.
- Con `Retorno 84` o umbral blando, apenas se mueve.

**Lectura:** el arranque parcial de `2026` es muy sensible al filtro de serrucho, pero no a la capa de retorno. Es una señal de que el tramo reciente podría estar siendo clasificado de forma algo optimista por la especificación base.

## 4.4 Periodos conflictivos

Los cambios no se distribuyen uniformemente. Se concentran en periodos “de borde” donde el selector duda entre:

- `LONG_TREND` y `NO_TRADE`, o
- `SHORT_TREND` y `NO_TRADE`.

### Tramos con mayor sensibilidad observada

1. **2015–2016**
   - tramo claramente frágil para la capa de cruces;
   - pequeños cambios en ventana o umbral desplazan semanas enteras entre `LONG_TREND` y `NO_TRADE`.

2. **2022**
   - tramo claramente frágil para la ventana de retorno;
   - acortar a `42` sesiones reduce bastante la permanencia en `SHORT_TREND`;
   - alargar a `84` la aumenta.

3. **Inicio de 2026**
   - tramo sensible a la medición de serrucho;
   - no parece cambiar de signo estructural, pero sí de convicción.

4. **2020, 2021, 2024**
   - muy estables en casi todas las variaciones;
   - los cambios son escasos y generalmente periféricos.

## 5. Partes estables del selector

Las piezas que mejor sobreviven a variaciones razonables son estas:

### 5.1 La estructura lenta `QQQ > SMA200`

Es la capa más estable de todas. No es la fuente principal de fragilidad del selector. Los cambios observados no nacen de esta dimensión, sino de cómo se decide si una zona dudosa es suficiente para `LONG_TREND`, `SHORT_TREND` o simplemente `NO_TRADE`.

### 5.2 Los umbrales del retorno, si se mueven poco

Mover `+3/-5` a `+2/-4` o `+4/-6` cambia solo **2,01%** y **1,55%** del histórico, respectivamente. Eso sugiere que la fragilidad no está tanto en el umbral fino del retorno como en la **ventana elegida** para medirlo.

### 5.3 Los grandes años alcistas recientes

`2020`, `2021` y `2024` son bastante estables. En ellos el selector conserva una lectura mayoritariamente `LONG_TREND` bajo casi todas las perturbaciones razonables. Esa parte de la clasificación sí parece sólida.

### 5.4 La identificación gruesa de 2022 como año hostil

Aunque cambia la intensidad, **2022 sigue siendo básicamente bajista/defensivo** en todas las pruebas razonables. La fragilidad está en el grado de persistencia de `SHORT_TREND`, no en la dirección general del diagnóstico.

## 6. Partes frágiles del selector

### 6.1 La capa de momentum depende más de la ventana que del umbral

Este es el hallazgo más claro de la auditoría:

- tocar el umbral del retorno mueve poco;
- tocar la ventana `63` hacia `42` o `84` mueve bastante más.

Eso implica que la especificación actual depende más de la **escala temporal elegida** que de la agresividad exacta del umbral.

### 6.2 La medición de serrucho es frágil en zonas laterales

Los cruces SMA50 no rompen el selector entero, pero sí condicionan de forma notable los periodos ambiguos. `2015`, `2016` y el arranque de `2026` son los casos más claros.

### 6.3 La clase intermedia `NO_TRADE` actúa como zona de absorción sensible

La mayor parte de los cambios no son saltos directos de `LONG_TREND` a `SHORT_TREND`, sino desplazamientos hacia o desde `NO_TRADE`.

Eso tiene dos implicaciones:

- la **dirección gruesa** del selector no es extremadamente frágil;
- la **convicción operativa** sí depende bastante de detalles finos en tramos conflictivos.

### 6.4 La capa `AGRESIVO / DEFENSIVO` es demasiado pobre para auditar robustez real

Como esa capa clasifica casi todo como `AGRESIVO`, su robustez aparente es engañosa. No parece robusta por calidad, sino por **falta de poder discriminante**. En términos prácticos, la primera capa útil es la de `LONG_TREND / SHORT_TREND / NO_TRADE`.

## 7. Años y tramos más sensibles

## 7.1 Años más sensibles

- **2015**: muy sensible a cruces/ruido.
- **2016**: sensible, aunque algo menos que 2015.
- **2022**: sensible a la escala temporal del retorno.
- **2026 (parcial)**: sensible a la capa de serrucho.

## 7.2 Años más estables

- **2020**: estable.
- **2021**: muy estable.
- **2024**: extremadamente estable.

## 7.3 Tramos conflictivos más frágiles

- zonas laterales o de transición de `2015–2016`;
- bear market de `2022`, sobre todo en la frontera `SHORT_TREND` vs `NO_TRADE`;
- arranque de `2026`, donde pequeños cambios de ruido reducen bastante la confianza alcista.

## 7.4 Sensibilidad a cambios razonables

Juicio resumido:

- **sensibilidad baja** a pequeños cambios de umbral del retorno;
- **sensibilidad media** a cambios en la ventana/umbral de cruces;
- **sensibilidad media-alta** a cambios en la ventana del retorno intermedio.

En otras palabras: el selector no parece colapsar con ajustes prudentes, pero tampoco está completamente blindado frente a decisiones de escala temporal.

## 8. Conclusión final

La primera versión auditada del selector muestra un comportamiento mixto.

### Señales a favor

- la clasificación histórica **no se descompone** con cualquier microvariación razonable;
- los grandes años alcistas recientes (`2020`, `2021`, `2024`) permanecen bastante estables;
- `2022` sigue apareciendo como año mayoritariamente hostil en todas las pruebas;
- los cambios más frecuentes son de **convicción** (`NO_TRADE`) más que de signo estructural completo.

### Señales en contra

- la ventana de retorno intermedio tiene un peso material: `63 → 42/84` cambia alrededor de `6,6%–7,2%` del histórico;
- la medición de ruido con cruces SMA50 es frágil en años laterales y transicionales;
- `2015`, `2016` y el inicio parcial de `2026` dependen demasiado de elecciones finas de serrucho;
- la capa `AGRESIVO/DEFENSIVO` prácticamente no discrimina y por tanto no aporta una robustez defendible.

### Juicio de conjunto

No sería honesto llamar a esta primera versión **plenamente robusta**. Pero tampoco parece un artefacto caótico o completamente inservible.

La lectura más defendible es esta:

- la **dirección gruesa** del selector es razonablemente estable;
- la **frontera entre convicción y prudencia** todavía es sensible en tramos conflictivos;
- la complejidad necesaria para estabilizarlo no parece enorme, pero sí exigiría al menos:
  - fijar mejor la escala temporal del momentum;
  - simplificar o amortiguar la capa de cruces/serrucho;
  - evitar que la primera capa útil dependa de una clasificación secundaria casi degenerada.

## 9. Recomendación: robusto / usable con cautelas / demasiado frágil

**Recomendación final: usable con cautelas.**

Motivos:

- **no** parece suficientemente robusto como para afirmar que pequeñas variaciones dejan casi intacta toda la clasificación;
- **sí** conserva bastante bien los grandes bloques históricos y los años más claros;
- la fragilidad actual está concentrada sobre todo en:
  - `2015–2016`;
  - la persistencia exacta de `2022` en `SHORT_TREND`;
  - la lectura reciente de `2026`;
  - la dependencia de la ventana del retorno intermedio y de la capa de cruces.

Por tanto, esta primera versión **puede servir como base de trabajo**, pero todavía requiere una estabilización metodológica prudente antes de poder recibir una etiqueta seria de “robusta”.
