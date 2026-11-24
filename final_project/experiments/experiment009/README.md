# experiment009 — Presentaciones con el resultado de los cuatro ensambles

El propietario aportó `ensemble_extension.zip` con resultados completos de la extensión de ensambles. Se elaboraron dos nuevas presentaciones españolas a partir de los CSV agregados, las cuatro figuras de la extensión y las 44 figuras anteriores. El paquete privado entregado en la conversación contiene los archivos editables `deck.md`, HTML, PDF, guiones y un exportador reproducible de Python; el repositorio **público** conserva por ahora únicamente este registro debido a las reglas de publicación de código de la competencia.

## Resultados verificados sobre predicciones OOF

| Estrategia | ROC AUC | Average precision |
|---|---:|---:|
| Logistic-offset XGBoost | **0.946205** | **0.507424** |
| Mejor XGBoost individual | 0.946120 | 0.503585 |
| Stacking con random forest | 0.945747 | 0.506383 |
| Blending de probabilidades | 0.943280 | 0.500913 |
| XGBoost sobre residuos explícitos | 0.940241 | 0.494046 |

Según la regla de máximo ROC AUC OOF, se seleccionó `offset_xgb_depth3_lr05`. La diferencia frente a `xgb_depth5_lr05` es **0.000085**. El rango exploratorio de diferencias emparejadas [−0.000615, +0.001010] incluye cero; **no** constituye evidencia de superioridad estadística.

## Presentaciones

- **Corta:** 23 diapositivas, 18.379 minutos de guion, 12 figuras.
- **Completa:** 91 diapositivas, 50 figuras: 44 anteriores y seis de la extensión (dos reconstruidas a partir de CSV).
- **Formatos:** Marp Markdown editable, HTML con transiciones, PDF estático y notas del presentador. Los HTML/PDF se generaron con un exportador offline reproducible, no directamente con Marp CLI.

## Método y límites

La presentación distingue el blending del bagging, el boosting con `base_margin` de la regresión explícita de residuos y el stacking con random forest. La comparación reutiliza predicciones OOF; el nivel meta no fue completamente anidado y la selección por máximo OOF puede ser optimista. No hay prueba independiente etiquetada ni resultado verificado del leaderboard privado.

Las 44 figuras anteriores se verificaron byte a byte contra el ZIP v8 y se conservaron sin modificaciones. Los PDF finales contienen 23 y 91 páginas, sin desbordamientos de texto. La comprobación de interacción HTML mediante Chromium headless se agotó por tiempo, aunque la estructura y los scripts se generaron.

El ZIP privado incluye documentación del proyecto, scripts, CSV agregados y figuras, **sin** modelos `.joblib`, predicciones individuales `.npz` ni envíos por transacción. Próximo experimento: `experiment010`, si se requiere nueva validación.
