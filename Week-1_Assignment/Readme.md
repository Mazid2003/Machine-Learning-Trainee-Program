# 📊 Week 1 Assignment: Data Cleaning and Preprocessing – Sales Dataset

**🧼 Objective:**

The goal of this assignment was to clean and prepare a raw sales dataset for analysis by handling missing values, duplicates, and formatting issues. This is a crucial first step in any data science pipeline.

### 1. Handling Missing Values

Numerical Columns (Quantity, Price):

Missing values were filled with the mean of the respective columns.

This approach maintains the data distribution and avoids skewing aggregate statistics.

Categorical Columns (Customer Name, Region):

Missing values were replaced with "Unknown" to preserve the structure of the dataset while clearly indicating unavailable entries.

Date Column (Sale Date):

Missing dates were filled with the most common sale date (mode).

This ensures temporal consistency and avoids dropping potentially useful records.

### 2. Removing Duplicates

Identified and removed duplicate rows based on all columns.

This step prevented overcounting during analysis and ensured data integrity.

### 3. Creating Derived Columns

Added a new column Total_Sale calculated as:
```
Total_Sale = Quantity × Price
```
This derived metric was used to analyze revenue patterns and peak sales periods.

### 4. Saving Cleaned Data
The cleaned DataFrame was saved as sales_data_cleaned.csv for future use in modeling and visualization.

## 📈 Insights from Cleaned Data

Top Products by Quantity Sold: Identified the top 3 products with the highest sales volume.

Sales by Region: Grouped data by region and visualized total sales quantity using a bar chart.

Peak Sales Date: Found the date with the highest total revenue, useful for campaign or demand analysis.

### Descriptive Statistics:

Generated summary statistics (mean, median, min, max) for Quantity and Price to understand central tendencies and spread.

## ✅ Why This Matters?

Clean, well-structured data is critical for accurate business decisions, analytics, and machine learning. This cleaning process ensures that:

The dataset is complete and consistent.

Missing data does not bias the results.

We have a solid foundation for visualization, forecasting, or building predictive models.

Let me know if you'd like a badge, tabl

## 📈 Summary Statistics & Insights

Descriptive Stats: Calculated mean, median, min, and max for Quantity and Price.

Top Products: Identified top 3 products by total quantity sold.

Regional Sales: Grouped data by Region to find:

Total quantity sold per region

Average price per region

Highest Sales Date: Identified the date with the highest total sales value.

Visualization: Created a bar chart showing sales quantity by region.

## 💡 Key Learnings

Real-world datasets often contain missing, duplicate, or inconsistent data.

Imputation, deduplication, and feature engineering are critical for accurate analytics.

Clean data is the foundation for building robust machine learning models and drawing business insights.

