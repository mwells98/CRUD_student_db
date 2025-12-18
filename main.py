from database import ComSciAss2

def menu():
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    app = ComSciAss2()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                id = int(input("Enter student ID: "))
            except ValueError:
                print("ID must be an integer")
                continue
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            email = input("Enter email: ")
            app.add_student(id, name, grade, email)

        elif choice == "2":
            app.view_student()

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("ID must be an integer")
                continue
            new_name = input("Enter new name (leave blank to skip): ") or None
            new_grade = input("Enter new grade (leave blank to skip): ") or None
            new_email = input("Enter new email (leave blank to skip): ") or None
            app.update_student(student_id, name=new_name, grade=new_grade, email=new_email)

        elif choice == "4":
            try:
                student_id = int(input("Enter student ID to delete: "))
            except ValueError:
                print("Enter a valid student ID")
                continue
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == 'y':
                app.delete_student(student_id)
            else:
                print("Deletion canceled.")

        elif choice == "5":
            app.closeConn()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
