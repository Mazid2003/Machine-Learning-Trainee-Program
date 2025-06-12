# 📊 Day 4 – Pandas: DataFrames, Importing CSV, Filtering, Grouping

Welcome to Day 4 of the ML Trainee Program! Today we dove deep into Pandas, a powerful Python library used extensively for data analysis and manipulation. Below is a comprehensive summary of the key topics and practical applications discussed during the session.

## 🔷 1. Introduction to Pandas and DataFrames

**🔹 What is Pandas?**

Pandas is an open-source Python library built on top of NumPy. It provides fast, flexible, and expressive data structures designed to work with structured (tabular or labeled) data.

**🔹 Key Data Structures:**

Series: 1D labeled array (like a column in Excel)

DataFrame: 2D labeled data structure (like a spreadsheet or SQL table)

**🔹 Why Use Pandas?**

Handles missing data efficiently

Reshaping and pivoting datasets is easy

Powerful groupby functionality for aggregation

Time series support

Read/write support for multiple file types (CSV, Excel, SQL)
```
import pandas as pd
```

## 🔷 2. Creating DataFrames

**🔸 From a Python Dictionary:**
```
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
```
**🔸 From Series or Lists:**
```
names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages = pd.Series([25, 30, 35, 40])
df = pd.DataFrame({'Name': names, 'Age': ages})
```
**🔸 From a List of Dictionaries:**
```
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}
]
df = pd.DataFrame(data)
```
## 🔷 3. Importing Data from CSV Files

**🔸 Reading a CSV File:**
```
df = pd.read_csv('filename.csv')
```
**🔸 Useful Parameters in read_csv():**

sep=',': Delimiter

index_col='ID': Use column as index

parse_dates=['Date']: Convert dates

usecols=[...]: Read specific columns

na_values=['NA']: Treat values as NaN
```
df = pd.read_csv('data.csv', index_col='ID', parse_dates=['Date'])
```
**🔸 Reading in Chunks (for large files):**
```
for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    process(chunk)
```
**🔸 Saving a DataFrame to CSV:**
```
df.to_csv('output.csv', index=False)
```
## 🔷 4. Exploring and Inspecting DataFrames
```
df.head()         # First 5 rows
df.tail()         # Last 5 rows
df.shape          # (rows, columns)
df.columns        # Column names
df.info()         # Column info
df.describe()     # Statistical summary
```
**🔸 Accessing Data:**
```
df['Name']            # Single column
df[['Name', 'Age']]   # Multiple columns
df.loc[2]             # Row by label
df.iloc[2]            # Row by index position
```
## 🔷 5. Filtering DataFrames
**🔸 Boolean Filtering:**
```
df[df['Age'] > 30]
```
**🔸 Multiple Conditions:**
```
df[(df['Age'] > 25) & (df['City'].isin(['Chicago', 'Houston']))]
```
**🔸 String Methods:**
```
df[df['Name'].str.startswith('A')]
```
**🔸 Resetting Index:**
```
df = df.reset_index(drop=True)
```
## 🔷 6. Grouping and Aggregation

**🔸 Grouping with groupby():**
```
grouped = df.groupby('City')
```
**🔸 Aggregating Groups:**
```
grouped['Sales'].sum()
grouped['Expenses'].mean()
```
**Multiple Aggregations**
```
grouped.agg({
    'Sales': ['sum', 'mean'],
    'Expenses': ['mean', 'max']
})
```
**🔸 Iterating Over Groups:**
```
for city, group in grouped:
    print(f"City: {city}")
    print(group)
```
**🔸 Grouping by Multiple Columns:**
```
df['Year'] = [2023, 2023, 2024, 2024, 2024]
grouped = df.groupby(['City', 'Year']).sum()
```
## 🔷 7. Practical Examples

**✅ Example 1: Filter High Sales**
```
df = pd.read_csv('sales_data.csv')
high_sales = df[df['Sales'] > 1000]
print(high_sales.head())
```
**✅ Example 2: Group by Category**
```
grouped = df.groupby('Category')['Sales'].sum()
```
**✅ Example 3: Filter + Group**
```
filtered = df[df['Region'] == 'North']
grouped = filtered.groupby('Product')['Profit'].mean()
```
## 🔷 8. Common Pitfalls and Best Practices
**❌ Avoid This:**
```
df[df['Age'] > 25 & df['City'] == 'New York']  # Incorrect
```
✅ Do This:
python
Copy
Edit
df[(df['Age'] > 25) & (df['City'] == 'New York')]
🔸 Avoid SettingWithCopyWarning:
python
Copy
Edit
filtered = df[df['Age'] > 30].copy()
filtered['NewCol'] = 1
🔸 Handle Missing Data:
python
Copy
Edit
df.isna()
df.fillna(value)
df.dropna()
✅ Summary
Pandas provides a robust set of tools for working with structured data.

Load, inspect, and manipulate data easily with DataFrames.

Use boolean indexing for filtering and groupby for aggregation.

Combine filtering and grouping for powerful data analysis workflows.

Always inspect your data using .info(), .head(), and .describe() before diving deep.


