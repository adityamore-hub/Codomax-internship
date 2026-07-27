import pandas as pd

import pandas as pd

df = pd.read_csv("student_scores1.csv", encoding="latin1")

print(df.head())

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Information:")
print(df.info())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nStatistics:")
print(df.describe())
