# LDS1071: Midterm II solved study guide

This is a reproducible, modular LaTeX solution to **all 16 exercises and all their subquestions** from the uploaded five-page **Guía de Estudio - Examen parcial II**. The original guide is in Spanish; explanatory solutions are in English, preserving its numbers, notation, and specified conventions.

## Structure

```text
study-guide/partial-2/
├── main.tex                 # Preamble, notation, TOC, and ordered inputs
├── exercises/
│   ├── exercise01.tex       # K-means
│   ├── exercise02.tex       # Elbow method
│   ├── ...
│   └── exercise16.tex       # Paired bootstrap
├── appendix_formulas.tex    # All relevant formulas and numerical check sheet
├── verify_numbers.py       # Pure-standard-library arithmetic checks
└── README.md
```

Each `exercises/exerciseNN.tex` corresponds to exactly one numbered exercise in the source and defines one `\section`. Every exercise **starts on a new page** and includes its full **problem statement, faithfully translated into English**, before the solution. `main.tex` is the only TeX entrypoint. The appendix is introduced after `\appendix`.

## Compile

From the repository root:

```bash
cd study-guide/partial-2
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The PDF is generated at `study-guide/partial-2/build/main.pdf`.

Run the arithmetic cross-checks:

```bash
python study-guide/partial-2/verify_numbers.py
```

To rebuild after editing, rerun `latexmk`. To clean auxiliary build files, from `study-guide/partial-2` run `latexmk -C -outdir=build main.tex`.

## Scope and interpretation

- All exercise subquestions (1a–16c) are answered with the translated problem statement immediately above each solution. The formula appendix extends the guide slightly by including related derivations (e.g., EM updates and the connection between cosine and normalized Euclidean distance), explicitly marked as context.
- **Exercise 11:** TF–IDF uses the guide's unsmoothed base-10 formula, not Scikit-Learn's default IDF convention.
- **Exercise 14:** the guide gives 8,000 labeled reviews but does *not* provide their actual text or labels. The pipeline code is an illustrative template, **not** a claimed training run.
- **Exercise 16:** the two published F1 scores do not allow a confidence interval without case-level true labels and paired predictions. The bootstrap procedure is described, not falsely computed.
- **Lecture 16 BPE (Exercise 10):** a fully counted, four-merge numerical example uses the supplied `set new new renew reset renew` corpus. The within-word merge restriction follows the lecture. A tie-break order is explicitly chosen to produce a reproducible illustration, not falsely attributed as the lecture's mandatory order.
- **Lecture 17 TF--IDF (Exercise 11):** the `sweet love` query and four original documents are included, with document frequencies, query/document TF--IDF vectors, cosine scores, ranking, and an illustration of sparse text vectors. Values follow the *lecture's* base-10, unsmoothed definition.
- **Additional constructed numerical examples:** DBSCAN with core/border/noise (Exercise 3); one E/M iteration for a two-Gaussian mixture with fixed variances (Exercise 4); five hierarchical linkage methods including Ward's SSE increase (Exercise 5). These are explicitly marked as extensions rather than claimed to be new source questions.
- This is a practice guide, not a guarantee of the content on the actual exam.

## Maintenance / agent handoff

Before editing, read the repository's root `README.md`, `AGENTS.md`, and `docs/handoff.md`. Preserve one file per exercise and source question numbering. Check each calculation, including the additional worked examples, with `verify_numbers.py` and compile twice (for TOC and references). Inspect representative rendered pages and confirm 16 exercise headings begin on separate PDF pages. Do not commit build logs/auxiliary files; the project `.gitignore` excludes generated PDFs from Git by default. The GitHub Actions **Build study guide PDF** workflow can generate a downloadable PDF artifact.
