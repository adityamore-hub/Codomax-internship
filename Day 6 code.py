import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_scores1.csv")

# Display dataset
print("Student Score Dataset:")
print(df)

# -------------------------------
# 1. Scatter Plot
# -------------------------------

plt.scatter(df["Hours"], df["Scores"])

plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Hours vs Student Scores")

plt.show()


# -------------------------------
# 2. Bar Chart
# -------------------------------

plt.bar(df["Hours"], df["Scores"])

plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Hours vs Student Scores - Bar Chart")

plt.show()


# -------------------------------
# 3. Line Chart
# -------------------------------

plt.plot(df["Hours"], df["Scores"], marker="o")

plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Hours vs Student Scores - Line Chart")

plt.show()