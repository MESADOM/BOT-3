# VERSION 2.2.2 ANALISIS 51

## 1. Objetivo

Identificar qué variables nacidas del propio mercado principal son las más útiles, simples e interpretables para clasificar contexto o régimen, sin usar como núcleo del análisis rachas de pérdidas, drawdown del sistema ni métricas internas de operaciones, y sin diseñar todavía un clasificador operativo final.

La misión de este documento es construir un inventario disciplinado de variables candidatas para investigación posterior, priorizando pocas variables con significado claro, estabilidad razonable y cálculo viable en tiempo real.

## 2. Mercado principal analizado

El mercado principal analizado es **QQQ**, que es la serie de referencia utilizada por el motor para:

- calcular variables de régimen;
- decidir estados de mercado;
- contextualizar tanto la pata long como la short;
- exportar en resultados las variables visibles `QQQ > SMA200`, `Retorno 63` y `Cruces SMA50`.

Esto vuelve a QQQ el lugar correcto para buscar variables base del selector. `QQQ3` sigue siendo el instrumento operativo de ejecución, pero no es la referencia principal elegida por el sistema para describir el contexto de mercado.

## 3. Familias de variables evaluadas

Se revisan cuatro familias mínimas, todas extraídas del propio mercado principal y todas compatibles con una filosofía simple e interpretable.

### 3.1 Tendencia / dirección

Variables que intentan responder si el mercado está estructuralmente alcista, bajista o en transición.

Candidatos simples:

- posición del precio frente a `SMA200`;
- retorno acumulado a 63 sesiones;
- pendiente de `SMA200`;
- relación `SMA50` frente a `SMA200`.

### 3.2 Ruido / persistencia

Variables que intentan distinguir si el movimiento reciente es limpio y persistente o serruchoso e inestable.

Candidatos simples:

- cruces recientes del precio respecto a `SMA50`;
- días desde el último cruce de `SMA50`;
- consistencia del signo del retorno en una ventana corta;
- separación estable entre precio y media rápida.

### 3.3 Volatilidad / estrés

Variables que miden si el mercado atraviesa un estado de tensión, compresión o expansión de rango.

Candidatos simples:

- volatilidad realizada de 21 sesiones;
- rango medio verdadero normalizado (ATR%);
- distancia del precio a la `SMA200` como proxy de tensión extrema;
- apoyo secundario de `VIX` solo como contraste, no como núcleo.

### 3.4 Sobreextensión

Variables que intentan detectar si el precio ya se ha alejado demasiado de una referencia lenta o media, de forma que el movimiento pueda estar maduro o vulnerable a rebote/normalización.

Candidatos simples:

- distancia del precio a `SMA50`;
- distancia del precio a `SMA200`;
- z-score simple de distancia a media larga;
- retorno acumulado a muy corto plazo como extensión táctica.

## 4. Variables candidatas revisadas

A continuación se listan las variables candidatas revisadas, con una evaluación cualitativa mínima sobre capacidad descriptiva, estabilidad temporal, redundancia, facilidad de cálculo en tiempo real, interpretabilidad y utilidad potencial para diferenciar años favorables y problemáticos.

### 4.1 `QQQ > SMA200`

**Familia:** tendencia / dirección.

**Qué describe:** separación binaria entre entorno por encima o por debajo de una referencia estructural lenta. Es probablemente la variable más directa para distinguir sesgo primario.

**Capacidad descriptiva cualitativa:** alta para separar estructura alcista de deterioro principal, aunque no distingue bien transición frente a caída madura.

**Estabilidad temporal:** alta. Cambia poco y evita mucho ruido de corto plazo.

**Redundancia:** media-alta frente a `SMA50 > SMA200` y frente a pendientes lentas; comparte mucha información de tendencia estructural.

**Facilidad de cálculo en tiempo real:** muy alta.

**Interpretabilidad práctica:** muy alta. Cualquier lectura del sistema puede explicarse con facilidad.

**Posible utilidad para distinguir años favorables y problemáticos:** alta como primer corte grueso, sobre todo para separar años de sesgo claramente alcista frente a años con deterioro estructural.

**Lectura crítica:** es informativa, pero demasiado binaria si se usa sola; necesita una segunda dimensión para distinguir tendencia limpia frente a entorno inestable.

### 4.2 Retorno 63

**Familia:** tendencia / dirección con componente de persistencia.

**Qué describe:** momentum intermedio del mercado principal en aproximadamente un trimestre bursátil.

**Capacidad descriptiva cualitativa:** media-alta. Añade gradación donde `QQQ > SMA200` solo da una respuesta binaria.

**Estabilidad temporal:** media. Es bastante más estable que el corto plazo, pero puede girar con cierta rapidez en cambios de fase.

**Redundancia:** media-alta frente a `QQQ > SMA200`, pendiente de `SMA200` y distancia a medias; no es idéntica, pero pisa mucho terreno común.

**Facilidad de cálculo en tiempo real:** muy alta.

**Interpretabilidad práctica:** alta. “Cómo ha venido comportándose el mercado en el último trimestre” es una lectura intuitiva.

**Posible utilidad para distinguir años favorables y problemáticos:** media-alta, especialmente para detectar deterioros que aún no se reflejan plenamente en la estructura lenta.

**Lectura crítica:** es probablemente útil como variable continua o tricotómica, pero su valor marginal cae bastante si ya se usa `QQQ > SMA200` y alguna medida de sobreextensión o persistencia.

### 4.3 Cruces SMA50

**Familia:** ruido / persistencia.

**Qué describe:** cuántas veces el precio alterna de lado respecto a la `SMA50` en una ventana reciente. Intenta medir serrucho o falta de direccionalidad limpia.

**Capacidad descriptiva cualitativa:** media. No describe sesgo de mercado, pero sí la limpieza o suciedad del trayecto.

**Stabilidad temporal:** media-baja. Puede reaccionar rápido a secuencias erráticas y cambiar mucho según la ventana elegida.

**Redundancia:** baja-media frente a variables de tendencia; aporta una dimensión diferente, más cercana al “ruido de ejecución” del mercado.

**Facilidad de cálculo en tiempo real:** alta.

**Interpretabilidad práctica:** alta. “Muchos cruces = mercado serrucho” es una lectura simple.

**Posible utilidad para distinguir años favorables y problemáticos:** media. Puede separar años de tendencia limpia de años laterales o trampas frecuentes, aunque no siempre discrimina bien crashes rápidos.

**Lectura crítica:** tiene valor real como descriptor de persistencia/ruido, pero es sensible a la longitud de ventana y al uso de `SMA50` concreta; por tanto, es útil más como complemento que como eje principal.

### 4.4 Distancia del precio a `SMA200`

**Familia:** sobreextensión, con lectura secundaria de estrés.

**Qué describe:** cuán lejos está el precio de su media estructural lenta. Captura si el mercado sigue cerca de su trayectoria de fondo o si ya está excesivamente separado.

**Capacidad descriptiva cualitativa:** alta. Distingue bien entre tendencia bajista temprana y caída ya madura/exigida.

**Estabilidad temporal:** media-alta. Mucho más estable que una métrica intradía o a 5 sesiones, aunque menos rígida que el simple `QQQ > SMA200`.

**Redundancia:** media frente a `QQQ > SMA200` y retorno 63. Comparte información direccional, pero añade la magnitud de la separación, que es valiosa.

**Facilidad de cálculo en tiempo real:** muy alta.

**Interpretabilidad práctica:** muy alta. “Demasiado por debajo de la media larga” es una lectura muy clara.

**Posible utilidad para distinguir años favorables y problemáticos:** alta, especialmente para diferenciar entornos bajistas ordenados frente a episodios de estrés o capitulación.

**Lectura crítica:** es una de las mejores variables candidatas del inventario porque combina simpleza, interpretación económica y utilidad potencial para detectar sobreextensión sin recurrir a información interna del sistema.

### 4.5 Distancia del precio a `SMA50`

**Familia:** sobreextensión / táctica.

**Qué describe:** grado de separación del precio respecto a una media más rápida, útil para leer extensión táctica de corto-medio plazo.

**Capacidad descriptiva cualitativa:** media. Puede captar sobreventa o sobrecompra táctica antes que la `SMA200`.

**Estabilidad temporal:** media-baja. Es bastante más nerviosa que la distancia a `SMA200`.

**Redundancia:** media con retorno 63 y cruces recientes; suele reflejar parte del mismo estado táctico.

**Facilidad de cálculo en tiempo real:** muy alta.

**Interpretabilidad práctica:** alta.

**Posible utilidad para distinguir años favorables y problemáticos:** media, sobre todo dentro de años problemáticos con caídas violentas o rebotes abruptos.

**Lectura crítica:** es útil, pero más sensible y menos robusta que la distancia a `SMA200`; por tanto, no parece un primer candidato núcleo si se busca austeridad de variables.

### 4.6 `SMA50 > SMA200` o separación `SMA50`-`SMA200`

**Familia:** tendencia / dirección.

**Qué describe:** confirma si la tendencia intermedia ya se alineó con la estructura de largo plazo.

**Capacidad descriptiva cualitativa:** media-alta en cambios de fase, pero llega tarde en aceleraciones rápidas.

**Estabilidad temporal:** alta.

**Redundancia:** alta frente a `QQQ > SMA200` y pendiente de medias.

**Facilidad de cálculo en tiempo real:** muy alta.

**Interpretabilidad práctica:** alta.

**Posible utilidad para distinguir años favorables y problemáticos:** media-alta, aunque puede reaccionar demasiado tarde en crashes y correcciones intensas.

**Lectura crítica:** informativa como confirmación estructural, pero pesada como selector principal si se desea detectar transición sin retrasarse demasiado.

### 4.7 Pendiente de `SMA200`

**Familia:** tendencia / dirección.

**Qué describe:** si la propia estructura lenta está ascendiendo, aplanándose o cayendo.

**Capacidad descriptiva cualitativa:** media. Mejora la lectura de tendencia porque evita depender solo del cruce precio-media.

**Estabilidad temporal:** muy alta.

**Redundancia:** alta con `QQQ > SMA200` y `SMA50 > SMA200`.

**Facilidad de cálculo en tiempo real:** alta.

**Interpretabilidad práctica:** media-alta.

**Posible utilidad para distinguir años favorables y problemáticos:** media, especialmente para diferenciar debilidad transitoria de deterioro más profundo.

**Lectura crítica:** buena variable de apoyo, pero probablemente decorativa si ya existen dos medidas estructurales más simples.

### 4.8 Volatilidad realizada 21d o ATR% 21d

**Familia:** volatilidad / estrés.

**Qué describe:** intensidad reciente de los movimientos. Ayuda a distinguir tendencia tranquila de mercado tensionado.

**Capacidad descriptiva cualitativa:** media-alta. Puede ser importante para detectar años problemáticos donde no solo cambia la dirección, sino también la violencia del trayecto.

**Estabilidad temporal:** media. Más estable que el movimiento diario, menos estable que una media larga.

**Redundancia:** baja-media frente a tendencia pura; aporta una dimensión bastante distinta.

**Facilidad de cálculo en tiempo real:** alta.

**Interpretabilidad práctica:** alta si se expresa como “rango/volatilidad reciente del mercado”.

**Posible utilidad para distinguir años favorables y problemáticos:** alta en episodios de estrés, crashes o fases de desorden, incluso cuando el sesgo direccional tarda en confirmarse.

**Lectura crítica:** es la mejor candidata de la familia volatilidad/estrés, pero debe tratarse con prudencia porque por sí sola puede confundir pánico puntual con contexto estructural.

### 4.9 Días desde último cruce de `SMA50`

**Familia:** ruido / persistencia.

**Qué describe:** cuánto tiempo lleva el precio sin alternar de lado respecto a la media rápida.

**Capacidad descriptiva cualitativa:** media.

**Estabilidad temporal:** media.

**Redundancia:** alta con `Cruces SMA50`; ambas miden persistencia desde ángulos muy próximos.

**Facilidad de cálculo en tiempo real:** alta.

**Interpretabilidad práctica:** alta.

**Posible utilidad para distinguir años favorables y problemáticos:** media.

**Lectura crítica:** variable razonable, pero probablemente redundante si ya se conserva `Cruces SMA50`.

## 5. Variables con mayor valor descriptivo

Si el objetivo es encontrar variables útiles, simples e interpretables, las que mejor sobreviven a una criba disciplinada son estas:

### 5.1 `QQQ > SMA200`

Tiene el mayor valor como descriptor estructural grueso. No explica todo, pero sí ofrece el primer corte más estable y comprensible.

### 5.2 Distancia del precio a `SMA200`

Es la variable con mejor equilibrio entre información adicional y sencillez. Mejora lo que `QQQ > SMA200` no captura: la magnitud de la separación y el grado de sobreextensión o estrés relativo.

### 5.3 Retorno 63

Aporta una lectura de momentum intermedio que puede detectar deterioro o recuperación antes de que la estructura lenta cambie por completo. Tiene valor, aunque no debería inflarse su papel porque solapa bastante con otras medidas de tendencia.

### 5.4 Cruces SMA50

Es la variable que mejor representa la dimensión de ruido/persistencia dentro del sistema actual. No parece ideal como núcleo, pero sí como una forma simple de detectar contexto serrucho.

### 5.5 Volatilidad realizada 21d o ATR% 21d

Es la mejor candidata fuera de las tres variables ya visibles. Tiene valor porque añade una dimensión distinta: no solo dirección, sino tensión del mercado. Puede ser útil para separar años difíciles por desorden y violencia de movimientos.

## 6. Variables redundantes o débiles

### 6.1 Variables redundantes

- **`SMA50 > SMA200`**: útil, pero muy solapada con `QQQ > SMA200` y con la pendiente de medias.
- **Pendiente de `SMA200`**: informativa, aunque probablemente excesiva si ya se usan una variable binaria estructural y una variable de distancia a media larga.
- **Días desde último cruce de `SMA50`**: aporta poco si ya se dispone de `Cruces SMA50`.
- **Distancia a `SMA50`**: interesante, pero una parte importante de su información ya aparece indirectamente en retorno 63, cruces y sobreextensión frente a `SMA200`.

### 6.2 Variables débiles o decorativas

- **Pendientes múltiples de varias medias a horizontes muy cercanos**: tienden a complicar el inventario sin añadir una lectura sustancialmente nueva.
- **Z-scores más sofisticados de distancia**: pueden ser elegantes, pero aquí empiezan a alejarse del criterio de simplicidad e interpretabilidad priorizado.
- **Combinaciones demasiado finas de transición estructural**: por ejemplo, reglas del tipo “casi cruce” muy ajustadas entre `SMA50` y `SMA200` parecen más sensibles que informativas para esta fase del trabajo.

### 6.3 Variables demasiado sensibles

- **Distancia a `SMA50`**: más nerviosa y propensa a cambiar de lectura con rapidez.
- **Cruces SMA50**: útil, pero sensible a la ventana elegida y al comportamiento errático local.
- **Volatilidad 21d**: valiosa, aunque puede dispararse por eventos concretos y dar una lectura exagerada si se usa sin contexto estructural.

## 7. Variables simples viables para tiempo real

Las variables más viables para cálculo en tiempo real, por simplicidad y trazabilidad, son:

- `QQQ > SMA200`
- distancia del precio a `SMA200`
- retorno 63
- cruces recientes respecto a `SMA50`
- volatilidad realizada 21d o `ATR%` 21d

Todas comparten ventajas prácticas importantes:

- se calculan con datos de mercado estándar del propio sistema;
- no requieren información futura;
- no dependen de resultados internos de las operaciones;
- pueden recalcularse diariamente de forma barata;
- se explican con facilidad ante una revisión manual.

## 8. Conjunto mínimo propuesto para investigación posterior

Sin diseñar aún un clasificador final, el conjunto mínimo y razonable para investigación posterior debería ser **muy corto** y cubrir dimensiones diferentes del contexto.

### Propuesta mínima

1. **`QQQ > SMA200`**
   - Papel: descriptor estructural base.
   - Razón: aporta el corte más simple y estable entre estructura favorable y desfavorable.

2. **Distancia del precio a `SMA200`**
   - Papel: sobreextensión / madurez del movimiento.
   - Razón: añade magnitud y ayuda a distinguir deterioro ordenado frente a caída ya muy exigida.

3. **Cruces SMA50** *o*, como alternativa de la misma familia, una medida muy simple de persistencia equivalente.
   - Papel: ruido / serrucho.
   - Razón: representa una dimensión distinta a tendencia y sobreextensión.

4. **Volatilidad realizada 21d o ATR% 21d**
   - Papel: estrés del mercado.
   - Razón: cubre una dimensión que hoy el sistema apenas recoge de forma explícita.

### Variable de reserva, no imprescindible en el núcleo inicial

- **Retorno 63**
  - Tiene valor, pero podría quedar en observación secundaria porque solapa bastante con `QQQ > SMA200` y distancia a `SMA200`.
  - Si el inventario se mantiene muy austero, es una candidata razonable a quedar fuera del primer núcleo de investigación.

### Lectura global del conjunto mínimo

Este conjunto intenta cubrir cuatro preguntas muy simples:

- **¿Dónde está el mercado respecto a su estructura lenta?** → `QQQ > SMA200`
- **¿Cuán alejado está de esa estructura?** → distancia a `SMA200`
- **¿Se mueve con limpieza o con serrucho?** → cruces `SMA50`
- **¿El entorno está calmado o tensionado?** → volatilidad 21d / `ATR%`

Esa cobertura es conceptualmente más sana que acumular muchas variables muy parecidas entre sí.

## 9. Conclusión final

El análisis apunta a que las variables del mercado principal con más valor para clasificar contexto o régimen, manteniendo simplicidad e interpretabilidad, no son muchas. La combinación más prometedora no surge de acumular señales, sino de cubrir unas pocas dimensiones claras:

- **estructura de fondo**;
- **grado de separación o sobreextensión**;
- **nivel de ruido/persistencia**;
- **estrés o volatilidad**.

Dentro de esa lógica, las variables ya visibles en el sistema actual sí tienen valor real:

- **`QQQ > SMA200`** tiene valor alto como base estructural;
- **`Retorno 63`** tiene valor útil, pero parcialmente redundante;
- **`Cruces SMA50`** sí aporta una dimensión distinta y por eso merece seguir viva como candidata, aunque con cautela por sensibilidad.

La variable que mejor destaca por equilibrio entre simpleza, sentido práctico e información incremental es la **distancia del precio a `SMA200`**. Además, una medida sencilla de **volatilidad/estrés** merece entrar en la investigación posterior porque añade una dimensión que hoy está menos representada.

En resumen: para distinguir años favorables y problemáticos, parece más prometedor combinar **muy pocas variables complementarias** que profundizar en múltiples variantes de tendencia que terminan diciendo casi lo mismo.

## 10. Recomendación: seguir con pocas variables / ampliar moderadamente / reducir aún más

**Recomendación final: seguir con pocas variables.**

Motivos:

- ya existe una base suficiente de variables explicables en el propio mercado principal;
- añadir demasiadas variantes de medias, pendientes y cruces aumentaría la redundancia;
- el mayor avance marginal probable no está en más complejidad, sino en elegir bien una variable por dimensión;
- antes de ampliar, conviene comprobar si el núcleo mínimo realmente discrimina entre años favorables y problemáticos de forma estable.

Por tanto, la línea más disciplinada para la siguiente fase es investigar un conjunto corto de variables candidatas, con prioridad para:

- `QQQ > SMA200`
- distancia a `SMA200`
- `Cruces SMA50`
- volatilidad realizada 21d o `ATR%` 21d

Y dejar **`Retorno 63`** como variable de apoyo o contraste, no necesariamente como parte fija del núcleo inicial.
