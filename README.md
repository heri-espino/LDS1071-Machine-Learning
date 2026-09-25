# LDS1071 — Machine Learning

Repositorio del curso **LDS1071 Aprendizaje de Máquina**.

La estructura separa el material oficial del curso, las entregas, los notebooks de trabajo y las guías de estudio para evitar mezclar archivos descargados, experimentos y productos finales.

## Estructura

```text
.
├── course-material/     # PDFs y material distribuido en clase/Blackboard
├── assignments/         # código y assets de actividades
├── submissions/         # archivos finales entregados
├── notebooks/           # exploraciones y notebooks de clase
├── study-guide/         # guías de estudio en LaTeX
├── docs/                # documentación del repositorio
└── hands-mlp/           # subtree de ageron/handson-mlp (se agrega localmente)
```

Los notebooks cuyo contenido todavía no permite asignar un nombre confiable permanecen en `notebooks/_unsorted/` en lugar de inventar una clasificación.

## Guía del Parcial I

Fuente:

```text
study-guide/partial-1/main.tex
```

Compilar localmente:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error study-guide/partial-1/main.tex
```

También existe un workflow manual de GitHub Actions: **Build study guide PDF**.

## Hands-On Machine Learning

El repositorio de Aurélien Géron se mantiene como **git subtree** bajo `hands-mlp/`, no como una copia desconectada ni como submodule.

Consulta `docs/handson-mlp-subtree.md` para agregarlo y actualizarlo desde upstream.

## Convención

- `course-material/`: material recibido.
- `assignments/`: archivos de trabajo de una actividad.
- `submissions/`: artefactos entregados.
- `notebooks/`: experimentos, ejemplos y notas ejecutables.
- `study-guide/`: documentos de estudio escritos para el curso.
