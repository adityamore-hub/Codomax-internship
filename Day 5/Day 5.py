import pandas as pd

# Load dataset
df = pd.read_csv("student_scores1.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

# Dataset statistics
print("\nDataset Statistics:")
print(df.describe())

# Dataset information
print("\nDataset Information:")
df.info()
