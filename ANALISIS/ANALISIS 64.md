# VERSION 2.2.2 ANALISIS 64

## 1. Objetivo

Determinar cómo rinde realmente el sistema general `long-short` vigente dentro de cada clase del selector de contexto, para comprobar si la segmentación `FAVORABLE / MIXTO / PROBLEMATICO` tiene valor práctico real y para verificar, de forma explícita, si `PROBLEMATICO` implica siempre mal comportamiento operativo o no.

Este documento:

- **no** toca producción;
- **no** diseña todavía variantes por régimen;
- **no** asume que `PROBLEMATICO` obligue automáticamente a cambiar el sistema;
- cruza la clasificación de régimen con el rendimiento **real** del general vigente.

La pregunta disciplinada es esta: **cuando el sistema general realmente opera, dónde gana, dónde sufre y qué valor práctico aporta la clase del selector para interpretar ese comportamiento**.

---

## 2. Selector y sistema evaluados

### 2.1. Documentos leídos obligatoriamente

Se han leído obligatoriamente:

- `ANALISIS 57.md`
- `ANALISIS 59.md`
- `ANALISIS 60.md`
- `ANALISIS 61.md`
- `ANALISIS 62.md`
- `ANALISIS 63.md`

### 2.2. Selector usado

Tomando la cadena `60–63`, la especificación provisionalmente mejor defendida sigue siendo la **Especificación A** de `ANALISIS 60`: la más simple, más interpretable y la que mejor conserva una clase `MIXTO` con contenido real.

Para mantener coherencia con el sistema general vigente, el cruce se hace sobre el `score_regimen` ya calculado por `META_BOT.py`, que operacionaliza esa misma idea base:

- `+1` si `QQQ > SMA200`;
- `+1` si `Retorno 63` es `POSITIVO`;
- `-1` si `Retorno 63` es `NEGATIVO`;
- `-1` si `Cruces SMA50` es `ALTO`.

Con ese score, la segmentación usada aquí es:

- **FAVORABLE** si `score >= 2`;
- **MIXTO** si `score = 0` o `1`;
- **PROBLEMATICO** si `score <= -1`.

### 2.3. Sistema evaluado

Se evalúa el **sistema general long-short vigente** de `META_BOT.py`, sin modificar reglas, sin introducir filtros nuevos y sin ramificar estrategias por régimen.

Punto metodológico importante:

- en el sistema vigente, las operaciones que nacen en `FAVORABLE` y `MIXTO` son de la pata **long**;
- las operaciones que nacen en `PROBLEMATICO` son de la pata **short**.

Por tanto, este análisis **no** mide una estrategia distinta por clase, sino cómo el sistema general actual acaba rindiendo cuando sus trades quedan clasificados por la clase del selector en el momento de entrada.

---

## 3. Segmentación por clases

### 3.1. Peso temporal del selector

Sobre `4.198` sesiones auditables con variables completas del selector, el reparto temporal queda así:

| Clase | Sesiones | Peso temporal |
|---|---:|---:|
| FAVORABLE | 2.419 | 57,6% |
| MIXTO | 1.159 | 27,6% |
| PROBLEMATICO | 620 | 14,8% |

### 3.2. Reparto de trades del sistema general por clase

El sistema general genera `67` operaciones cerradas en total. Repartidas por clase del selector en la entrada:

| Clase | Nº trades | % trades |
|---|---:|---:|
| FAVORABLE | 28 | 41,8% |
| MIXTO | 30 | 44,8% |
| PROBLEMATICO | 9 | 13,4% |

Primera lectura:

- `FAVORABLE` domina en tiempo, pero **no** domina en número de trades de forma aplastante.
- `MIXTO`, aun ocupando solo el `27,6%` del tiempo, concentra el mayor número de trades (`30`).
- `PROBLEMATICO` ocupa poco tiempo y pocos trades, pero no es irrelevante: ahí entran los episodios short del sistema general.

### 3.3. Resultado agregado por clase

Capital inicial del backtest: `1.000 €`.

Resultado total del sistema general: `+21.965,83 €` netos, equivalente a `+2.196,6%`, con drawdown máximo global de `-28,5%`.

Desglose por clase:

| Clase | Retorno acumulado | Drawdown clase | Nº trades | Beneficio medio/trade | Contribución al total |
|---|---:|---:|---:|---:|---:|
| FAVORABLE | `+3.914,95 €` (`+391,5%`) | `-23,9%` | 28 | `+139,82 €` | 17,8% |
| MIXTO | `+13.519,61 €` (`+1.352,0%`) | `-34,8%` | 30 | `+450,65 €` | 61,5% |
| PROBLEMATICO | `+4.531,27 €` (`+453,1%`) | `-7,7%` | 9 | `+503,47 €` | 20,6% |

Lectura inicial muy importante:

- `FAVORABLE` **sí gana**, pero no es donde más gana el sistema.
- `MIXTO` es la clase con **mayor contribución absoluta** y también con drawdown más alto.
- `PROBLEMATICO` **no** equivale a mal resultado operativo: con pocos trades aporta más beneficio medio por trade que `FAVORABLE` y casi tanto como la mejor clase en eficiencia.

---

## 4. Rendimiento del general en FAVORABLE

### 4.1. Métricas

| Métrica | Valor |
|---|---:|
| Retorno acumulado | `+3.914,95 €` |
| Retorno sobre capital inicial | `+391,5%` |
| Drawdown de la curva filtrada | `-23,9%` |
| Nº trades | 28 |
| Beneficio medio por trade | `+139,82 €` |
| Contribución al resultado total | 17,8% |

### 4.2. Lectura

`FAVORABLE` **no concentra por sí sola** los mejores resultados del sistema general. Sí contiene tramos buenos y claramente rentables, pero su papel práctico es más modesto de lo que la intuición podría sugerir.

Esto significa varias cosas:

1. La clase `FAVORABLE` **sí es descriptivamente útil**: el sistema gana en ella.
2. Pero **no es decisiva por sí sola** como sello de “aquí está el grueso del edge”.
3. En el sistema vigente, muchos de los mejores resultados no vienen de los tramos más limpiamente favorables, sino de zonas menos puras o más transicionales.

### 4.3. Juicio operativo provisional

`FAVORABLE` parece describir un contexto razonablemente sano para la pata long, pero **no basta** para concluir que la segmentación ya tenga un uso operativo directo del tipo “solo lo bueno está aquí”.

Dicho de forma simple: `FAVORABLE` ayuda a entender, pero no monopoliza el beneficio del general.

---

## 5. Rendimiento del general en MIXTO

### 5.1. Métricas

| Métrica | Valor |
|---|---:|
| Retorno acumulado | `+13.519,61 €` |
| Retorno sobre capital inicial | `+1.352,0%` |
| Drawdown de la curva filtrada | `-34,8%` |
| Nº trades | 30 |
| Beneficio medio por trade | `+450,65 €` |
| Contribución al resultado total | 61,5% |

### 5.2. Lectura

`MIXTO` no actúa aquí como una bolsa inútil o puramente confusa. Al contrario:

- concentra el mayor beneficio total del sistema general;
- concentra el mayor número de trades;
- y aporta una parte desproporcionada del resultado frente a su peso temporal (`27,6%` del tiempo, pero `61,5%` del beneficio).

Eso sí, este rendimiento viene con una contrapartida clara:

- es también la clase con **mayor drawdown** dentro de la curva segmentada (`-34,8%`).

### 5.3. Interpretación práctica

Esta es una de las conclusiones más relevantes del análisis:

- `MIXTO` **no** parece una clase vacía;
- **sí** funciona como zona donde el sistema general encuentra muchas oportunidades reales;
- pero también es una zona menos limpia, con más tensión y más dispersión en la experiencia operativa.

Por tanto, `MIXTO` se comporta más como **transición útil y productiva** que como simple cajón de sastre. No obstante, esa utilidad no es “limpia”: viene acompañada de una mayor irregularidad de la curva.

---

## 6. Rendimiento del general en PROBLEMATICO

### 6.1. Métricas

| Métrica | Valor |
|---|---:|
| Retorno acumulado | `+4.531,27 €` |
| Retorno sobre capital inicial | `+453,1%` |
| Drawdown de la curva filtrada | `-7,7%` |
| Nº trades | 9 |
| Beneficio medio por trade | `+503,47 €` |
| Contribución al resultado total | 20,6% |

### 6.2. Lectura principal

Esta clase desmonta la hipótesis fuerte de que `PROBLEMATICO` implique siempre mal comportamiento operativo.

De hecho, en el sistema general vigente ocurre lo contrario en varios puntos importantes:

- con solo `9` trades aporta `20,6%` del beneficio total;
- su beneficio medio por trade (`+503,47 €`) es el **más alto** de las tres clases;
- su drawdown segmentado (`-7,7%`) es el **más bajo** de las tres clases.

### 6.3. Qué significa realmente aquí PROBLEMATICO

En el sistema general actual, `PROBLEMATICO` no debe leerse como “entorno donde el sistema siempre falla”, sino más bien como:

- entorno hostil para una lectura long limpia;
- entorno donde la pata short del sistema pasa a ser relevante;
- señal de que el mercado está deteriorado o tensionado, **no** de que el general quede automáticamente inutilizado.

Esto es crucial para la interpretación práctica del selector.

`PROBLEMATICO` sí tiene valor descriptivo: identifica un entorno difícil. Pero **ese entorno difícil para el mercado no equivale necesariamente a un entorno malo para el sistema general long-short**, precisamente porque el sistema dispone de componente short.

### 6.4. Casos donde PROBLEMATICO sigue funcionando razonablemente bien

Sí, existen y no son anecdóticos.

Desglose de `PROBLEMATICO` por año:

| Año | Nº trades | Beneficio neto |
|---|---:|---:|
| 2016 | 2 | `-23,50 €` |
| 2019 | 1 | `+339,28 €` |
| 2022 | 5 | `+4.677,99 €` |
| 2025 | 1 | `-462,50 €` |

Lectura:

- Hay casos flojos (`2016`, `2025`).
- Hay casos razonablemente buenos (`2019`).
- Y hay un caso **extraordinariamente bueno** (`2022`).

Conclusión explícita: **`PROBLEMATICO` no implica automáticamente cambiar el sistema ni implica automáticamente mal resultado operativo**. Es una clase que puede concentrar daño para enfoques largos, pero también puede concentrar parte importante del edge del sistema general cuando el short captura bien ese deterioro.

---

## 7. Caso específico de 2022

### 7.1. Contexto del selector en 2022

En `2022`, el selector clasificó aproximadamente:

- `82,6%` del tiempo como `PROBLEMATICO`;
- `13,2%` como `MIXTO`;
- `4,3%` como `FAVORABLE`.

Es decir, 2022 fue, de forma muy nítida, el gran año `PROBLEMATICO` del histórico reciente.

### 7.2. Resultado del sistema general en 2022 dentro de PROBLEMATICO

Dentro de `PROBLEMATICO`, el sistema general ejecutó en 2022 **5 trades**, todos de la pata short, con este resultado:

| Entrada | Salida | Módulo | Beneficio neto |
|---|---|---|---:|
| 2022-03-03 | 2022-03-11 | SHORT | `+707,71 €` |
| 2022-03-23 | 2022-03-24 | SHORT | `+119,38 €` |
| 2022-04-13 | 2022-05-17 | SHORT | `+2.112,40 €` |
| 2022-06-01 | 2022-06-23 | SHORT | `+1.175,00 €` |
| 2022-10-25 | 2022-11-10 | SHORT | `+563,50 €` |

Resumen 2022 en `PROBLEMATICO`:

| Métrica | Valor |
|---|---:|
| Nº trades | 5 |
| Beneficio neto acumulado | `+4.677,99 €` |
| Beneficio medio por trade | `+935,60 €` |
| Drawdown dentro de ese subconjunto | `0,0%` |

### 7.3. Interpretación explícita sobre 2022

Este es probablemente el hallazgo más importante de todo el documento.

En 2022:

- `PROBLEMATICO` **sí** identificó un entorno históricamente hostil;
- pero eso **no** implicó mal comportamiento del sistema general;
- al contrario, fue uno de los bloques más rentables del histórico precisamente porque el sistema general pudo operar por el lado short.

Por tanto, el caso 2022 obliga a una conclusión muy clara:

> **`PROBLEMATICO` describe dificultad de mercado, pero no equivale automáticamente a inutilidad operativa del sistema general long-short.**

En este sistema, 2022 demuestra que una clase puede ser “problemática” para la estructura del mercado y, aun así, ser **muy explotable** para el general.

---

## 8. Valor práctico real de la segmentación

### 8.1. Qué sí aporta la segmentación

La segmentación sí aporta valor práctico real, pero **más descriptivo que decisorio**.

Aporta porque permite ver que:

- `FAVORABLE` no concentra automáticamente todo lo bueno;
- `MIXTO` no es una clase vacía y, de hecho, concentra gran parte del beneficio del general;
- `PROBLEMATICO` no significa necesariamente “dejar de operar”, ya que puede contener fases muy rentables, especialmente cuando el short funciona.

### 8.2. Qué no permite concluir todavía

La segmentación todavía **no** permite concluir una regla operativa simple del tipo:

- “operar solo en FAVORABLE”, o
- “reducir siempre en PROBLEMATICO”, o
- “tratar MIXTO como ruido”.

Los datos de este cruce van justamente contra esas simplificaciones.

### 8.3. Juicio por clase

#### FAVORABLE
Útil como descriptor de entorno sano, pero **no decisivo** para explicar dónde se genera la mayor parte del resultado.

#### MIXTO
Útil de verdad. No solo como transición conceptual, sino como zona donde el general produce mucho. Eso sí, con más tensión y más drawdown.

#### PROBLEMATICO
Útil como descriptor de estrés o deterioro del mercado, pero **no decisivo en sentido negativo**. Puede coincidir con mal rendimiento en algunos episodios, pero también con muy buen rendimiento operativo del sistema general, especialmente en shocks bajistas bien capturados.

### 8.4. Síntesis metodológica

La clase del selector parece tener **valor práctico para interpretar** el comportamiento del general, pero todavía **no tiene valor suficiente para dictar por sí sola una acción operativa universal**.

En especial:

- `PROBLEMATICO` parece **descriptivo**, no automáticamente prescriptivo;
- `MIXTO` parece más fértil de lo esperado;
- y `FAVORABLE` es útil, pero no es el contenedor exclusivo del buen comportamiento.

---

## 9. Conclusión final

El cruce entre clasificación de régimen y rendimiento real del sistema general deja una conclusión bastante más matizada de la intuición inicial.

### Conclusiones centrales

1. **La segmentación sí tiene valor práctico**, porque distingue contextos con comportamientos distintos del sistema general.
2. **Ese valor es más interpretativo que normativo**: ayuda a entender dónde y cómo gana el sistema, pero no justifica todavía reglas operativas rígidas por clase.
3. **FAVORABLE no concentra de forma dominante los mejores tramos**. Gana, pero no monopoliza el edge.
4. **MIXTO es mucho más importante de lo que parecería**: concentra la mayor parte del beneficio del sistema general, aunque con más drawdown.
5. **PROBLEMATICO no implica automáticamente mal comportamiento operativo**. Esa inferencia queda directamente refutada por los datos.
6. **2022 es el contraejemplo decisivo**: fue claramente `PROBLEMATICO` y, al mismo tiempo, extraordinariamente rentable para el general por la vía short.

### Juicio final sobre PROBLEMATICO

La clase `PROBLEMATICO` debe interpretarse como:

- un entorno de mercado difícil o deteriorado;
- potencialmente hostil para ciertas lecturas;
- pero **no** como una sentencia automática contra el sistema general long-short.

Dicho de la forma más clara posible: **en este sistema, `PROBLEMATICO` puede ser descriptivamente negativo sin ser operativamente negativo**.

---

## 10. Recomendación: segmentación útil operativamente / útil con reservas / todavía insuficiente

### Recomendación final

**Útil con reservas.**

### Motivos

- La segmentación sí ordena mejor la historia operativa del general.
- Permite ver que las tres clases tienen personalidad distinta.
- Refuerza la idea de que `MIXTO` y `PROBLEMATICO` contienen información real y no meros restos del modelo.

Pero al mismo tiempo:

- `FAVORABLE` no concentra por sí sola lo mejor;
- `PROBLEMATICO` no autoriza una decisión automática de retirada o cambio;
- y `MIXTO` sigue siendo muy relevante, lo que impide una lectura binaria simple.

### Recomendación operativa prudente en esta fase

La segmentación **sí merece seguir usándose como herramienta de análisis estructurado**, pero **todavía con reservas** y sin convertirla en una regla de producción ni en un disparador automático de variantes por régimen.

La evidencia de este análisis apoya exactamente una lectura prudente:

- **útil para entender**;
- **útil para investigar**;
- **todavía insuficiente para mandar por sí sola**.
