# 📅 Day 9 – Linear Regression | Internship 

**🧠 Learning Objective:**

To understand the theory and implementation of Simple and Multiple Linear Regression using scikit-learn. Learn how to build, evaluate, and visualize regression models and interpret the results using key metrics.

## 🧪 Mini Project: 

**Predicting Student Performance**

**🎯 Goal:**

Predict student scores based on the number of hours studied using Simple Linear Regression.

**📁 Dataset:**

Hours,Score
2.5,21
5.1,47
3.2,27
...

**✅ Tasks Completed:**

Loaded and cleaned the student_scores.csv dataset.

Trained a Simple Linear Regression model using Hours as input and Score as output.

Visualized the regression line on top of the scatter plot.

Evaluated model using:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

Built a residual plot to verify model assumptions.

**📊 Output:**

R² Score: ~0.95 (High correlation between hours studied and scores)

Conclusion: Model predicts student performance accurately from study hours.

## 🏡 Assignment:

**House Price Prediction with Multiple Linear Regression**

**🎯 Goal:**

Predict house prices based on various features such as area, bedrooms, bathrooms, stories, and other categorical inputs.

**📁 Dataset:**

housing.csv – containing features like:

area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning, furnishingstatus, etc.

**✅ Tasks Completed:**

Preprocessed the dataset:

Handled categorical features using one-hot encoding

Dropped or imputed missing values

Trained a Multiple Linear Regression model

Evaluated using:

MAE, MSE, RMSE, R² Score

**Visualized:**

Simple Regression Line (area vs price)

Actual vs Predicted Plot

Residual Plot

Saved the trained model using joblib as house_price_model.pkl

### 📊 Model Performance:

| Metric | Value (Example) |
| ------ | --------------- |
| MAE    | ₹ 850,000       |
| MSE    | 1.1 × 10¹²      |
| RMSE   | ₹ 1,050,000     |
| R²     | 0.89            |

**🧠 Key Insights:**

Area, Air Conditioning, and Furnishing Status were top contributors.

Model explained 89% of the variance in house price.

**📘 Key Concepts Covered:**

Concept	Explanation
Underfitting	Model is too simple and performs poorly
Overfitting	Model memorizes training data, fails on new data
Feature Importance	Regression coefficients indicate which features impact the target most
Multicollinearity	High correlation between features can distort coefficients
Residual Plot	Used to check homoscedasticity and model assumptions

## 🛠 Tools & Libraries Used:

Python

Pandas, NumPy

Matplotlib, Seaborn

scikit-learn

joblib

## ✅ End-of-Day Outcome:

By the end of Day 9, I:

Understood the math and use-cases of Linear Regression.

Implemented both Simple and Multiple Linear Regression models.

Learned to evaluate model performance using MAE, MSE, RMSE, and R².

Visualized regression lines, predictions, and residuals.

Successfully saved and reused the trained model.
