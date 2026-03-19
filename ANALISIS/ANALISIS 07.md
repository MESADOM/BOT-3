# ANALISIS 07

## 1. Título
Consolidado maestro del análisis 07 sobre falsos positivos del módulo short en la versión 2.2.1.

## 2. Objetivo del análisis
Concentrar en un único archivo maestro los resultados ya generados para el análisis 07, centrado en detectar **shorts fallidos** (falsos positivos) y resumir qué patrones comunes no quedan filtrados por las reglas actuales, sin rehacer el análisis desde cero salvo en lo imprescindible para verificar consistencia documental.

## 3. Archivos fuente localizados

### Resultados reales del análisis 07
- `VERSION 2.2.1 ANALISIS 07.md`
  - **Tipo:** markdown.
  - **Estado:** resultado real previo del análisis 07.
  - **Uso en esta consolidación:** fuente principal reutilizada para construir este archivo maestro.

### Archivos utilizados para producir o contextualizar el análisis
- `META_BOT.py`
  - **Tipo:** script principal del motor.
  - **Rol:** ejecución del backtest y generación de operaciones para aislar los shorts perdedores.
- `SORT.py`
  - **Tipo:** script / módulo short.
  - **Rol:** reglas de entrada, trailing stop y salida del módulo short analizado.
- `VERSION 2.2.1 BASE SHORT.md`
  - **Tipo:** markdown de referencia funcional.
  - **Rol:** definición de las reglas vigentes de la versión base 2.2.1 del módulo short.
- `datos/QQQ.csv`
  - **Tipo:** CSV de mercado.
  - **Rol:** serie base usada por el motor para señales y métricas de régimen.
- `datos/QQQ3.csv`
  - **Tipo:** CSV de mercado.
  - **Rol:** serie operativa usada por el motor para entradas, salidas y PnL.
- `datos/VIX.csv`
  - **Tipo:** CSV de mercado.
  - **Rol:** dataset cargado por el motor; en esta versión no aporta una pieza diferenciadora explícita al análisis documental final.

### Artefactos intermedios o no persistidos
- **Scripts auxiliares ad-hoc en línea:** usados únicamente en terminal para contar shorts, filtrar perdedores y revisar métricas comparativas.
- **Salidas temporales de consola / TSV temporal:** utilizadas durante la validación manual y eliminadas después.
- **Logs específicos del análisis 07:** no se localizaron archivos persistidos en el repositorio.
- **Figuras / gráficos específicos del análisis 07:** no se localizaron.
- **Outputs auxiliares persistidos del análisis 07:** no se localizaron.

## 4. Metodología realmente utilizada
- Se reutilizó el informe ya generado del análisis 07 como base principal.
- Se ejecutó el motor existente de la versión 2.2.1 para obtener el conjunto de operaciones y verificar la consistencia del informe previo.
- Se aislaron las operaciones con `modulo_activo = SHORT_TREND`.
- Se clasificaron como falsos positivos las operaciones short con `beneficio_neto_eur < 0`.
- Se revisaron exclusivamente las variables ya disponibles en el sistema y ya observadas en el análisis previo:
  - `regimen_entrada`
  - `motivo_regimen`
  - `retorno_63`
  - `cruces_sma50_ventana`
  - distancia de `QQQ` frente a `SMA50`
  - duración
  - motivo de salida
- Para esta consolidación **no se rehízo el análisis desde cero**; solo se reordenó y documentó en un archivo maestro único, verificando que la evidencia previa siguiera siendo coherente con el estado actual del repositorio.

## 5. Resultados principales
- Total de operaciones short detectadas en la versión revisada: **11**.
- Shorts perdedores identificados: **4**.
- Shorts ganadores identificados: **7**.
- El patrón dominante de los shorts fallidos es que **entran con estructura bajista válida para el módulo short, pero el contexto global sigue catalogado como `AGRESIVO`**, dejando abierta la puerta a rebotes fuertes.
- Los falsos positivos no parecen venir de mercado lateral clásico, sino de **entradas short tardías dentro de una caída ya extendida**.
- En los casos perdedores, el fallo se materializa por **rebote técnico que dispara el trailing stop**, no por desaparición progresiva de la señal short.

## 6. Métricas clave

### Resumen agregado
- Shorts totales: **11**.
- Shorts perdedores: **4**.
- Shorts ganadores: **7**.
- Proporción de shorts perdedores: **36,36%**.

### Métricas agregadas de los 4 shorts perdedores
- Beneficio neto medio: **-242,00 €**.
- Rango de beneficio neto: **-462,50 €** a **-27,00 €**.
- Rentabilidad media: **-2,4779%**.
- Duración media: **8 días**.
- Rango de duración: **5 a 10 días**.
- `retorno_63` medio: **-0,1297**.
- `cruces_sma50_ventana`: **0 en los 4 casos**.
- Porcentaje real invertido medio: **33,68%**.
- Unidades ejecutadas: **50 en los 4 casos**.

### Casos perdedores
| Caso | Entrada | Salida | Beneficio neto € | Rentabilidad % | Retorno 63 | Cruces SMA50 | Distancia QQQ vs SMA50 | Motivo salida |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 2016-02-08 | 2016-02-17 | -27,00 | -2,8436% | -0,0828 | 0 | -10,57% | COVER_TRAILING |
| 2 | 2022-10-19 | 2022-10-27 | -89,00 | -0,8487% | -0,0970 | 0 | -7,89% | COVER_TRAILING |
| 3 | 2022-11-09 | 2022-11-14 | -389,50 | -3,7460% | -0,1561 | 0 | -5,72% | COVER_TRAILING |
| 4 | 2025-04-15 | 2025-04-25 | -462,50 | -2,4733% | -0,1830 | 0 | -6,67% | COVER_TRAILING |

## 7. Patrones detectados
1. **Sesgo alcista residual no filtrado.**
   - Los 4 shorts perdedores entran con `regimen_entrada = AGRESIVO`.
   - En los 4 casos el `motivo_regimen` es `AGRESIVO: caso intermedio resuelto a favor del sesgo alcista`.
   - Esto revela una tensión entre la lógica short y la capa de contexto general del sistema.

2. **Short tardío en caída ya extendida.**
   - En los 4 casos, `QQQ` entra claramente por debajo de `SMA50`.
   - La distancia frente a `SMA50` oscila entre **-5,72% y -10,57%**.
   - Esto sugiere que el mercado ya estaba suficientemente estirado como para facilitar rebotes de alivio.

3. **El filtro de cruces no captura este tipo de falso positivo.**
   - Todos los perdedores tienen `cruces_sma50_ventana = 0`.
   - Por tanto, no son episodios de serrucho; son falsos positivos dentro de una caída direccional que revierte con violencia.

4. **La pérdida llega por rebote y barrido del trailing.**
   - Los 4 casos cierran con `COVER_TRAILING`.
   - Ningún caso perdedor cierra por `COVER_SIGNAL`.
   - El problema dominante es el rebote post-entrada, no el deterioro lento de la señal.

5. **Ventana temporal corta de fallo.**
   - Todas las pérdidas ocurren en operaciones relativamente breves.
   - Eso refuerza la idea de que el error no es entrar en un entorno totalmente equivocado a largo plazo, sino entrar tarde justo antes de un rebote técnico fuerte.

6. **Caso de reversión muy rápida.**
   - El caso con entrada **2022-11-09** mostró una reversión especialmente veloz del comportamiento tras la entrada.
   - Es la señal más clara de vulnerabilidad a shortear caídas maduras con capacidad inmediata de rebote.

## 8. Limitaciones o incidencias
- El repositorio **no contiene** un conjunto amplio de artefactos persistidos del análisis 07; el resultado persistido real localizado fue el markdown previo del análisis.
- No se localizaron logs dedicados, figuras, outputs auxiliares ni CSVs específicos generados por el análisis 07.
- La consolidación depende de los resultados disponibles en el estado actual del repositorio y del informe previo ya generado.
- Como el usuario pidió no rehacer el análisis desde cero, esta consolidación prioriza la **reutilización documental** frente a una reexploración completa de hipótesis.
- Existe una inconsistencia textual en la petición original entre `01` y `07`; para mantener coherencia con el análisis realmente existente, se consolida como **ANALISIS 07**.

## 9. Conclusión final breve
El análisis 07 muestra que los falsos positivos del módulo short en la versión 2.2.1 se concentran en **shorts abiertos demasiado tarde dentro de caídas ya maduras**, cuando el sistema todavía mantiene un sesgo global `AGRESIVO` y el mercado conserva capacidad de rebotar con fuerza. La regla actual filtra razonablemente el serrucho, pero todavía **no filtra bien el short tardío previo a rebote técnico**.

## 10. Lista completa de archivos generados o utilizados

### Archivo maestro final generado
- `ANALISIS/ANALISIS 07.md`
  - **Estado final:** entregable principal y archivo maestro único.

### Archivos utilizados como base o evidencia
- `VERSION 2.2.1 ANALISIS 07.md` *(resultado previo reutilizado para consolidación; se elimina tras consolidar para evitar duplicidad de salida)*
- `META_BOT.py`
- `SORT.py`
- `VERSION 2.2.1 BASE SHORT.md`
- `datos/QQQ.csv`
- `datos/QQQ3.csv`
- `datos/VIX.csv`

### Archivos intermedios no persistidos
- Scripts temporales ejecutados en terminal para inspección puntual.
- Salidas temporales de consola usadas durante la validación.
