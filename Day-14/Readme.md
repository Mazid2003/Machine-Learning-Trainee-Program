# 📅 Day 14 – Principal Component Analysis (PCA): Summary

**🎯 Objectives**

Understand PCA and its use for dimensionality reduction and data visualization.

Learn the mathematics behind PCA (covariance, eigenvalues/vectors).

Implement PCA using scikit-learn.

Analyze explained variance, reconstruct data, and evaluate performance.

Explore applications, limitations, and advanced variants like Kernel PCA.

## 🧠 What is PCA?

PCA transforms high-dimensional, correlated data into a smaller set of uncorrelated principal components that capture the most variance. It helps in simplifying data while retaining its essential patterns.

## 🔧 Key Concepts

| Concept              | Summary                                                             |
| -------------------- | ------------------------------------------------------------------- |
| Standardization      | Ensures all features contribute equally by scaling to mean=0, std=1 |
| Covariance Matrix    | Measures how features vary together                                 |
| Eigenvalues/Vectors  | Identify directions (components) of maximum variance                |
| Principal Components | Top-k directions explaining most variance                           |

## 📊 PCA Steps in Python

- Standardize features using StandardScaler.

- Apply PCA() and extract components.

- Visualize using 2D/3D plots and explained variance ratio.

- Reconstruct original data and compute reconstruction error.

## ✅ Why PCA?

- Reduces noise and redundancy in data.

- Improves model speed and performance.

- Useful for visualizing high-dimensional datasets.

- Helps in feature extraction and avoiding overfitting.

## ⚖️ Applications

| Domain           | Use Case                               |
| ---------------- | -------------------------------------- |
| Image Processing | Compression and feature extraction     |
| Genomics         | Gene pattern discovery                 |
| Finance          | Risk analysis and market segmentation  |
| NLP              | Dimensionality reduction in embeddings |
| Marketing        | Customer segmentation & profiling      |

## ⚠️ Limitations

- Assumes linearity and Gaussian data distribution.

- Components may lack intuitive meaning.

- Sensitive to scaling and outliers.

- Loses information if too few PCs are retained.

## 📌 Visualizations & Tools Used

- Scree Plot for variance ratio

- 2D scatter plot for PC projections

- Reconstruction MSE for performance check

- Impact of scaling and outliers on PCA results

## 🧠 Advanced Variants

- Kernel PCA for non-linear data

- Sparse PCA for interpretable components

- Incremental PCA for large datasets

- Robust PCA for noisy data handling

## 📝 Summary Table

| Aspect              | Details                                      |
| ------------------- | -------------------------------------------- |
| Goal                | Dimensionality reduction                     |
| Output              | Uncorrelated principal components            |
| Core Math           | Covariance, eigenvectors, eigenvalues        |
| Data Prep           | Standardization recommended                  |
| Component Selection | Based on explained variance ratio            |
| Strengths           | Efficient, visual, removes multicollinearity |
| Limitations         | Linear assumption, interpretability issues   |


