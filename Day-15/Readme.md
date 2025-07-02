# Day-15: 💼 Customer Segmentation Mini Project 

**Date: 27/06/2025**

**🎯 Learning Objectives**

In this mini-project, I aimed to:

- Understand the business purpose of customer segmentation.

- Perform data cleaning, feature engineering, and exploratory analysis.

- Apply clustering algorithms (mainly K-Means) to segment customers.

- Analyze clusters to derive actionable insights.

- Develop clear visualizations and business recommendations.

- Build skills in data preprocessing, model selection, evaluation, and presentation.

## 1️⃣ What is Customer Segmentation?

Customer segmentation is the process of dividing customers into distinct groups based on shared characteristics. These segments help businesses:

- Deliver personalized marketing.

- Improve customer experience.

- Develop tailored products.

- Allocate resources efficiently.

## 2️⃣ Why is Customer Segmentation Important?

| Purpose                  | Benefit                                       |
| ------------------------ | --------------------------------------------- |
| 🎯 Targeted Marketing    | Higher engagement, better conversion          |
| 🛠 Product Development   | Design offerings matching customer needs      |
| 🔁 Customer Retention    | Focus on high-value or at-risk customers      |
| 💰 Resource Optimization | Improve ROI by prioritizing valuable segments |
| 🚀 Competitive Edge      | Understand customer preferences faster        |

## 3️⃣ Types of Customer Segmentation

| Type          | Example Variables                  |
| ------------- | ---------------------------------- |
| Demographic   | Age, Gender, Income                |
| Geographic    | Region, City, Climate              |
| Behavioral    | Purchase frequency, Loyalty        |
| Psychographic | Lifestyle, Interests               |
| RFM           | Recency, Frequency, Monetary value |


## 4️⃣ Project Workflow

| Step                         | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| **Define Objective**         | Identify groups for targeted marketing and strategy |
| **Data Collection**          | Customer demographic and transactional data         |
| **Data Cleaning**            | Handle missing values, outliers                     |
| **EDA**                      | Understand feature distributions and relationships  |
| **Model Selection**          | K-Means clustering chosen for scalability           |
| **Apply Clustering**         | Identify distinct customer segments                 |
| **Profile Segments**         | Summarize characteristics of each cluster           |
| **Business Recommendations** | Translate clusters into actions                     |
| **Presentation**             | Create clear, visual reports                        |

## 5️⃣ Dataset Overview

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| CustomerID     | Unique customer identifier                    |
| Age            | Customer age                                  |
| Gender         | Male / Female                                 |
| Annual Income  | In thousands (\$k)                            |
| Spending Score | Score from 1-100 indicating spending behavior |

## 6️⃣ Data Cleaning & Feature Engineering

- 🧹 Missing values: Checked, none found.

- 🔢 Encoding: Gender converted using binary encoding.

- ⚖ Scaling: StandardScaler applied to Age, Annual Income, Spending Score.

- 🚫 Outliers: Visual inspection via boxplots; none extreme enough to remove.

## 7️⃣ Exploratory Data Analysis (EDA)

- 📊 Plotted histograms to see feature distributions.

- 🔥 Used heatmaps to check feature correlations.

- 🧭 Pairplots to explore interactions between variables.

## 8️⃣ Segmentation Method

- ✅ Chosen Algorithm: K-Means Clustering

- Scalable to larger datasets.

- Clear interpretability (centroids represent segments).

- ✅ Other considered: Hierarchical clustering (visual exploration).

## 9️⃣ Optimal Cluster Selection

- 🟣 Elbow Method: Plotted inertia vs. cluster number → elbow at k=4

- 🟣 Silhouette Score: Confirmed k=4 gave good separation (score ≈ 0.45)

## 🔟 Cluster Profiling

| Cluster | Profile                               | Insight                |
| ------- | ------------------------------------- | ---------------------- |
| 0       | Young, low income, high spender       | Build loyalty programs |
| 1       | Middle-aged, high income, low spender | Upsell premium offers  |
| 2       | Older, mid income, mid spender        | Retention strategies   |
| 3       | Mixed age, low income, low spender    | Reactivation campaigns |

## 1️⃣1️⃣ Business Recommendations

- Design cluster-specific marketing campaigns.

- Tailor loyalty, upsell, cross-sell strategies.

- Allocate marketing budgets efficiently.

- Monitor segment engagement over time.

## 1️⃣2️⃣ Suggested KPIs

| KPI                              | Purpose                         |
| -------------------------------- | ------------------------------- |
| 🎯 CLV (Customer Lifetime Value) | Track value by segment          |
| 🛒 Average Order Value           | Monitor spending                |
| 🔁 Retention / Churn             | Assess loyalty                  |
| 💸 Campaign Conversion Rate      | Measure marketing effectiveness |
| 📈 Segment-wise Revenue          | Evaluate growth                 |

## 1️⃣3️⃣ Challenges

- Data quality impacts cluster accuracy.

- Feature choice crucial for meaningful segments.

- Clusters must be business-interpretable.

- Customer behavior evolves → regular updates needed.

## 1️⃣4️⃣ Extensions

- Add RFM features or online behavior data.

- Try Gaussian Mixture, DBSCAN, or deep clustering.

- Deploy real-time segmentation in production.

## 1️⃣5️⃣ Summary

| Step                    | Description                     |
| ----------------------- | ------------------------------- |
| 🎯 **Define Objective** | Goal-driven segmentation        |
| 📦 **Data Collection**  | Customer data gathered          |
| 🧹 **Data Cleaning**    | Preprocessing for quality       |
| 📊 **EDA**              | Patterns & insights             |
| ⚙ **Model Selection**   | K-Means clustering used         |
| 🔍 **Apply Clustering** | 4 clusters identified           |
| 📝 **Profile Segments** | Clear segment personas          |
| 💡 **Recommendations**  | Actionable marketing strategies |
| 📈 **Monitor & Update** | Continuous improvement          |

> 💡 This project demonstrated my ability to apply machine learning for real business impact, including model development, interpretation, and strategy design.
