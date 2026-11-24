# experiment011 — Ampliación de la presentación corta (EDA y PCA)

La nueva versión del proyecto se entregó al propietario como ZIP privado `LDS1071_fraud_presentacion_corta_eda_pca_v11.zip`, que incluye todos los notebooks, resultados y figuras previos, más la presentación corta reconstruida. El código y las imágenes derivados de la competencia se mantienen fuera del repositorio público hasta satisfacer las condiciones de publicación de Kaggle.

## Objetivo y cambios

- Presentación corta en español: **36 diapositivas**, **21 gráficas**, guion estimado de **18.14 minutos**.
- Inventario verificado en el CSV original: 699,960 filas de entrenamiento, 299,984 de prueba, 24 predictores (13 numéricos, cinco categóricos y seis booleanos), más id e is_fraud.
- El EDA se presenta primero y cubre histogramas, densidades, ECDF, correlaciones Pearson/Spearman, categorías, banderas, asociaciones por pares, patrones por hora y día, tasas por cuantiles, valores extremos IQR, Isolation Forest, discriminación marginal y desplazamientos train/test.
- La PCA mediante SVD retiene el 90% de varianza como alternativa para regresión logística, ajustada **dentro** de cada fold; su menor desempeño OOF se explica sin asumir que preservar varianza implica preservar capacidad predictiva.
- Se añadió la distinción entre etiqueta binaria y **predicción de probabilidad** en [0,1], con función sigmoide y evaluación oficial ROC AUC.
- Se incorporaron explícitamente los contenidos de las diapositivas **31, 32, 35, 36 y 53** de la presentación completa v10: comparación de candidatos, correlación OOF entre modelos, PCA, diagnósticos logísticos y desempeño frente a costo computacional.
- Matemáticas delimitadas correctamente en Markdown Marp con `$$...$$`, reducidas a escala similar al texto en las exportaciones.
- Se conserva la presentación extensa de 93 diapositivas **sin modificaciones**, y la antigua versión corta bajo `presentation/archive/v10/presentacion_corta/`.

## Reconstruir (en el ZIP privado)

Desde `final_project/presentation/`:

```powershell
conda activate lds1071-fraud
python build_presentacion_corta_v11.py
```

Se generan `presentacion_corta/deck.md`, `slides.html`, `slides.pdf`, `slides_metadata.json` y `guion_del_presentador.md` mediante el exportador offline. El Markdown es compatible con Marp, pero las exportaciones distribuidas **no se atribuyen a Marp CLI**.

## Verificación

- PDF: 36 páginas; ningún texto fuera de los límites de página.
- HTML: 36 secciones, 21 imágenes de gráficas, seis fórmulas renderizadas; JavaScript pasa `node --check`.
- Los 51 PNG previos son idénticos byte por byte (SHA-256) y el PDF de la presentación completa tiene SHA-256 sin cambios.
- El guion es una estimación temporal, no una grabación de ensayo; 36 diapositivas requieren un ritmo ágil.

No se ejecutaron nuevos modelos ni se modificó la comparación de ROC AUC: el bootstrap y las conclusiones siguen siendo los del experimento010. La comparación de la predicción OOF de `xgb_nested_grid` aún requiere recuperar ese vector en el equipo del propietario.

## Próximos pasos

Ensayar la exposición para verificar el tiempo real y, de ser necesario, trasladar algunos diagnósticos a material de apoyo. Mantener intactos datos, figuras y resultados de experimentos anteriores.
