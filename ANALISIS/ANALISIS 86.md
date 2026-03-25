# VERSION 2.2.2 — ANALISIS 86 (DOCUMENTO UNIFICADO DE CIERRE)

## Estado de la tarea

La **Tarea 86** queda consolidada en este único documento, unificando la validación final de la familia de salida compuesta basada en:

1. `max_ganancia_flotante_eur` (MFE) mínimo,
2. porcentaje de devolución sobre ese máximo favorable,
3. condición de debilidad de impulso `ret20 < 0`.

---

## Objetivo de la ronda final

Determinar si la familia 86 ofrece una mejora operativa real del sistema sin tocar entradas ni señales base, mediante una ronda cerrada y disciplinada (sin optimización libre).

---

## Alcance y restricciones aplicadas

- No se modifican reglas de entrada.
- No se modifica estrategia base fuera de la familia 86.
- No se prueban variantes adicionales fuera de las definidas.
- Se fuerza veredicto final de continuidad o descarte operativo.

---

## Variantes comparadas (solo estas)

- **86a:** MFE `>= 300 €`, devolución `>= 70 %`, `ret20 < 0`
- **86b:** MFE `>= 400 €`, devolución `>= 70 %`, `ret20 < 0`
- **86c:** MFE `>= 300 €`, devolución `>= 80 %`, `ret20 < 0`
- **86d:** lógica `200 / 70 % / ret20 < 0` solo en **LONG**
- **86e:** lógica `200 / 70 % / ret20 < 0` solo en **SHORT**

---

## Baseline de referencia

- **Capital final:** `22.965,83 €`
- **Beneficio neto total:** `21.965,83 €`
- **Drawdown máximo global:** `-28,4862 %`

---

## Resultado comparado de variantes

| Variante | Activaciones | Capital final (€) | Beneficio neto (€) | Diferencia vs baseline (€) | Drawdown máx global (%) |
|---|---:|---:|---:|---:|---:|
| Baseline | 0 | 22.965,83 | 21.965,83 | 0,00 | -28,4862 |
| 86a | 5 | 21.621,58 | 20.621,58 | -1.344,25 | -28,4862 |
| 86b | 3 | 22.965,83 | 21.965,83 | 0,00 | -28,4862 |
| 86c | 5 | 21.621,58 | 20.621,58 | -1.344,25 | -28,4862 |
| 86d | 4 | 22.965,83 | 21.965,83 | 0,00 | -28,4862 |
| 86e | 5 | 19.689,78 | 18.689,78 | -3.276,05 | -28,4862 |

---

## Lectura estructural de resultados

### 1) Variantes neutras

- **86b** y **86d** generan activaciones principalmente de tipo relabel.
- No cambian PnL agregado.
- No mejoran drawdown máximo.

### 2) Variantes activas con coste

- **86a** y **86c** activan de forma efectiva, pero recortan beneficio neto en `-1.344,25 €`.
- No aportan mejora en drawdown máximo.

### 3) Variante más dañina

- **86e (solo SHORT)** concentra el peor deterioro:
  - `-3.276,05 €` vs baseline,
  - daño concentrado especialmente en SHORT 2022.

---

## Hallazgos solicitados

### Impacto en años malos

- Ninguna variante mejora materialmente los años malos del baseline.
- El principal deterioro diferencial se observa en 2022 SHORT (año fuerte en baseline que queda recortado por salidas prematuras).

### Impacto en ganadoras grandes `>= 300 €`

- Baseline: 18 operaciones.
- 86a/86c: 17.
- 86b/86d: 18.
- 86e: 16.

### Impacto en ganadoras fuertes `>= 1000 €`

- Baseline: 8 operaciones.
- 86a/86b/86c/86d: 8.
- **86e: 6**.

### Peor operación individual

No mejora en ninguna variante:

- `2026-01-23 -> 2026-02-05`
- `-1.029,50 €`

### Resultado separado LONG vs SHORT

| Variante | LONG neto (€) | SHORT neto (€) |
|---|---:|---:|
| Baseline | 17.434,56 | 4.531,27 |
| 86a | 17.434,56 | 3.187,02 |
| 86b | 17.434,56 | 4.531,27 |
| 86c | 17.434,56 | 3.187,02 |
| 86d | 17.434,56 | 4.531,27 |
| 86e | 17.434,56 | 1.255,22 |

Conclusión de módulo: el daño operativo aparece sobre todo en SHORT.

---

## Trades que cambian (síntesis consolidada)

- **86a / 86c:** alteran la secuencia SHORT de 2022 con salidas más tempranas y peor captura posterior.
- **86b / 86d:** cambios principalmente de motivo, sin impacto agregado material.
- **86e:** máximos cambios efectivos en SHORT (incluye recorte severo de operaciones que en baseline eran grandes ganadoras).

---

## Veredicto final de la Tarea 86

La familia 86 **no queda validada como mejora operativa global** del sistema en esta ronda final cerrada.

Razones de cierre:

1. Las variantes activas destruyen captura neta.
2. Las variantes neutras no aportan edge real.
3. No hay mejora en drawdown máximo global.
4. No hay mejora en extremos de pérdida.

### Decisión

Se cierra la Tarea 86 como hilo principal de mejora:

- no hay variante activa apta para producción,
- no hay beneficio-riesgo superior al baseline,
- el coste de oportunidad de las variantes activas es inaceptable para despliegue.

[PEGA AQUÍ EXACTAMENTE EL MISMO BLOQUE DE SALIDA ESTÁNDAR DE LA TAREA 77]
