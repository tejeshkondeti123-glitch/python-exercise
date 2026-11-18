# Student Data Manager Using Files

FILENAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student record saved.")

def view_students():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            records = file.readlines()
        if not records:
            print("No student records available.")
        else:
            print("\nRoll No | Name | Marks")
            for record in records:
                print(record.strip().replace(",", " | "))
    except FileNotFoundError:
        print("No records file found yet.")

while True:
    print("\n--- Student Data Manager ---")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting.")
        break
    else:
        print("Invalid choice.")

# output
# --- Student Data Manager ---
# 1. Add student
# 2. View students
# 3. Exit
# Enter choice: 3
# Exiting.
# PS C:\python uploads> 