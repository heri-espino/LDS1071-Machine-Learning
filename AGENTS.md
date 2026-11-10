# AGENTS.md — LDS1071 Machine Learning

## Repository context
- This repository organizes coursework by lecture number. Start with `README.md` and `docs/course-map.md` before changing course materials.
- The original lecture PDFs live under `course-material/lectures/`. Keep every original lecture available through Git history; rename without recompressing or editing its bytes unless explicitly requested.
- Lecture filenames follow `NN_Topic-1_Topic-2.pdf` (ASCII, descriptive topic labels, preserving the original lecture number).
- Local notebooks use the corresponding lecture prefix where possible. Do not overwrite notebooks or results.

## Modification workflow
1. Inspect the current default branch and open PRs, and check for branch changes before writing.
2. Read existing docs and inspect the relevant lecture agenda/title before selecting a filename; do not infer a detailed topic without evidence.
3. For PDF renames, preserve Git blob IDs. Verify there are no filename collisions and no unintended content changes.
4. Update `docs/course-map.md` when adding or renaming lectures and maintain `docs/handoff.md` with limitations or outstanding checks.
5. Commit and push completed changes; do not force-push, rewrite history, or merge a pull request without explicit authorization.

## Known caveats
- Lecture 14 currently has no PDF in `course-material/lectures/`; do not fabricate one.
- The PDF uploaded as class 22 has an internal slide title that says session 21.

## Study guide maintenance
- For `study-guide/partial-2/`, keep one numbered exercise per `exercises/exerciseNN.tex`, include them in `main.tex`, and maintain `appendix_formulas.tex`.
- Preserve the source guide's numerical givens and formulas (especially its unsmoothed base-10 TF--IDF convention). Document explicitly where illustrative methods extend the supplied problems.
- Recompile LaTeX and run `python study-guide/partial-2/verify_numbers.py` after changes. Generated PDFs are excluded from Git; publish via the build workflow artifact instead.

- The Part II guide presents the complete translated question in a `problem` box before each solution, with `\\clearpage` before each exercise input. Maintain separate-page sections.
- Supplemental lecture examples must label their provenance (lecture 16 BPE, lecture 17 TF--IDF) and distinguish new numerical illustrations from source material. Check numerical claims with standard-library assertions in `verify_numbers.py`.
