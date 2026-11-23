# AGENTS.md — Final Project

Read repository root `README.md`, `AGENTS.md`, `docs/handoff.md`, then `final_project/README.md` before making changes.

**Competition code publication restriction:** This repository is public. The Kaggle S6E11 rules require publicly shared competition code also to be published in the competition's Kaggle Discussion or Notebook. Do not push code here until that requirement is met. Do not push Kaggle train/test data, record-level predictions, fitted models, or secrets.

Once publication is compliant:
- Keep one self-contained teaching notebook with EDA, PCA/SVD, and five-fold stratified CV.
- Fit imputation, one-hot encoding, scaling, and optional PCA within each training fold. Drop identifier `id` from model inputs.
- Optimize ROC AUC; also track average precision, log loss, Brier and computational expense.
- Keep every candidate's fold metrics and OOF predictions; do not confuse a model blend with bootstrap bagging.
- Name experiments sequentially: `experiment001`, `experiment002`, etc. Preserve reproducibility and handoffs.
- Check concurrent branches and PRs. Never merge without explicit authorization.

## experiment002 — visualization extension

A locally packaged, not-yet-public notebook extends the plan to 13 configurations across five families (linear logistic, PCA logistic, spline logistic, random forest, XGBoost). It uses saved Seaborn plots and full-train grouped EDA, with fixed-seed 30,000-row plot/anomaly samples. Never infer causal effect from marginal fraud-rate curves or remove extreme transactions automatically. For additive spline logistic, fit SplineTransformer inside each CV training fold. Notebook publication gate remains in force.

## experiment003 safeguard

The enhanced 56-cell notebook includes a ten-condition logistic assumption audit and XGBoost corrections on logistic **logits** using `base_margin`. Pass stage-1 logits both when fitting and predicting the boosted stage; do not substitute the probabilities or omit the margin at inference. Fit both stages inside each CV training fold and preserve the same five stratified folds used for other candidates. Full experiment is 15 candidates × 5 folds; a 6,000-row smoke test is not a full-data result. The source notebook and reproducibility artifacts are currently only in the owner-delivered ZIP pending Kaggle public-code-sharing compliance.

## experiment004 / publication gate

The owner's private v4 notebook is 96 cells and retains all 15 candidate specs across five folds. Figures 20–25 are EDA; figures 26–41 are OOF-based model, ensemble, and submission diagnostics. Labels and legends explain balancing and sampling; never compute prevalence from class-balanced display samples or misinterpret OOF-selected ensembles as independent test performance. `SAVE_FOLD_MODELS=True` enables first-fold importance and sample-bounded partial dependence (which can be disabled using `RUN_PDP=False`). Full 75 fits remain unrun. Next experimental stage is sequential `experiment005`. Keep Kaggle competition code off public GitHub until the required competition-associated public sharing occurs.

## experiment005 — Conda, GridSearchCV and GPU behavior

Read the final-project PowerShell setup in `final_project/README.md`. `environment.yml` is the canonical Python 3.11 Conda spec with `ipykernel`; `requirements.txt` provides pip dependencies. The current privately distributed notebook has 100 cells and 19 candidate configurations. Preserve experiments 001–004 and the sequential experiment005 diagnostics.

`XGBOOST_DEVICE='auto'` attempts `tree_method='hist', device='cuda:0'` only after a tiny XGBoost CUDA fit and verification of the **actual booster device** from `save_config()`. CPU fallback is intentional; the configured `device` parameter alone is not trustworthy. Fixed XGBoost, nested-grid XGBoost and logistic-offset correction share this device. CatBoost independently probes GPU and falls back to CPU. Keep `GRID_SEARCH_N_JOBS=1` for single-GPU searches and record effective `model_device` in outer fold and inner-grid results.

GridSearchCV uses a stratified training-only subset for each outer training fold, with preprocessing fitted inside each inner fold. Refit the inner selected model on the full outer train partition; do not select hyperparameters using outer validation labels. Full planned run: 19 × 5 outer fits + 240 inner fits. Smoke tests passed on CPU-only hardware; actual GPU execution and full-data model quality are not established.

Do not publish competition code to the public GitHub repo without also posting it on the competition-associated Kaggle Notebook/Discussion, as required by Kaggle's code-sharing rule. Do not commit original Kaggle data, record-level outputs, model binaries or secrets.

## Presentation handoff — experiment006

The private `LDS1071_credit_fraud_marp_presentation_v6.zip` contains all 44 original figures, `presentation/deck.md`, `themes/fraud-minimal.css`, self-contained `slides.html`, 59-page `slides.pdf`, a figure manifest and reproducible build scripts. The PDF was generated with an offline layout renderer rather than the official Marp CLI; use the documented Marp CLI commands on the owner's machine if strict Marp-renderer exports are required. Preserve the original 44 images and all 59 slides when editing. Do not publish competition-derived code or data to this public repository before complying with Kaggle's code-sharing rule.
