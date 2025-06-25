# 📅 Day 13 – Hierarchical Clustering: Comprehensive Deep Dive

**Date: 25/06/2025**

**🎯 Objectives**

Understand how Hierarchical Clustering works and how it differs from K-Means.

Explore types (Agglomerative & Divisive), distance metrics, and linkage methods.

Learn to build and interpret dendrograms.

Implement clustering using scikit-learn and scipy.

Compare clustering quality using silhouette score.

Understand real-world applications, limitations, and best practices.

## 🔍 What is Hierarchical Clustering?

Hierarchical clustering is an unsupervised learning technique that builds a tree-like structure (dendrogram) of clusters. Unlike K-Means, it doesn't require predefining the number of clusters and helps in exploratory data analysis.

## 🧱 Types of Hierarchical Clustering

| Type          | Description                                 |
| ------------- | ------------------------------------------- |
| Agglomerative | Bottom-up: Merge points into clusters       |
| Divisive      | Top-down: Split one big cluster recursively |

**✅ Agglomerative is more common and used in this project.**

## 🧮 Distance Metrics & Linkage Criteria

**Distance Metrics:** Euclidean, Manhattan, Cosine, Correlation

**Linkage Types:**

| Linkage  | Description                             |
| -------- | --------------------------------------- |
| Single   | Closest point between clusters          |
| Complete | Farthest point between clusters         |
| Average  | Mean distance of all points in clusters |
| Ward     | Minimizes within-cluster variance       |

### 🌲 Dendrograms

A dendrogram is a tree diagram that shows the merge process of clusters. You can “cut” it at a certain height to decide the number of clusters.

### 🧪 Implementation (Python)

- Used scipy to plot dendrograms

- Used AgglomerativeClustering from scikit-learn to generate cluster labels

- Tested multiple linkage methods and evaluated with Silhouette Score

### 📊 Key Findings (Based on Iris Dataset)

| Linkage  | Silhouette Score |
| -------- | ---------------- |
| Ward     | 0.4467           |
| Average  | 0.4803           |
| Complete | 0.4496           |
| Single   | **0.5046** ✅     |

**🔎 Single Linkage performed best in this run — showing more distinct and separated clusters.**

## ⚖️ Pros & Cons

| ✅ Advantages                         | ⚠️ Limitations                 |
| ------------------------------------ | ------------------------------ |
| No need to predefine K               | Slow on large datasets (O(n³)) |
| Dendrogram gives multi-level insight | Sensitive to outliers          |
| Intuitive and easy to visualize      | Merges are irreversible        |


