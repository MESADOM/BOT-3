# VERSION 2.2.2 ANALISIS 75

## 1. Objetivo

Emitir un dictamen metodológico sobre si la evidencia acumulada ya permite **priorizar una familia concreta de modulación de exposición por régimen** para la siguiente tanda de investigación, o si todavía conviene **mantener una fase exploratoria sin priorización cerrada**.

El foco de este documento es deliberadamente prudente:

- **no** diseña reglas definitivas;
- **no** implementa nada en producción;
- **no** declara ninguna familia lista para operar;
- y **sí** decide si la investigación ya puede concentrarse en una familia concreta o si todavía necesita una comparación adicional.

La decisión debe responder a una pregunta muy concreta: con la evidencia disponible, ¿tiene sentido abrir ya una tanda específica centrada en la **familia nominal**, en la **familia porcentual**, o es metodológicamente más sano **seguir explorando sin priorizar todavía**?

---

## 2. Evidencia revisada

### 2.1. Lectura obligatoria solicitada

Se han leído obligatoriamente:

- `ANALISIS 64.md`
- `ANALISIS 65.md`
- `ANALISIS 66.md`
- `ANALISIS 67.md`
- `ANALISIS 68.md`
- `ANALISIS 69.md`
- `ANALISIS 70.md`
- `ANALISIS 71.md`

También se ha intentado leer, como exigían las instrucciones:

- `ANALISIS 72.md`
- `ANALISIS 73.md`
- `ANALISIS 74.md`

Pero **esos tres archivos no existen actualmente en el repositorio**, por lo que no pueden formar parte de la evidencia literal. El dictamen se apoya, por tanto, en la cadena verificable realmente disponible `64–71`, sin inventar continuidad documental inexistente.

### 2.2. Qué deja la evidencia acumulada

La cadena `64–71` deja una base metodológica relativamente clara:

1. **El selector sí tiene valor analítico real**, pero todavía como capa de modulación prudente más que como motor de ramificación completa.
2. **`MIXTO` no es una clase residual**: concentra gran parte del beneficio histórico del general, aunque con más tensión y drawdown.
3. **`PROBLEMATICO` no equivale a inutilidad operativa**, pero su absorción histórica todavía presenta concentración y heterogeneidad interna.
4. **La siguiente fase debe seguir siendo simple, auditable y reversible**, porque la evidencia todavía no justifica una arquitectura compleja.
5. Dentro de las familias de exposición, la discusión ya se ha estrechado sobre dos candidatas principales:
   - **familia nominal**: topes máximos nominales por régimen;
   - **familia porcentual**: reducción proporcional o multiplicadores de exposición por régimen.

### 2.3. Pregunta metodológica real en este punto

Ya no se trata de decidir si la exposición por régimen merece investigación en abstracto. Eso ya quedó suficientemente abierto en `68–71`.

La pregunta real ahora es más exigente:

- si alguna de las dos familias principales ya muestra **madurez suficiente** para recibir prioridad;
- o si la diferencia entre ambas todavía es demasiado incompleta como para cerrar esa prioridad con rigor.

---

## 3. Madurez de la familia nominal

### 3.1. Sentido económico

La familia nominal tiene un sentido económico claro y fácil de defender:

- impone una barrera externa al tamaño máximo comprometido;
- ayuda a contener expansión excesiva en contextos dudosos;
- y encaja bien con la intuición de proteger más en `MIXTO` y `PROBLEMATICO` sin rediseñar la lógica del sistema.

Ese sentido económico es especialmente comprensible en una fase exploratoria porque la regla actúa como **freno visible** más que como ajuste fino opaco.

**Juicio:** sentido económico **medio-alto**.

### 3.2. Valor histórico sugerido por la evidencia

La evidencia acumulada sugiere que la familia nominal **merece investigación**, sobre todo porque:

- `MIXTO` aporta mucho valor histórico, pero con tensión suficiente como para justificar disciplina adicional;
- `PROBLEMATICO` sigue siendo una clase hostil, aunque no inutilizable;
- y un tope nominal podría actuar como protección simple donde no conviene dejar crecimiento totalmente libre.

Sin embargo, el valor histórico observado es todavía **indirecto**:

- no procede de una demostración empírica amplia de que el nominal mejore resultados;
- procede más bien de una lectura conceptual coherente con la evidencia de riesgo y heterogeneidad de `64–71`.

**Juicio:** valor histórico **moderado, pero todavía inferido más que demostrado**.

### 3.3. Preservación del general

Aquí la familia nominal puntúa bien:

- conserva el sistema general;
- no toca señales;
- no obliga a reinterpretar clases;
- y su agresividad sobre la arquitectura es baja.

Es una familia defensiva y externa, lo que favorece una buena preservación del baseline.

**Juicio:** preservación del general **alta**.

### 3.4. Facilidad operativa

Es probablemente su mejor punto:

- muy fácil de explicar;
- muy fácil de auditar;
- muy fácil de implementar en una fase futura;
- muy compatible con control operativo y con una integración tipo IBKR.

**Juicio:** facilidad operativa **muy alta**.

### 3.5. Robustez razonable esperable

La familia nominal presenta una robustez potencial aceptable por simplicidad, pero no todavía por validación histórica.

Puntos a favor:

- pocos grados de libertad;
- poca ambigüedad estructural;
- menor riesgo de sobreajuste que alternativas más continuas.

Puntos en contra:

- depende mucho del valor nominal elegido;
- el importe puede volverse arbitrario frente al capital acumulado y al crecimiento compuesto;
- una barrera única puede tratar de forma demasiado tosca clases y momentos muy distintos.

**Juicio:** robustez razonable **media**, apoyada más en simplicidad que en evidencia demostrada.

### 3.6. Grado de madurez agregado de la familia nominal

Evaluación sintética:

- **grado de madurez:** **medio-alto para seguir investigando**;
- **claridad del valor añadido:** **alta en disciplina y auditabilidad**, **media** en mejora histórica todavía no demostrada;
- **riesgos pendientes:** arbitrariedad del importe, rigidez excesiva, riesgo de capar fases favorables o episodios absorbibles de `PROBLEMATICO`;
- **coste de complejidad:** **bajo**;
- **facilidad de futura implementación:** **muy alta**.

Conclusión parcial: la familia nominal está **bien preparada como candidata seria**, pero su ventaja todavía parece apoyarse más en la simplicidad que en una evidencia diferencial concluyente frente a la familia porcentual.

---

## 4. Madurez de la familia porcentual

### 4.1. Sentido económico

La familia porcentual también tiene sentido económico claro:

- permite traducir el régimen a una **cautela proporcional**;
- mantiene la relación entre exposición y contexto sin introducir cortes duros;
- y se adapta mejor al crecimiento del sistema que un nominal fijo.

Su lógica parece especialmente coherente con una evidencia donde:

- `MIXTO` tiene valor real, pero no limpio;
- `PROBLEMATICO` contiene episodios absorbibles y otros no;
- y conviene modular intensidad sin apagar ni capar de forma brusca la operativa útil.

**Juicio:** sentido económico **alto**.

### 4.2. Valor histórico sugerido por la evidencia

La familia porcentual parece alinearse muy bien con lo que sugieren `68`, `69` y `71`:

- aparece como la forma más natural de dosificar la exposición;
- preserva mejor el carácter continuo del sistema general;
- y parece mejor adaptada a la mezcla de productividad y tensión observada en `MIXTO` y en partes de `PROBLEMATICO`.

Aun así, el valor histórico sigue siendo mayoritariamente **prospectivo**:

- la cadena revisada argumenta con fuerza su idoneidad metodológica;
- pero todavía no demuestra con una comparación empírica cerrada que supere ya a la familia nominal.

**Juicio:** valor histórico **moderado-alto como hipótesis**, pero todavía **no decisivo**.

### 4.3. Preservación del general

La familia porcentual también preserva bien el general, e incluso en algunos sentidos mejor que la nominal:

- conserva señales y arquitectura;
- mantiene el sistema como baseline;
- y evita cortes absolutos que podrían amputar de forma innecesaria la captura de años fuertes.

Su principal virtud aquí es la continuidad: ajusta intensidad, no capacidad de forma binaria.

**Juicio:** preservación del general **alta**.

### 4.4. Facilidad operativa

La facilidad operativa sigue siendo buena, aunque algo peor que la nominal:

- es intuitiva;
- puede implementarse sin gran dificultad;
- pero exige más cuidado al definir multiplicadores y escalones;
- y es algo menos trivial de auditar manualmente que un tope absoluto.

**Juicio:** facilidad operativa **alta**, pero no máxima.

### 4.5. Robustez razonable esperable

Aquí aparece su principal tensión metodológica.

Puntos a favor:

- se adapta mejor al capital y a la evolución del sistema;
- trata mejor la gradación entre regímenes;
- puede proteger sin imponer rigidez extrema.

Puntos en contra:

- invita con facilidad a probar demasiados porcentajes;
- abre una superficie paramétrica más amplia;
- y por tanto aumenta el riesgo de sobreoptimización si no se acota con mucha disciplina.

**Juicio:** robustez razonable **media**, potencialmente buena en teoría, pero más frágil que la nominal si el proceso investigador pierde control.

### 4.6. Grado de madurez agregado de la familia porcentual

Evaluación sintética:

- **grado de madurez:** **medio-alto para investigación específica**;
- **claridad del valor añadido:** **alta** en coherencia con la modulación por régimen, **media** en superioridad todavía no demostrada;
- **riesgos pendientes:** exceso de grados de libertad, sobreoptimización de multiplicadores, falsa precisión prematura;
- **coste de complejidad:** **medio**;
- **facilidad de futura implementación:** **alta**.

Conclusión parcial: la familia porcentual parece **ligeramente más natural** como traducción del régimen a exposición, pero también introduce más sensibilidad paramétrica y todavía no tiene una superioridad empírica suficientemente cerrada para recibir prioridad automática.

---

## 5. Riesgos pendientes

Los riesgos que siguen abiertos son suficientemente relevantes como para frenar una priorización apresurada.

### 5.1. Riesgos comunes a ambas familias

1. **La evidencia sigue siendo más conceptual que confirmatoria.**  
   La cadena `64–71` justifica abrir investigación, pero no cierra todavía una victoria clara entre nominal y porcentual.

2. **`MIXTO` y `PROBLEMATICO` siguen siendo delicados.**  
   `MIXTO` concentra mucho valor y mucho drawdown; `PROBLEMATICO` conserva heterogeneidad interna y absorción no plenamente robusta.

3. **La muestra útil no es tan amplia como para premiar ajustes finos.**  
   Sobre todo en entornos hostiles, el riesgo de extraer conclusiones demasiado fuertes a partir de pocos bloques sigue presente.

4. **Existe peligro real de confundir plausibilidad con validación.**  
   Que una familia sea elegante o intuitiva no significa todavía que merezca prioridad cerrada.

### 5.2. Riesgos específicos de la familia nominal

- arbitrariedad del importe absoluto;
- posible incoherencia con el crecimiento compuesto;
- rigidez excesiva en años fuertes;
- tratamiento demasiado tosco de contextos heterogéneos.

### 5.3. Riesgos específicos de la familia porcentual

- proliferación de multiplicadores y escalones;
- mayor riesgo de sobreajuste;
- tentación de afinar demasiado pronto diferencias entre `FAVORABLE`, `MIXTO` y `PROBLEMATICO`;
- complejidad analítica superior a la de la familia nominal.

---

## 6. Condiciones mínimas para priorizar

Para priorizar una familia concreta en la siguiente tanda, debería cumplirse un umbral metodológico mínimo más exigente que el actual.

### 6.1. Condiciones mínimas generales

Una familia debería mostrar simultáneamente:

1. **sentido económico claro y no meramente narrativo**;
2. **valor añadido histórico reconocible** frente al baseline y frente a la otra familia;
3. **preservación razonable del general** en años o clases productivas;
4. **coste de complejidad contenido**;
5. **robustez razonable** sin depender de una calibración excesivamente fina;
6. **facilidad de implementación futura** suficiente para no convertir la investigación en un problema de ingeniería innecesario.

### 6.2. Qué faltaría para priorizar nominal

La familia nominal debería demostrar mejor que:

- su simplicidad no se paga con una pérdida excesiva de captura útil;
- el valor añadido no depende de un importe demasiado arbitrario;
- y su posible ventaja frente a la porcentual no es solo facilidad operativa, sino también calidad metodológica del resultado.

### 6.3. Qué faltaría para priorizar porcentual

La familia porcentual debería demostrar mejor que:

- su mayor naturalidad económica se traduce en una mejora defendible y no solo elegante;
- no necesita demasiados grados de libertad para funcionar;
- y su ventaja frente a la nominal compensa realmente el mayor coste de complejidad.

---

## 7. Evaluación del estado actual

### 7.1. Comparación sintética entre familias

| Criterio | Familia nominal | Familia porcentual |
|---|---|---|
| Sentido económico | Medio-alto | Alto |
| Valor histórico hoy | Moderado e indirecto | Moderado-alto, pero todavía prospectivo |
| Preservación del general | Alta | Alta |
| Facilidad operativa | Muy alta | Alta |
| Robustez razonable hoy | Media por simplicidad | Media con más sensibilidad paramétrica |
| Coste de complejidad | Bajo | Medio |
| Facilidad de futura implementación | Muy alta | Alta |
| Madurez global actual | Medio-alta | Medio-alta |

### 7.2. Dictamen sobre la madurez relativa

La lectura más prudente es la siguiente:

- **ninguna familia está verde**: ambas merecen investigación seria;
- **ninguna familia está madura de forma concluyente** para monopolizar ya la siguiente tanda;
- la **nominal** gana en simplicidad, auditabilidad y coste de complejidad;
- la **porcentual** gana en naturalidad económica y en continuidad con la idea de modular exposición;
- pero la diferencia entre ambas **todavía no es lo bastante nítida** como para cerrar una priorización sin comparación adicional.

### 7.3. Claridad real del valor añadido

La familia nominal aporta una claridad muy fuerte en **control operativo**.

La familia porcentual aporta una claridad muy fuerte en **coherencia económica con la modulación de exposición**.

El problema metodológico actual es que esas dos fortalezas compiten entre sí y la evidencia disponible todavía no resuelve cuál domina cuando se exige simultáneamente:

- prudencia;
- preservación del general;
- robustez razonable;
- y facilidad de futura implementación.

### 7.4. Juicio metodológico del estado actual

Con la evidencia actual ya **sí tiene sentido** abrir una siguiente tanda más específica, pero **no todavía cerrada en una sola familia**.

La fase ya no debería ser una exploración abierta y difusa de “todo tipo de ideas”, porque la investigación ha madurado lo suficiente como para acotar el foco. Sin embargo, tampoco parece sano saltar directamente a una priorización unilateral de nominal o porcentual.

Por tanto, el estado actual es este:

- ya hay base para una **comparación adicional y disciplinada entre las dos familias principales**;
- no hay todavía base suficiente para afirmar que una de las dos merezca prioridad exclusiva.

---

## 8. Conclusión final

La evidencia acumulada en `ANALISIS 64–71` permite afirmar que la investigación sobre modulación de exposición por régimen **ha alcanzado un nivel de madurez suficiente para dejar atrás la exploración genérica**, pero **todavía no ha alcanzado un nivel de discriminación suficiente para priorizar con rigor una sola familia**.

La familia nominal presenta una ventaja clara en simplicidad, auditabilidad, coste de complejidad y facilidad futura de implementación.

La familia porcentual presenta una ventaja clara en continuidad económica con el problema real de exposición y en capacidad conceptual para modular intensidad sin imponer cortes rígidos.

Sin embargo:

- la ventaja de la nominal todavía parece apoyarse sobre todo en su sencillez;
- la ventaja de la porcentual todavía parece apoyarse sobre todo en su elegancia metodológica;
- y ninguna de las dos ha demostrado todavía un diferencial suficientemente cerrado en valor histórico y robustez como para recibir prioridad exclusiva.

El dictamen prudente, por tanto, no es seguir en una exploración completamente abierta, pero tampoco forzar una priorización prematura.

Lo más sano es **abrir una comparación adicional, limitada y directamente enfocada a nominal vs porcentual**, bajo la misma plantilla de evaluación y sin saltar todavía a reglas finales.

---

## 9. Recomendación: priorizar nominal / priorizar porcentual / seguir explorando

### Recomendación metodológica final

**Abrir comparación adicional.**

Formulado en la terna pedida:

- **priorizar nominal:** **no todavía**;
- **priorizar porcentual:** **no todavía**;
- **seguir explorando:** **sí, pero ya no en fase abierta**, sino en una **exploración comparativa acotada entre familia nominal y familia porcentual**.

### Justificación final del dictamen

Se recomienda **seguir explorando con comparación adicional** porque es la única salida plenamente coherente con la evidencia actual:

- reconoce que la investigación ya maduró y que el foco debe estrecharse;
- evita forzar una prioridad que todavía no está suficientemente ganada;
- preserva la prudencia metodológica exigida por la heterogeneidad de `MIXTO` y `PROBLEMATICO`;
- y mantiene el proceso dentro de una complejidad razonable, sin pasar ni a reglas definitivas ni a producción.

En resumen:

- **sí** hay base para una siguiente tanda específica;
- esa tanda debe centrarse en **nominal vs porcentual**;
- y el dictamen correcto **no** es priorizar una familia única todavía, sino **compararlas de forma directa y disciplinada antes de decidir**.
