# experiment010 — rediseño visual y bootstrap emparejado

Se preparó de manera privada la revisión `LDS1071_fraud_whitegrid_bootstrap_v10.zip`, que conserva los notebooks, los experimentos anteriores y todas las figuras previas. El repositorio es público; para cumplir las condiciones de publicación del concurso, aquí se conserva **sólo este registro metodológico**, no los notebooks ejecutables ni las figuras/código derivados de los datos de Kaggle.

## Presentaciones

- **Corta:** 23 diapositivas, guion orientativo de **18.71 minutos**, 12 figuras.
- **Completa:** 93 diapositivas y 51 figuras; incluye las 44 figuras originales, las seis gráficas de ensambles y una gráfica nueva de la prueba bootstrap.
- Plantilla: fondo blanco, líneas finas, tipografía sobria y paleta `sns.color_palette("deep")` (Seaborn `whitegrid`), **sin** tarjetas redondeadas ni fondos grises.
- Las diapositivas **4, 5, 10, 12, 18, 19, 20 y 22** de la versión corta presentan imagen grande a la izquierda y explicación técnica a la derecha.
- Formatos privados: Markdown editable para Marp (fórmulas LaTeX delimitadas por `$$...$$`), HTML autónomo con transiciones, PDF estático y notas del ponente.
- Se conservó la versión anterior en `presentation/archive/v9/`.

## Bootstrap emparejado realmente ejecutado

Los resultados proceden de 699,960 observaciones etiquetadas y las cinco series OOF de `ensemble_extension.zip`. Bootstrap no paramétrico **emparejado y estratificado por clase**, **600 réplicas**, semilla `20261123`, usando idénticos índices remuestreados para todos los modelos y cálculo exacto de ROC AUC ponderada con empates.

| Método | ROC AUC OOF | Diferencia vs. XGBoost individual fijo | IC percentil 95% de diferencia |
|---|---:|---:|---:|
| XGBoost individual fijo (prof. 5, tasa 0.05) | 0.946120 | 0.000000 | — |
| Regresión logística corregida con XGBoost | **0.946205** | **+0.000085** | **[−0.000263, +0.000440]** |
| Stacking con bosque aleatorio | 0.945747 | −0.000373 | [−0.000674, −0.000123] |
| Promedio de probabilidades | 0.943280 | −0.002840 | [−0.003391, −0.002363] |
| XGBoost sobre residuos explícitos | 0.940241 | −0.005879 | [−0.006932, −0.004854] |

**Conclusión:** la ventaja puntual de la corrección logística sobre el XGBoost individual es muy pequeña y el intervalo incluye cero. No se demostró una mejora estadísticamente sólida; los intervalos tampoco eliminan el optimismo de selección por OOF, la posible dependencia entre transacciones o las limitaciones del stacking no completamente anidado.

## Comparación con XGBoost ajustado mediante GridSearchCV

El **mejor XGBoost individual identificado en el CSV de ensambles** fue una configuración **fija** (profundidad 5, tasa 0.05), que no debe confundirse con el candidato ajustado mediante `GridSearchCV` (`xgb_nested_grid`). El ZIP proporcionado **no contenía** el vector OOF de `xgb_nested_grid`; por tanto, no se atribuyó ninguna AUC exacta a ese modelo. La notebook privada `paired_bootstrap_comparison.ipynb` detecta automáticamente `outputs/all_candidate_predictions.npz` y añade esa comparación cuando está disponible en el equipo del propietario.

## Reproducibilidad y controles

- La nueva notebook reutiliza los modelos/predicciones guardados; **no** repite los 19 candidatos originales.
- Tiene 12 celdas, emplea `bootstrap_core.py` y guarda CSV agregados, figuras Seaborn y un manifiesto bajo `outputs/bootstrap_comparison/`.
- El código de AUC ponderada pasó una prueba sintética contra `sklearn.metrics.roc_auc_score(..., sample_weight=...)`, incluyendo empates; la notebook pasó una prueba de ejecución con ocho réplicas.
- PDF: 23 y 93 páginas; no se detectaron solapamientos de texto; todas las **50** figuras anteriores se conservaron byte por byte, y se añadió la número 51.
- HTML: estructura y JavaScript sintácticamente correctos, pero Chromium headless agotó su tiempo de carga en el entorno de validación; no se afirma una prueba interactiva completada.
- Los entregables privados HTML/PDF se generaron con un renderizador offline reproducible, **no** con el ejecutable de Marp CLI. Los `deck.md` sí son fuentes editables compatibles con Marp.

Siguiente paso si se requieren conclusiones más fuertes: incorporar `xgb_nested_grid__oof` y, de ser posible, evaluar la selección en un conjunto etiquetado independiente o mediante un diseño completamente anidado.
