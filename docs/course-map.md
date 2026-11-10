# Course map

Este archivo relaciona el orden de las lectures con los notebooks locales y con el material de referencia de `ageron/handson-mlp`.

| Lecture | Temas principales | Notebooks locales | Referencia en `hands-mlp/` |
|---:|---|---|---|
| 01 | Course introduction | — | `01_the_machine_learning_landscape.ipynb` |
| 02 | Learning types; KNN; train/test split | `02_Learning-types_KNN_Iris.ipynb` | `01_the_machine_learning_landscape.ipynb`, `03_classification.ipynb` |
| 03–05 | End-to-end ML project workflow | — | `02_end_to_end_machine_learning_project.ipynb` |
| 06 | Learning theory; optimization intuition | `06_Learning-theory_Optimization_Coordinate-vs-gradient-descent.ipynb`; `06_Learning-theory_Optimization_Surface-visualization.ipynb`; `06_Learning-theory_Stochastic-optimization_Stratified-minibatches-Iris.ipynb` | `04_training_linear_models.ipynb` |
| 07 | Learning-theory practice | — | — |
| 08 | Review | — | — |
| 09 | Distance-based clustering; K-means | `09_Distance-based-clustering_Kmeans-sklearn.ipynb`; `09_Distance-based-clustering_Kmeans-image-segmentation.ipynb`; `09_Distance-based-clustering_Kmeans-semisupervised-digits.ipynb` | `08_unsupervised_learning.ipynb` |
| 10 | DBSCAN; introduction to Gaussian mixture models | `10_DBSCAN_Make-moons.ipynb`; `10_GMM_Bivariate-normal-density.ipynb` | `08_unsupervised_learning.ipynb` |
| 11 | GMM; likelihood; hierarchical clustering | `11_GMM_Covariance-visualization.ipynb`; `11_Hierarchical-Clustering_Agglomerative-sklearn.ipynb` | `08_unsupervised_learning.ipynb` |
| 12 | Hierarchical clustering continuation | — | `08_unsupervised_learning.ipynb` |
| 13 | Dimensionality reduction | the lecture-09 digits notebook also contains t-SNE, UMAP, ICA and PCA visualizations | `07_dimensionality_reduction.ipynb` |
| 15 | Dimensionality reduction; principal component analysis (PCA) | — | `07_dimensionality_reduction.ipynb` |
| 16 | PCA review; random projections; manifold learning; introduction to text processing | — | `07_dimensionality_reduction.ipynb`, `03_classification.ipynb` |
| 17 | Text processing; numerical text and word representations | — | — |
| 18 | Bag of Words; text clustering | — | — |
| 19 | Numerical text representation; text clustering (continuation) | — | — |
| 20 | Text classification; model evaluation and selection | `14_Text-classification_TFIDF-vs-CountVectorizer_R3.ipynb` | — |
| 21 | Regularization; model evaluation and selection | — | — |
| 22 | Text classification review; model evaluation and selection | — | — |
| 23 | Model evaluation and selection; introduction to decision trees and tree ensembles | — | `06_decision_trees.ipynb`, `07_ensemble_learning_and_random_forests.ipynb` |
| 24 | Decision trees; tree ensembles | — | `06_decision_trees.ipynb`, `07_ensemble_learning_and_random_forests.ipynb` |
| 25 | Tree ensembles; random forests | — | `07_ensemble_learning_and_random_forests.ipynb` |
| 26 | Random forests; boosting | — | `07_ensemble_learning_and_random_forests.ipynb` |

## Notes on classification

- The K-means image-segmentation notebook and the semi-supervised digits notebook are grouped under lecture 09 because their main algorithmic role is K-means.
- The digits notebook is cross-referenced with lecture 13 because it also contains t-SNE, UMAP, ICA and PCA visualizations.
- The bivariate-normal and covariance notebooks are grouped with GMM rather than as generic probability notebooks because they were created to visualize the Gaussian components/covariance geometry used by GMM.
- The copied `02_end_to_end_machine_learning_project.ipynb` is not duplicated locally: it already belongs in the `hands-mlp/` subtree.
- Clearly unrelated notebooks from the original Drive dump (for example Black–Scholes/MCMC, Delaunay, and an education-economics plot) are intentionally excluded from the cleaned course tree. They remain recoverable from Git history.
- Lectures 07 and 08 lack reliable embedded title metadata, so their names are deliberately conservative instead of inventing unsupported subtopics.

- The lecture-15 title is conservative: its large PDF could not be text-inspected through the connector, so PCA is inferred from lecture 16's explicit review of PCA; verify the detailed agenda when feasible.
- The PDF under lecture 22 contains an internal cover title reading *Sesión 21*; its repository number remains 22, matching the uploaded filename, until the course sequence is independently reconciled.
