import pandas as pd

# Load the dataset
file_path = "currency.csv"
df = pd.read_csv(file_path)

# Inspect the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore the structure
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())
