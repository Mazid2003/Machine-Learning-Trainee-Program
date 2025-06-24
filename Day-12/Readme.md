# 🎯Day-12: K-Means Clustering - A Deep Dive

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

```
from sklearn.cluster import KMeans

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
```

## ✅ Final Clustering (K=5)

Cluster visualization with centroids:
```
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
```

## 📊 Cluster Interpretation

| Cluster | Characteristics              | Insights                       |
| ------- | ---------------------------- | ------------------------------ |
| 0       | Low income, high spending    | Careless spenders              |
| 1       | High income, low spending    | Careful conservative customers |
| 2       | Moderate income and spending | Average consumers              |
| 3       | High income, high spending   | Target premium customers       |
| 4       | Low income, low spending     | Budget-conscious customers     |

## 📚 Key Learnings

K-Means is best for spherical clusters and numeric data.

Choosing K is critical (use Elbow or Silhouette).

Feature scaling (StandardScaler) improves results.

Outliers and poor initialization affect clustering.

## 🚀 Applications

Customer Segmentation

Image Compression

Anomaly Detection

Recommendation Systems

## 🛠️ Tools Used

Python 

pandas, numpy

matplotlib

scikit-learn

libraries

## 💡 Conclusion

This project gave me hands-on experience in:

Understanding how unsupervised learning groups similar data.

Using scikit-learn to apply K-Means in the real world.

Interpreting and visualizing business insights from clusters.


