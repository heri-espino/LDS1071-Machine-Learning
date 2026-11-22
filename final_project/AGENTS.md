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
