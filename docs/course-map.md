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

## Notes on classification

- The K-means image-segmentation notebook and the semi-supervised digits notebook are grouped under lecture 09 because their main algorithmic role is K-means.
- The digits notebook is cross-referenced with lecture 13 because it also contains t-SNE, UMAP, ICA and PCA visualizations.
- The bivariate-normal and covariance notebooks are grouped with GMM rather than as generic probability notebooks because they were created to visualize the Gaussian components/covariance geometry used by GMM.
- The copied `02_end_to_end_machine_learning_project.ipynb` is not duplicated locally: it already belongs in the `hands-mlp/` subtree.
- Clearly unrelated notebooks from the original Drive dump (for example Black–Scholes/MCMC, Delaunay, and an education-economics plot) are intentionally excluded from the cleaned course tree. They remain recoverable from Git history.
- Lectures 07 and 08 lack reliable embedded title metadata, so their names are deliberately conservative instead of inventing unsupported subtopics.
