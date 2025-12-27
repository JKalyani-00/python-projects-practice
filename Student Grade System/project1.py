# Initializing dictionary
student_grades = {}

# Individual functions (un-nested)
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks updated to {grade}")
    else:
        print(f"{name} not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]         
        print(f"{name} has been successfully deleted") 
    else:
        print(f"{name} not found!")

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            # Fixed the f-string syntax here
            print(f"{name}: {grade}")
    else:
        print("No students found")

def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice = "))
            if choice == 1:
                name= input("Enter student name= ")
                grade=int(input("Enter student grade: "))
                add_student(name,grade)

            elif choice == 2:
                name=input("Enter student name= ")
                grade=int(input("Enter student grade: "))
                update_student(name,grade)

            elif choice == 3:
                 name = input("Enter student name = ") 
                 delete_student(name)

            elif choice == 4:
                display_all_students()

            elif choice == 5:
                print("Closing...")
                break 

            else:
                print("Invalid choice!")

        except ValueError:
            print("Error: Please enter a valid number.")

# Call the function once to start
if __name__ == "__main__":
    main()