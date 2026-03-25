# TAREA 84 — ANÁLISIS UNIFICADO (VERSIÓN 2.2.5)

> Este documento consolida en **un solo archivo** todo el análisis funcional de la TAREA 84.

## 1) Diagnóstico del problema

Se observó una incoherencia entre:

- `rentabilidad_pct` (resultado final del trade en porcentaje), y
- el rango flotante porcentual (`max_ganancia_flotante_pct` / `max_perdida_flotante_pct`).

Las causas identificadas fueron:

1. Falta de definición explícita y única del denominador para los porcentajes flotantes.
2. Posible mezcla de bases (capital total antes de entrar vs capital desplegado), lo que rompe comparabilidad.
3. Riesgo de desajuste por gap en salida si el `precio_salida` no participa en los extremos flotantes.

## 2) Definición elegida (única y consistente)

Se fija como base única:

- **`capital_antes_eur`**

Aplicada a los tres porcentajes clave:

- `rentabilidad_pct = beneficio_neto / capital_antes_eur * 100`
- `max_ganancia_flotante_pct = max_ganancia_flotante_eur / capital_antes_eur * 100`
- `max_perdida_flotante_pct = max_perdida_flotante_eur / capital_antes_eur * 100`

Motivo: comparar porcentajes de una misma operación exige mismo denominador.

## 3) Cálculo actual implementado

### 3.1 Extremos flotantes

Para asegurar contención del resultado final en el rango, los extremos se calculan así:

- `maximo_flotante = max(maximo_desde_entrada, precio_salida)`
- `minimo_flotante = min(minimo_desde_entrada, precio_salida)`

Con esto, el cierre efectivo siempre queda dentro del rango observado.

### 3.2 Fórmulas monetarias (EUR)

**LONG**

- `beneficio_neto = (precio_salida - precio_entrada) * unidades - comisión`
- `max_ganancia_flotante_eur = (maximo_flotante - precio_entrada) * unidades - comisión`
- `max_perdida_flotante_eur = (minimo_flotante - precio_entrada) * unidades - comisión`

**SHORT**

- `beneficio_neto = (precio_entrada - precio_salida) * unidades - comisión`
- `max_ganancia_flotante_eur = (precio_entrada - minimo_flotante) * unidades - comisión`
- `max_perdida_flotante_eur = (precio_entrada - maximo_flotante) * unidades - comisión`

## 4) Coherencia exigida y validación

Condición de consistencia esperada por trade:

- `max_perdida_flotante_pct <= rentabilidad_pct <= max_ganancia_flotante_pct`

Resultado de validación en la ejecución completa:

- Operaciones: **67**
- Incoherencias detectadas: **0**

## 5) Cambios de trazabilidad en código

Además de la lógica, se dejó explicación directa en los `.py`:

- en `META_BOT.py`, sobre base única y contención del resultado final en el rango flotante;
- en `LONG.py` y `SORT.py`, sobre por qué se mantienen ambos extremos (`maximo_desde_entrada` y `minimo_desde_entrada`).

## 6) Conclusiones

1. La definición de porcentajes flotantes queda unificada y explícita.
2. La comparabilidad con `rentabilidad_pct` queda resuelta al usar `capital_antes_eur` como base común.
3. La inclusión de `precio_salida` en los extremos evita incoherencias por gaps de salida.
4. La evidencia de ejecución confirma consistencia total (0 incoherencias en 67 operaciones).
