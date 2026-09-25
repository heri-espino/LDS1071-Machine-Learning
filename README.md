# ML — Guía resuelta del Parcial I

Guía de estudio en LaTeX para **Aprendizaje de Máquina (LDS1071)**. El documento responde las preguntas de la guía del primer parcial e incluye:

- fundamentos de aprendizaje supervisado y no supervisado;
- representación de `X` y `y`;
- entrenamiento, validación y prueba;
- generalización, underfitting y overfitting;
- MAE, MSE y RMSE;
- matriz de confusión, accuracy, precision, recall y F1;
- clases desbalanceadas;
- parámetros e hiperparámetros;
- lectura básica de scikit-learn;
- flujo completo de un proyecto de ML;
- los seis ejercicios integradores resueltos;
- diagramas hechos directamente en TikZ/PGFPlots.

## Compilar localmente

Con una distribución de LaTeX que incluya `latexmk`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

O con `pdflatex`:

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

El PDF resultante será `main.pdf`.

## Compilar en GitHub Actions

El workflow **Build study guide PDF** es manual. En GitHub:

1. abre **Actions**;
2. selecciona **Build study guide PDF**;
3. pulsa **Run workflow**;
4. al terminar, descarga el artifact con `main.pdf`.

No se compila automáticamente en cada `push`.
