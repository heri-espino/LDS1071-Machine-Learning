# Project handoff — 2026-11-22

## Scope
The competition is Kaggle Playground Series S6E11: Predicting Credit Card Fraud. The requested deliverable is a single scikit-learn-based Jupyter notebook, five-fold CV, PCA retaining ~90% feature variance as an *experiment*, logistic regression, random forest, XGBoost, tuned hyperparameters and multi-model blending.

## Local work already completed
A 22-cell notebook and accompanying project package were created locally and successfully smoke-tested using a 15,000-row stratified development sample (5 folds, 4 candidates). Test submission files were created with 299,984 rows and validated against Kaggle's provided submission schema. These are **smoke-test** results, not full-data competition validation. The full 11-candidate × 5-fold sweep on all 699,960 training rows is still pending.

## Critical publication gate
The repo is public. Kaggle's rule for sharing competition code publicly requires posting it in the associated competition Kaggle Notebook or Discussion. For that reason, only this documentation scaffold was committed to GitHub; the runnable competition notebook remains in the conversation download pending Kaggle publication. Do not push raw competition CSVs, record-level predictions, or model binaries to this repo.

## Next steps
1. Retrieve the complete project ZIP from the 2026-11-22 conversation.
2. Publish the notebook on the competition-associated Kaggle page before making it public in GitHub, if public publication is desired.
3. Add the notebook, requirements, and `experiment001` summary files to `final_project/` after satisfying the sharing rule.
4. Run all full-data candidates, record fold metrics and submission, and preserve experiment results. Create `experiment002` for a holdout/nested-CV assessment if needed.

## Visualization/nonlinearity extension — experiment002 (2026-11-22)

Prepared a 49-cell version of the single final-project notebook with professional Seaborn charts, quantile-binned nonlinear fraud-rate diagnostics, interaction heatmaps with cell counts, Wilson 95% binomial intervals, conservative 3×IQR outlier screens, and unlabeled Isolation Forest anomaly scores. Added spline logistic regression to the baseline/PCA/RF/XGBoost comparison; planned **13 candidates, 65 five-fold fits**. Diagrams save to ignored `outputs/figures/`; aggregate results and all artifacts are packaged in the current ChatGPT conversation, not pushed to this public repo because of Kaggle's public-code-sharing requirement.

EDA from full labeled data: 1.67% overall fraud; joint highest quintiles of merchant risk and velocity show 9.10% fraud versus 0.03% for lowest-lowest; these are marginal comparisons, not causal effects. Numerical amount 3×IQR upper-tail flags 61,219 rows (8.75%). Isolation Forest on a fixed-seed 30k sample (unlabeled features; 2% contamination) flags 600, of which 85 are fraudulent (14.17%), versus 1.39% among unflagged; this is *in-sample descriptive association*, not held-out detection accuracy.

Validation: all exploratory cells executed and saved their PNGs; a separate **temporary** 3k train / 3k test smoke test (five model families × five folds; tree counts reduced further in the validation copy) completed all post-CV visualizations and submission format assertions. A full-data 65-fit sweep remains outstanding. Use the packaged project ZIP to continue. Preserve experiment001; do not expose raw contest data/predictions or push code until the Kaggle publication requirement is satisfied.

## experiment003 handoff — logit-offset boosting (2026-11-22)

The latest local notebook (56 cells, delivered in conversation ZIP `LDS1071_credit_fraud_offset_boosting_v3.zip`) contains Section 5.1 logistic assumption audit, Section 5.2 a `LogisticOffsetXGBClassifier` with frozen logistic baseline and XGBoost `binary:logistic` corrections trained with logistic raw-score `base_margin`, plus Section 8.4 OOF diagnostic charts and metrics. An unchanged baseline logistic versus two new offset variants and standalone XGBoost was tested on 6,000 stratified rows / five folds (capped trees): OOF ROC AUC 0.941169 baseline, 0.940566 depth-2 offset, 0.939514 depth-3 offset, 0.919934 standalone XGB. The two offset variants did **not** improve in the small smoke test. Saved in local ZIP: notebook, full Python test harness, candidate/fold metric CSVs, residual-summary CSVs and Figure 19. Reproduce by placing original Kaggle dataset ZIP beside the notebook and running `experiments/experiment003/test_offset_boost.py` from the unpacked project.

Full 699,960-row candidate tuning is unrun: **15 × 5 = 75 CV fits**, two sequential estimators in offset candidates. Preserve experiment001/002 and current audit findings. No competition code is committed to public GitHub until it is also published on Kaggle as required by public code-sharing rules. Do not upload row-level predictions, original CSVs, or secrets.

## experiment004 — 2026-11-22 visualization extension

Updated private, runnable Jupyter notebook (now 96 cells) with additional numbered figures 20–41: Seaborn single-feature discrimination, balanced ECDFs, category/Boolean interaction/support heatmaps, hour×weekday risk surfaces, pair plots, unlabeled train/test drift, OOF multi-metric/risk-score comparisons, capture/lift and review-budget curves, operating-point confusion matrices, calibration with clamped Wilson error bars, subgroup AUC/AP, top-1% rank-set Jaccard overlap, logistic/tree importance, partial dependence on bounded 400-row subsample, blend impact, hyperparameter comparisons, fold stability, and submission score checks. All plots saved to `outputs/figures/` and indexed by `figure_catalog.csv`.

Validated structure/compile; executed added EDA on actual full training/test files and model-side plots after a five-fold 4,000-row smoke run across five model families with shorter tree configurations and 400 unlabeled test examples for visualization. This is **not** the full 699,960-row, 75-fit experiment. Full experiment and final submission are pending. Complete local notebook, previews, and experiment004 documentation are in the owner's `LDS1071_credit_fraud_visual_diagnostics_v4.zip`, intentionally not public due to competition public-code-sharing rules. Preserve prior experiments and use `experiment005` for eventual full-data results.

## experiment005 — Conda + XGBoost/CatBoost search, GPU preference (2026-11-22)

The newest privately delivered notebook is 100 cells. Conda `environment.yml` and pip `requirements.txt` specify Python 3.11, ipykernel, JupyterLab, scikit-learn, XGBoost, CatBoost, Seaborn and plotting dependencies. `final_project/README.md` gives complete Windows PowerShell commands, Jupyter kernel registration and how to launch the notebook with the Kaggle ZIP placed beside it.

Added 2 native-categorical CatBoost fixed candidates and 2 `GridSearchCV` nested-search candidates (`xgb_nested_grid`, `catboost_nested_grid`); 19 candidate specs overall. Each nested search compares 8 grid points × 3 inner folds on a stratified subsample of no more than 20,000 records from the respective outer train split, and retrains the selected settings on the full outer training fold for held-out OOF scoring. At full settings: 95 outer fits, 240 additional inner fits. Grid CSVs archive every attempted point and selected parameters. A 3,000-row/5-fold, 5-family reduced smoke test completed; a separate logit-offset XGBoost smoke passed. **The full 699,960-row experiment has not run.**

The user specifically requested that XGBoost hyperparameter searches use GPU if possible. Added `XGBOOST_DEVICE='auto'`, `XGBOOST_GPU_ID='0'`, a real CUDA training probe and fitted-booster device inspection (XGBoost can silently fall back). Fixed XGBoost, grid-tuned XGBoost and logistic-offset boosting prefer CUDA when actually available, with CPU fallback including retries on GPU runtime errors. CatBoost also probes GPU and retries CPU if needed. Keep `GRID_SEARCH_N_JOBS=1` to prevent GPU memory oversubscription. Result tables record actual training devices.

Validation runtime has no NVIDIA CUDA device; CPU fallback verified. GPU training, GPU acceleration claims, and Windows Conda environment creation have **not** been verified on the owner's machine. The latest project ZIP contains the executable notebook, experiment005 smoke aggregates, figures and runnable test harness, but the public repository intentionally includes only documentation/dependencies pending Kaggle's competition-specific public code-sharing requirements.

Next: test CUDA probe on owner's workstation, run full experiments when resources allow, review OOF and inner-grid stability, produce Kaggle submission and preserve aggregate full-data outcomes in the next sequential experiment, `experiment006`.

## experiment006 — presentation report and verification (2026-11-22)

The owner uploaded `figures.zip` (44 original PNGs; numbered 01–43 with two distinct 34 subgroup charts). Delivered a complete ZIP `LDS1071_credit_fraud_marp_presentation_v6.zip`, preserving the existing final-project notebook and experiment001–005 artifacts, plus `outputs/figures/` and `presentation/` with a minimal Seaborn-inspired custom Marp theme, editable 59-slide Markdown source, browser-tested interactive self-contained HTML, and 59-page PDF. Offline PDF fallback was used because the Marp CLI was not locally available; the ZIP documents official CLI regeneration instructions. Validation: all 44 figure files represented once in source, HTML and PDF; Python PDF confirms 59 pages with 44 image placements, PDF sample pages visually reviewed; Chromium verified navigation and zoom with no JS errors. No numeric-performance claims were invented from images. Full materials withheld from public GitHub pending Kaggle sharing compliance; this change adds only documentation and a presentation README placeholder.
