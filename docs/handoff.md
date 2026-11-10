# Agent handoff

## Lecture PDF naming pass

- Scope: rename the twelve newly uploaded PDFs numbered 15–26 in `course-material/lectures/`, while retaining their exact Git blob SHA (byte-for-byte preservation).
- Conventions: `NN_Topic-1_Topic-2.pdf` from `README.md`; the lecture number remains the number of the original uploaded filename.
- Evidence: top navigation/first slides were inspected for classes 16–26; the topics appear in `docs/course-map.md`. Class 15 was over the connector's available PDF text-reading size; its descriptive title includes PCA based on lecture 16's explicit opening PCA review and the dimensionality-reduction sequence. Inspect the class-15 agenda if/when raw-file access becomes available and refine only if necessary.
- Class 22's PDF cover labels itself “Sesión 21”, although its uploaded filename was “Clase 22 ML (1).pdf”. Do not silently modify numbering; reconcile against the official course plan if a conflicting class number matters.
- The lecture-14 PDF is absent and was not created.
- No notebooks, original PDF contents, or other course artifacts were modified by the renaming pass.

## Next steps
- If additional lectures are uploaded, inspect opening agenda/navigation, rename consistently, and extend `docs/course-map.md`.

## Solved Midterm II guide

- Source: user-provided five-page `Guía Parcial II.pdf` (practice exercise sheet; not an exhaustive exam outline).
- Location: `study-guide/partial-2/main.tex`, with one `exercises/exerciseNN.tex` per exercise (16 total), `appendix_formulas.tex`, `README.md`, and `verify_numbers.py`.
- The solutions, in English, preserve the original Spanish vocabulary tokens and course-specific numerical conventions; notably, Exercise 11 requires \(\log_{10}(N/df)\), without Scikit-Learn smoothing.
- Exercise 14 has no raw review dataset; the displayed classification pipeline is illustrative and does not claim measured performance. Exercise 16 supplies only two F1 summaries; no bootstrap confidence interval can be computed without case-level predictions.
- Locally validated with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` (25 pages, no overfull boxes) and `python verify_numbers.py` (all arithmetic checks pass).
- `.gitignore` excludes generated PDFs; `.github/workflows/build-study-guide.yml` supports selecting partial-1 or partial-2 for downloadable GitHub Actions artifacts.
- Next: if the source exercise sheet is revised, update individual exercises and numerical checks; rebuild before committing. Do not invent answers to data-dependent questions without data.

## Midterm II expanded exercises and lecture examples

- Added faithful English problem-statement boxes before all 16 exercise solutions. All exercises are forced to begin on a new page in `study-guide/partial-2/main.tex`.
- Exercise 3 has a constructed 8-point DBSCAN computation (Euclidean neighborhoods, cores, borders, and noise); Exercise 4 includes an illustrative fixed-variance 1D GMM EM iteration; Exercise 5 adds average, centroid and Ward linkage to the original single/complete problem. Ward values are explicitly SSE increases and must not be confused with Euclidean dendrogram heights.
- Exercise 10 extends the lecture-16 word-boundary example with a four-merge BPE run over `set new new renew reset renew`. Candidate pair counts use word multiplicities, exclude cross-word boundaries and explicitly resolve the ties. The original lecture excerpt does not mandate those tie choices.
- Exercise 11 works through lecture-17 search for `sweet love` in four documents, including IDF, TF--IDF vectors, cosine scores, ranking and an explanation of sparse vectors, using base-10 IDF and no smoothing.
- Verified `python study-guide/partial-2/verify_numbers.py` (original and extended numerical assertions), `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` (43 pages), absence of overfull LaTeX boxes, and PDF text extraction confirming exercises 1--16 begin on 16 distinct pages. The compiled PDF is available as an attached user artifact and reproducible via GitHub Actions.
- The updated formula appendix includes Ward, BPE pair-count frequencies, text-retrieval cosine and sparsity. New exercises are pedagogical extensions, not additional questions claimed to appear in the supplied five-page practice guide.

## Midterm II linkage, information criteria, and covariance review (2026-11-10)

- Added three separate-page review chapters under `study-guide/partial-2/reviews/`: `linkage_selection.tex`, `information_criteria.tex`, and `gmm_covariance.tex`. They contain separate, clearly labeled constructed practice prompts, detailed solutions, mathematical comparisons, and a reproducible Scikit-Learn/SciPy code example. `main.tex` includes them after the 16 supplied-guide exercises and before the consolidated appendix.
- Verified lecture 12 slide sections 42--56: single, complete, average, centroid; single chaining, centroid height inversion, and balance observation for complete/average. Ward is an additional extension beyond the lecture's four named criteria. Important correction: centroid inversion leaves the nested tree intact but makes merge heights nonmonotone.
- Verified lecture 10 slides 28--40 and 44 onward: GMM EM E/M steps, four `covariance_type` structures (spherical, diag, tied, full), and AIC/BIC complexity tradeoff. The covariance type constrains the mixture model and M-step; it is not a different EM algorithm.
- The generated numerical inversion example uses A=(-1,0), B=(1,0), C=(0,1.9), with centroid merge heights 2 then 1.9. A second hypothetical example (n=100,K=3,p=2) illustrates AIC selecting full and BIC selecting tied, using explicit parameter counts. Neither example is misrepresented as an original source problem.
- `verify_numbers.py` now checks inversion geometry, parameter counts and AIC/BIC arithmetic, optionally cross-checking with SciPy. `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` succeeded, producing 53 pages with no overfull boxes; a selection of rendered pages was inspected.
- The user can obtain the compiled PDF and complete source ZIP from the conversation attachments; the repository excludes compiled PDFs via `.gitignore`, but GitHub Actions can regenerate them reproducibly.

## Exercise 7 silhouette distance example

- Added a constructed three-cluster 1D silhouette example in `study-guide/partial-2/exercises/exercise07.tex`, immediately after the original guide exercise: `C1={0,2,7}`, `C2={8,9}`, `C3={15,18}`. All values are calculated from Euclidean distances, rather than assuming a(i), b(i) are given.
- Checked values: for x=2 in C1, a=3.5, alternative averages 6.5 and 14.5, b=6.5, s=6/13; for x=7 in C1, a=6, alternative averages 1.5 and 9.5, b=1.5, s=-0.75.
- Definition: exclude only the observation itself when calculating a(i); b(i) is the minimum of whole-cluster *mean* distances, not the nearest individual neighbor. The example is explicitly labeled supplementary and does not misstate the source guide.
- Added the computation procedure to `appendix_formulas.tex`, standard-library assertions to `verify_numbers.py`, and a scope note to the local README. LaTeX compiled successfully to 55 pages with no overfull boxes; new example pages 19–20 were rendered and inspected; all numerical checks passed.
