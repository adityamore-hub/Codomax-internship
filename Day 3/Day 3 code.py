import numpy as np

marks = np.array([78, 85, 92, 67, 88])

print("Marks:", marks)

print("\nFirst Student:", marks[0])
print("Last Student:", marks[-1])
print("First Three Marks:", marks[:3])

print("\nMarks + 5:", marks + 5)
print("Marks - 5:", marks - 5)
print("Marks * 2:", marks * 2)
print("Marks / 2:", marks / 2)

print("\nTotal Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

study_hours = np.array([2, 4, 6, 8, 10])

predicted_scores = study_hours * 10

print("\nStudy Hours:", study_hours)
print("Predicted Scores:", predicted_scores)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nMatrix:")
print(matrix)

print("\nElement at Row 2, Column 3:", matrix[1, 2])
print("First Row:", matrix[0])
print("Second Column:", matrix[:, 1])

print("\nSquare of Matrix:")
print(matrix ** 2)
