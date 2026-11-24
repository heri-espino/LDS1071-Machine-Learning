# LDS1071 — credit-fraud presentation (publication scaffold)

The complete **59-slide** presentation has been created and delivered privately to the project owner in the November 22, 2026 ChatGPT ZIP `LDS1071_credit_fraud_marp_presentation_v6.zip`.

Artifacts in that ZIP, under `final_project/presentation/`: editable `deck.md` (Marp Markdown), `themes/fraud-minimal.css`, self-contained `slides.html` (fade transitions, zoom, keyboard navigation), `slides.pdf` (59 static pages), figure manifest, and Python/PowerShell rebuild scripts. The source archive contains **all 44** owner-provided PNG files under `final_project/outputs/figures/`.

The PDF and HTML were generated via the included offline Python/browser workflow because official Marp CLI could not be installed in the authoring environment. The ZIP documents the genuine Marp CLI commands for re-exporting the Markdown source on a workstation with Node.js and a browser. PDF and HTML have equivalent slide content, not identical typography. Quality checks counted 59 slides/pages and 44 images in each output.

**Public-sharing safeguard:** This repository is public. The full presentation, derived figures, source notebook, and competition code were deliberately **not** pushed here pending compliance with Kaggle's competition-specific public-code-sharing requirements (including publication on the competition-associated Kaggle Notebook/Discussion as appropriate). This README is a documentation-only scaffold.

The supplied `figures.zip` did not contain numerical fold-level CSVs, so detailed performance claims should be checked against the separate training outputs before publication.

## Two Spanish presentations — experiment007 (2026-11-23)

A private updated project ZIP, `LDS1071_fraud_presentaciones_es_v7.zip`, contains two full Spanish-language presentations plus the earlier English version:

- `presentation/presentacion_corta/`: **20 slides**, a **17.55-minute speaking plan** (leaving room within 20 minutes), **13 selected original figures**, fully editable Marp `deck.md`, standalone animated `slides.html`, static 20-page `slides.pdf`, and `guion_del_presentador.md`.
- `presentation/presentacion_completa/`: **75 slides**, **all 44 original figures**, expanded methods/math/model descriptions, matching Marp Markdown, standalone animated HTML, 75-page PDF, and detailed speaker notes.
- Shared source: `presentation/build_presentaciones_es.py` and `presentation/themes/fraud-es.css`. Original 44 figure PNG hashes are unchanged.

The presentations explain EDA, nonlinear patterns, outlier treatment, logistic assumptions, PCA, random forests, XGBoost/CatBoost, five-fold out-of-fold validation, nested GridSearchCV, probability blending, logit-offset boosting and decision limitations. They explicitly distinguish **blending** from classical bagging, and **offset boosting** from logistic meta-model stacking, which has *not* been implemented. They do not invent a definitive full-run winner because the user supplied 44 figures but no corresponding full-run metric CSV files.

The included HTML/PDF were exported through the reproducible **offline Python renderer**, not the official Marp CLI; the Markdown is Marp-compatible and may be compiled using the documented CLI commands. Browser interaction could not be independently tested in the current environment; HTML structure/JS syntax and PDF pages/figures were verified.

**Public-sharing safeguard:** only this documentation is public. The complete code/derived figures remain in the owner's private ZIP pending Kaggle competition code-sharing compliance.

## Plantilla whitegrid y dos versiones españolas — experiment010

La revisión del propietario contiene `presentacion_corta/deck.md` y `presentacion_completa/deck.md`, respectivamente de 23 y 93 diapositivas, más exportaciones HTML/PDF. Fondo blanco, paleta Seaborn deep, tipografía sobria, sin tarjetas redondeadas, matemáticas con delimitadores LaTeX. Páginas 4, 5, 10, 12, 18, 19, 20 y 22 de la corta: figura grande a la izquierda y explicación a la derecha. Diapositiva 22: bootstrap pareado B=600, IC 95% de diferencia offset vs XGBoost fijo [−0.000263,+0.000440]. La comparación con XGBoost de GridSearchCV requiere el vector OOF faltante. El v9 original está preservado en `presentation/archive/v9/` del ZIP privado. Los archivos fuente/figuras no se publican aquí hasta cumplir los requisitos de Kaggle.

## Presentación corta v11

La versión reducida pasó a 36 diapositivas (21 figuras), con un plan de exposición de 18.14 minutos. Añade la descripción de variables y EDA al principio, PCA/SVD, probabilidades de clasificación y los análisis de las diapositivas 31, 32, 35, 36 y 53 de la versión extensa. Fórmulas LaTeX en `$$...$$`, renderizadas en el tamaño del texto; `build_presentacion_corta_v11.py` recompila PDF/HTML sin recalcular modelos. La versión larga se preservó y los anteriores archivos breves v10 se archivaron. El código fuente actualizado sigue distribuido en el ZIP privado.
