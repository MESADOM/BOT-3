# VERSION 2.2.1 ANALISIS 13

## 1. Objetivo

Evaluar alternativas **controladas** a la dependencia rígida de la condición `SMA50 < SMA200` para autorizar entradas short en la versión 2.2.1, con el fin de estudiar si el módulo short está llegando demasiado tarde a caídas relevantes y si existe alguna forma prudente de anticipar parte de esa captura **sin tocar la lógica long, sin tocar producción y sin abrir una optimización masiva**.

El punto de partida es la base short vigente de la 2.2.1:

- `QQQ < SMA200`
- `SMA50 < SMA200`
- `retorno_63 < -0.08`
- `cruces_sma50_ventana < 4`
- confirmación short de 1 día
- trailing stop short del 8%

## 2. Hipótesis de trabajo

1. El análisis 08 ya mostró que el bloqueo dominante en varios falsos negativos fue `SMA50 >= SMA200`, incluso cuando ya existía debilidad táctica o incluso `meta_regimen=SHORT_TREND`.
2. El análisis 07 también mostró que abrir shorts demasiado tarde en caídas maduras eleva el riesgo de rebote técnico y falsos positivos.
3. Por tanto, la hipótesis útil no es “quitar el cruce y listo”, sino probar si existe una **autorización temprana estrechamente acotada** que:
   - reduzca parte de los falsos negativos del análisis 08;
   - no dispare demasiado el ruido que el análisis 07 ya identificó;
   - mantenga una contribución short razonable dentro del sistema completo.
4. Si al relajar el bloqueo estructural mejora la captura aparente pero el coste en ruido empeora claramente el sistema global, debe concluirse sin rodeos que la relajación **no compensa**.

## 3. Variantes probadas

Se comparó la base 2.2.1 frente a tres variantes pequeñas, interpretables y deliberadamente prudentes.

### Variante A — Base 2.2.1
Se mantiene el filtro estructural completo actual, incluida la exigencia de `SMA50 < SMA200`.

### Variante B — Excepción controlada en caída rápida
Se permite short sin exigir cruce completo si se cumple simultáneamente:

- `QQQ < SMA200`
- `retorno_63 < -0.04`
- `cruces_sma50_ventana < 2`
- distancia `QQQ` vs `SMA50` entre `-15%` y `-5%`
- separación `SMA50` vs `SMA200` no superior a `+11%`

Interpretación: intentar no esperar al cruce completo cuando ya hay aceleración bajista real, pero evitando serrucho y evitando precios todavía pegados a `SMA50`.

### Variante C — Debilidad estructural alternativa
Se permite short sin cruce completo si se cumple simultáneamente:

- `QQQ < SMA200`
- `retorno_63 < -0.09`
- `cruces_sma50_ventana < 2`
- distancia `QQQ` vs `SMA50` entre `-11%` y `-3%`
- `SMA50` todavía puede seguir por encima de `SMA200`, pero solo hasta un máximo de `+3%`

Interpretación: usar como sustituto del cruce completo una **proximidad estructural** entre medias, exigiendo además momentum bajista suficientemente claro.

### Variante D — Combinación momentum + tendencia sin cruce completo
Se permite short sin cruce completo si se cumple simultáneamente:

- `QQQ < SMA200`
- `retorno_63 < -0.08`
- `cruces_sma50_ventana < 2`
- distancia `QQQ` vs `SMA50` entre `-10%` y `-3%`
- separación `SMA50` vs `SMA200` no superior a `+6%`

Interpretación: autorizar antes que la base cuando ya coinciden sesgo bajista, momentum negativo y una transición estructural avanzada, aunque todavía no exista el cruce `SMA50 < SMA200`.

## 4. Justificación de cada variante

### Base 2.2.1
Se usa como control porque ya sabemos por análisis previos que el short actual aporta valor defensivo, aunque llega tarde a varias caídas y no mejora la rentabilidad total del sistema.

### Excepción controlada en caída rápida
Ataca directamente el patrón del análisis 08: crashes o tramos de caída en los que `QQQ` ya va claramente por debajo de medias, pero `SMA50 < SMA200` todavía no ha llegado. Se restringe con `cruces < 2` y una ventana acotada de extensión bajo `SMA50` para evitar abrir shorts en cualquier desplome indiscriminado.

### Debilidad estructural alternativa
Busca una alternativa más conservadora que la caída rápida: no elimina la lectura estructural, sino que sustituye el cruce confirmado por una **casi-convergencia** `SMA50`–`SMA200`. La idea es capturar transiciones bajistas que ya están muy cerca del deterioro completo, pero un poco antes.

### Momentum + tendencia sin cruce completo
Es una solución intermedia. Exige más cercanía estructural que la excepción de caída rápida, pero menos rigidez que la base. Intenta combinar debilidad direccional y contexto bajista sin esperar al cruce definitivo.

## 5. Resultados comparativos

### 5.1 Tabla comparativa principal

> Nota metodológica: el “Sharpe o equivalente” usado aquí es un **Sharpe equivalente a nivel de trades cerrados**, calculado sobre la serie de retornos por operación. Se utiliza esta métrica comparable porque para estas variantes no existía una curva diaria persistida previa como en el análisis 10.

| Variante | Retorno total sistema % | Beneficio neto € | Drawdown % | Sharpe equivalente | Profit factor | Nº trades short | Falsos negativos | Falsos positivos | Contribución short € | Peso short sobre PnL total % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base 2.2.1 | 2096.28 | 20962.83 | -28.49 | 3.749 | 4.776 | 11 | 9 | 4 | 3528.27 | 16.83 |
| Excepción controlada en caída rápida | 1169.76 | 11697.63 | -36.46 | 2.558 | 2.484 | 20 | 8 | 12 | -1799.48 | -15.38 |
| Debilidad estructural alternativa | 1861.50 | 18615.03 | -28.49 | 3.269 | 3.597 | 13 | 8 | 6 | 1500.66 | 8.06 |
| Momentum + tendencia sin cruce | 1840.63 | 18406.26 | -22.06 | 3.459 | 3.346 | 15 | 8 | 6 | 855.24 | 4.65 |

### 5.2 Variación frente a la base 2.2.1

| Variante | Delta beneficio neto € | Delta drawdown pts | Delta Sharpe eq | Delta profit factor | Delta trades short | Delta falsos negativos | Delta falsos positivos | Delta contribución short € |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Excepción controlada en caída rápida | -9265.20 | -7.97 | -1.191 | -2.292 | +9 | -1 | +8 | -5327.75 |
| Debilidad estructural alternativa | -2347.80 | 0.00 | -0.480 | -1.179 | +2 | -1 | +2 | -2027.61 |
| Momentum + tendencia sin cruce | -2556.57 | +6.43 | -0.290 | -1.430 | +4 | -1 | +2 | -2673.03 |

## 6. Cambios en falsos negativos y falsos positivos

### 6.1 Falsos negativos

La referencia para falsos negativos fue la lista consolidada en el análisis 08: **9 caídas relevantes sin short real**.

Resultado:

- La base sigue dejando fuera las 9 de 9.
- Las tres variantes solo consiguen reducir la cifra de `9` a `8`.
- En todos los casos, la única caída relevante previamente no capturada que pasó a tener algún short fue la venta de **2025-02-19 a 2025-04-08**.
- Ninguna variante consiguió capturar de forma útil el crash de **2020-02-19 a 2020-03-16**, que era uno de los casos más importantes si el objetivo era anticipar un desplome realmente severo.

### 6.2 Falsos positivos

- Base 2.2.1: `4` shorts perdedores.
- Excepción controlada en caída rápida: `12` shorts perdedores.
- Debilidad estructural alternativa: `6` shorts perdedores.
- Momentum + tendencia sin cruce: `6` shorts perdedores.

Es decir:

- la mejora en captura aparente fue solo de **1 falso negativo menos**;
- el coste en ruido fue de **+2** a **+8 falsos positivos adicionales**.

### 6.3 Lectura separada: captura aparente vs coste en ruido

#### Mejoras aparentes en captura
- Sí, existe una señal de que relajar `SMA50 < SMA200` puede abrir antes en algún tramo como `2025-02/04`.
- Esa mejora existe, pero fue **muy pequeña**: solo 1 caso adicional sobre los 9 falsos negativos ya identificados.

#### Coste en ruido
- La excepción de caída rápida convirtió el bloque short en un generador neto de pérdidas.
- Las otras dos variantes no llegaron a destruir el short, pero sí recortaron fuertemente su utilidad.
- El patrón dominante de ruido volvió a ser compatible con lo ya visto en el análisis 07: entrar antes no necesariamente mejora el timing; a menudo solo adelanta el rebote en contra.

#### Impacto real sobre el sistema global
- Todas las variantes empeoraron el beneficio neto del sistema completo frente a la base.
- Solo la variante `Momentum + tendencia sin cruce` mejoró drawdown de forma visible, pero lo hizo a costa de un recorte importante del retorno y de una caída severa de la contribución short.
- Ninguna variante mejoró simultáneamente captura, ruido y resultado global.

## 7. Riesgos de sobreajuste

1. La muestra short sigue siendo pequeña.
   - La base trabaja con 11 shorts; mover 2–4 trades ya altera bastante las métricas.
2. Las tres variantes se han diseñado para ser interpretables, pero siguen naciendo de patrones observados en un histórico concreto.
3. El hecho de que todas terminen capturando sobre todo el tramo 2025 y no el crash 2020 sugiere que hay riesgo de estar ajustando excepciones a episodios parciales, no a una mejora robusta del comportamiento general.
4. La aparente mejora de drawdown en la variante `Momentum + tendencia sin cruce` podría seducir si se mira aislada, pero sería peligroso convertirla en “ganadora” porque empeora retorno, profit factor y aportación short.
5. El análisis no pretende declarar un nuevo ganador; solo medir el coste real de aflojar el bloqueo estructural.

## 8. Conclusión final

La evidencia de este análisis apunta a que **sí hay una intuición correcta detrás de cuestionar la rigidez de `SMA50 < SMA200`**: la base 2.2.1 probablemente llega tarde a algunas caídas relevantes y, en efecto, las variantes probadas logran abrir antes en al menos un tramo que la base no capturaba.

Pero el resultado cuantitativo es claro: **relajar ese bloqueo estructural empeora el sistema**.

- La mejora de captura fue mínima: solo `1` falso negativo menos.
- El coste en ruido fue alto: entre `+2` y `+8` falsos positivos.
- Las tres variantes redujeron el beneficio neto del sistema completo.
- La variante más agresiva convirtió incluso la contribución short en negativa.
- La variante más “presentable” en drawdown (`Momentum + tendencia sin cruce`) también pierde demasiado retorno y demasiado valor short para justificar su adopción.

Dicho sin rodeos: **en esta prueba, aflojar la dependencia de `SMA50 < SMA200` no resolvió el problema de llegar tarde; solo compró un poco de captura adicional al precio de bastante más ruido**.

## 9. Recomendación: prometedor / frágil / descartar

### Excepción controlada en caída rápida
**Recomendación: descartar.**

Captura algo más, pero el ruido adicional es excesivo, el drawdown empeora y el short pasa a restar valor al sistema.

### Debilidad estructural alternativa
**Recomendación: frágil.**

Es más prudente que la variante de caída rápida, pero la mejora real sigue siendo mínima y el deterioro de beneficio, profit factor y contribución short sigue siendo demasiado claro.

### Momentum + tendencia sin cruce
**Recomendación: frágil.**

Es la menos mala de las relajaciones probadas por su mejora de drawdown, pero esa mejora no compensa la pérdida de retorno ni la caída de la aportación short. No hay base suficiente para promoverla.

### Balance final
**Recomendación global del análisis 13: descartar, por ahora, la relajación directa de `SMA50 < SMA200` como solución principal.**

Si se quiere seguir investigando el problema de “llegar tarde”, la evidencia de esta ronda sugiere que el siguiente paso no debería ser abrir shorts antes de forma más laxa, sino trabajar sobre un filtro que diferencie mejor entre:

- caída temprana con continuidad real;
- caída tardía vulnerable a rebote técnico.

Ese problema parece más cercano a **calidad del timing** que a simple ausencia de permiso estructural.
