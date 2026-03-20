# VERSION 2.2.1 ANALISIS 19b

## 1. Objetivo
Decidir si existe base suficiente para proponer una candidata experimental **2.2.2** del módulo short, o si debe mantenerse la **2.2.1** sin cambios por el momento.

## 2. Evidencia revisada
Se ha revisado obligatoriamente la evidencia pedida con este resultado:
- `ANALISIS/ANALISIS 15.md`: **no existe** en el repositorio actual.
- `ANALISIS/ANALISIS 16.md`: leído.
- `ANALISIS/ANALISIS 17.md`: leído.
- `ANALISIS/ANALISIS 18.md`: leído.

Lectura conjunta de la evidencia realmente disponible:
- `ANALISIS 16` reconoce que el filtro short por distancia a `SMA200 <= -15%` mejora el agregado frente a 2.2.1, pero concluye que esa mejora es **temporalmente dudosa** porque depende casi por completo de `2022-H2` y de muy pocos trades.
- `ANALISIS 17` confirma que esa misma mejora sí produce una **mejora global real** frente a la base 2.2.1, al elevar retorno, Sharpe y profit factor global sin empeorar el drawdown máximo de la base.
- `ANALISIS 18` audita esa mejora y la clasifica como **útil pero frágil**, por riesgo de sobreajuste, dependencia de umbral fino y muestra short pequeña.

Conclusión de la evidencia revisada:
- sí existe una única mejora short con señal favorable clara, que es el filtro anti-sobreextensión por distancia a `SMA200`;
- pero la cadena de evidencia no demuestra todavía robustez suficiente para elevarla con confianza a candidata experimental abierta;
- además, falta uno de los documentos obligatorios de esta tarea (`ANALISIS 15.md`), por lo que la trazabilidad documental exigida no está completa.

## 3. Decisión final
**Recomendar mantener 2.2.1 y no abrir todavía una nueva candidata.**

Motivo principal:
la mejora candidata más razonable existe, pero su ventaja sigue apoyándose en evidencia demasiado concentrada y metodológicamente frágil para justificar el salto de análisis a candidata experimental 2.2.2.

## 4. En caso de candidata: especificación exacta del cambio
No aplica, porque en esta revisión **no se propone candidata 2.2.2**.

La mejora que habría aspirado a ser candidata sería:
- bloquear la entrada short si `QQQ / SMA200 - 1 <= -15%`.

Sin embargo, hoy no se promueve porque la evidencia disponible no basta para sostenerla como candidata con respaldo suficiente.

## 5. Riesgos pendientes
Los riesgos pendientes que justifican no abrir candidata son estos:
- **evidencia obligatoria incompleta**: falta `ANALISIS/ANALISIS 15.md`.
- **concentración temporal excesiva**: la mejora observada se concentra casi totalmente en `2022-H2`.
- **dependencia de pocos trades**: la ventaja proviene de un número muy pequeño de operaciones modificadas.
- **casos problemáticos no resueltos**: la mejora no corrige todos los episodios débiles relevantes, incluido el caso señalado en `2025-04-15`.
- **riesgo de sobreajuste por umbral fino**: el corte en `-15%` frente a `SMA200` es interpretable, pero todavía no está demostrado como frontera robusta y no como ajuste de muestra.
- **conflicto entre señal positiva y robustez insuficiente**: `ANALISIS 17` aporta mejora global real, pero `ANALISIS 16` y `ANALISIS 18` no permiten considerarla todavía estable ni sólida.

## 6. Validación adicional necesaria
Para reconsiderar la apertura de una candidata experimental 2.2.2 tendría que cumplirse, como mínimo, lo siguiente:
- disponer y revisar `ANALISIS/ANALISIS 15.md` para cerrar la trazabilidad documental exigida;
- confirmar que la mejora del filtro `QQQ / SMA200 - 1 <= -15%` no depende solo de `2022-H2`, sino que conserva ventaja razonable al analizar estabilidad por subperiodos;
- verificar que la mejora no se sostiene únicamente por 2 o 3 trades concretos, sino por una señal repetible en más de un episodio bajista;
- comprobar sensibilidad paramétrica mínima alrededor del umbral para asegurar que la mejora no desaparece por pequeños cambios cercanos;
- exigir antes de producción una validación adicional específica sobre robustez temporal y sobre los casos tardíos que la regla todavía no corrige.

Condición concreta para reconsiderarlo:
solo debería reabrirse la opción de candidata si esa mejora mantiene ventaja global **y** además supera una validación adicional que reduzca claramente la sospecha de dependencia de tramo y de sobreajuste.

## 7. Conclusión final breve
La evidencia disponible permite decir que existe una mejora short prometedora, pero **no permite todavía defenderla como candidata experimental 2.2.2 con suficiente solidez**.

La decisión correcta hoy es **mantener la 2.2.1 sin cambios** y no abrir una nueva candidata hasta que la mejora deje de ser solo prometedora y pase a ser también suficientemente robusta.
