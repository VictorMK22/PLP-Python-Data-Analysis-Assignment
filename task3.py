import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# File path
file_path = "currency.csv"

try:
    # Attempt to load the dataset
    df = pd.read_csv(file_path)
    print("File successfully loaded.")
    
    # Check for missing data and handle it
    if df.isnull().values.any():
        print("Warning: Dataset contains missing values. Cleaning data...")
        df = df.dropna()  # Drop rows with missing values
        print("Missing values removed.")

    # Ensure 'Code' column exists
    if 'Code' not in df.columns or 'Symbol' not in df.columns:
        raise KeyError("Required columns 'Code' or 'Symbol' not found in the dataset.")

    # Convert 'Code' column to numerical values
    df['Code_Num'] = pd.factorize(df['Code'])[0]

    # Line Chart
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Code_Num'], color='blue', marker='o', linestyle='-')
    plt.title('Line Chart of Code Values Over Index')
    plt.xlabel('Index')
    plt.ylabel('Code (Numerical Representation)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar Chart
    plt.figure(figsize=(10, 6))
    symbol_counts = df['Symbol'].value_counts().head(10)
    sns.barplot(x=symbol_counts.index, y=symbol_counts.values, palette='viridis')
    plt.title('Top 10 Most Frequent Symbols')
    plt.xlabel('Symbol')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Symbol'].value_counts(), bins=20, kde=False, color='purple')
    plt.title('Distribution of Symbol Frequencies')
    plt.xlabel('Frequency of Symbols')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df.index, y=df['Code_Num'], color='blue')
    plt.title('Scatter Plot of Code Values Over Index')
    plt.xlabel('Index')
    plt.ylabel('Code (Numerical Representation)')
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the file path and try again.")
except KeyError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: Invalid data detected - {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
