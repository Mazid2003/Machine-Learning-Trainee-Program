# 🧹 Day 5 – Data Cleaning with Pandas

**Date:13/06/2025**

ML Trainee Program – Practical Data Preprocessing

**✅ Topics Covered**

Introduction to Data Cleaning

Handling Null (Missing) Values

Detecting and Removing Duplicates

Renaming Columns

Best Practices for Data Cleaning

Practical Hands-on Examples

## 🔷 1. Introduction to Data Cleaning

Data cleaning is a crucial step in the data analysis and machine learning pipeline. Real-world datasets often come with missing, duplicate, or inconsistent values, which can affect model performance and analysis outcomes.

**Why it matters:**

Ensures data reliability and accuracy

Prevents downstream processing errors

Makes analysis and modeling more effective

Supports better decision-making

## 🔷 2. Handling Null / Missing Values

**🔹 What are Nulls?**

Nulls represent missing or undefined data. In Pandas, nulls are usually represented as NaN, None, or NaT.

**🔹 Detecting Nulls:**
```
df.isnull()           # Boolean DataFrame of nulls
df.isnull().sum()     # Count nulls per column
df.isnull().sum().sum()  # Total nulls
df.isnull().values.any()  # Check if any nulls exist
```
**🔹 Dropping Null Values:**
```
df.dropna()               # Drops rows with any nulls
df.dropna(axis=1)         # Drops columns with nulls
df.dropna(how='all')      # Drops rows where all values are null
df.dropna(thresh=2)       # Keeps rows with at least 2 non-null values
df.dropna(subset=['Age']) # Drops rows with nulls in 'Age'
```
**🔹 Filling Null Values:**
```
df['Age'].fillna(0)                     # Fill with constant
df['Age'].fillna(df['Age'].mean())     # Fill with mean
df.fillna(method='ffill')              # Forward fill
df.fillna(method='bfill')              # Backward fill
df['Age'].interpolate(method='linear') # Interpolation
```
## 🔷 3. Identifying and Removing Duplicates

**🔹 Detect Duplicates:**
```
df.duplicated()
```
**🔹 Remove Duplicates:**
```
df.drop_duplicates()                     # Keep first occurrence
df.drop_duplicates(keep='last')          # Keep last occurrence
df.drop_duplicates(subset=['Name'])      # Based on specific column
```
Duplicates should be removed to avoid data bias and redundancy.

## 🔷 4. Renaming Columns

Renaming columns enhances clarity and makes datasets easier to work with.

**🔹 Rename Specific Columns:**
```
df.rename(columns={'Nm': 'Name', 'Ag': 'Age'}, inplace=True)
```
**🔹 Rename All Columns at Once:**
```
df.columns = ['Name', 'Age']
```
## 🔷 5. Best Practices for Data Cleaning

✅ Use .info(), .head(), .describe() regularly to inspect your data

✅ Make a copy of the original data before making major changes

✅ Handle nulls appropriately depending on data type and context

✅ Document all cleaning steps for reproducibility

✅ Be cautious of SettingWithCopyWarning when modifying filtered data

## 🔷 6. Practical Examples

**🔸 Example 1: Fill Null Values**
```
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
```
**🔸 Example 2: Remove Duplicate Rows**
```
df = df.drop_duplicates(subset=['Name'])
```
**🔸 Example 3: Rename Columns**
```
df.rename(columns={'Nm': 'Name', 'Ag': 'Age'}, inplace=True)
```
## ✅ Summary

Nulls are handled using isnull(), dropna(), fillna(), and interpolate()

Duplicates can be detected via duplicated() and removed with drop_duplicates()

Column names can be renamed for clarity using rename() or by modifying df.columns

Cleaning data properly prepares it for reliable analysis and modeling


