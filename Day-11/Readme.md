# 📅 Day 11 – Introduction to Unsupervised Learning

**🎯 Learning Objective:**

Today, I learned the fundamentals of unsupervised learning, how it's different from supervised learning, and explored popular algorithms like K-Means Clustering and Principal Component Analysis (PCA).

**📌 Key Concepts Covered:**

## 🔹 What is Unsupervised Learning?

Learns patterns from unlabeled data.

No predefined output — the goal is to discover hidden structures or groupings in the data.

| Aspect    | Supervised Learning        | Unsupervised Learning                |
| --------- | -------------------------- | ------------------------------------ |
| Data      | Labeled                    | Unlabeled                            |
| Objective | Predict outcome            | Discover structure                   |
| Examples  | Classification, Regression | Clustering, Dimensionality Reduction |
| Feedback  | From labels                | From internal patterns               |

## 🔹 Why Use Unsupervised Learning?

Explore unknown data.

Reduce dimensions for visualization or modeling.

Perform customer segmentation, anomaly detection, and market basket analysis.

## 🔹 Types of Unsupervised Learning:

**Clustering**(e.g., K-Means, Hierarchical, DBSCAN)

**Dimensionality Reduction** (e.g., PCA, t-SNE, Autoencoders)

## Common Unsupervised Learning Algorithms

### 🔹 K-Means Clustering

Assigns data points to K clusters by minimizing the sum of squared distances to cluster centers.

Steps:

Initialize K centroids randomly.

Assign each data point to nearest centroid.

Recalculate centroids as mean of assigned points.

Repeat until convergence.

### 🔹 Hierarchical Clustering

Builds clusters incrementally by merging or splitting.

Results in a dendrogram — a tree-like diagram showing cluster relationships.

Useful for smaller datasets or when the number of clusters is unknown.

### 🔹 Principal Component Analysis (PCA)

Transforms features into a smaller set of uncorrelated components (principal components).

Each component captures the maximum variance possible.

Used for visualization, noise reduction, and speeding up other algorithms.

## 🔹 Hands-on: K-Means Clustering in Python

Used synthetic data of customers with Annual Income and Spending Score.

Scaled the data using StandardScaler.

Applied KMeans with n_clusters=3.

Visualized the results using a scatter plot.

Evaluated clustering using Silhouette Score.

- Silhouette Score: Measures how similar a point is to its own cluster vs other clusters.

- Calinski-Harabasz Index: Ratio of between-cluster dispersion to within-cluster dispersion.

- Davies-Bouldin Index: Lower values indicate better clustering.

## 🔹 Real-World Use Cases:

Customer Segmentation

Fraud/Anomaly Detection

Document Clustering

Image Compression

Gene Analysis

## ⚠️ Challenges in Unsupervised Learning:

No labels to validate clusters

Choosing the right number of clusters (e.g., K)

Sensitive to feature scaling

Hard to interpret some cluster results

## 📝 Summary:

Today I gained a solid understanding of unsupervised learning techniques, especially clustering with K-Means, and how they’re used in real-world applications like customer segmentation. I also explored how to evaluate cluster quality using the Silhouette Score.
