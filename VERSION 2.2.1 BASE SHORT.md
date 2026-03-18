# VERSION 2.2.1 BASE SHORT

## Summary
Se fija como versión base 2.2.1 la lógica definitiva del módulo short, manteniendo intacta la pata long, el sizing short vigente, las comisiones, el capital inicial y la estructura general del motor. La activación short queda restringida a contexto bajista real con confirmación de 1 día y trailing stop short del 8%.

## Reglas definitivas del módulo short
- El short solo se activa en estructura bajista real.
- La estructura bajista real queda definida por la concurrencia simultánea de las siguientes condiciones sobre QQQ y sus métricas de régimen:
  - `QQQ < SMA200`
  - `SMA50 < SMA200`
  - `retorno_63 < -0.08`
  - `cruces_sma50_ventana < 4`
- La confirmación short definitiva es de 1 día.
- Se mantienen los bloqueos short existentes de reentrada y salida en todo lo que no entre en conflicto con la definición anterior.
- El trailing stop short definitivo es del 8%.
- Se mantiene la lógica de salida short actual.
- Se mantiene el sizing short actual.
- La lógica long no se modifica.

## Decisiones descartadas
Se deja constancia de que fueron probadas previamente y no se adoptan como base de la versión 2.2.1 las siguientes alternativas:
- `retorno_63 < -0.04`
- `retorno_63 < -0.12`
- confirmación short de 2 días
- `cruces_sma50_ventana < 3`
- `cruces_sma50_ventana < 2`
- salida short inmediata por pérdida de señal
- sizing short al 75%
- sizing short al 50%
- sizing short al 25%

## Conclusión
El short sí aporta valor al sistema, pero solo cuando está fuertemente filtrado. La mejora del short proviene de seleccionar mejor el contexto bajista y de utilizar un trailing stop más ceñido. No se adopta una reducción de sizing ni una salida más agresiva porque empeoran el equilibrio global entre rentabilidad y riesgo.
