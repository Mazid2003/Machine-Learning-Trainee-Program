# 🎯 K-Means Clustering - Customer Segmentation

This project is part of my Day 12 Internship Task and demonstrates the **K-Means Clustering** algorithm applied to **Customer Segmentation** using the `Mall_Customers.csv` dataset.

---

## 📌 Objectives Covered

- Understand the K-Means algorithm and clustering logic.
- Implement K-Means using **scikit-learn**.
- Apply the **Elbow Method** to choose the optimal number of clusters.
- Visualize clusters and centroids.
- Interpret business meaning behind clusters.
- Learn best practices and limitations of K-Means.

---

## 📊 Dataset

`Mall_Customers.csv` contains:

| Column              | Description                      |
|---------------------|----------------------------------|
| CustomerID          | Unique ID for customer           |
| Gender              | Male / Female                    |
| Age                 | Age of customer                  |
| Annual Income (k$)  | Income in thousands of dollars   |
| Spending Score (1-100) | Score assigned by the mall based on spending behavior |

We use only `Annual Income` and `Spending Score` for 2D clustering.

---

## 🧠 K-Means Clustering Intuition

1. Randomly pick `K` centroids.
2. Assign each point to the nearest centroid.
3. Recalculate centroids as the mean of the cluster points.
4. Repeat until centroids converge.

📐 **Mathematical Objective**: Minimize Within-Cluster Sum of Squares (WCSS).

---

## 📈 Optimal K using Elbow Method

The Elbow Method helps determine the best `K` by plotting WCSS vs. K:

```python
from sklearn.cluster import KMeans

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

