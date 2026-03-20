# VERSION 2.2.2 ANALISIS 60

## 1. Objetivo

Comparar varias especificaciones mínimas rivales del selector de contexto, todas dentro de la arquitectura ya definida en `ANALISIS 56–59`, para identificar cuál ofrece el mejor equilibrio entre interpretabilidad, estabilidad y utilidad histórica, sin tocar producción, sin abrir nuevas estrategias y sin optimizar agresivamente el selector.

La pregunta no es qué variante “encaja mejor” con un episodio concreto, sino cuál conserva mejor estas propiedades al mismo tiempo:

- coherencia histórica;
- estabilidad de clasificación;
- simplicidad estructural;
- facilidad de explicación;
- utilidad práctica para investigación posterior.

## 2. Especificaciones comparadas

Se comparan exactamente tres especificaciones mínimas rivales, manteniendo la misma taxonomía de salida:

- `FAVORABLE`
- `MIXTO`
- `PROBLEMATICO`

### Especificación A

Variables:

- `QQQ > SMA200`
- `Retorno 63`
- `Cruces SMA50`

Regla mínima usada, consistente con `ANALISIS 57`:

- `+1` si `QQQ > SMA200`, `-1` si no.
- `+1` si `Retorno 63 > +3%`.
- `-1` si `Retorno 63 < -5%`.
- `-1` si `Cruces SMA50 > 4`.
- `FAVORABLE` si `score >= 2`.
- `MIXTO` si `score = 0 o 1`.
- `PROBLEMATICO` si `score <= -1`.

### Especificación B

Variables:

- `QQQ > SMA200`
- `Distancia a SMA200`
- `Cruces SMA50`
- `ATR% 21d`

Regla mínima usada para conservar parsimonia:

- `+1` si `QQQ > SMA200`, `-1` si no.
- `+1` si la distancia a `SMA200` es `> +3%`.
- `-1` si la distancia a `SMA200` es `< -3%`.
- `-1` si `Cruces SMA50 > 4`.
- `-1` si `ATR% 21d > 2,5%`.
- `FAVORABLE` si `score >= 2`.
- `MIXTO` si `score = 0 o 1`.
- `PROBLEMATICO` si `score <= -1`.

### Especificación C

Variables:

- `QQQ > SMA200`
- `Distancia a SMA200`
- `Cruces SMA50`
- `ATR% 21d`
- `Retorno 63` solo como apoyo secundario

Base igual que la especificación B, con un uso deliberadamente secundario de `Retorno 63`:

- primero se calcula la clase base de B;
- solo si la salida base es `MIXTO`, se permite a `Retorno 63` desempatar:
  - si el `score` base es `1` y `Retorno 63 > +3%`, la clase sube a `FAVORABLE`;
  - si el `score` base es `0` y `Retorno 63 < -5%`, la clase baja a `PROBLEMATICO`.

Esto preserva la condición de que el retorno intermedio sea un apoyo secundario y no el núcleo principal de la decisión.

## 3. Metodología de comparación

### Datos y frecuencia

Se utilizó `datos/QQQ.csv` del repositorio y se reconstruyeron las variables directamente sobre la serie diaria de `QQQ`, sin modificar código de producción.

La comparación se hizo con revisión **semanal** sobre cierres de los lunes, para mantener coherencia con la lógica ya descrita en `ANALISIS 57` y evitar un selector excesivamente nervioso.

### Periodo auditable

El periodo comparado va de `2014` a `2026-03-02`, una vez disponibles `SMA200`, `Retorno 63`, `Cruces SMA50` y `ATR% 21d` con suficiente historial.

### Métricas mínimas auditadas

Se compararon las tres especificaciones por:

- distribución de clases;
- número de cambios de clase por año;
- estabilidad del bloque `2020–2025`;
- tratamiento de `2015`, `2016`, `2022` y `2026`;
- tamaño relativo de la clase `MIXTO`;
- complejidad relativa e interpretabilidad.

### Regla de lectura

No se optimizaron umbrales finos para hacer encajar años concretos. Los umbrales usados se mantuvieron deliberadamente simples y auditables, buscando una comparación estructural entre especificaciones rivales, no una búsqueda oportunista del mejor ajuste ex post.

## 4. Resultados por especificación

### 4.1. Distribución global y cambios de clase

| Especificación | FAVORABLE | MIXTO | PROBLEMATICO | Cambios medios/año 2020–2025 |
|---|---:|---:|---:|---:|
| A | 57,5% | 27,4% | 15,0% | 8,0 |
| B | 71,7% | 11,4% | 17,0% | 4,7 |
| C | 76,7% | 6,1% | 17,1% | 4,0 |

### 4.2. Estabilidad y distribución en 2020–2025

| Especificación | FAVORABLE | MIXTO | PROBLEMATICO | Cambios totales 2020–2025 |
|---|---:|---:|---:|---:|
| A | 58,7% | 22,8% | 18,5% | 48 |
| B | 69,8% | 9,3% | 21,0% | 28 |
| C | 74,0% | 4,6% | 21,4% | 24 |

Lectura inicial:

- `A` es la más móvil, pero también la que conserva una zona intermedia material.
- `B` y `C` son más estables en número de cambios, pero lo logran a costa de comprimir mucho `MIXTO` y expandir con fuerza `FAVORABLE`.
- En términos de investigación, menos cambios no equivale automáticamente a mejor estabilidad si la clasificación se vuelve demasiado binaria y pierde matiz histórico.

### 4.3. Tratamiento de años y tramos críticos

| Especificación | 2015 | 2016 | 2022 | 2026* |
|---|---|---|---|---|
| A | 31,2% F / 54,2% M / 14,6% P; 19 cambios | 39,1% F / 37,0% M / 23,9% P; 14 cambios | 4,4% F / 13,3% M / 82,2% P; 7 cambios | 14,3% F / 85,7% M / 0,0% P; 2 cambios |
| B | 64,6% F / 20,8% M / 14,6% P; 10 cambios | 50,0% F / 17,4% M / 32,6% P; 11 cambios | 4,4% F / 2,2% M / 93,3% P; 3 cambios | 85,7% F / 14,3% M / 0,0% P; 2 cambios |
| C | 79,2% F / 6,2% M / 14,6% P; 5 cambios | 56,5% F / 10,9% M / 32,6% P; 11 cambios | 4,4% F / 2,2% M / 93,3% P; 3 cambios | 85,7% F / 14,3% M / 0,0% P; 2 cambios |

`* 2026` solo es observación parcial hasta `2026-03-02`.

### 4.4. Resultado interpretativo por especificación

#### Especificación A

- reproduce casi exactamente la fotografía ya observada en `ANALISIS 57`;
- mantiene una clase `MIXTO` suficientemente grande como para absorber transiciones reales;
- trata `2015` y `2016` como años incómodos y mezclados, no como años claramente sanos;
- reconoce `2022` como predominantemente `PROBLEMATICO` sin volver todo lo demás un binario rígido;
- deja `2026` en observación mayoritariamente `MIXTO`, que parece una salida prudente para un tramo parcial y todavía ambiguo.

#### Especificación B

- gana estabilidad mecánica clara frente a A;
- pero desplaza demasiados periodos hacia `FAVORABLE`;
- reduce `MIXTO` hasta un tamaño pequeño para el tipo de taxonomía que se busca;
- reinterpreta `2015` como mayoritariamente favorable, algo difícil de defender si se prioriza coherencia histórica;
- convierte el arranque parcial de `2026` en mayoritariamente favorable, una lectura más agresiva de la deseable en esta fase.

#### Especificación C

- es la más estable en recuento de cambios y la más afirmativa en la expansión de `FAVORABLE`;
- al usar `Retorno 63` como desempate, apenas recupera matiz: más bien acelera la salida de `MIXTO`;
- deja `2015` casi “blanqueado” como favorable, lo que debilita su credibilidad histórica;
- mantiene `2022` muy bien capturado como `PROBLEMATICO`, pero esa virtud ya estaba en A y B;
- el coste principal es que casi vacía la clase intermedia, reduciendo la utilidad de la taxonomía de tres estados.

## 5. Ventajas y debilidades de cada una

### A

**Ventajas**

- máxima simplicidad entre las tres;
- continuidad documental directa con `ANALISIS 57`;
- `MIXTO` conserva un papel real;
- mejor equilibrio entre prudencia y capacidad descriptiva;
- muy fácil de explicar: estructura, retorno intermedio y serrucho.

**Debilidades**

- cambia más de clase que B y C;
- puede resultar algo más nerviosa en tramos grises;
- usa menos información que B y C sobre estrés y sobreextensión estructural.

### B

**Ventajas**

- incorpora explícitamente dos dimensiones defendidas en `ANALISIS 56`: sobreextensión (`distancia a SMA200`) y estrés (`ATR% 21d`);
- reduce claramente el número de cambios de clase;
- endurece la lectura de `2022` sin necesidad de complicar demasiado la lógica.

**Debilidades**

- aumenta la complejidad respecto a A;
- encoge demasiado `MIXTO`;
- trata `2015` y el inicio de `2026` de forma excesivamente favorable;
- resulta algo menos intuitiva porque combina estructura, desplazamiento, ruido y estrés en una sola suma mínima.

### C

**Ventajas**

- mantiene las dimensiones de B y añade un apoyo secundario de momento intermedio;
- es la más estable por cambios totales;
- refuerza la convicción de clasificación cuando el caso base está cerca del borde.

**Debilidades**

- es la menos parsimoniosa de las tres;
- el apoyo secundario de `Retorno 63` apenas mejora la coherencia histórica y sí reduce todavía más `MIXTO`;
- se acerca demasiado a una clasificación casi binaria;
- su facilidad de explicación empeora: ya no basta con decir “estructura + ruido + estrés”, sino también explicar por qué el retorno solo desempata algunos casos.

## 6. Tratamiento de años y tramos críticos

### 2015

`2015` es una prueba importante porque no fue un año uniformemente desastroso, pero sí claramente incómodo y serruchoso. Aquí:

- `A` lo trata como mayoritariamente `MIXTO`, con un núcleo `PROBLEMATICO` visible y una porción menor `FAVORABLE`; esta lectura parece la más disciplinada.
- `B` lo desplaza a mayoría `FAVORABLE`, lo que parece demasiado benevolente.
- `C` lo desplaza todavía más a `FAVORABLE`, lo que debilita bastante su credibilidad.

### 2016

`2016` también exige una lectura híbrida. Aquí:

- `A` reparte mejor entre `FAVORABLE`, `MIXTO` y `PROBLEMATICO`.
- `B` y `C` reconocen parte del problema, pero vuelven a sobrerrepresentar `FAVORABLE`.

### 2022

`2022` es el caso crítico de daño estructural. Las tres variantes lo capturan bien como `PROBLEMATICO`, pero con matices:

- `A` deja todavía una franja pequeña de `MIXTO`, lo cual puede ser razonable para rebotes y transiciones dentro del año.
- `B` y `C` lo endurecen aún más, pero la mejora práctica sobre A es modesta, porque A ya resolvía este año de manera convincente.

### 2026

`2026` debe tratarse con cautela por ser parcial. Aquí la diferencia es importante:

- `A` lo deja principalmente en `MIXTO`, lo que encaja mejor con la regla de no usar un año parcial como ancla narrativa.
- `B` y `C` lo convierten en mayoritariamente `FAVORABLE`, una lectura más agresiva y menos prudente para un tramo todavía corto.

## 7. Papel de la clase MIXTO

La comparación deja una conclusión muy clara: la principal diferencia real entre A, B y C no está en `2022`, sino en el tamaño y la función de `MIXTO`.

| Especificación | Tamaño de MIXTO |
|---|---:|
| A | 27,4% |
| B | 11,4% |
| C | 6,1% |

Interpretación:

- `A` conserva una clase intermedia con peso suficiente para representar transiciones, serrucho y ambigüedad disciplinada.
- `B` ya comprime bastante `MIXTO`; empieza a parecer que muchos tramos se fuerzan hacia un juicio fuerte.
- `C` casi vacía `MIXTO`; eso reduce la honestidad descriptiva de una taxonomía que precisamente nació para evitar el binario artificial.

Por tanto, si el propósito del selector sigue siendo **investigación** y no activación operativa, `MIXTO` no debe minimizarse agresivamente. Debe existir con tamaño suficiente para expresar incertidumbre real sin devorar todo el histórico. En esta comparación, A es la única que mantiene ese equilibrio de forma convincente.

## 8. Comparación de complejidad e interpretabilidad

| Especificación | Complejidad relativa | Interpretabilidad | Facilidad de explicación | Utilidad para investigación |
|---|---|---|---|---|
| A | Baja | Muy alta | Muy alta | Alta |
| B | Media | Alta | Media-Alta | Media-Alta |
| C | Media-Alta | Media | Media | Media |

### Lectura cualitativa

- `A` es la más fácil de auditar y justificar. Además, si falla, se sabrá con claridad en qué dimensión falla.
- `B` añade riqueza descriptiva, pero ya obliga a explicar mejor la interacción entre estructura, distancia y estrés.
- `C` no aporta un salto proporcional a su complejidad adicional: más bien convierte la lógica en menos transparente sin una ganancia clara en utilidad histórica.

## 9. Conclusión final

La comparación sugiere que la **especificación A** ofrece el mejor equilibrio global entre coherencia histórica, estabilidad suficiente, simplicidad, interpretabilidad y utilidad para investigación posterior.

El resultado importante no es que A sea la más estable en términos mecánicos; no lo es. Lo relevante es que:

- conserva una clase `MIXTO` útil y no residual;
- trata `2015` y `2016` con prudencia razonable;
- reconoce `2022` como claramente `PROBLEMATICO`;
- evita leer `2026` de forma demasiado triunfalista;
- sigue siendo la variante más simple de entender, auditar y discutir.

`B` y `C` mejoran la estabilidad aparente en número de cambios, pero lo hacen comprimiendo demasiado la ambigüedad histórica. Para la fase actual, eso parece un coste demasiado alto. En especial, `C` añade un quinto elemento lógico para obtener una ganancia marginal pequeña y con bastante riesgo de sobreafirmación retrospectiva.

## 10. Recomendación: A / B / C / ninguna suficientemente convincente

**Recomendación final: A.**

Justificación resumida:

- es la más parsimoniosa;
- mantiene la mejor función para `MIXTO`;
- es suficientemente robusta sin volverse excesivamente rígida;
- no depende de “ganar” un año aislado;
- deja abierta la puerta a estudiar después si distancia a `SMA200` y `ATR% 21d` merecen entrar más adelante, pero sin necesidad de incorporarlos ya como núcleo de la especificación mínima rival preferida.

En consecuencia, si hay que elegir hoy una especificación mínima rival como referencia conceptual para seguir investigando el selector, la candidata más convincente es **A**.
