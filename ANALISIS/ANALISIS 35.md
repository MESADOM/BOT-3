# VERSION 2.2.2 CANDIDATA IMPLEMENTACION 01

## 1. Objetivo

Dejar implementada en el sistema una versión derivada de la **VERSION 2.2.1** que incorpora **únicamente** un filtro anti-sobreextensión short por distancia a `SMA200`, sin añadir más cambios de lógica sobre long, trailing, sizing, confirmación short ni estructura bajista base.

## 2. Base usada

La base usada es la lógica vigente documentada en `VERSION 2.2.1 BASE SHORT.md` y ejecutada en `SORT.py`.

Se mantiene intacto todo lo siguiente:

- estructura bajista real short;
- confirmación short de 1 día;
- trailing stop short del 8%;
- sizing short vigente;
- bloqueos existentes de reentrada;
- lógica long actual.

## 3. Cambio exacto implementado

Se añadió una comprobación **adicional y aislada** en la validación de entrada short de `SORT.py`, quedando integrada ya en el flujo normal del sistema.

Ese chequeo:

- **no reemplaza** ninguna condición base de la 2.2.1;
- **solo añade** un bloqueo extra previo a la entrada short;
- queda encapsulado en funciones separadas para que la diferencia respecto a la base sea visible y fácilmente trazable.

## 4. Regla del filtro anti-sobreextensión

Regla experimental implementada exactamente:

- bloquear entrada short si `QQQ / SMA200 - 1 <= -0.15`.

Equivalencia exacta usada en código:

- `QQQ / SMA200 - 1`
- se implementa como
- `qqq_close_referencia / sma200_referencia - 1`

La equivalencia es exacta porque `qqq_close_referencia` representa el precio de referencia diario de `QQQ` usado por el motor y `sma200_referencia` representa la `SMA200` del mismo punto temporal.

## 5. Archivos modificados

- `SORT.py`
- `ANALISIS/ANALISIS 35.md`

## 6. Parámetros añadidos

Se añadió una constante explícita en `SORT.py`:

- `UMBRAL_BLOQUEO_SOBREEXTENSION_SHORT_SMA200 = -0.15`

Interpretación:

- el umbral `-0.15` queda visible, explícito y fácilmente reversible.
- la regla queda aplicada de forma global, sin depender de un interruptor adicional.

## 7. Forma de activar/desactivar la candidata

La regla ya no depende de una variable booleana.

Si en el futuro se quisiera revertir, bastaría con retirar la llamada al bloqueo `_bloquear_short_por_sobreextension_sma200(hoy)` dentro de `permite_entrada(...)` o eliminar esa función adicional.

## 8. Confirmación de que no se tocó:

### lógica long

No se modificó ningún archivo ni ninguna condición de la pata long.

### trailing

No se modificó el trailing short del 8% ni la lógica de salida short.

### sizing

No se modificó ningún parámetro ni regla de sizing.

### confirmación short

No se modificó la confirmación short de 1 día.

### `SMA50 < SMA200`

No se relajó ni se alteró la condición estructural `SMA50 < SMA200`.

## 9. Riesgos o advertencias

- La regla queda integrada en el sistema y, aunque ya no depende de un toggle, sigue partiendo de una evidencia previa concentrada en pocos episodios.
- Los análisis previos indican que la señal es prometedora pero frágil y muy sensible a pocos episodios.
- El caso problemático de `2025-04-15` seguía vivo en la evidencia previa; por tanto, este cambio no debe interpretarse como resolución general del problema short tardío.
- La mejora sigue siendo un cambio localizado en short; no debe extrapolarse como validación automática de otras líneas de mejora.

## 10. Conclusión final breve

Queda implementada una **VERSION 2.2.2** con un único cambio sobre la base short: bloquear entradas short cuando `QQQ / SMA200 - 1 <= -0.15`; el resto de la lógica permanece intacto y el cambio sigue siendo simple de localizar y revertir.
