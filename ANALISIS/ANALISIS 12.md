# VERSION 2.2.1 ANALISIS 12

## 1. Objetivo

Diseñar, probar y evaluar una batería pequeña de filtros anti-sobreextensión para la pata **short** de la versión base **2.2.1**, con el fin de estudiar si puede reducirse el problema de **entradas short tardías dentro de caídas ya demasiado extendidas**, **sin tocar producción**, **sin modificar la lógica long** y **sin declarar todavía una nueva versión ganadora**.

## 2. Hipótesis de trabajo

La hipótesis de partida, alineada con los análisis previos, fue la siguiente:

1. La versión short 2.2.1 ya filtra razonablemente el serrucho y el contexto bajista estructural.
2. Su debilidad principal no parece ser el exceso de entradas en lateral, sino el hecho de que todavía puede entrar **demasiado tarde** en caídas maduras.
3. Un filtro simple de **sobreextensión previa** podría mejorar la calidad de algunas entradas short, sobre todo reduciendo falsos positivos asociados a rebotes técnicos.
4. La mejora, si existe, probablemente será **local** y sensible al umbral elegido, por lo que debe leerse con prudencia.

## 3. Variantes probadas

Se mantuvo intacta la lógica short base de la 2.2.1 y solo se añadió, antes de la entrada, un filtro extra por variante.

### Base de comparación
- **Base 2.2.1**: sin filtro anti-sobreextensión adicional.

### Variante A — Distancia a SMA50
- **Regla exacta**: bloquear la entrada short si, en el día de señal, `QQQ / SMA50 - 1 <= -7%`.
- **Qué intenta resolver**: evitar ventas cuando el precio ya llega demasiado separado de la media corta y el rebote técnico es más probable.

### Variante B — Distancia a SMA200
- **Regla exacta**: bloquear la entrada short si, en el día de señal, `QQQ / SMA200 - 1 <= -15%`.
- **Qué intenta resolver**: evitar ventas cuando la caída ya está muy hundida también frente a la media larga, no solo frente a la media de 50 sesiones.

### Variante C — Caída acumulada reciente
- **Regla exacta**: bloquear la entrada short si el retorno acumulado de 21 sesiones es `<= -7%`.
- **Qué intenta resolver**: evitar entrar tras un tramo mensual ya demasiado acelerado.

### Variante D — Volatilidad previa excesiva
- **Regla exacta**: bloquear la entrada short si la volatilidad realizada de 21 sesiones anualizada es `>= 40%`.
- **Qué intenta resolver**: evitar contextos previos demasiado violentos, donde el rebote posterior puede barrer el trailing con facilidad.

### Variante E — Combinación simple media + volatilidad
- **Regla exacta**: bloquear la entrada short si `distancia_SMA50 <= -7%` **o** `volatilidad_21d_anualizada >= 40%`.
- **Qué intenta resolver**: combinar una medida de extensión del precio y otra de inestabilidad del contexto sin añadir demasiada complejidad.

## 4. Metodología

### Enfoque
- Se tomó como referencia la lógica short actual definida en **`VERSION 2.2.1 BASE SHORT.md`**.
- No se modificó la pata long.
- No se cambió ninguna regla de producción del motor principal.
- Se probaron solo variantes **simples, interpretables y comparables**.
- No se hizo búsqueda masiva ni optimización agresiva.

### Fuentes priorizadas
- `ANALISIS/ANALISIS 03.md`
- `ANALISIS/ANALISIS 06.md`
- `ANALISIS/ANALISIS 07.md`
- `ANALISIS/ANALISIS 08.md`
- `ANALISIS/ANALISIS 11.md` **no estaba presente en el repositorio**, así que no pudo utilizarse.

### Implementación de prueba
- Se creó un script auxiliar de trabajo, `analysis_12.py`, que:
  - ejecuta el backtest actual;
  - enriquece el dataset diario con métricas extra (`dist_sma50`, `dist_sma200`, `retorno_21_extra`, `vol21_anual`);
  - aplica cada variante como filtro adicional sobre `SORT.permite_entrada`;
  - recalcula resultados completos del sistema para cada variante.

### Métricas comparadas
Para cada variante se midió al menos:
- retorno total del sistema;
- drawdown máximo;
- Sharpe de trade como métrica equivalente de calidad riesgo/retorno;
- profit factor de shorts;
- número de trades short;
- falsos positivos relevantes reducidos;
- falsos negativos relevantes introducidos;
- calidad de captura de los shorts.

### Definiciones operativas usadas en esta comparación
- **Falsos positivos relevantes reducidos**: trades short perdedores de la base que desaparecen en la variante.
- **Falsos negativos relevantes**: trades short ganadores de la base que desaparecen por la variante.
- **Calidad de captura**: lectura cualitativa del impacto del filtro sobre el timing y sobre la sustitución de entradas; adicionalmente se observó el ratio medio de captura favorable por trade, pero se priorizó la interpretación de casos concretos porque la muestra short es pequeña.

## 5. Resultados comparativos

### Tabla resumen

| Variante | Regla resumida | Retorno total sistema | Drawdown máx | Sharpe (trade) | Profit factor short | Nº trades short | Lectura rápida |
|---|---|---:|---:|---:|---:|---:|---|
| Base 2.2.1 | Sin filtro extra | 2096,28% | -28,49% | 3,749 | 4,645 | 11 | Referencia |
| A - SMA50 | bloquear si dist. SMA50 <= -7% | 2134,37% | -28,49% | 3,817 | 5,370 | 10 | Mejora moderada |
| B - SMA200 | bloquear si dist. SMA200 <= -15% | 2196,58% | -28,49% | 3,872 | 10,257 | 9 | Mejor resultado puntual |
| C - caída 21d | bloquear si retorno 21d <= -7% | 2087,31% | -28,03% | 3,731 | 4,047 | 11 | Sin mejora real |
| D - volatilidad 21d | bloquear si vol 21d >= 40% | 2027,43% | -28,49% | 3,666 | 6,618 | 10 | Empeora el sistema |
| E - combinación | bloquear si dist. SMA50 <= -7% o vol >= 40% | 2072,27% | -28,49% | 3,733 | 11,906 | 9 | Mejora local, no global |

### Lectura detallada por variante

#### Variante A — Distancia SMA50
- Mejora el retorno total del sistema frente a la base.
- Mejora Sharpe y profit factor short.
- Reduce algunos shorts perdedores claros, pero desplaza el timing de varias entradas.
- El problema es que la mejora no es limpia: elimina un ganador base (`2022-03-03`) y sigue dejando un caso muy débil en 2025, solo que algo más tarde y con peor resultado (`2025-04-17`, `-867,50 €`).

#### Variante B — Distancia SMA200
- Es la variante con mejor resultado agregado en esta batería.
- Mantiene el drawdown del sistema y mejora retorno total, Sharpe y profit factor short.
- Elimina dos perdedores relevantes de la base (`2022-10-19` y `2022-11-09`).
- A cambio, elimina un ganador pequeño (`2022-07-07`) y sustituye parte del timing por una entrada posterior rentable (`2022-10-25`, `+563,50 €`).
- Aun así, **no** corrige el caso `2025-04-15`, por lo que no resuelve de forma general el problema del short tardío.

#### Variante C — Caída reciente 21d
- No aporta mejora robusta.
- Reduce algo el drawdown, pero empeora retorno total, Sharpe y profit factor short frente a la base.
- Solo elimina un perdedor pequeño de la base (`2016-02-08`) y sacrifica ganadores o desplaza entradas útiles.
- Conclusión local: la caída de 21 días, aislada, no parece separar bien los shorts tardíos de los shorts útiles.

#### Variante D — Volatilidad previa
- Mejora el profit factor short, pero el sistema total empeora.
- Filtra el caso débil de `2025-04-15`, pero también se carga un ganador importante de la base (`2022-06-01`) y lo reemplaza por una entrada mucho más pobre (`2022-06-16`, `+24,00 €`).
- Lectura: la volatilidad previa captura parte del exceso, pero castiga demasiado contextos bajistas válidos.

#### Variante E — Combinación simple
- Reduce varios perdedores base y dispara el profit factor short.
- Sin embargo, también elimina demasiados trades válidos y el retorno total del sistema queda por debajo de la base.
- La combinación es útil como evidencia de dirección, pero en esta muestra **sobrefiltra**.

## 6. Impacto sobre falsos positivos y timing de entrada

### Base 2.2.1: problema observado
Los falsos positivos relevantes de la base seguían concentrándose en shorts abiertos tarde dentro de caídas maduras, especialmente en:
- `2022-10-19`;
- `2022-11-09`;
- `2025-04-15`.

### Qué consiguió reducir cada variante
- **Variante A (SMA50)**:
  - reduce `2022-10-19`, `2022-11-09` y `2025-04-15`;
  - pero introduce una nueva entrada tardía todavía peor en `2025-04-17`.
- **Variante B (SMA200)**:
  - reduce `2022-10-19` y `2022-11-09`;
  - no reduce `2025-04-15`.
- **Variante C (caída 21d)**:
  - apenas reduce un perdedor menor y no ataca los casos principales.
- **Variante D (volatilidad)**:
  - sí reduce `2025-04-15`,
  - pero deteriora demasiado el bloque ganador de 2022.
- **Variante E (combinación)**:
  - limpia varios falsos positivos,
  - pero a costa de perder demasiada captura bajista válida.

### Falsos negativos relevantes detectados
- **Variante A**: elimina el ganador base `2022-03-03`.
- **Variante B**: elimina el ganador pequeño `2022-07-07`.
- **Variante C**: elimina o desplaza ganadores de `2018-12-12` y `2022-07-07`.
- **Variante D**: elimina el ganador importante `2022-06-01`.
- **Variante E**: elimina `2022-03-03`, `2022-06-01` y `2022-07-07`.

### Calidad de captura de los shorts
La lectura cualitativa del timing fue más útil que cualquier métrica única de captura, porque al añadir filtros cambian las fechas de entrada y la composición de la muestra.

Patrones observados:
- Los filtros basados en **distancia a medias** son los que mejor mejoran el timing en esta batería.
- El filtro de **SMA200** fue el que mejor evitó entrar en varios shorts demasiado degradados **sin destruir demasiada captura buena**.
- El filtro de **volatilidad** y la **combinación** muestran que sí existe señal anti-sobreextensión, pero todavía demasiado tosca para adoptarla tal cual.
- Ninguna variante evitó de forma consistente **todos** los shorts tardíos problemáticos.

## 7. Riesgos de sobreajuste

Los riesgos de sobreajuste son altos y deben declararse explícitamente:

1. **Muestra short pequeña**: la base solo tiene 11 trades short reales, así que cambios de 1 o 2 operaciones alteran mucho las métricas.
2. **Umbrales sensibles**: un umbral simple como `-15%` frente a `SMA200` puede parecer muy bueno en esta muestra y dejar de serlo fácilmente fuera de muestra.
3. **Dependencia de sustitución temporal**: algunas mejoras no vienen solo de eliminar trades malos, sino de desplazar entradas a otra fecha mejor dentro del mismo tramo.
4. **No hay validación fuera de muestra separada** en este análisis.
5. **No hubo búsqueda masiva**, lo cual era una regla correcta para esta tarea, pero también implica que las conclusiones son exploratorias y no definitivas.

## 8. Conclusión final

Sí hay evidencia de que **un filtro anti-sobreextensión simple puede mejorar localmente la calidad de entrada short** en la versión 2.2.1, especialmente cuando el filtro se basa en la **distancia del precio a la SMA200**.

Sin embargo, la mejora **no parece todavía lo bastante robusta** como para considerarla definitiva:
- la muestra de shorts es pequeña;
- varias mejoras dependen de desplazar el timing de entradas concretas;
- ninguna variante resuelve de forma limpia todos los casos tardíos problemáticos;
- algunas variantes reducen falsos positivos, pero introducen falsos negativos o degradan la captura de caídas válidas.

La lectura más honesta es esta:
- **sí merece la pena seguir investigando filtros anti-sobreextensión para short**;
- **todavía no hay base suficiente para declarar ganador definitivo**;
- la variante más prometedora de esta batería es la basada en **distancia a SMA200**, pero solo como **candidata a revisión adicional**, no como cambio listo para producción.

Si hubiera que sintetizar el resultado en una sola frase: **hay señal útil, pero todavía no hay robustez suficiente para convertirla en decisión final**.

## 9. Recomendación: seguir / descartar / revisar

### Recomendación final: **revisar**

Lectura por variante:
- **Variante A - SMA50**: **revisar**.
- **Variante B - SMA200**: **seguir revisando**; es la candidata más prometedora de esta batería.
- **Variante C - caída 21d**: **descartar** en su forma actual.
- **Variante D - volatilidad 21d**: **revisar solo como complemento**, no como filtro único.
- **Variante E - combinación**: **revisar**, pero no adoptar tal cual por sobrefiltrado.

Recomendación operativa concreta para el siguiente paso:
- mantener intacta la base 2.2.1 en producción;
- no declarar nueva versión ganadora;
- si se continúa el trabajo, centrar la siguiente iteración en:
  1. una familia muy corta de umbrales alrededor de **distancia a SMA200**;
  2. comprobar si la mejora sigue existiendo sin degradar la captura de 2022;
  3. revisar específicamente el caso `2025-04-15`, que sigue siendo la prueba más incómoda para la hipótesis.
