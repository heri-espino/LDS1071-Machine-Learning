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
