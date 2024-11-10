import pandas as pd

# Load the dataset
df = pd.read_csv("data/customers.csv")

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
