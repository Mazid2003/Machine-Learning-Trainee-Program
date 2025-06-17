# 📅 Day 7 Log – Data Visualization with Seaborn

**🧠 Learning Objective**

The primary goal for Day 7 was to deepen my understanding of statistical data visualization using Seaborn, building upon the foundational skills learned with Matplotlib. I learned how to:

- Visualize distributions, relationships, and categorical data.

- Work with Pandas DataFrames seamlessly in Seaborn.

- Customize themes, color palettes, and figure aesthetics for presentation-ready charts.

## 📘 What is Seaborn?

Seaborn is a high-level Python library built on top of Matplotlib. It provides a simplified syntax for complex statistical plots and integrates perfectly with Pandas DataFrames, making it ideal for data analysis.

**🔑 Highlights:**

- Fewer lines of code for more attractive plots.

- Built-in color palettes and themes.

- Great for statistical visualizations (e.g., boxplots, heatmaps, KDEs).

### 🔧 Setup & Installation
```
pip install seaborn
```
### 🔗 Importing Libraries
```
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```
### 💻 Practice: Loading Built-in Datasets
```
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
iris = sns.load_dataset('iris')
```
## 📊 Seaborn Plot Types Covered

**🔹 1. Distribution Plots**

- histplot() – Histogram + KDE

- kdeplot() – Kernel Density Estimate

- boxplot() – Box-and-whisker summary

- violinplot() – Combines KDE and boxplot

**🔹 2. Relationship Plots**

- scatterplot() – Relationship between 2 numeric variables

- lineplot() – Trend visualization over time or ordinal values

- pairplot() – Scatterplot matrix

- jointplot() – Combined scatter + distribution

**🔹 3. Categorical Plots**

- countplot() – Frequency of each category

- barplot() – Aggregated value for each category

- stripplot() – Categorical scatter plot

- catplot() – Versatile figure-level plotting for categories

## 🎨 Styling & Themes
```
sns.set_theme(style='darkgrid')        # Other options: whitegrid, ticks, dark
sns.set_palette('pastel')              # Other options: deep, muted, bright, dark
```
### 🧪 Mini Project: EDA on Titanic Dataset

**✅ Tasks:**

- Distribution of numeric features – Age, Fare

- Relationship plots – Age vs. Fare, Age vs. Survived

- Categorical plots – Survival by Sex, Class distribution

- Use of multiple Seaborn charts with themes

- Added titles, axis labels, legends

- Saved plots using plt.savefig()

### 📝 Assignment: Visual Storytelling with Seaborn

**✅ Dataset Used: Iris Dataset**

**👇 Task Breakdown:**

**✔ 2 Distribution Plots**

- Distribution of Sepal Length

- Distribution of Petal Width

**✔ 2 Relationship Plots**

- Sepal Length vs Sepal Width (scatter)

- Petal Length vs Petal Width (scatter)

**✔ 2 Categorical Plots**

- Boxplot: Petal Length by Species

- Violinplot: Sepal Width by Species

**🖼️ All figures are customized with:**

- 🎨 Custom palettes

- 📌 Titles and axis labels

- 🧭 Legends

- 💾 Saved with plt.savefig("filename.png")



