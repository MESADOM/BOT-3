# VERSION 2.2.1 ANALISIS 14

## 1. Objetivo

Evaluar si pequeñas variaciones de la gestión de salida short alrededor del trailing stop vigente del **8%** pueden **reducir giveback** y **mejorar la eficiencia de captura** sin convertir la salida en una regla excesivamente nerviosa ni rediseñar la lógica short de la versión **2.2.1**.

Este análisis toma como base estricta la configuración vigente de la versión 2.2.1:
- mismas entradas long;
- mismo motor general;
- mismo sizing short;
- mismos filtros estructurales del módulo short;
- única palanca sensibilizada: la gestión de salida short alrededor del trailing actual.

Nota de trazabilidad: la instrucción pedía leer prioritariamente `ANALISIS 11`, `ANALISIS 05` y `ANALISIS 07`. En el repositorio actual **no existe** `ANALISIS/ANALISIS 11.md`, por lo que la priorización real se apoyó en `ANALISIS 05`, `ANALISIS 07`, `ANALISIS 09`, `VERSION 2.2.1 BASE SHORT.md`, `SORT.py` y el motor `META_BOT.py`.

## 2. Hipótesis de trabajo

Hipótesis principal:

> Un ajuste pequeño del trailing short alrededor del 8% podría mejorar la retención del tramo favorable de algunos trades sin degradar demasiado la protección frente a rebotes.

Subhipótesis evaluadas:

1. **Trailing ligeramente más estrecho** (`6%` o `7%`) podría reducir giveback, pero con riesgo de salir antes de tiempo y empeorar la captura de tendencias cortas que todavía no han madurado.
2. **Trailing ligeramente más amplio** (`9%` o `10%`) podría dejar respirar mejor al trade, pero con riesgo de devolver demasiado MFE y empeorar las pérdidas por rebote.
3. **Variante adaptativa simple** solo sería interesante si lograse mejorar algo sin añadir complejidad material ni sensibilidad excesiva.

## 3. Variantes probadas

Todas las variantes se comparan contra la base **2.2.1** con trailing short fijo del **8%**.

### Base 2.2.1
- **Regla exacta:** `stop = mínimo_desde_entrada * (1 + 0.08)`.
- Si `qqq3_close_hoy >= stop`, salida `COVER_TRAILING`.
- Si se pierde la señal short base, salida `COVER_SIGNAL`.

### Variante A — trailing 6%
- **Regla exacta:** igual que la base, sustituyendo `0.08` por `0.06`.
- Interpretación: versión ligeramente más ceñida y más sensible al rebote.

### Variante B — trailing 7%
- **Regla exacta:** igual que la base, sustituyendo `0.08` por `0.07`.
- Interpretación: estrechamiento moderado, todavía en el vecindario del trailing actual.

### Variante C — trailing 9%
- **Regla exacta:** igual que la base, sustituyendo `0.08` por `0.09`.
- Interpretación: ampliación moderada para dejar algo más de aire.

### Variante D — trailing 10%
- **Regla exacta:** igual que la base, sustituyendo `0.08` por `0.10`.
- Interpretación: ampliación simple ya probada en sensibilidad previa, todavía razonablemente cercana al vecindario del 8%.

### Variante E — adaptativa simple 8% -> 7%
- **Regla exacta:**
  - mientras el trade no alcance un avance favorable del **12%** desde entrada, trailing del **8%**;
  - una vez alcanzado un avance favorable de **12% o más**, el trailing se estrecha a **7%**.
- Interpretación: regla muy simple y legible, diseñada para comprobar si tiene sentido apretar algo la protección una vez que el trade ya ha demostrado recorrido favorable suficiente.

### Métricas utilizadas

Para cada variante se midieron:
- retorno total del sistema;
- drawdown máximo del sistema;
- **Sharpe equivalente por trade** del sistema completo (se usa equivalente porque el motor expone de forma directa la secuencia de trades cerrados, no una curva diaria mark-to-market preparada para Sharpe diario);
- nº de trades short;
- duración media de los shorts;
- giveback medio;
- frecuencia de salida por trailing;
- impacto en perdedores por rebote.

Para la captura de MFE se usan dos lecturas:
1. **Lectura principal:** giveback medio, por ser la medida más robusta y directamente comparable con el objetivo de la tarea.
2. **Lectura secundaria:** retención estimada de MFE en trades ganadores. Esta métrica se calculó sobre la serie de cierres dentro del trade y puede verse distorsionada por gaps de ejecución al cierre/apertura; por eso se interpreta solo como apoyo, no como señal decisiva.

## 4. Resultados comparativos

### Tabla principal

| Variante | Regla | Capital final € | Retorno total % | Drawdown máx % | Sharpe eq. | Shorts | Duración media | Giveback medio % | Salidas trailing | Perdedores por rebote | PnL short € |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base 8% | trailing fijo 8% | 21,962.83 | 2,096.28 | -28.4862 | 3.749 | 11 | 11.45 d | 7.01 | 9/11 = 81.82% | 4 | 3,528.27 |
| 6% | trailing fijo 6% | 21,807.83 | 2,080.78 | -28.4862 | 3.730 | 11 | 11.36 d | 7.38 | 9/11 = 81.82% | 5 | 3,373.27 |
| 7% | trailing fijo 7% | 21,962.83 | 2,096.28 | -28.4862 | 3.749 | 11 | 11.45 d | 7.01 | 9/11 = 81.82% | 4 | 3,528.27 |
| 9% | trailing fijo 9% | 21,962.83 | 2,096.28 | -28.4862 | 3.749 | 11 | 11.45 d | 7.01 | 9/11 = 81.82% | 4 | 3,528.27 |
| 10% | trailing fijo 10% | 21,128.16 | 2,012.82 | -31.2385 | 3.574 | 10 | 13.80 d | 9.69 | 9/10 = 90.00% | 4 | 2,944.08 |
| Adaptativa 8%->7% | 8% hasta MFE 12%, luego 7% | 21,962.83 | 2,096.28 | -28.4862 | 3.749 | 11 | 11.45 d | 7.01 | 9/11 = 81.82% | 4 | 3,528.27 |

### Lecturas inmediatas

- **El 8% no fue superado de forma robusta por ninguna variante.**
- **El 6% empeora** el beneficio short y aumenta el número de perdedores por rebote de **4 a 5**, sin mejorar drawdown ni Sharpe.
- **El 7% y el 9% son idénticos a la base** en esta muestra histórica: no cambian trades, salidas ni agregados.
- **El 10% deteriora claramente** retorno total, drawdown, Sharpe equivalente y beneficio short.
- La **adaptativa simple** tampoco aportó diferencia observable frente a la base en el histórico evaluado.

## 5. Impacto en giveback y captura de MFE

### Punto de partida relevante de análisis previos

El análisis 05 ya advertía dos hechos importantes:
- el short de la 2.2.1 sí tenía asimetría favorable;
- pero también mostraba **giveback material** antes de la salida, con el trailing del 8% participando en la mayor parte de los cierres.

La pregunta aquí era si un ajuste pequeño alrededor del 8% conseguía reducir ese giveback sin romper el equilibrio actual.

### Comparativa específica

| Variante | Giveback medio % | Cambio vs base | Lectura de captura |
|---|---:|---:|---|
| 6% | 7.38 | +0.37 | No mejora el giveback agregado; además empeora el PnL short. |
| Base 8% | 7.01 | 0.00 | Punto de referencia. |
| 7% | 7.01 | 0.00 | Sin cambio efectivo frente a base. |
| 9% | 7.01 | 0.00 | Sin cambio efectivo frente a base. |
| 10% | 9.69 | +2.68 | Claramente peor retención del tramo favorable. |
| Adaptativa 8%->7% | 7.01 | 0.00 | No añade mejora observable. |

### Interpretación

1. **No apareció evidencia de que estrechar ligeramente el trailing mejore el giveback.**
   - El `6%`, que era la opción más razonable para intentar reducir devolución, no solo **no reduce** el giveback medio, sino que además **reduce el PnL short agregado**.

2. **Ampliar el trailing a 10% empeora la captura efectiva.**
   - El trade aguanta más tiempo, pero el resultado es más devolución de recorrido favorable y peores métricas agregadas.

3. **El vecindario 7%-9% parece una zona de estabilidad discreta en esta muestra.**
   - En la práctica, `7%`, `8%`, `9%` y la adaptativa simple generan exactamente los mismos cierres históricos observados.
   - Eso sugiere que, con esta lógica y este dataset, los puntos de salida relevantes no se mueven dentro de ese rango estrecho.

### Sobre la retención estimada de MFE

La retención estimada de MFE en ganadores no aporta una señal mejor que el giveback en esta tarea, porque:
- depende de una reconstrucción con cierres dentro del trade;
- puede verse afectada por gaps entre cierre y ejecución;
- y no cambia la conclusión central.

Por prudencia, el hallazgo operativo debe apoyarse en la combinación de:
- giveback medio,
- PnL short agregado,
- estabilidad de trades,
- y efecto sobre perdedores por rebote.

## 6. Impacto en drawdown y sistema global

### Resumen

- **Base 8%**: drawdown máximo de **-28.4862%**.
- **6%**: drawdown **igual** al de la base.
- **7%**: drawdown **igual** al de la base.
- **9%**: drawdown **igual** al de la base.
- **10%**: drawdown empeora a **-31.2385%**.
- **Adaptativa simple**: drawdown **igual** al de la base.

### Lectura global

1. **No hay evidencia de mejora defensiva real al estrechar ligeramente por debajo del 8%.**
   - Si el `6%` hubiese reducido giveback de forma útil y además protegido mejor el sistema, habría una base para considerarlo.
   - No ocurrió: el drawdown no mejora y el PnL short cae.

2. **Abrir el trailing hasta 10% sí daña el sistema global.**
   - El deterioro no es solo del bloque short; también aparece en capital final y Sharpe equivalente del sistema completo.

3. **La salida actual del 8% parece bien colocada como punto de equilibrio.**
   - No es una salida extremadamente nerviosa.
   - Tampoco deja respirar tanto al trade como para degradar claramente la captura.

## 7. Riesgos de sobreajuste

Este análisis debe leerse con cautela por varios motivos:

1. **Muestra short pequeña.**
   - La versión 2.2.1 trabaja con solo **11 trades short** en la base.
   - Diferencias de uno o dos trades pueden alterar bastante la lectura agregada.

2. **Vecindario con poca sensibilidad observable.**
   - El hecho de que `7%`, `8%`, `9%` y la adaptativa simple coincidan exactamente en resultados históricos sugiere que sería fácil inventar una narrativa optimista sin sustancia real.
   - Aquí la lectura prudente es la contraria: **si no hay diferencia observable, no hay motivo para vender una mejora**.

3. **El 6% da una “señal tentadora” pero no robusta.**
   - Podría parecer intuitivo que un trailing más ceñido reduzca giveback.
   - Sin embargo, en la muestra no lo consigue de forma neta y además incrementa el número de perdedores.

4. **La adaptativa simple no justifica complejidad adicional.**
   - Si una regla adaptativa no cambia nada en la muestra actual, no debe presentarse como mejora potencial solo por ser conceptualmente elegante.

## 8. Conclusión final

La evidencia de este análisis **no respalda** modificar la salida short de la versión 2.2.1 alrededor del trailing actual del **8%**.

Conclusión operativa principal:
- **el trailing 8% sigue siendo la opción más razonable** dentro del vecindario probado;
- **estrechar a 6%** vuelve la salida algo más nerviosa y empeora el bloque short sin ofrecer mejora defensiva real;
- **mover a 7% o 9%** no cambia nada en esta muestra, por lo que no aporta valor práctico;
- **ampliar a 10%** sí deteriora claramente capture, drawdown y retorno;
- **la adaptativa simple** tampoco aporta una mejora observable.

Por tanto, la hipótesis de que pequeños ajustes simples alrededor del 8% podían reducir giveback y mejorar eficiencia de captura **no queda confirmada** de forma robusta en este histórico.

## 9. Recomendación: mantener / ajustar / descartar cambios

### Recomendación final: **mantener**

Recomendación concreta:
- **mantener el trailing short del 8%** en la versión base 2.2.1;
- **descartar** por ahora el cambio a `6%` y `10%`;
- **no implementar** `7%`, `9%` ni la adaptativa simple, porque no muestran mejora observable y solo añadirían ruido de mantenimiento o falsa sensación de refinamiento.

En otras palabras: dentro de este vecindario, **no hay evidencia suficiente para justificar un ajuste**. El 8% permanece como el mejor compromiso entre:
- contención de giveback,
- estabilidad frente a rebotes,
- no volver la salida demasiado nerviosa,
- y preservar el equilibrio global del sistema.
