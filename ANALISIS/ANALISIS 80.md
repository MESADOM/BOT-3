# TAREA 80 — SALIDA DEFENSIVA POR FUNCIONAMIENTO DEL SISTEMA DEBIL

## 1) Explicación de la lógica

Se implementó una salida defensiva adicional, sin tocar entradas ni estrategia base:

- Se calcula el beneficio flotante diario de la operación abierta usando `qqq3_close`.
- Si el beneficio flotante es `<= -200 €` **y** `funcionamiento_sistema_2 == DEBIL`, se programa cierre al `open` del día siguiente.
- Motivo de salida registrado: `STOP_200_SISTEMA_DEBIL`.

`funcionamiento_sistema_2` se clasifica reutilizando la lógica vigente de fase débil del sistema:

- `qqq_mayor_sma200 == False`
- `retorno_estado == "NEGATIVO"`
- `cruces_estado == "ALTO"`

---

## 2) Cuántos trades activó

En el histórico actual:

- Activaciones de `STOP_200_SISTEMA_DEBIL`: **0 trades**.

---

## 3) Comparación con stop fijo puro

Escenarios comparados:

1. Baseline (sin esta salida nueva)
2. Tarea 80 (stop `-200` + filtro `DEBIL`)
3. Stop fijo puro simulado (stop `-200` sin filtro `DEBIL`)

Resultados agregados:

- Baseline: `67` operaciones, `21.965,83 €`
- Tarea 80: `67` operaciones, `21.965,83 €` (0 activaciones)
- Stop fijo puro simulado: `69` operaciones, `21.451,33 €` (9 activaciones)

---

## 4) Impacto en años malos

Años negativos relevantes:

- 2015: `-140,50 €` (sin cambios)
- 2016: `-170,00 €` (sin cambios)
- 2026:
  - Baseline / Tarea 80: `-852,50 €`
  - Stop fijo puro simulado: `-459,00 €`

Lectura:

- Con filtro `DEBIL`, la tarea 80 no cambia el resultado de años malos en esta muestra (no activa).
- El stop fijo puro sí reduce daño en 2026, a costa de menor retorno total.

---

## 5) Impacto en ganadoras grandes

Se define “ganadora grande” como operación con beneficio neto `>= 300 €`.

- Baseline / Tarea 80:
  - Nº: `18`
  - Suma: `24.796,17 €`

- Stop fijo puro simulado:
  - Nº: `18`
  - Suma: `23.550,17 €`

Lectura:

- La tarea 80 no afecta ganadoras grandes en este histórico.
- El stop fijo puro mantiene recuento pero recorta captura agregada.

---

## 6) Conclusiones

1. La salida `STOP_200_SISTEMA_DEBIL` quedó integrada correctamente y respeta la lógica actual de debilidad del sistema.
2. En esta muestra histórica no se activa (`0` casos), por lo que no cambia el baseline.
3. El stop fijo puro tiene más capacidad defensiva, pero con coste de oportunidad en beneficio total.
4. La versión de tarea 80 prioriza selectividad (solo en fase débil reciente), manteniendo intacta la estrategia base.

---

## 7) Estudio adicional solicitado: Opción A y Opción B

Se ejecutó un barrido adicional manteniendo la misma lógica de salida base (`pérdida flotante <= -200`) y cambiando únicamente la definición de “debilidad” para activar `STOP_200_SISTEMA_DEBIL`.

### Referencia (TAREA 80 actual, 3 de 3)

- Condición de debilidad: se exigen las 3 a la vez
  - `qqq_mayor_sma200 == False`
  - `retorno_estado == NEGATIVO`
  - `cruces_estado == ALTO`
- Resultado:
  - Operaciones: `67`
  - Beneficio neto total: `21.965,83 €`
  - Activaciones stop: `0`

### Opción A — Suavizar debilidad (2 de 3)

- Condición de debilidad: basta cumplir `2 de 3` (mismas tres variables anteriores).
- Resultado:
  - Operaciones: `67`
  - Beneficio neto total: `21.965,83 €`
  - Activaciones stop: `0`

**Lectura:** en este histórico, pasar de 3/3 a 2/3 no añade activaciones reales; por tanto no vuelve la idea “más testeable” en esta muestra concreta.

### Opción B — Combinar con deterioro de precio/trade (ret20)

Definición usada para el experimento:

- `ret20 = qqq_close / qqq_close_hace_20_sesiones - 1`
- salida si:
  - pérdida flotante `<= -200`
  - y `ret20 < 0`
  - y opcionalmente filtro suave de régimen

#### B1) ret20 < 0 (sin filtro adicional)

- Resultado:
  - Operaciones: `67`
  - Beneficio neto total: `22.405,83 €`
  - Activaciones stop: `5`

#### B2) ret20 < 0 + filtro suave de régimen

- Filtro suave usado: `(qqq_mayor_sma200 == False) OR (retorno_estado == NEGATIVO)`.
- Resultado:
  - Operaciones: `67`
  - Beneficio neto total: `21.965,83 €`
  - Activaciones stop: `0`

### Opinión

1. **Opción A (2 de 3)**, al menos en este histórico, no cambia nada frente a TAREA 80: mismo resultado y 0 activaciones. No parece aportar valor práctico.
2. **Opción B sin filtro adicional (ret20 < 0)** sí genera una señal defensiva “viva” (5 activaciones) y además mejora el neto total en esta muestra. Es la opción más prometedora de las dos para seguir investigando.
3. **Opción B con filtro suave** (como lo definimos aquí) vuelve a cero activaciones, perdiendo la capacidad de intervención. Si se quiere mantener filtro, convendría uno todavía más laxo o directamente empezar por B sin filtro.
4. Recomendación: avanzar con **B sin filtro** como siguiente candidato de validación formal (walk-forward / sensibilidad de umbral y ventana de retorno) antes de considerar cambios en producción.
