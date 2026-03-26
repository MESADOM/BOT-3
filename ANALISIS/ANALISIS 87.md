# VERSION 2.2.6 — Mejora introducida

## Cambio de versión

La versión operativa del sistema queda actualizada a **2.2.6**.

## Mejora introducida en 2.2.6

Se mantiene la estrategia base (entradas y señales) y se incorpora de forma explícita una salida defensiva adicional (**Lógica A**) con estas reglas:

- `ret20 < 0`
- `beneficio_flotante_eur <= -200`
- motivo de salida: `STOP_200_RET20_NEG`

## Objetivo de la mejora

- Forzar salida solo cuando hay deterioro real de la operación (pérdida flotante relevante + momentum corto negativo).
- Mantener claridad y trazabilidad con un motivo de salida único y legible.
- Conservar el framework general sin introducir nuevas familias de reglas.

## Trazabilidad

La ejecución registra en métricas el contador:

- `activaciones_logica_a`

Esto permite auditar cuántas veces se activó la mejora en cada corrida.
