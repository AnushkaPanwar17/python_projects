import json
import os
FILE_NAME = "students.json"
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
def add_student():
    students = load_students()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    student = {
        "roll": roll,
        "name": name,
        "course": course
    }
    students.append(student)
    save_students(students)
    print("Student added successfully!")
def view_students():
    students = load_students()
    if not students:
        print("No records found.")
        return
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Course: {s['course']}")
def update_student():
    students = load_students()
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["course"] = input("Enter new course: ")
            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found.")
def delete_student():
    students = load_students()
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")
def main_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main_menu()