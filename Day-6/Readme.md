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














