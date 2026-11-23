# LDS1071 Final Project — Credit Card Fraud Prediction

**Competition:** [Kaggle Playground Series S6E11](https://www.kaggle.com/competitions/playground-series-s6e11)  
**Deliverable:** one Jupyter notebook under `final_project/credit_card_fraud.ipynb`  
**Metric:** ROC AUC; final submission deadline: November 30, 2026 at 23:59 UTC.

## Project status

The notebook and experiment001 smoke-test results have been prepared and validated locally, but **competition code has not yet been published in this public repository**.

The competition's official public-code-sharing rule requires competition code that is shared publicly to **also** be shared on the competition's Kaggle discussion forum or Kaggle notebooks. Until the notebook has been published there, do not commit it to this public repository. Do not commit competition data, record-level predictions, or fitted model binaries.

The reproducible notebook package is available to the project owner in the ChatGPT conversation from November 22, 2026. After compliant Kaggle publication, add the notebook and its requirements, experiment001 documentation, and handoff files here.

## Planned implementation

- Exploratory analysis: data distribution, numerical/target correlations, grouped fraud rates.
- Five-fold shuffled stratified CV, reproducible seed, preprocessing **inside each fold**.
- Logistic regression with and without 90%-variance PCA/SVD; random forest; XGBoost.
- Compare hyperparameter candidates using ROC AUC, average precision, log loss, Brier, and resource use.
- Retain predictions for **every** candidate; compare a single model with best-per-family, top-3, and all-candidate probability blends.
- Create `id,is_fraud` Kaggle submission probabilities.

The GitHub repository's lecture notebooks and prior submissions remain unchanged.

## Visualization extension (experiment002)

The project owner's locally distributed notebook now includes Seaborn visualizations of fraud prevalence, missingness, distributions, correlations, categorical/Boolean risk, nonlinear binned rates, time-of-day effects, pairwise interaction heatmaps, 3×IQR numerical extremes, and Isolation Forest anomaly diagnostics. A spline-logistic candidate was added, bringing the planned full experiment to **13 candidates × 5 stratified folds = 65 model fits**. Figures contain labeled axes, legends and sampling limitations; potential outliers are not automatically removed.

The enhanced notebook and figures were validated locally using original training data for grouped EDA rates and a reduced five-fold smoke test for execution. **Full-data 65-fit model tuning remains unexecuted.** Competition code remains out of this public repository until publication on the associated Kaggle notebook/discussion satisfies the sharing rules. See `final_project/notes/HANDOFF.md`.

## experiment003 — logistic-offset gradient boosting and assumption diagnostics

An updated 56-cell notebook is available in the project owner's November 22 conversation download, but competition code remains **unpublished** to this public repo pending Kaggle's associated competition Notebook/Discussion publication requirement. The notebook now lists/audits logistic-regression assumptions (Section 5.1), then compares logistic regression with XGBoost fitted on corrections to the logistic **logits** through `base_margin` (Section 5.2). Both stages and preprocessing are fitted within each outer fold; inference supplies corresponding logit offsets. Section 8.4 includes Seaborn figures of OOF binned residual corrections and paired model metrics.

The planned full run now has **15 candidate configurations × 5 stratified folds = 75 pipelines**. A 6,000-row smoke test with capped tree counts found OOF ROC AUC 0.94117 for logistic regression, 0.94057 for depth-2 offset boosting, 0.93951 for depth-3 offset boosting, and 0.91993 for standalone depth-3 XGBoost. These are **not full-data scores or Kaggle leaderboard results**. Next, run full-data tuning; keep the original prior experiments intact and share code on the competition's Kaggle forum/notebook before publishing in this GitHub repository.

## experiment004 — Expanded exploratory/model visualization (2026-11-22)

A **96-cell** single Jupyter notebook, distributed privately in the owner's conversation as `LDS1071_credit_fraud_visual_diagnostics_v4.zip`, preserves the five-fold 15-candidate (75-fit) model experiment and adds figures 20–41. New Seaborn plots include single-feature AUC screening, class-conditional ECDFs, categorical/Boolean and time interactions, pairwise views, train/test feature shift, OOF four-metric scorecard, fit-time efficiency, score distributions, cumulative lift/capture, review-budget precision/recall, operating-rule confusion matrices, OOF calibration intervals, subgroup quality, top-risk-set Jaccard overlap, model-specific importance, sample-bounded partial dependence, blend impact, hyperparameter effects, fold stability, and test-score sanity diagnostics. Plots are saved to `outputs/figures/` with a CSV catalog.

Six new data-EDA sections executed using the original competition train/test files (full training data for aggregate rates), and all new model-side plots executed in a **4,000-row / five-fold / five-candidate smoke run**. Some plots use sampled rows; an optional `RUN_PDP` switch skips partial dependence. None of those results are full-data final scores. Existing experiment001–003 material remains untouched. The full 699,960-row × 15 × 5 experiment remains **pending**. Because the repository is public, the executable notebook remains only in the owner-delivered ZIP until it can also be shared in the competition's Kaggle Notebook/Discussion as required. Do not push competition records or predictions.
