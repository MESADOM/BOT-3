# VERSION 2.2.1 ANALISIS 30

## 1. Objetivo

Revalidar de forma concentrada y definitiva la única línea de mejora que seguía viva tras los análisis anteriores: el filtro anti-sobreextensión **short** basado en la distancia del precio a la `SMA200`, manteniendo **todo lo demás idéntico a la base 2.2.1**, sin tocar la lógica long, sin abrir nuevas familias de cambios y sin modificar producción.

La pregunta concreta de este análisis es estrictamente local:

- comprobar si la mejora observada previamente alrededor de `QQQ / SMA200 - 1 <= -15%` tiene una **zona razonable de robustez**;
- o si, por el contrario, depende de un **punto demasiado fino** como para tratarla como mejora fiable.

## 2. Hipótesis de validación

La hipótesis sometida a prueba es la siguiente:

- si el filtro anti-sobreextensión por distancia a `SMA200` captura una debilidad **real y estructural** del módulo short de la 2.2.1, entonces una familia **muy corta** de umbrales vecinos alrededor del `-15%` debería conservar una mejora razonable frente a la base;
- si la mejora desaparece o cambia bruscamente con desplazamientos pequeños del umbral, entonces la señal debe considerarse **sensible** y con riesgo elevado de sobreajuste.

## 3. Umbrales probados

Se mantuvo intacta la base **2.2.1** y solo se añadió este filtro previo a la entrada short:

- **bloquear entrada short si** `QQQ / SMA200 - 1 <= umbral`.

Familia corta probada alrededor del mejor hallazgo previo:

- `-13%`
- `-14%`
- `-15%`  ← hallazgo previo a revalidar
- `-16%`
- `-17%`

Base de comparación:

- **2.2.1 base**: sin filtro extra por distancia a `SMA200`.

## 4. Resultados comparativos vs 2.2.1

### Tabla resumen

| Variante | Retorno total sistema | Delta vs base | Drawdown máx | Sharpe diario anualizado | Profit factor global | Profit factor short | Nº trades short | Trades short bloqueados | Falsos positivos reducidos | Falsos negativos introducidos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Base 2.2.1 | 2096,28% | — | -33,55% | 0,6720 | 4,776 | 4,645 | 11 | 0 | — | — |
| SMA200 `-13%` | 2180,03% | +83,75 pts | -33,55% | 0,6815 | 5,298 | 9,919 | 9 | 4 | `2022-10-19`, `2022-11-09` | `2022-06-01`, `2022-07-07` |
| SMA200 `-14%` | 2192,88% | +96,60 pts | -33,55% | 0,6828 | 5,323 | 10,181 | 9 | 4 | `2022-10-19`, `2022-11-09` | `2022-06-01`, `2022-07-07` |
| SMA200 `-15%` | 2196,58% | +100,30 pts | -33,55% | 0,6832 | 5,330 | 10,257 | 9 | 3 | `2022-10-19`, `2022-11-09` | `2022-07-07` |
| SMA200 `-16%` | 2070,18% | -26,10 pts | -33,55% | 0,6689 | 4,586 | 3,746 | 11 | 1 | ninguno | `2022-07-07` |
| SMA200 `-17%` | 2070,18% | -26,10 pts | -33,55% | 0,6689 | 4,586 | 3,746 | 11 | 1 | ninguno | `2022-07-07` |

### Lectura comparativa

#### Base 2.2.1
La base sigue siendo el punto de referencia con:

- `2096,28%` de retorno total;
- `-33,55%` de drawdown máximo;
- `4,776` de profit factor global;
- `4,645` de profit factor short;
- `11` trades short.

#### Umbral `-13%`
Mejora claramente el agregado frente a la base, pero lo hace con un coste ya apreciable:

- mejora retorno, Sharpe y profit factor global;
- reduce dos falsos positivos relevantes (`2022-10-19` y `2022-11-09`);
- pero bloquea además dos ganadores base (`2022-06-01` y `2022-07-07`).

Lectura: mejora **sí**, pero con una poda algo agresiva del bloque ganador de 2022.

#### Umbral `-14%`
Es muy parecido al `-15%` en las métricas agregadas y mantiene mejora clara frente a la base:

- retorno total casi al nivel del mejor punto;
- profit factor short muy alto;
- misma limpieza de los dos falsos positivos principales de 2022;
- mismo coste en falsos negativos que el `-13%`, porque también bloquea `2022-06-01` y `2022-07-07`.

Lectura: existe una mejora real en este vecindario, pero no completamente limpia.

#### Umbral `-15%`
Sigue siendo el mejor punto local de esta familia corta:

- mayor retorno total del sistema;
- mejor Sharpe de la batería;
- mejor profit factor global;
- mejor profit factor short;
- mantiene el drawdown máximo igual a la base.

Además, frente a `-13%` y `-14%`, mejora algo la calidad del compromiso:

- sigue eliminando los dos falsos positivos relevantes (`2022-10-19` y `2022-11-09`);
- ya no bloquea el ganador importante `2022-06-01`;
- solo sacrifica el ganador pequeño `2022-07-07`.

#### Umbral `-16%`
Aquí aparece el quiebre de robustez local:

- la mejora desaparece;
- el retorno total cae por debajo de la base;
- el Sharpe cae por debajo de la base;
- el profit factor global cae por debajo de la base;
- el profit factor short cae con fuerza;
- ya no elimina ninguno de los falsos positivos principales que justificaban la hipótesis.

Lectura: mover el umbral solo un punto adicional desde `-15%` a `-16%` rompe la tesis práctica de mejora.

#### Umbral `-17%`
Repite exactamente la lectura de `-16%` en esta muestra:

- no aporta mejora frente a la base;
- no limpia los cortos problemáticos clave;
- mantiene únicamente el coste de bloquear un ganador pequeño.

Lectura: la ventaja observada no continúa al aflojar un poco más el filtro.

## 5. Sensibilidad local del umbral

La sensibilidad local es la pieza central de este análisis.

### Lo que sí se observa
Sí aparece una **pequeña banda favorable** en torno al hallazgo previo:

- `-13%`, `-14%` y `-15%` mejoran el retorno total frente a la base;
- `-14%` y `-15%` además lo hacen con métricas muy similares y claramente mejores en profit factor global y short;
- por tanto, **no** estamos ante un punto completamente aislado en el sentido estricto de “solo un valor funciona”.

### Lo que limita esa lectura
Sin embargo, esa banda es **estrecha y asimétrica**:

- al mover el umbral desde `-15%` a `-16%`, la mejora se rompe de forma brusca;
- `-16%` y `-17%` ya quedan por debajo de la base en retorno, Sharpe y profit factor global;
- `-13%` y `-14%` todavía mejoran, pero lo hacen con una poda más agresiva de shorts ganadores válidos del bloque 2022.

### Veredicto de sensibilidad
La lectura más precisa es esta:

- **sí existe una banda local razonable**, centrada sobre todo en `-14%` / `-15%`;
- pero esa banda **no es amplia ni especialmente estable**;
- la pendiente al lado “flojo” del umbral (`-16%`, `-17%`) se deteriora demasiado rápido.

Por tanto, la mejora **no depende de un único punto exacto**, pero sí de una **zona corta y delicada**, lo bastante sensible como para seguir considerándola vulnerable a sobreajuste.

## 6. Impacto en trades short bloqueados

### Base short de referencia
Los `11` trades short de la base fueron:

- `2016-02-08`
- `2016-03-02`
- `2018-12-12`
- `2022-03-03`
- `2022-03-23`
- `2022-04-13`
- `2022-06-01`
- `2022-07-07`
- `2022-10-19`
- `2022-11-09`
- `2025-04-15`

### Trades bloqueados por variante

#### Umbral `-13%`
Trades short base bloqueados: **4**

- `2022-06-01`
- `2022-07-07`
- `2022-10-19`
- `2022-11-09`

Efecto:

- falsos positivos reducidos: `2`
- falsos negativos introducidos: `2`
- aparecen reentradas sustitutas en `2022-06-06` y `2022-11-02`.

#### Umbral `-14%`
Trades short base bloqueados: **4**

- `2022-06-01`
- `2022-07-07`
- `2022-10-19`
- `2022-11-09`

Efecto:

- falsos positivos reducidos: `2`
- falsos negativos introducidos: `2`
- aparecen reentradas sustitutas en `2022-06-06` y `2022-10-25`.

#### Umbral `-15%`
Trades short base bloqueados: **3**

- `2022-07-07`
- `2022-10-19`
- `2022-11-09`

Efecto:

- falsos positivos reducidos: `2`
- falsos negativos introducidos: `1`
- aparece una reentrada sustituta útil en `2022-10-25`.

#### Umbral `-16%`
Trades short base bloqueados: **1**

- `2022-07-07`

Efecto:

- falsos positivos reducidos: `0`
- falsos negativos introducidos: `1`
- aparece reentrada sustituta en `2022-07-11`, pero la mejora agregada desaparece.

#### Umbral `-17%`
Trades short base bloqueados: **1**

- `2022-07-07`

Efecto:

- falsos positivos reducidos: `0`
- falsos negativos introducidos: `1`
- resultado agregado idéntico al `-16%` en esta muestra.

### Lectura conjunta
El mejor compromiso de esta familia sigue siendo `-15%`, porque:

- elimina los dos falsos positivos principales que daban soporte a la hipótesis;
- solo introduce un falso negativo pequeño;
- y evita el sobrebloqueo adicional que sí aparece en `-13%` y `-14%`.

Aun así, persiste una debilidad importante:

- **ningún umbral probado corrige el caso `2025-04-15`**, que sigue siendo la objeción estructural más incómoda para la hipótesis del filtro.

## 7. Riesgos de sobreajuste

Los riesgos de sobreajuste siguen siendo altos y este análisis no los elimina, solo los acota mejor.

### Riesgo 1 — Muestra short pequeña
La base sigue teniendo muy pocos trades short. Con una muestra tan corta:

- mover `1` o `2` operaciones cambia mucho el profit factor short;
- y también altera con facilidad la narrativa de mejora.

### Riesgo 2 — Banda corta, no meseta amplia
Aunque ahora puede decirse que el `-15%` no está completamente solo, la zona favorable es **corta**:

- `-14%` y `-15%` son defendibles;
- `-13%` aún mejora, pero ya se vuelve más agresivo contra ganadores válidos;
- `-16%` y `-17%` rompen la mejora.

Eso no parece una meseta robusta amplia, sino una zona local relativamente estrecha.

### Riesgo 3 — Dependencia de pocos episodios concretos
La mejora sigue dependiendo de limpiar principalmente:

- `2022-10-19`
- `2022-11-09`

Eso sigue siendo útil, pero mantiene la sospecha de que una parte importante de la ventaja proviene de unos pocos casos decisivos de 2022.

### Riesgo 4 — Caso tardío relevante no resuelto
El filtro sigue sin bloquear:

- `2025-04-15`

Eso debilita la tesis de que la regla esté capturando de forma general la sobreextensión short; más bien parece capturarla **parcialmente**.

## 8. Conclusión final

La revalidación local permite decir algo más preciso que en análisis anteriores:

- el filtro anti-sobreextensión short por distancia a `SMA200` **no** depende de un punto absolutamente único y aislado;
- sí existe una **pequeña banda favorable** alrededor del hallazgo previo, sobre todo en `-14%` y `-15%`;
- sin embargo, esa banda es **estrecha**, **asimétrica** y **metodológicamente frágil**.

La lectura más honesta es esta:

- `-15%` sigue siendo el mejor compromiso local de la familia probada;
- `-14%` confirma que hay algo de señal alrededor;
- pero la ruptura rápida en `-16%` y `-17%`, junto con la persistencia del caso `2025-04-15`, impide presentar esta mejora como robusta en sentido fuerte.

En otras palabras:

- **hay señal real**;
- **hay algo de vecindad útil**;
- pero **todavía no hay una robustez suficientemente amplia como para rebajar de verdad la sospecha de sobreajuste**.

## 9. Recomendación: robusta / dudosa / frágil / descartar

### Recomendación final: **frágil**

Motivo:

- no debe descartarse, porque `-14%` y `-15%` sí sostienen mejora real frente a la base;
- pero tampoco puede calificarse como robusta, porque la zona favorable es corta y se rompe demasiado rápido al moverse a `-16%`;
- y sigue sin resolver un caso tardío relevante fuera del bloque 2022.

Conclusión operativa final:

- la mejora **sobrevive** a una refutación mínima local;
- pero la sobrevive solo como mejora **frágil**, no como mejora robusta ni lista para promoción.
