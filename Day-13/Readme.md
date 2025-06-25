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

