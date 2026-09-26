# LDS1071 — Machine Learning

Repositorio del curso **LDS1071 Aprendizaje de Máquina**.

La organización sigue el **orden pedagógico de las lectures**. Los PDFs y notebooks comienzan con el número de la clase a la que pertenecen, de modo que el orden alfabético de GitHub coincide con el orden del curso.

## Estructura

```text
.
├── course-material/
│   ├── lectures/        # PDFs del curso, en orden de clase
│   └── extras/          # avisos, actividades y material auxiliar
├── notebooks/           # notebooks propios/complementarios, ordenados por lecture
├── submissions/         # archivos finales entregados
├── study-guide/         # guías de estudio
├── docs/
└── hands-mlp/           # subtree de ageron/handson-mlp
```

## Convención de lectures

```text
NN_Topic-1_Topic-2.pdf
```

Ejemplos:

```text
09_Distance-based-clustering_Kmeans.pdf
10_DBSCAN_GMM.pdf
11_GMM_Likelihood_Hierarchical-Clustering.pdf
```

Una lecture puede contener varios temas; el nombre intenta reflejar la secuencia real del PDF, no asignar artificialmente un solo tema a cada clase.

## Convención de notebooks

```text
NN_Topic_Subtopic_short-title.ipynb
```

Ejemplos:

```text
09_Distance-based-clustering_Kmeans-sklearn.ipynb
10_GMM_Bivariate-normal-density.ipynb
11_Hierarchical-Clustering_Agglomerative-sklearn.ipynb
```

Los notebooks son material complementario del curso y de **Hands-On Machine Learning**. El mapeo lecture → notebook → capítulo upstream está documentado en `docs/course-map.md`.

## Submissions

`submissions/` contiene únicamente los artefactos finales entregados, con matrícula, nombre y actividad en el nombre del archivo.

## Guía del Parcial I

```text
study-guide/partial-1/main.tex
```

Compilar localmente:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error study-guide/partial-1/main.tex
```

El workflow **Build study guide PDF** también permite compilarla manualmente desde GitHub Actions.

## Hands-On Machine Learning

El repositorio de Aurélien Géron se mantiene como **git subtree** bajo `hands-mlp/`.

Consulta `docs/handson-mlp-subtree.md` para agregarlo y actualizarlo desde upstream.
