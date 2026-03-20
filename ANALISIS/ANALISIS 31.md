# VERSION 2.2.1 ANALISIS 31

## 1. Objetivo

Determinar si la mejora del filtro anti-sobreextensión depende de pocos episodios concretos o si muestra una robustez temporal razonable a través de subperiodos, comparando la **base 2.2.1** frente a la **variante auditada** dentro de la familia ya validada en análisis previos, sin abrir nuevas reglas ni tocar producción.

Este documento se centra en dos preguntas:
- si la mejora está distribuida por el tiempo o concentrada en muy pocos tramos;
- si la ventaja nace de una señal repetible o de unos pocos trades/shocks concretos.

## 2. Variante auditada

### Base
- **Base 2.2.1**: lógica vigente sin filtro anti-sobreextensión adicional.

### Variante auditada
- **Filtro anti-sobreextensión por distancia a SMA200**.
- **Regla exacta**: bloquear la entrada short si `QQQ / SMA200 - 1 <= -15%`.

### Nota de trazabilidad relevante
Se han leído obligatoriamente `ANALISIS 16`, `17`, `18` y `19b`. El archivo `ANALISIS/ANALISIS 30.md` **no existe en el repositorio actual**, así que no es posible extraer literalmente de él la “mejor variante” pedida sin inventar contenido inexistente.

Para no fabricar una variante nueva ni romper la restricción de trabajar dentro de la familia ya validada, se audita la **misma variante ya consolidada en la cadena 16 → 19b**, que además es la única mejora short explícitamente defendida en esa trazabilidad: el filtro `SMA200 <= -15%`.

## 3. Segmentación temporal usada

Se comparó base vs variante por tres ejes:

1. **Año de cierre de operación**.
2. **Semestre de cierre de operación** (`H1`, `H2`).
3. **Grandes regímenes de mercado ya definidos** en análisis previos:
   - **ALCISTA**: `QQQ > SMA200` y `SMA50 > SMA200`.
   - **BAJISTA**: `QQQ < SMA200` y `SMA50 < SMA200`.
   - **LATERAL**: resto de casos.

Cada operación se asignó al régimen de su **fecha de entrada**, porque la mejora auditada actúa en el **momento de entrada short**.

### Métricas mínimas revisadas
En cada segmento se midieron como mínimo:
- retorno por periodo;
- drawdown por periodo;
- número de trades short por periodo;
- beneficio short por periodo;
- contribución relativa de los trades bloqueados;
- porcentaje del beneficio total explicado por pocos episodios.

## 4. Resultados por periodo

## 4.1 Resumen global

| Configuración | Retorno total sistema | Capital final € | Drawdown máx. global | Nº trades short | Beneficio short € | Peso short sobre beneficio total |
|---|---:|---:|---:|---:|---:|---:|
| Base 2.2.1 | 2096,28% | 21.962,83 | -33,55% | 11 | 3528,27 | 16,06% |
| Variante SMA200 -15% | 2196,58% | 22.965,83 | -33,55% | 9 | 4531,27 | 19,73% |
| Delta variante vs base | +100,30 pts | +1003,00 | 0,00 pts | -2 | +1003,00 | +3,67 pts |

### Lectura global
- La mejora existe y es **real a nivel agregado**.
- Pero la mejora es **claramente defensiva**, no expansiva:
  - no añade actividad short;
  - reduce el número de shorts de `11` a `9`;
  - mejora porque **bloquea entradas malas/tardías** y retemporiza un episodio de 2022.
- La mejora total del sistema coincide prácticamente con la mejora del bloque short: **+1003,00 €**.

## 4.2 Resultados por año

| Año | Base retorno % | Variante retorno % | Delta % | Base DD % | Variante DD % | Base shorts | Variante shorts | Base short € | Variante short € | Lectura |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2014 | 9,00 | 9,00 | 0,00 | -1,32 | -1,32 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2015 | -14,05 | -14,05 | 0,00 | -17,11 | -17,11 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2016 | -17,00 | -17,00 | 0,00 | -15,82 | -15,82 | 2 | 2 | -23,50 | -23,50 | Sin cambio |
| 2017 | 34,53 | 34,53 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2018 | 46,08 | 46,08 | 0,00 | -5,23 | -5,23 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2019 | 39,37 | 39,37 | 0,00 | -9,78 | -9,78 | 1 | 1 | 339,28 | 339,28 | Sin cambio |
| 2020 | 225,98 | 225,98 | 0,00 | -3,13 | -3,13 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2021 | 265,30 | 265,30 | 0,00 | -4,78 | -4,78 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2022 | 311,62 | 411,92 | +100,30 | -4,56 | 0,00 | 7 | 5 | 3674,99 | 4677,99 | Mejora fuerte |
| 2023 | 117,40 | 117,40 | 0,00 | -2,19 | -1,98 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2024 | 399,60 | 399,60 | 0,00 | -3,81 | -3,59 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2025 | 763,70 | 763,70 | 0,00 | -2,47 | -2,35 | 1 | 1 | -462,50 | -462,50 | Sin cambio; caso débil persiste |
| 2026 | -85,25 | -85,25 | 0,00 | -4,48 | -4,29 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |

### Lectura anual
- La mejora **solo aparece en 2022**.
- En **12 de 13 años** el retorno es exactamente igual.
- No hay años donde la variante empeore el resultado agregado.
- Tampoco hay evidencia de mejora repartida entre varios años: la mejora anual está **100% concentrada en un solo ejercicio**.
- **2025 no mejora nada**: el trade perdedor relevante sigue intacto.

## 4.3 Resultados por semestre

| Semestre | Base retorno % | Variante retorno % | Delta % | Base DD % | Variante DD % | Base shorts | Variante shorts | Base short € | Variante short € | Lectura |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2014-H1 | -2,80 | -2,80 | 0,00 | -1,32 | -1,32 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2014-H2 | 11,80 | 11,80 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2015-H1 | -8,90 | -8,90 | 0,00 | -6,14 | -6,14 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2015-H2 | -5,15 | -5,15 | 0,00 | -7,96 | -7,96 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2016-H1 | -12,10 | -12,10 | 0,00 | -10,53 | -10,53 | 2 | 2 | -23,50 | -23,50 | Sin cambio |
| 2016-H2 | -4,90 | -4,90 | 0,00 | -9,57 | -9,57 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2017-H1 | 29,86 | 29,86 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2017-H2 | 4,67 | 4,67 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2018-H1 | 17,05 | 17,05 | 0,00 | -5,23 | -5,23 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2018-H2 | 29,03 | 29,03 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2019-H1 | 60,83 | 60,83 | 0,00 | 0,00 | 0,00 | 1 | 1 | 339,28 | 339,28 | Sin cambio |
| 2019-H2 | -21,46 | -21,46 | 0,00 | -0,56 | -0,56 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2020-H1 | 148,68 | 148,68 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2020-H2 | 77,30 | 77,30 | 0,00 | -3,13 | -3,13 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2021-H1 | 105,40 | 105,40 | 0,00 | -4,78 | -4,78 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2021-H2 | 159,91 | 159,91 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2022-H1 | 355,57 | 355,57 | 0,00 | 0,00 | 0,00 | 4 | 4 | 4114,49 | 4114,49 | Sin cambio |
| 2022-H2 | -43,95 | 56,35 | +100,30 | -4,56 | 0,00 | 3 | 1 | -439,50 | 563,50 | Mejora total concentrada aquí |
| 2023-H1 | -65,95 | -65,95 | 0,00 | -2,19 | -1,98 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2023-H2 | 183,35 | 183,35 | 0,00 | -1,25 | -1,15 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2024-H1 | 287,45 | 287,45 | 0,00 | 0,00 | 0,00 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| 2024-H2 | 112,15 | 112,15 | 0,00 | -3,81 | -3,59 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2025-H1 | 305,90 | 305,90 | 0,00 | -2,47 | -2,35 | 1 | 1 | -462,50 | -462,50 | Sin cambio; no corrige 2025 |
| 2025-H2 | 457,80 | 457,80 | 0,00 | -1,81 | -1,73 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |
| 2026-H1 | -85,25 | -85,25 | 0,00 | -4,48 | -4,29 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |

### Lectura semestral
- La mejora **solo altera un semestre de 25**: `2022-H2`.
- En **24 de 25 semestres** no hay mejora ni deterioro material.
- Por tanto, la mejora está **100% concentrada en `2022-H2`**.
- La hipótesis de dependencia desproporcionada de `2022-H2` queda **confirmada**.

## 4.4 Resultados por grandes regímenes de mercado

| Régimen | Base retorno % | Variante retorno % | Delta % | Base DD % | Variante DD % | Base shorts | Variante shorts | Base short € | Variante short € | Lectura |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ALCISTA | 1323,56 | 1323,56 | 0,00 | -28,49 | -28,49 | 0 | 0 | 0,00 | 0,00 | Sin cambio |
| BAJISTA | 374,33 | 474,63 | +100,30 | -5,83 | -5,83 | 11 | 9 | 3528,27 | 4531,27 | Mejora total concentrada aquí |
| LATERAL | 398,40 | 398,40 | 0,00 | -2,19 | -1,98 | 0 | 0 | 0,00 | 0,00 | Sin cambio material |

### Lectura por régimen
- Toda la mejora aparece, como era esperable, en **BAJISTA**.
- Esto confirma que la mejora es coherente con su función short.
- Pero el hecho de mejorar en régimen bajista **no prueba robustez temporal**: dentro de ese régimen la mejora sigue concentrada en un único subtramo (`2022-H2`).

## 5. Concentración del beneficio

## 5.1 Beneficio incremental total
La variante mejora a la base en **+1003,00 €**.

Ese incremento representa:
- **100%** del delta anual en `2022`;
- **100%** del delta semestral en `2022-H2`;
- aproximadamente **103,89%** de la mejora explicado por la combinación de:
  - pérdidas evitadas en trades bloqueados; y
  - un único trade nuevo rentable;
  con un pequeño ajuste neto negativo por el bloqueo de un ganador menor.

## 5.2 Trades bloqueados y nuevo trade generado

### Trades short bloqueados por la variante
- `2022-07-07 -> 2022-07-12`: **+39,00 €**.
- `2022-10-19 -> 2022-10-27`: **-89,00 €**.
- `2022-11-09 -> 2022-11-14`: **-389,50 €**.

**Resultado agregado de los trades bloqueados**: `-439,50 €` en la base.

### Trade nuevo que aparece en la variante
- `2022-10-25 -> 2022-11-10`: **+563,50 €**.

### Contribución relativa de los trades bloqueados
- Las **pérdidas evitadas** por bloquear trades malos suman **+478,50 €** (`89,00 + 389,50`).
- El coste de bloquear un ganador pequeño es **-39,00 €**.
- El nuevo trade aporta **+563,50 €**.

Descomposición del delta total de `+1003,00 €`:
- **47,71%** proviene de pérdidas evitadas por bloquear dos trades malos.
- **56,18%** proviene de un solo trade nuevo ganador.
- **-3,89%** corresponde al ganador pequeño sacrificado.

Conclusión de concentración:
- **103,89% del beneficio incremental bruto** se explica por **3 episodios concretos** (2 bloqueos beneficiosos + 1 nuevo trade ganador), compensados por un pequeño episodio negativo.
- La mejora **no** está repartida entre muchos trades; está dominada por **muy pocos casos**.

## 5.3 Porcentaje del beneficio total explicado por pocos episodios
Tomando el beneficio incremental de la variante frente a la base como referencia:
- el **100%** del beneficio incremental lo explica `2022-H2`;
- el **56,18%** lo explica **un único trade** (`2022-10-25 -> 2022-11-10`);
- el **95,91%** lo explican **tres episodios** (`+563,50`, `+389,50`, `+89,00`), antes de descontar el bloqueo del pequeño ganador de `+39,00`;
- el **100%** de la mejora neta queda explicado al añadir ese cuarto episodio menor.

Esto es una concentración **muy alta**.

## 6. Dependencia de episodios concretos

## 6.1 Dependencia de `2022-H2`
La dependencia de `2022-H2` es **extrema**:
- la mejora total del sistema fuera de `2022-H2` es **0,00 €**;
- `2022-H2` pasa de **-43,95%** a **+56,35%**;
- el beneficio short del semestre pasa de **-439,50 €** a **+563,50 €**.

Por tanto, no es correcto describir esta mejora como repartida o estable a través del tiempo. La mejora depende **desproporcionadamente** de `2022-H2`.

## 6.2 Dependencia de `2025`
La hipótesis de dependencia de `2025` queda **rechazada** en el sentido positivo:
- `2025` no aporta nada al beneficio incremental;
- `2025-H1` queda exactamente igual;
- el short perdedor de `2025-04-15 -> 2025-04-25` (**-462,50 €**) **sigue vivo**.

Esto empeora la lectura de robustez, porque la variante:
- sí arregla un tramo muy concreto de 2022;
- pero **no demuestra repetibilidad** en un episodio problemático más reciente.

## 6.3 Dependencia de pocos trades concretos
La mejora depende de muy pocos trades:
- 3 trades bloqueados respecto a la base;
- 1 trade nuevo en la variante;
- solo 4 episodios explican toda la diferencia neta;
- de esos 4, realmente **3 concentran casi toda la mejora económica**.

Dado que la base solo tenía **11 trades short**, este nivel de concentración implica una **fragilidad muestral alta**.

## 6.4 Dependencia de pocos shocks de mercado
La mejora parece estar vinculada, sobre todo, al entorno de rebotes violentos y reentrada durante el tramo bajista de **octubre-noviembre de 2022**.

Eso sugiere que la variante no está demostrando una superioridad estable a través de múltiples shocks independientes, sino una mejor respuesta a un **cluster muy localizado** del bear market de 2022.

## 7. Fragilidad temporal

### Señales a favor
- La variante **no empeora** el agregado en ningún año ni semestre.
- La lógica económica del filtro sigue siendo coherente: evitar shorts tardíos demasiado extendidos.
- La mejora es claramente **defensiva**: limpia ruido short sin aumentar exposición.

### Señales en contra
- **Concentración extrema por tiempo**: 1 año de 13 y 1 semestre de 25 explican todo el delta.
- **Concentración por trades**: un trade nuevo y dos pérdidas evitadas explican casi toda la mejora.
- **Fragilidad muestral**: pasar de 11 a 9 trades short deja mucho peso en muy pocas observaciones.
- **Falta de repetición en 2025**: no corrige el caso débil más incómodo fuera de 2022.
- **No hay evidencia expansiva**: no mejora por capturar más oportunidades válidas de forma amplia, sino por ser más prudente en un tramo concreto.

### Juicio de fragilidad temporal
La mejora es **más defensiva que expansiva** y su perfil es el siguiente:
- **útil localmente**;
- **no destructiva** fuera del tramo favorable;
- pero **temporalmente frágil** por concentración extrema en `2022-H2` y por dependencia de pocos episodios.

No sería riguroso llamarla “robusta” con esta evidencia.

## 8. Conclusión final

La auditoría temporal muestra que la mejora del filtro anti-sobreextensión **sí mejora el agregado** frente a la base 2.2.1, pero **no lo hace de forma distribuida en el tiempo**.

Patrón observado:
- mejora global real: **sí**;
- mejora repartida por años: **no**;
- mejora repartida por semestres: **no**;
- mejora concentrada en `2022-H2`: **sí, totalmente**;
- mejora apoyada en pocos trades concretos: **sí**;
- mejora repetida en `2025`: **no**.

La lectura correcta es prudente:
- la variante parece **válida como ajuste defensivo local**;
- pero **no demuestra una robustez temporal razonable** a través de subperiodos;
- su beneficio depende demasiado de **pocos episodios concretos** para justificar una lectura fuerte de estabilidad.

## 9. Recomendación: suficientemente estable / dependiente de pocos casos / no justificable

### Recomendación final: **dependiente de pocos casos**

Justificación:
- existe una mejora agregada real y por tanto **no** la clasificaría como “no justificable”;
- pero esa mejora está demasiado concentrada en `2022-H2` y en muy pocos trades como para llamarla “suficientemente estable”;
- su utilidad actual es la de una mejora **defensiva, localizada y frágil**, no la de una mejora temporalmente robusta.

En consecuencia:
- **no tocar producción**;
- **no declarar robustez temporal**;
- **no presentar esta mejora como estable** mientras siga dependiendo de un conjunto tan pequeño de episodios.
