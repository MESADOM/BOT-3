# VERSION 2.2.3 ANALISIS 79

## 1. Objetivo

Implementar una salida defensiva dinámica que solo actúe cuando coinciden dos condiciones durante la vida de una operación:

1. pérdida flotante `<= -200 €`;
2. régimen **reevaluado** en ese momento degradado a `MIXTO` o `PROBLEMATICO`.

No se han tocado reglas de entrada.

---

## 2. Lógica implementada

Se añadió en `META_BOT.py` una condición de salida prioritaria:

- se calcula diariamente la pérdida flotante de la posición abierta usando `qqq3_close` del día;
- se clasifica el régimen actual con la lógica vigente del sistema en reevaluación **diaria durante la operación** (`score_regimen_diario` calculado en `preparar_datos`) con mapeo:
  - `FAVORABLE` si `score >= 2`;
  - `MIXTO` si `score = 0 o 1`;
  - `PROBLEMATICO` si `score <= -1`;
- si `perdida_flotante <= -200` y la clase actual es `MIXTO` o `PROBLEMATICO`, se agenda salida con motivo:
  - `STOP_200_REGIMEN_DEGRADADO`.

Esta validación se evalúa **durante la operación** y con prioridad frente a la salida de módulo (`SELL_*` / `COVER_*`).

---

## 3. Cuántas operaciones afectó

Con la ejecución completa de `META_BOT.py` en la versión actual:

- operaciones cerradas por el nuevo motivo: **4**.
- efecto estructural adicional: una salida temprana permitió una reentrada posterior, por lo que el total de operaciones cerradas pasó de **67** a **68**.

Operaciones con `STOP_200_REGIMEN_DEGRADADO`:

1. Entrada `2021-04-08` → salida `2021-05-06` (`-252,86 €` neto).
2. Entrada `2023-10-12` → salida `2023-10-17` (`-112,5 €` neto).
3. Entrada `2025-05-14` → salida `2025-05-26` (`-312,0 €` neto).
4. Entrada `2026-01-23` → salida `2026-02-02` (`-636,0 €` neto).

---

## 4. Diferencia: régimen de entrada vs régimen reevaluado

Para los 4 casos activados:

- clase en entrada:
  - `1` caso en `FAVORABLE` (score de entrada `2`);
  - `3` casos en `MIXTO` (score de entrada `1`).
- clase reevaluada en activación: en todos los casos cayó en zona no favorable (`MIXTO/PROBLEMATICO`), cumpliendo la regla.

Resultado en este histórico concreto:

- diferencia práctica entre “usar solo régimen de entrada” y “usar régimen reevaluado” para esta regla: **1 operación de diferencia** (la entrada `2021-04-08`, nacida en `FAVORABLE`, solo se activa con reevaluación dinámica).

Aun así, se mantiene la implementación reevaluada porque es la versión metodológicamente correcta (evita depender de una foto fija de entrada si el contexto cambia después).

---

## 5. Impacto en drawdown

Comparativa agregada (baseline inmediato vs versión con STOP dinámico):

- drawdown máximo total antes: **-28,4862%**;
- drawdown máximo total después: **-28,4862%**;
- impacto neto: **0,0000 pp**.

No hay mejora de drawdown total en esta muestra.

---

## 6. Impacto en beneficio neto

Comparativa agregada:

- capital final antes: **22.965,83 €**;
- capital final después: **22.707,83 €**;
- diferencia: **-258,00 €**.

Por tanto, en este histórico la regla añade defensa local en pérdidas, pero con coste neto de beneficio.

---

## 7. Ejemplos relevantes

### Ejemplo A — 2025

- salida defensiva en `2025-05-26` por `STOP_200_REGIMEN_DEGRADADO`;
- evita mantener el tramo adverso inicial;
- permite reentrada posterior (`2025-06-09`) y recuperación parcial en el movimiento alcista siguiente.

### Ejemplo B — 2026

- salida defensiva en `2026-02-02` con pérdida material;
- en este tramo no compensó el resultado agregado del sistema, contribuyendo al deterioro neto frente al baseline.

### Ejemplo C — 2023

- activación técnica de la regla con impacto económico pequeño frente a otras salidas del histórico.

---

## 8. Conclusiones

1. La regla quedó integrada como **salida dinámica**, sin alterar entradas.
2. Se activó en **4 operaciones** y cambió la secuencia operativa total (`67 -> 68` operaciones).
3. En esta corrida no mejoró drawdown máximo total.
4. El impacto económico agregado fue negativo (`-258 €` frente al baseline inmediato).
5. Diferencia empírica entrada vs reevaluación en esta muestra: sí existe (`1` caso), reforzando que la reevaluación dinámica aporta información adicional frente a la foto de entrada.

---

## 9. Comparativa de umbrales de la misma lógica

Se probó exactamente la misma condición de salida dinámica variando solo el umbral monetario:

- `-150 €`
- `-200 €`
- `-250 €`
- `-300 €`

Referencia adicional de contexto (sin STOP monetario-regimen activo): `67` operaciones, capital final `22.965,83 €`, beneficio neto `21.965,83 €`, drawdown máx `-28,4862%`.

| Umbral | Operaciones | Stops activados | Capital final € | Beneficio neto € | Drawdown máx % |
|---:|---:|---:|---:|---:|---:|
| `-150` | 69 | 6 | 22.386,83 | 21.386,83 | -28,4862 |
| `-200` | 68 | 4 | 22.707,83 | 21.707,83 | -28,4862 |
| `-250` | 68 | 3 | 22.314,33 | 21.314,33 | -28,4862 |
| `-300` | 68 | 3 | 22.451,83 | 21.451,83 | -28,4862 |

### Lectura rápida

- Ningún umbral mejoró el drawdown máximo total en esta muestra.
- El mejor capital final entre los cuatro probados fue `-200`.
- El peor fue `-250`.
- Endurecer demasiado (`-150`) aumentó activaciones, pero deterioró más el resultado.

### Conclusión operativa de esta comparativa

Si hay que elegir **solo entre estos cuatro umbrales** para esta lógica y este histórico, el más razonable es `-200`:

1. es el que menos daña el resultado final dentro del conjunto probado;
2. mantiene una activación intermedia (ni tan agresiva como `-150`, ni tan permisiva/inconsistente como `-250/-300` en resultado);
3. no aporta mejora de drawdown total, por lo que su valor queda más en control táctico de salidas puntuales que en mejora estructural del perfil agregado.
