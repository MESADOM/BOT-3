# VERSION 2.2.2 ANALISIS 55

## 1. Objetivo

Determinar la viabilidad operativa real de un futuro selector de contexto calculado con datos accesibles desde el ecosistema de IBKR, priorizando simplicidad operativa, robustez, continuidad entre backtest e implementación real y bajo coste de mantenimiento diario o periódico.

Este documento **no diseña todavía el selector final** ni propone una implementación de producción. Su objetivo es estudiar qué familias de datos merecen formar parte del futuro selector y cuáles deberían descartarse por fragilidad operativa, baja replicabilidad histórica o dependencia excesiva de fuentes externas.

## 2. Datos necesarios para el selector

Para estudiar un selector de contexto útil y mantenible conviene separar las variables candidatas en tres familias: datos del mercado principal, confirmadores externos simples y datos de operaciones propias.

### 2.1. Mercado principal

Son los datos más importantes porque tienen mejor continuidad entre investigación y operativa real, y además ya están alineados con la lógica actual del sistema.

Variables candidatas razonables:

- precio de cierre diario del activo de referencia principal (`QQQ` o el benchmark elegido);
- medias móviles simples largas e intermedias (`SMA50`, `SMA100`, `SMA200`);
- retornos acumulados por ventana fija (`retorno_20`, `retorno_63`, `retorno_126`);
- distancia del precio a `SMA200` y a `SMA50`;
- pendiente simple de `SMA50` o `SMA200`;
- volatilidad histórica realizada a 20 o 63 sesiones;
- amplitud o estabilidad del movimiento, aproximable por número de cruces con una media de referencia en ventana fija;
- rango diario medio o `ATR` diario si se quiere medir compresión/expansión sin usar intradía;
- gap de apertura respecto al cierre previo, solo si IBKR permite consolidarlo con suficiente estabilidad para el activo elegido.

### 2.2. Confirmadores externos simples

Deben ser pocos, muy líquidos, fáciles de descargar históricamente y con sentido económico claro. Si no cumplen esas condiciones, no merecen entrar en el selector.

Variables candidatas razonables:

- volatilidad implícita simple vía `VIX` diario;
- fuerza/debilidad de mercado amplio mediante `SPY` o `SPX` diario;
- confirmación de riesgo tecnológico comparando `QQQ` frente a `SPY` o `NDX`;
- confirmación monetaria muy simple con `TLT` o rendimiento de bono largo solo si la serie histórica es limpia y fácil de mantener;
- amplitud muy básica usando un ETF de small caps (`IWM`) como termómetro secundario, sin llegar a indicadores complejos de breadth.

### 2.3. Operaciones propias

Son datos internos del sistema. Pueden ser útiles para modular agresividad o freno, pero deben tratarse con prudencia porque introducen riesgo de sobreajuste y pueden romper la comparación limpia entre mercado y ejecución.

Variables candidatas razonables:

- resultado de la última operación;
- secuencia corta de operaciones ganadoras/perdedoras;
- drawdown actual del sistema;
- tiempo desde la última salida;
- número de señales recientes no ejecutadas;
- rentabilidad acumulada reciente del propio sistema en una ventana fija;
- exposición actual o porcentaje de capital realmente desplegado.

## 3. Fuentes de datos y su papel

### 3.1. Mercado principal

**Fuente operativa preferente:** datos diarios de mercado servidos por IBKR para los activos que ya se operan o se usan como benchmark.

**Papel dentro del futuro selector:**

- definir régimen principal;
- medir tendencia, deterioro o recuperación;
- detectar sobreextensión;
- medir estabilidad o serrucho del mercado;
- sostener el núcleo del selector tanto en backtest como en tiempo real.

**Disponibilidad esperable:** alta.

**Ventaja clave:** es la familia con mayor probabilidad de ser replicable de forma consistente entre histórico y real.

### 3.2. Confirmadores externos simples

**Fuente operativa preferente:** también IBKR, siempre que el dato venga de símbolos líquidos, estándar y fáciles de contratar o consultar en histórico diario.

**Papel dentro del futuro selector:**

- confirmar o desmentir el contexto principal;
- reducir falsos positivos del activo principal;
- distinguir entre deterioro aislado del activo y deterioro más amplio del mercado;
- aportar una capa secundaria de prudencia sin obligar a una arquitectura compleja.

**Disponibilidad esperable:** media-alta si se limitan a ETFs e índices muy líquidos.

**Advertencia:** cuanto más exótico sea el confirmador, más crece el riesgo de divergencias entre backtest y real, cambios de símbolo, huecos de histórico o dependencia contractual de mercado de datos.

### 3.3. Operaciones propias

**Fuente operativa preferente:** registro interno del sistema, generado por el propio motor y persistido localmente después de cada cierre o ejecución.

**Papel dentro del futuro selector:**

- introducir frenos operativos simples;
- evitar reentradas demasiado rápidas;
- adaptar prudencia después de secuencias adversas;
- monitorizar salud del sistema más que dirección del mercado.

**Disponibilidad esperable:** muy alta, siempre que el sistema guarde correctamente sus operaciones y estados.

**Advertencia:** si estas variables pesan demasiado, el selector deja de medir contexto de mercado y pasa a medir comportamiento reciente del propio modelo, lo que aumenta el riesgo de sobreajuste.

## 4. Frecuencia de actualización recomendada

La prioridad debe ser usar una cadencia estable y barata de mantener.

### 4.1. Cálculo diario al cierre

Conviene recalcular al cierre oficial o tras el cierre con margen operativo:

- precios diarios del activo principal;
- medias móviles;
- retornos por ventana;
- distancia a medias;
- volatilidad histórica diaria;
- cruces o medidas de serrucho;
- `VIX` diario y otros confirmadores simples de cierre;
- estado interno derivado de operaciones propias cerradas ese día.

**Motivo:** el sistema actual está estructurado sobre lógica diaria, por lo que recalcular al cierre maximiza continuidad entre backtest y real y minimiza ruido intradía.

### 4.2. Revisión semanal

Tiene sentido recalcular o revisar con menor frecuencia:

- rankings o comparaciones relativas entre varios confirmadores secundarios;
- métricas agregadas de estabilidad de mercado de ventana larga;
- control de calidad del histórico descargado;
- chequeos de consistencia entre fuentes y símbolos.

**Motivo:** estos elementos no aportan demasiado valor si se recalculan cada minuto y, en cambio, aumentan complejidad operativa.

### 4.3. Revisión mensual o cuando cambie la infraestructura

Debe reservarse para:

- validar continuidad de símbolos e históricos;
- revisar si algún dato externo dejó de ser fácil de obtener;
- comprobar que el backfill histórico sigue siendo reproducible;
- revisar contratos, permisos o cambios de naming en IBKR.

## 5. Riesgos operativos detectados

### 5.1. Riesgos del mercado principal

- desajustes por usar precios distintos entre backtest y real si a veces se usa cierre oficial y otras cierre ajustado;
- errores por corporativas si no se unifica el tratamiento de dividendos y splits;
- huecos de histórico si falla una descarga diaria y no hay rutina de validación;
- dependencia de que el mismo símbolo represente siempre el mismo activo con la misma convención histórica.

**Riesgo operativo estimado:** bajo-medio.

### 5.2. Riesgos de confirmadores externos simples

- necesidad de permisos adicionales de market data en IBKR;
- diferencias históricas entre índice, ETF y producto negociable equivalente;
- fallos silenciosos si un confirmador no actualiza pero el resto sí;
- tentación de añadir demasiados confirmadores y volver frágil la arquitectura.

**Riesgo operativo estimado:** medio.

### 5.3. Riesgos de operaciones propias

- contaminación del selector con reglas derivadas del resultado reciente del sistema;
- persistencia incompleta o corrupta del log de operaciones;
- cambios de versión que alteran la comparabilidad histórica de las métricas internas;
- falsos bloqueos si el estado interno queda desalineado con la realidad de la cartera.

**Riesgo operativo estimado:** medio si se usan pocas variables; alto si se construyen métricas internas complejas.

### 5.4. Puntos de fallo operativos transversales

- descarga incompleta del día y cálculo sobre una sesión no cerrada realmente;
- diferencias horarias entre mercado, servidor y rutina batch;
- recalcular con datos parciales por lanzar el proceso antes del cierre definitivo;
- no detectar `NaN`, duplicados o fechas ausentes;
- mezclar series ajustadas y no ajustadas;
- depender de datos que en backtest se consiguen fácil en CSV pero en real requieren mantenimiento manual constante.

## 6. Arquitectura simple de cálculo en tiempo real

La arquitectura recomendada debe ser deliberadamente sencilla, orientada a batch diario con una sola fuente principal y muy pocos confirmadores.

### 6.1. Qué se calcula al cierre

Bloque diario principal:

1. descargar o actualizar series diarias del activo principal y de un conjunto mínimo de confirmadores;
2. validar integridad: fecha esperada, no nulos, no duplicados, rango razonable;
3. recalcular indicadores diarios base del activo principal;
4. recalcular indicadores diarios de confirmadores simples;
5. actualizar métricas internas derivadas de operaciones propias;
6. guardar una tabla final de contexto ya preparada para el siguiente día operativo.

Resultado esperado del bloque diario:

- una fila por sesión con todas las variables candidatas ya congeladas;
- un estado de contexto reproducible;
- trazabilidad suficiente para comparar la misma fecha entre backtest y real.

### 6.2. Qué se recalcula con menos frecuencia

Bloque semanal o periódico:

- auditoría de calidad de históricos;
- recomputación completa de métricas agregadas si hubo huecos o correcciones;
- revisión de símbolos auxiliares;
- control de consistencia entre versiones del motor y estados persistidos.

### 6.3. Qué no merece cálculo intradía

Para este futuro selector, salvo que más adelante se demuestre lo contrario, no merece la pena recalcular durante la sesión:

- medias móviles largas;
- retornos de 63 o 126 sesiones;
- drawdown estructural del sistema;
- confirmadores externos lentos como `VIX` de cierre;
- métricas de serrucho calculadas con ventana diaria.

La ganancia operativa de recalcularlas intradía es baja y el coste de complejidad aumenta mucho.

## 7. Qué datos conviene evitar

Para preservar robustez y continuidad, conviene evitar o posponer:

- datos macroeconómicos con calendario irregular y revisiones posteriores;
- amplitud compleja de mercado basada en series difíciles de reconstruir históricamente;
- indicadores propietarios o webs de terceros sin API estable;
- sentimiento de noticias, redes sociales o NLP externo;
- datos de opciones más allá de un uso muy simple de `VIX`, porque la microestructura y la limpieza histórica complican mucho la réplica;
- métricas intradía complejas si el sistema base opera con lógica diaria;
- series alternativas que no estén disponibles de forma homogénea en histórico y en real;
- selectores que dependan de demasiados umbrales internos derivados de operaciones propias.

En resumen: todo dato que exija mantenimiento manual frecuente, validaciones especiales o reconciliación continua entre proveedores debería quedar fuera del primer selector viable.

## 8. Viabilidad global con IBKR

### 8.1. Disponibilidad de datos necesarios

- **Mercado principal:** alta viabilidad.
- **Confirmadores externos simples:** viabilidad media-alta si se limitan a 1-3 símbolos muy líquidos.
- **Operaciones propias:** viabilidad alta, porque dependen del propio sistema.

### 8.2. Simplicidad de actualización

- **Mercado principal:** alta, especialmente con cierre diario.
- **Confirmadores externos simples:** media, siempre que no se multipliquen los activos auxiliares.
- **Operaciones propias:** alta si existe un registro único y estable de operaciones.

### 8.3. Robustez operativa

- **Mercado principal:** es la familia más robusta.
- **Confirmadores externos simples:** robusta solo si se mantiene minimalista.
- **Operaciones propias:** robusta para frenos simples, menos robusta para lógica contextual compleja.

### 8.4. Dependencia de fuentes externas

- **Mercado principal:** baja, porque puede concentrarse casi todo en IBKR.
- **Confirmadores externos simples:** media.
- **Operaciones propias:** muy baja.

### 8.5. Facilidad de replicación histórica

- **Mercado principal:** alta.
- **Confirmadores externos simples:** media-alta con ETFs o índices estándar.
- **Operaciones propias:** media, porque exige congelar exactamente la lógica de generación y persistencia de estados.

### 8.6. Riesgo operativo de cada familia de datos

| Familia de datos | Disponibilidad | Simplicidad de actualización | Robustez operativa | Dependencia externa | Replicación histórica | Riesgo operativo |
|---|---|---:|---:|---:|---:|---|
| Mercado principal | Alta | Alta | Alta | Baja | Alta | Bajo-Medio |
| Confirmadores externos simples | Media-Alta | Media | Media | Media | Media-Alta | Medio |
| Operaciones propias | Alta | Alta | Media | Muy baja | Media | Medio |

## 9. Conclusión final

La viabilidad operativa de un futuro selector de contexto en IBKR es **realista** siempre que se construya sobre una base muy simple:

- núcleo apoyado en datos diarios del mercado principal;
- muy pocos confirmadores externos, todos líquidos y estándar;
- uso prudente de métricas derivadas de operaciones propias solo como freno operativo, no como corazón del selector.

La continuidad entre backtest y real será mucho mejor si el selector se apoya en series diarias fáciles de descargar, recalcular y auditar. En cambio, la robustez cae rápidamente cuando se añaden datos intradía, amplitud compleja, macro con revisiones o confirmadores externos difíciles de mantener.

Por tanto, antes de diseñar el selector final, el camino más sólido es definir una **capa de contexto diaria mínima**, reproducible y auditada, en la que cada variable candidata tenga una justificación operativa clara y una fuente sostenible en IBKR.

## 10. Recomendación: viable simple / viable con cautelas / demasiado frágil todavía

**Recomendación final: viable con cautelas.**

Es viable porque IBKR permite sostener razonablemente bien un selector de contexto diario apoyado en precio, tendencia, volatilidad simple y un conjunto muy pequeño de confirmadores líquidos. Sin embargo, la viabilidad depende de mantener disciplina estricta en tres principios:

1. usar pocas familias de datos;
2. recalcular casi todo al cierre;
3. descartar desde el inicio cualquier variable cuya réplica histórica y mantenimiento real no sean triviales.

Si se respetan esos principios, el futuro selector podrá evolucionar con continuidad entre investigación y ejecución real. Si no se respetan, el riesgo no será tanto estadístico como **operativo**: fallos silenciosos, datos inconsistentes y una arquitectura demasiado frágil para dinero real.
