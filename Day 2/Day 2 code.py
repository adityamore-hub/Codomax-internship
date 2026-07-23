def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
study_hours = float(input("Enter study hours per day: "))
score = float(input("Enter your exam score: "))

bonus = 5
final_score = score + bonus

grade = calculate_grade(final_score)

print("\nStudent Details")
print("Name:", name)
print("Age:", age)
print("Study Hours:", study_hours)
print("Original Score:", score)
print("Final Score:", final_score)
print("Grade:", grade)

print("\nMultiplication Table")
for i in range(1, 11):
    print(f"{i} x {age} = {i * age}")

print("\nCountdown")
count = 5
while count > 0:
    print(count)
    count -= 1

is_pass = final_score >= 50

print("\nData Types")
print(type(name))
print(type(age))
print(type(study_hours))
print(type(final_score))
print(type(is_pass))

print("\nOperators")
print("Addition:", score + bonus)
print("Subtraction:", final_score - score)
print("Multiplication:", study_hours * 2)
print("Division:", final_score / 2)
print("Modulus:", age % 2)
print("Power:", age ** 2)
print("Floor Division:", age // 2)

if is_pass and study_hours >= 2:
    print("\nCongratulations! You passed.")
else:
    print("\nKeep practicing and study more.")
