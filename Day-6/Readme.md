# 📊 Day 6 – Data Visualization with Matplotlib

**Date: 16/06/2025**

## 📌 Overview

Data Visualization is the graphical representation of data that enables better understanding, interpretation, and communication of data patterns, trends, and outliers. It plays a critical role in data analysis and decision-making.

In this session, we explored Matplotlib, a fundamental Python library for creating static, interactive, and animated visualizations.

## 📚 1. What is Matplotlib?

Matplotlib is a 2D plotting library in Python that enables the creation of high-quality charts and plots.

It is a part of the SciPy stack and widely used for visual analytics.

The commonly used module is matplotlib.pyplot, which offers MATLAB-like functionality.

## ⚙️ 2. Anatomy of a Matplotlib Figure

Understanding the structure of a Matplotlib figure is key:

| Component  | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| `Figure`   | The top-level container for all plot elements.                    |
| `Axes`     | The area where data is plotted (can have multiple axes/subplots). |
| `Axis`     | Represents X and Y axes with ticks, limits, and labels.           |
| `Elements` | Titles, legends, labels, ticks, gridlines, markers, etc.          |

## 3. Code Walkthrough and Practice

**3.1 ✅ Basic Line Plot**
```
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
```
This produces a simple 2D line graph.

Grid helps improve readability.

## 📊 4. Types of Charts

**🔹 Line Chart**
```
plt.plot(months, sales, color='green', linestyle='--', marker='o')
```
Used to show trends over time.

**🔹 Bar Chart**
```
plt.bar(categories, values, color='orange')
```
Suitable for comparing categorical values.

**🔹 Scatter Plot**
```
plt.scatter(x, y, color='blue', marker='x')
```
Used to identify relationships or correlations between variables.

**🔹 Pie Chart**
```
labels = ['Python', 'Java', 'C++']
sizes = [40, 30, 30]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Popularity")
plt.axis('equal')  # Ensures the pie is circular
plt.show()
```
Shows percentage distribution.

Use autopct to display values.

## 🎨 5. Plot Customization Techniques

**Example:**
```
plt.plot(x, y, color='red', label='Revenue', marker='s')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.show()
```
### Common Customization Options:

| Feature     | Example Usage     |
| ----------- | ----------------- |
| Color       | `color='blue'`    |
| Marker      | `marker='o'`      |
| Line Style  | `linestyle='--'`  |
| Legend      | `plt.legend()`    |
| Axis Limits | `plt.xlim(0, 10)` |
| Grid        | `plt.grid(True)`  |

## 🧩 6. Multiple Plots / Subplots
```
plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title("Plot 1")

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title("Plot 2")

plt.tight_layout()
plt.show()
```
subplot(rows, cols, index) helps in organizing multiple plots in one figure.

tight_layout() avoids overlap.

## 📈 7. Plotting from Pandas DataFrames
```
import pandas as pd
df = pd.read_csv('sales.csv')

df['Total Sales'].plot(kind='line', title='Sales Over Time')
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()
plt.show()
```
pandas.DataFrame.plot() integrates directly with Matplotlib.

Very useful for fast and simple visualizations from dataframes.

### 🧠 Common Errors & Solutions

| Error                        | Cause                                     | Fix                                  |
| ---------------------------- | ----------------------------------------- | ------------------------------------ |
| `plt.show()` doesn't display | Missing `%matplotlib inline` in notebooks | Add `%matplotlib inline` at top      |
| Pie chart looks oval         | Axes not equal                            | Use `plt.axis('equal')`              |
| Overlapping labels           | Tight layout not used                     | Add `plt.tight_layout()`             |
| Legends missing              | No `plt.legend()` or labels               | Add `label` in plot & `plt.legend()` |
| x and y length mismatch      | Unequal data lengths                      | Ensure `len(x) == len(y)`            |

## 📝 Summary Notes

Matplotlib is foundational for any data analyst or data scientist.

Start with plt.plot() and gradually explore other charts.

Always focus on clarity: use labels, legends, grids, and colors wisely.

Combine Matplotlib with Pandas for faster EDA and visualization workflows.

Use subplots to compare multiple data series in a single figure.

### ✅ What I Learned

Created different types of plots using matplotlib.pyplot

Customized plots with legends, titles, and styles

Learned to create subplots and visualizations from DataFrames

Debugged common visualization issues










