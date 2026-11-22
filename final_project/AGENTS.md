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
