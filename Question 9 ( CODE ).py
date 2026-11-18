# Student Grading System

students = []

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append({"name": name, "marks": marks, "grade": grade})

print("\n--- Student Results ---")
for student in students:
    print(student["name"], "- Marks:", student["marks"], "- Grade:", student["grade"])


# output
# Enter number of students: 4 

# Student 1
# Enter student name: tejesh
# Enter marks out of 100: 98

# Student 2
# Enter student name: rakesh 
# Enter marks out of 100: 87

# Student 3
# Enter student name: agilesh
# Enter marks out of 100: 95

# Student 4
# Enter student name: surya
# Enter marks out of 100: 97

# --- Student Results ---
# tejesh - Marks: 98.0 - Grade: A+
# rakesh - Marks: 87.0 - Grade: A
# agilesh - Marks: 95.0 - Grade: A+
# surya - Marks: 97.0 - Grade: A+