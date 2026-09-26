# LDS1071 — Machine Learning

Repositorio del curso **LDS1071 Aprendizaje de Máquina**.

La organización separa el material distribuido en clase, los notebooks de trabajo, las entregas finales y las guías de estudio.

## Estructura

```text
.
├── course-material/     # PDFs y material oficial del curso
├── notebooks/           # prácticas, actividades, ejemplos y exploraciones
├── submissions/         # archivos finales efectivamente entregados
├── study-guide/         # guías de estudio en LaTeX
├── docs/                # documentación del repositorio
└── hands-mlp/           # subtree de ageron/handson-mlp
```

## Convenciones de nombres

### PDFs de material del curso

```text
seccion.subseccion_short-title.pdf
```

Ejemplos:

```text
06.00_learning-theory.pdf
10.00_distance-based-clustering.pdf
12.00_hierarchical-clustering.pdf
```

### Entregas

```text
ID-Nombre-Actividad.ext
```

Ejemplo:

```text
175199-Heriberto_Espino_Montelongo-04-Segmentacion_imagenes_KMeans.zip
```

`submissions/` contiene únicamente archivos finales entregados; los notebooks de trabajo permanecen en `notebooks/`.

## Guía del Parcial I

Fuente:

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
