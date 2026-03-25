import pandas as pd

data = {
    'Name': ['Sneha', 'Rahul', 'sneha', 'Ananya', None],
    'Marks': [90, 80, 90, None, 70]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

df = df.drop_duplicates()
df['Name'] = df['Name'].fillna("Unknown")
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['Name'] = df['Name'].str.lower()

print("\nCleaned Data:\n", df)

'''Data cleaning is an essential step in data analysis and machine learning. In this program, duplicates are removed to avoid repeated records that may bias the results.

Missing values are handled by either replacing them with meaningful values such as the mean or a placeholder. Text data is standardized by converting all names to lowercase to maintain consistency.'''