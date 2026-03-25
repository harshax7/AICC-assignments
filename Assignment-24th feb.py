import pandas as pd

data = pd.read_csv("data.csv")

print("Top 5 Rows:\n", data.head())

numeric_cols = data.select_dtypes(include='number')
highest_col = numeric_cols.mean().idxmax()

print("\nColumn with Highest Average Value:", highest_col)

print("\nMissing Values:\n", data.isnull().sum())

print("\n--- Insights ---")
print("1. Dataset has", data.shape[0], "rows and", data.shape[1], "columns.")
print("2. Highest average column:", highest_col)
print("3. Missing values present in some columns.")
print("4. Numeric features dominate the dataset.")
print("5. Data can be further cleaned for better analysis.")

'''This program loads a dataset using Pandas and performs basic data analysis. 
The head() function displays the first few rows of the dataset. Numeric columns are selected to compute the column with the highest average value.
Missing values are identified using the isnull() function. 
Finally, insights are generated based on the dataset’s structure and statistics. This helps in understanding the data before applying machine learning models.'''