# TAREA 77 — STOP MONETARIO FIJO SIMPLE

## Objetivo de la prueba
Validar el impacto de introducir un cierre obligatorio por pérdida flotante fija por operación de **-200 €** (nuevo motivo `STOP_MONETARIO_200`) manteniendo intactas las señales de entrada y la lógica base de generación de señales.

## Cambios realizados
- Se añadió en `META_BOT.py` un umbral global `STOP_MONETARIO_EUR = -200.0` y el motivo de salida `STOP_MONETARIO_200`.
- Se integró el stop dentro del flujo estructural del motor de salida (no como análisis paralelo):
  - cálculo diario de beneficio flotante para long y short con la misma convención ya usada (diferencia de precio por unidades),
  - disparo de salida cuando `beneficio_flotante_hoy <= -200`.
- Se añadió el seguimiento de extremos flotantes por operación:
  - `max_ganancia_flotante_eur`, `max_perdida_flotante_eur`,
  - fechas asociadas de máximos/mínimos flotantes,
  - porcentajes flotantes respecto al capital previo a la entrada.
- Se adaptó la salida tabulada para mostrar exactamente las columnas solicitadas, en el orden solicitado.
- Se cambió serialización numérica TSV para usar punto decimal (`.`).
- Versión del sistema actualizada a `2.2.3`.

## Años o tramos donde más afecta
Impacto principal por beneficio neto anual (nuevo sistema vs versión previa inmediata):
- **2025: -1711.00 €** (mayor impacto negativo).
- **2024: +440.00 €**.
- **2026: +393.50 €**.
- **2023: +363.00 €**.

Distribución de cierres por `STOP_MONETARIO_200`:
- 2020: 1
- 2021: 1
- 2023: 2
- 2024: 1
- 2025: 3
- 2026: 1

## Cuántas operaciones fueron cerradas por este nuevo stop
- Total operaciones cerradas por `STOP_MONETARIO_200`: **9**.

## Cuántas operaciones originalmente ganadoras habría cortado
Comparando contra la ejecución inmediatamente anterior (sin este stop monetario), y emparejando por fecha de entrada + señal de entrada:
- Operaciones que el nuevo stop cerró y que en la versión previa acababan ganando: **1**.

## Impacto en beneficio neto
- Beneficio neto total versión previa: **21,965.83 €**.
- Beneficio neto total con `STOP_MONETARIO_200`: **21,451.33 €**.
- Impacto neto: **-514.50 €**.

## Impacto en drawdown
- Drawdown máximo versión previa: **-28.4862 %**.
- Drawdown máximo con `STOP_MONETARIO_200`: **-28.4862 %**.
- Cambio observado: **0.0000 pp**.

## Conclusiones y riesgos
- El stop monetario fijo queda implementado de forma estructural y homogénea para long/short.
- Reduce de forma directa pérdidas extremas por operación, pero en este histórico concreto también:
  - aumenta rotación (67 -> 69 operaciones),
  - reduce beneficio agregado total (-514.50 €),
  - corta al menos una operación que antes terminaba ganadora.
- Riesgo principal: un umbral fijo en euros no escala automáticamente con volatilidad ni con tamaño de posición relativo; puede resultar demasiado estricto en ciertos tramos (especialmente en entornos tendenciales con ruido alto) y demasiado laxo en otros.
- Recomendación futura (no aplicada en esta tarea): evaluar sensibilidad del umbral por tramos de volatilidad para mantener robustez sin romper el requisito actual de stop fijo.
