# TAREA 78 — STOP MONETARIO CONDICIONADO POR RET20 NEGATIVO

## objetivo
Implementar una salida defensiva adicional para operaciones abiertas, manteniendo intactas las entradas y la lógica base de señales.

Regla aplicada:
- Si la pérdida flotante de la posición es `<= -200 €`
- y `ret20 < 0`
- entonces se fuerza salida con motivo explícito `STOP_200_RET20_NEG`.

## lógica implementada
Se añadió en `META_BOT.py`:
1. Cálculo de `ret20` como retorno de 20 sesiones sobre `qqq_close`.
2. Nueva condición de salida dentro del motor cuando hay operación abierta:
   - valoración flotante con la misma convención del sistema (mark-to-market con `qqq3_close` y PnL bruto por unidades, según sea LONG o SHORT),
   - comprobación conjunta `beneficio_flotante_eur <= -200` y `ret20 < 0`,
   - asignación de motivo `STOP_200_RET20_NEG`.
3. Prioridad de esta nueva condición sobre la salida estándar del módulo en ese mismo día.

No se modificaron señales de entrada ni la lógica base de generación de señales.

## comparación frente a no usar este filtro
Comparativa corrida completa:

- **Sin filtro (baseline)**
  - operaciones: 67
  - beneficio neto total: **21.965,83 €**
  - capital final: **22.965,83 €**
  - drawdown máx global: **-28,4862 %**

- **Con filtro STOP_200_RET20_NEG**
  - operaciones: 67
  - beneficio neto total: **22.405,83 €**
  - capital final: **23.405,83 €**
  - drawdown máx global: **-28,4862 %**

**Impacto neto:** +**440,00 €** en beneficio acumulado, mismo número de trades y mismo drawdown máximo global en esta muestra.

## cuántos trades se cierran por esta regla
Se cerraron **5 trades** con motivo `STOP_200_RET20_NEG`.

## cuántos eran trades que luego acababan recuperándose
Definición usada: trades cerrados por la nueva regla que, en baseline (sin la regla), acaban con beneficio neto positivo al final de su ciclo.

Resultado: **0 trades**.

## impacto sobre drawdown
- Drawdown máximo global de la curva por operaciones: **sin cambios** en esta corrida (**-28,4862 %** antes y después).
- Aunque no cambia el mínimo global, sí mejora pérdidas en al menos un caso concreto (entrada 2024-08-20), reduciendo daño local en ese tramo.

## impacto sobre grandes ganadoras
Definición usada de “grandes ganadoras”: trades con beneficio neto `>= 1.000 €`.

- baseline: **8**
- con filtro: **8**

Además:
- máxima ganadora: **4.998,50 €** en ambos casos,
- promedio top-5 ganadoras: **2.993,38 €** en ambos casos.

=> No hay erosión observable de la cola de grandes ganancias en esta muestra.

## conclusiones
1. La regla se integró de forma conservadora y sin tocar lógica de entrada.
2. El filtro aporta mejora neta de resultado (+440 €) en el histórico actual.
3. No se detectaron “falsos stops” que luego terminaran en ganador (0 recuperaciones).
4. No afecta negativamente a grandes ganadoras en esta muestra.
5. El drawdown máximo global no cambia, aunque sí hay mejora puntual de pérdidas en determinados trades.

En conjunto, el `STOP_200_RET20_NEG` se comporta como una defensa razonable bajo deterioro de impulso corto (`ret20 < 0`) con coste de oportunidad bajo en el backtest actual.

## comparación de la misma lógica con varios umbrales
Se probó exactamente la misma regla (`ret20 < 0` + stop monetario flotante) variando solo el umbral:

-150, -200, -250 y -300.

Referencia sin filtro (stop prácticamente desactivado con umbral extremadamente bajo):
- operaciones: 67
- beneficio neto: 21.965,83 €
- capital final: 22.965,83 €
- stops por esta regla: 0

Resultados:

| Umbral stop flotante (€) | Operaciones | Cierres `STOP_200_RET20_NEG` | Beneficio neto (€) | Capital final (€) | Drawdown máx (%) |
|---:|---:|---:|---:|---:|---:|
| -150 | 68 | 7 | 22.084,83 | 23.084,83 | -28,4862 |
| -200 | 67 | 5 | 22.405,83 | 23.405,83 | -28,4862 |
| -250 | 67 | 4 | 22.405,83 | 23.405,83 | -28,4862 |
| -300 | 67 | 4 | 22.405,83 | 23.405,83 | -28,4862 |

Lectura rápida:
- El mejor resultado final en este histórico lo dan **-200, -250 y -300** (empate en beneficio/capital).
- **-150** fuerza más salidas (7) y empeora frente a -200.
- El drawdown máximo global no cambia en estos escenarios.

## conclusión sobre umbrales
Para este dataset, el punto de equilibrio práctico está en **-200**:

1. Es el umbral más estricto que ya alcanza el mejor resultado final.
2. Umbrales más laxos (-250/-300) no mejoran adicionalmente.
3. Umbral más agresivo (-150) sobre-filtra y reduce rendimiento.

Conclusión operativa: **mantener -200 €** es razonable por simplicidad y por relación robustez/rendimiento observada.
