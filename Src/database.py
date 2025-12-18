import sqlite3
from validators import valid_id, valid_name, valid_grade, valid_email

class ComSciAss2:
    def __init__(self, db_name='ComSci_113.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT,
                grade TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def add_student(self, id, name, grade, email):
        if not valid_id(id):
            print('ID must be numeric and no longer than 8 digits')
            return
        if not valid_name(name):
            print('Name must only contain letters and be no longer than 12 characters')
            return
        if not valid_grade(grade):
            print('Grade must be A, B, C, D, or F')
            return
        if not valid_email(email):
            print('Email must be valid and end with .com')
            return

        try:
            self.cursor.execute(
                "INSERT INTO students (id, name, grade, email) VALUES (?, ?, ?, ?)",
                (id, name, grade.upper(), email)
            )
            self.conn.commit()
            print("Student added successfully.")
        except sqlite3.Error as e:
            print(f'Error adding student: {e}')

    def view_student(self):
        self.cursor.execute("SELECT * FROM students")
        records = self.cursor.fetchall()
        if not records:
            print("No students found.")
            return
        for student in records:
            print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Email: {student[3]}")

    def update_student(self, student_id, name=None, grade=None, email=None):
        updated_fields = []
        updated_values = []

        if name:
            if not valid_name(name):
                print('Name must only contain letters and be no longer than 12 characters')
                return
            updated_fields.append('name = ?')
            updated_values.append(name)
        if grade:
            if not valid_grade(grade):
                print('Grade must be A, B, C, D, or F')
                return
            updated_fields.append('grade = ?')
            updated_values.append(grade.upper())
        if email:
            if not valid_email(email):
                print('Email must be valid and end with .com')
                return
            updated_fields.append('email = ?')
            updated_values.append(email)

        if not updated_fields:
            print("Nothing to update")
            return

        updated_values.append(student_id)
        query = f"UPDATE students SET {', '.join(updated_fields)} WHERE id = ?"
        self.cursor.execute(query, updated_values)
        self.conn.commit()

        if self.cursor.rowcount:
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        if self.cursor.rowcount:
            print("Student deleted.")
        else:
            print("Student not found.")

    def closeConn(self):
        self.conn.close()
