# CRUD_student_db

A Python CLI application to manage student records with validation and SQLite database.  
This project demonstrates CRUD (Create, Read, Update, Delete) operations, data validation using regex, and persistent data storage—skills that are foundational for data analytics.

---

## **Project Overview**

The Student Manager allows users to:

- **Add Students** – insert new student records with ID, Name, Grade, and Email.  
- **View Students** – retrieve all student records from the database.  
- **Update Students** – modify existing records while ensuring input validation.  
- **Delete Students** – remove student records with a confirmation step.  

### **Data Validation Features**

This project uses **regular expressions** to ensure data integrity:

- `ID` – numeric only, max 8 digits.  
- `Name` – alphabetic only, max 12 characters.  
- `Grade` – only `A`, `B`, `C`, `D`, or `F`.  
- `Email` – must contain `@` and end with `.com`.  

---

## **Relevance to Data Analytics**

This project simulates **real-world data management tasks**, which are critical in data analytics:

1. **Data Integrity** – Ensuring that the data is valid before storing it is a key step in any analytics workflow.  
2. **CRUD Operations** – Reading, writing, updating, and deleting records is analogous to interacting with datasets in Python, SQL, or data warehouses.  
3. **Database Interaction** – Using **SQLite** introduces you to SQL querying, a core skill for data analytics.  
4. **Automation & Reproducibility** – Building a programmatic interface to manage data prepares you for larger-scale analytics tasks where manual data entry is impractical.  

---

## **Technologies Used**

- **Python 3.x** – core programming language.  
- **SQLite3** – lightweight database for persistent storage.  
- **Regex** – input validation for consistent and clean data.  

---

## **Project Structure**
```
CRUD_student_db/
├── README.md
├── .gitignore
├── requirements.txt
└── src/
└── main.py
```
---

## **How to Run**

1. Clone the repository:
```bash
git clone https://github.com/mwells98/CRUD_student_db.git
```

2. Navigate to the src folder:
```bash
cd CRUD_student_db/src
```

3. Run the program:
```bash
python main.py
```

4. Follow the CLI prompts to add, view, update, or delete students

---

## **Requirements**

* Python 3.9+
* No external packages required (sqlite3 and re are standard libraries)

---
