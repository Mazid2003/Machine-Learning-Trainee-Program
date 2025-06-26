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

## 📊 Step-by-Step PCA Algorithm

- Standardize the data to zero mean and unit variance.

- Compute covariance matrix of standardized data.

- Calculate eigenvalues and eigenvectors of covariance matrix.

- Sort eigenvectors by descending eigenvalues.

- Select top kk eigenvectors based on explained variance.

- Project data onto new subspace defined by selected eigenvectors.

- Use ZZ for further analysis or modeling.

## ✅ Why PCA?

- Reduces noise and redundancy in data.

- Improves model speed and performance.

- Useful for visualizing high-dimensional datasets.

- Helps in feature extraction and avoiding overfitting.

## PCA Intuition

Imagine you have a dataset with two highly correlated features (e.g., height and weight). Plotting them shows data points clustered roughly along a line:

- PCA finds the direction (line) where data varies the most (maximum variance).

- The first principal component is that line.

- The second component is orthogonal (at right angles) to the first and explains remaining variance.

- Projecting data onto these components reduces redundancy.

## ⚖️ Applications

| Domain           | Use Case                               |
| ---------------- | -------------------------------------- |
| Image Processing | Compression and feature extraction     |
| Genomics         | Gene pattern discovery                 |
| Finance          | Risk analysis and market segmentation  |
| NLP              | Dimensionality reduction in embeddings |
| Marketing        | Customer segmentation & profiling      |

## Advantages of PCA

- Efficient dimensionality reduction.

- Removes multicollinearity by creating uncorrelated features.

- Helps visualize high-dimensional data.

- Can improve speed and accuracy of downstream models.

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


