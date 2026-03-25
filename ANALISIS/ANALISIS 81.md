# TAREA 81 — PROTECCION BREAK-EVEN TRAS BENEFICIO FLOTANTE RELEVANTE

## Descripción de la lógica

Se implementó la protección en el **motor principal** (`META_BOT.py`) para no alterar la estrategia base de los módulos LONG/SHORT:

1. En cada sesión con posición abierta, el motor calcula `ganancia_flotante_eur`.
2. Actualiza `max_ganancia_flotante_eur` con el máximo flotante observado.
3. Si `max_ganancia_flotante_eur >= 300`, activa `proteccion_break_even_activa`.
4. Desde ese punto, si `ganancia_flotante_eur <= 0`, marca salida con motivo `BREAK_EVEN_TRAS_300`.
5. Si no aplica break-even, mantiene intactas las salidas originales (`TRAILING` / `SIGNAL`) de LONG/SHORT.

Si una operación nunca alcanza +300 € flotantes, la regla no aplica.

## Cuántas operaciones protege

- Operaciones protegidas por la regla (`BREAK_EVEN_TRAS_300`): **2**.

## Cuántas ganadoras recorta antes de tiempo

- Ganadoras recortadas por esta regla: **0**.

## Cuántas operaciones que acabaron perdiendo habría salvado

- Operaciones que en la versión previa acababan en pérdida y pasan a no-pérdida por esta regla: **0**.

## Impacto en drawdown y beneficio neto

Comparativa contra la versión previa (sin la protección):

- Beneficio neto total:
  - Antes: **21,965.83 €**
  - Ahora: **21,924.83 €**
  - Cambio: **-41.00 €**

- Drawdown máximo global:
  - Antes: **-28.4862%**
  - Ahora: **-28.4862%**
  - Cambio: **0.0000 pp**

## Conclusiones

- La regla entra en muy pocas operaciones históricas (2/62), por lo que su impacto global es pequeño.
- No recorta ganadoras en este histórico.
- Reduce una pérdida grande pero empeora otra, con efecto neto ligeramente negativo en beneficio final.
- El drawdown máximo global no cambia en la muestra.
- Funcionalmente, la protección queda correctamente aplicada: tras superar +300 € flotantes, cualquier vuelta a 0 € o menos fuerza salida con motivo claro `BREAK_EVEN_TRAS_300`.
