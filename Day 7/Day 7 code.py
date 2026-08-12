import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("student_scores1.csv")

print("Dataset:")
print(df)

# Input and output
X = df[["Hours"]]
y = df["Scores"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Input:")
print(X_train)

print("\nTesting Input:")
print(X_test)

print("\nTraining Output:")
print(y_train)

print("\nTesting Output:")
print(y_test)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))