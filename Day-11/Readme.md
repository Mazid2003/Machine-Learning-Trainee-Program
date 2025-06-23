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

## 🔹 Hands-on: K-Means Clustering in Python

Used synthetic data of customers with Annual Income and Spending Score.

Scaled the data using StandardScaler.

Applied KMeans with n_clusters=3.

Visualized the results using a scatter plot.

Evaluated clustering using Silhouette Score.

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
