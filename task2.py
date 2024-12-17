import pandas as pd

#Load your dataset
file_path = "currency.csv"
df = pd.read_csv(file_path)

# Compute basic statistics for numerical columns
print("Basic Statistics for Numerical Columns:")
print(df.describe())

# Convert 'Code' column to numeric, invalid parsing will be set as NaN
df['Code'] = pd.to_numeric(df['Code'], errors='coerce')

# Group by 'Name' and calculate the mean, ignoring NaN value
grouped_data = df.groupby('Name')['Code'].mean()

print("\nGroup-wise Mean of Numerical Column:")
print(grouped_data)

# 3. Identify patterns or interesting findings
# Example: Find the top N groups based on mean value
top_groups = grouped_data.sort_values(ascending=False).head(5)
print("\nTop 5 Groups with Highest Mean:")
print(top_groups)
