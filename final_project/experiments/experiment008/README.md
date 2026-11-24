# experiment008 — Ensemble comparison from saved OOF artifacts

The project owner requested a second notebook to avoid repeating the original expensive modeling run. The privately delivered ZIP `LDS1071_fraud_ensembles_v8.zip` adds `final_project/ensemble_comparison.ipynb` (22 cells) and preserves the first notebook, both Spanish presentations and all 44 original PNG figures without modifying their bytes.

## Original local inputs

The first notebook writes relative to its kernel's working directory:
- `outputs/all_candidate_predictions.npz`: `candidate__oof` and `candidate__test` for every candidate
- `outputs/candidate_metrics.csv` and `outputs/run_manifest.json`
- `outputs/models/logit_C1_fold1.joblib` through `logit_C1_fold5.joblib` when `SAVE_FOLD_MODELS=True`

The new notebook searches both repository-root `outputs/` and `final_project/outputs/`. It checks cache metric consistency, fold assignments and correspondence between saved LR model predictions and cached held-out probabilities. The author's private computer files are not accessible directly to this conversation and are **not** inside this ZIP.

## Five-way comparison

A benchmark (best standalone, excluding logit-offset) is compared with exactly four ensemble architectures:

1. **Blending:** equal-weight average of the best standalone model from each family, based on original OOF AUC; no new fitting.
2. **Logit-offset boosting:** cached original two-stage logistic + XGBoost candidate; XGBoost trained on binary-logistic loss with LR logits provided through `base_margin`, not explicit residual regression.
3. **Explicit probability-residual modeling:** a new fold-wise `XGBRegressor(objective='reg:squarederror')` trained on original fold-train probability residuals `r=y-p_LR`. Corrected validation and test predictions use `clip(p_LR+g(X),1e-7,1-1e-7)`. Existing fold LR preprocessing is reused and its parameters are frozen.
4. **RF stacking:** a `RandomForestClassifier` trained **only** on the base candidates' saved OOF probability columns. Its out-of-fold second-level predictions are computed by a further five-fold split and the final meta-model is fitted to all base OOF rows for test inference.

The new notebook selects the largest *apparent* pooled OOF ROC AUC among all five and exports a metric table, ROC/PR/importance/stability plots, all five separate submission CSVs, a selected submission CSV and a JSON provenance manifest to `final_project/outputs/ensemble_extension/`. Old outputs are not overwritten.

**Important methodological limitation:** selecting candidates/weights by OOF ROC AUC introduces selection optimism. Meta-cross-validation on previously saved OOF features is NOT fully nested cross-validation because base models used some meta-validation labels while predicting other meta-training records. The stack also receives fold-averaged test input probabilities rather than single-fold OOF inputs. The observed maximum is exploratory; fully nested retraining or a never-used holdout is necessary for an unbiased claim.

## PowerShell reproduction

From the repository root, after unpacking the private ZIP **without deleting existing outputs**:

```powershell
conda activate lds1071-fraud
Set-Location .\final_project
Test-Path .\outputs\all_candidate_predictions.npz
(Get-ChildItem .\outputs\models\logit_C1_fold*.joblib).Count
jupyter lab ensemble_comparison.ipynb
```

If the cache resides at the repository root, adjust the preflight paths to `..\outputs\...`; the notebook itself auto-detects both. The tests should find the NPZ and **five** LR fold models. Select kernel `Python (LDS1071 Fraud)` and run all cells. The new notebook stops with an explicit message when a required original artifact is missing.

## Validation and safety

- 22 notebook cells validated, all 11 Python code cells compiled.
- A 4,000-row five-fold end-to-end development smoke test passed with cached fold LR models, predictions and a **synthetic offset proxy** to exercise the existing-offset import path (the proxy is not a fitted offset model; scores from this test are not valid for the real competition).
- A privacy-preserving `test_synthetic_smoke.py` in the private ZIP also passed, generating fictional training data and checking 5 scoreboard rows, four PNGs and the submission schema. It tests automatic discovery of `outputs/` in the repository root.
- The full 699,960-row extension cannot be executed here: the user's real OOF arrays and fitted fold binaries are on their workstation.
- Never upload original Kaggle rows, row-level OOF/test predictions, fitted models or secrets to public GitHub. The repository is public and competition code publication is subject to the contest's associated Kaggle Notebook/Discussion sharing rule, so this README is a documentation-only scaffold.

Next: run the second notebook against the owner's original cached full-run artifacts. Preserve aggregate results in `experiment009` if a new experiment follows.