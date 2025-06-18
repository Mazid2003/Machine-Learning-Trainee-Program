# Day 8 Log – Introduction to Supervised Learning

**🎯 Learning Objective**

Day 8 was focused on understanding Supervised Machine Learning, where models learn from labeled data to make predictions. The primary goal was to differentiate between regression and classification, implement basic models using Scikit-learn, and gain hands-on experience with the end-to-end ML pipeline.

## 📘 Supervised Learning – Theory Recap

**🧠 What is Supervised Learning?**

Supervised learning is a machine learning approach where the model is trained on input data (features) and known output labels (targets). The aim is to learn a mapping from inputs to outputs so the model can predict results on new data.

### ✅ Types of Supervised Learning:

| Type           | Goal                      | Example Use Cases                      |
| -------------- | ------------------------- | -------------------------------------- |
| Regression     | Predict continuous values | Predicting house prices or blood sugar |
| Classification | Predict categories        | Predicting survival or email spam      |


### 🔁 Machine Learning Workflow

The supervised learning pipeline covered the following steps:

Import Libraries – pandas, numpy, sklearn, seaborn, matplotlib.

Load Dataset – Titanic for classification; Diabetes for regression.

Data Cleaning – Dropping missing values, encoding categorical variables.

Feature & Label Separation – Identifying input variables (X) and target (y).

Train-Test Split – Ensuring unbiased model evaluation.

Model Training – Using LinearRegression or LogisticRegression.

Prediction – Generating predictions on test data.

Evaluation – Using metrics like Accuracy, MSE, Confusion Matrix.

Visualization – Scatterplots for regression, heatmaps for classification.

## 🧪 Hands-on Practice Highlights

**🏠 Regression Example: Diabetes Dataset**

- **Objective:** Predict diabetes progression based on clinical features.

- **Model Used:** Linear Regression.

- **Evaluation Metric:** Mean Squared Error (MSE) and R² Score.

- **Insight:** The model could explain around 45% of the variance. BMI and blood pressure were key contributors.

🚢 Classification Example: Titanic Dataset
Objective: Predict survival of passengers.

Model Used: Logistic Regression.

Evaluation Metrics: Accuracy and Confusion Matrix.

Insight: Female passengers and first-class travelers had a higher survival rate.

📊 Visualizations Used
Visualization	Purpose
Scatter Plot	Actual vs Predicted for Regression
Confusion Matrix	Evaluate classification performance
Count Plot / Bar Plot	Show distribution of categorical data
Heatmap	Feature correlation & confusion matrix

🔍 Key Concepts Learned
Concept	Description
Feature	An independent variable (e.g., age, fare, BMI)
Label	The target output variable (e.g., survived, disease score)
Train-Test Split	Divides data to train and evaluate the model
Accuracy	Percentage of correct predictions (used in classification)
MSE	Average squared error (used in regression)
Overfitting	When the model performs well on training but poorly on new data
Confusion Matrix	A summary of true vs. predicted classes

📁 Mini Project Summary
Title: Titanic Survival Classification

Model Used: Logistic Regression

Highlights: Data cleaning, feature engineering (sex encoding), accuracy evaluation, and confusion matrix plotting.

Outcome: Identified key survival influencers like gender and passenger class.

📁 Assignment Summary
Title: Diabetes Progression Prediction

Model Used: Linear Regression

Dataset: sklearn’s load_diabetes

Evaluation: MSE ≈ 2900; R² ≈ 0.45

Outcome: Demonstrated how patient data can predict disease progression over time.

✅ Day 8 Learning Outcomes
By the end of the session, I was able to:

Understand and explain what supervised learning is.

Distinguish between regression and classification tasks.

Use Scikit-learn to train simple ML models.

Prepare datasets for machine learning tasks.

Evaluate models using appropriate metrics.

Visualize model outputs effectively.

Apply the full ML pipeline independently.


