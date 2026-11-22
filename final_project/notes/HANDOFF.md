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
