# TAREA 84 — CORREGIR Y ESTANDARIZAR LOS PORCENTAJES FLOTANTES

## Diagnóstico del problema

Se detectó una incoherencia conceptual entre el **resultado final del trade en %** (`rentabilidad_pct`) y los porcentajes flotantes solicitados (`max_ganancia_flotante_pct`, `max_perdida_flotante_pct`):

1. No existía una definición única y explícita implementada para esos dos campos en el motor actual.
2. El cálculo de `rentabilidad_pct` ya estaba definido sobre `capital_antes_eur`.
3. Si los flotantes se calculan con otra base (por ejemplo capital desplegado), se mezclan denominadores y la comparación directa deja de ser coherente.
4. Además, para asegurar que el resultado final quede dentro del rango flotante, hay que contemplar también el `precio_salida` dentro de los extremos observados (`maximo_desde_entrada` / `minimo_desde_entrada`), evitando desajustes por gaps entre cierre y apertura.

## Definición elegida

Se unificó la definición sobre **`capital_antes_eur`** (opción 1):

- `max_ganancia_flotante_pct = max_ganancia_flotante_eur / capital_antes_eur * 100`
- `max_perdida_flotante_pct = max_perdida_flotante_eur / capital_antes_eur * 100`

Motivo principal: `rentabilidad_pct` ya está sobre esa misma base, por lo que los tres porcentajes pasan a ser comparables de forma directa y estable.

## Cómo se calcula ahora

### Base común

Todos estos porcentajes usan el mismo denominador:

- `capital_antes_eur`

### Fórmulas en EUR (incluyendo comisión, igual que el resultado final)

Para **LONG**:

- `beneficio_neto = (precio_salida - precio_entrada) * unidades - comisión`
- `max_ganancia_flotante_eur = (maximo_flotante - precio_entrada) * unidades - comisión`
- `max_perdida_flotante_eur = (minimo_flotante - precio_entrada) * unidades - comisión`

Para **SHORT**:

- `beneficio_neto = (precio_entrada - precio_salida) * unidades - comisión`
- `max_ganancia_flotante_eur = (precio_entrada - minimo_flotante) * unidades - comisión`
- `max_perdida_flotante_eur = (precio_entrada - maximo_flotante) * unidades - comisión`

### Extremos usados

- `maximo_flotante = max(maximo_desde_entrada, precio_salida)`
- `minimo_flotante = min(minimo_desde_entrada, precio_salida)`

Con esto, el precio de salida siempre queda dentro de `[minimo_flotante, maximo_flotante]`.

## Ejemplos de coherencia

### Coherencia de base

Al usar `capital_antes_eur` en:

- `rentabilidad_pct`
- `max_ganancia_flotante_pct`
- `max_perdida_flotante_pct`

se eliminan comparaciones entre métricas con distinto denominador.

### Coherencia de rango

Como el `precio_salida` se incluye explícitamente en los extremos flotantes, y se aplica la misma comisión en los tres cálculos (final, máximo favorable y máximo adverso), el resultado final en porcentaje queda acotado por:

- `max_perdida_flotante_pct <= rentabilidad_pct <= max_ganancia_flotante_pct`

En validación de la ejecución completa (`67` operaciones), no aparecen incoherencias en esa condición.

## Conclusiones

1. Se corrigió y estandarizó la definición de porcentajes flotantes.
2. La base única seleccionada fue `capital_antes_eur` para mantener coherencia con `rentabilidad_pct`.
3. Se robusteció el rango flotante incluyendo el precio real de salida en los extremos.
4. Se verificó que desaparecen incoherencias graves entre resultado final % y rango flotante %.
