# DBMS SQL Practice Lab

This file contains a consolidated list of all practical SQL/Relational Algebra questions with copy-pastable database setup code.

### Chapter 1: Introduction

#### 2017 (A) | Label: 2(a)

```markdown
2. a) Find the names of all employees who earn more than their managers. (4)
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2017 (A) | Label: 2(b)

```markdown
2. b) Find the names of all employees who live in the same city and on the same street as their managers. (4)
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2017 (A) | Label: 2(c)

```markdown
2. c) Find the names of all employees within the database that do not work for "NBL company". (4)
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2017 (A) | Label: 2(d)

```markdown
2. d) Find the names of all employees in the database who earn... [Continued in back page]

# Pokhara University - Database Management System (Fall 2017) (A) - Back Page

---
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2018 | Label: 2(a)

```markdown
2. a) Consider the following relational Schema: (8)
      - `Department (DepartmentID, DepartmentName)`
      - `Designation (DesignationID, DesignationName, Salary)`
      - `Employee (EmpID, EmpName, Gender, DesignationID, DepartmentID)`
      - `Allowance (AllowanceID, AllowanceName)`
      - `Allowance Details (DetailID, EmpID, AllowanceID, Amount)`
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2019 | Label: 2(i)

```markdown
2. i) Find Employee details working on a project name starts with 'L'.
   ii) List all the employee details who are working under project manager "Rohan".
   iii) List the employees who are still not assigned with any project.
   iv) List the employees who are working in more than one project.
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

### Chapter 2: ER and Relational Model

#### 2017 (A) | Label: 1(b)

```markdown
1. b) Draw an ER diagram for the following scenario.  
      A university contains many faculties. The faculties in turn are divided into several colleges. Each college offers numerous programs and each program contains many courses. Teachers can teach many different courses and even the same course numerous times. Courses can also be taught by many teachers. A student is enrolled in only one program but a program can contain many students. Students can be enrolled in many courses at the same time and the courses have many students enrolled. (8)
```

```sql
-- Student, Course, Enrolls_In Setup
CREATE TABLE IF NOT EXISTS STUDENT (Student_ID INT PRIMARY KEY, Student_name VARCHAR(50), Major VARCHAR(50));
CREATE TABLE IF NOT EXISTS COURSE (Course_ID INT PRIMARY KEY, Course_name VARCHAR(100), Credits INT);
CREATE TABLE IF NOT EXISTS ENROLLS_IN (Student_ID INT, Course_ID INT, Grade VARCHAR(2), PRIMARY KEY (Student_ID, Course_ID));
INSERT INTO STUDENT VALUES (1, 'Milan', 'CS'), (2, 'Sangeeta', 'IT'), (3, 'Binod', 'CS');
INSERT INTO COURSE VALUES (101, 'Database', 3), (102, 'Advanced Physics', 4), (103, 'Computing', 3);
INSERT INTO ENROLLS_IN VALUES (1, 101, 'A'), (2, 101, 'B'), (1, 102, 'B'), (3, 103, 'A');
```

---

#### 2017 (A) | Label: 2(a)

```markdown
2. a) Consider the following schema:
      - `employee (person_name, street, city)`
      - `works (person_name, company_name, salary)`
      - `company (company_name, city)`
      - `manages (person_name, manager_name)`
      
      Give an expression in relational algebra to express each of the following queries:
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2018 | Label: 1(b)

```markdown
1. b) Suppose you are given the following requirements for a simple database for the Employee Management System: (8)
      i. An employee may work in up to two departments or may not be assigned to any department.
      ii. Each department must have one and may have up to three phone numbers.
      iii. Each department can have anywhere between 1 and 30 employees.
      iv. Each phone is used by one, and only one, department.
      v. Each phone is assigned to at least one, and may be assigned to up to 30 employees.
      vi. Each employee is assigned at least one, but no more than 5 phones.
      
      Construct a clean and concise ER diagram for the database. Clearly indicate the cardinality mappings.
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2019 | Label: 2(a)

```markdown
2. a) Using the following schema represent the following queries using Relational algebra: (8)
   - `PROJECT (Project_num, ProjectName, ProjectType, ProjectManager)`
   - `EMPLOYEE (Empnum, Empname)`
   - `ASSIGNED_TO (Projectnum, Empnum)`
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2021 | Label: 2(a)

```markdown
2. a) Consider following relations, where the primary keys are underlined. Give an expression in the relational algebra to express each of the following queries: (8)
   - `Doctor(SSN, FirstName, LastName, Specialty, YearsOfExperience, PhoneNum)`
   - `Patient(SSN, FirstName, LastName, Address, DOB, PrimaryDoctor_SSN)`
   - `Medicine(TradeName, UnitPrice, GenericFlag)`
   - `Prescription(Id, Date, Doctor_SSN, Patient_SSN)`
   - `Prescription_Medicine(Prescription Id, TradeName, NumOfUnits)`

   i. List the trade name of generic medicine with unit price less than $50.
   ii. List the first and last name of patients whose primary doctor named 'John Smith'
   iii. List the first and last name of doctors who are not primary doctors to any patient.
   iv. List the SSN of distinct patients who have 'Aspirin' prescribed to them by doctor named 'John Smith'.
```

```sql
-- Doctors, Patients, Hospitals Setup
CREATE TABLE IF NOT EXISTS Doctors (DoctorID INT PRIMARY KEY, DoctorName VARCHAR(50), Department VARCHAR(50), Address VARCHAR(100), Salary DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS Patients (PatientID INT PRIMARY KEY, PatientName VARCHAR(50), Address VARCHAR(100), Age INT, Gender VARCHAR(10));
CREATE TABLE IF NOT EXISTS Hospitals (PatientID INT, DoctorID INT, HospitalName VARCHAR(100), Location VARCHAR(100), PRIMARY KEY (PatientID, DoctorID));
INSERT INTO Doctors VALUES (1, 'Dr. Sharma', 'Surgery', 'Kathmandu', 60000), (2, 'Dr. Bhatta', 'Cardiology', 'Pokhara', 45000);
INSERT INTO Patients VALUES (1, 'Rita', 'Pokhara', 25, 'Female'), (2, 'Mina', 'Kathmandu', 40, 'Female');
INSERT INTO Hospitals VALUES (1, 2, 'Ciwat', 'Pokhara'), (2, 1, 'Teaching', 'Kathmandu');
```

---

#### 2025 | Label: 2(a)

```markdown
2. a) Consider the relational database of Figure below, where the primary keys are underlined. Give an expression in the relational algebra to express each of the following queries: (8)
`Student (SID, Name, Department, CGPA)`  
`Course (CID, CourseName, CreditHours)`  
`Enrollment (SID, CID, Semester, Grade)`

i. Find the names of students who are enrolled in the course with CID = 'CSE101'
ii. Get the names of all students who have a CGPA greater than 3.0 and are in the 'CE' department.
iii. List all students who have enrolled in 'Database Systems' and received grade 'A'
iv. Get the names of students not enrolled in any course.
```

```sql
-- Student, Course, Enrolls_In Setup
CREATE TABLE IF NOT EXISTS STUDENT (Student_ID INT PRIMARY KEY, Student_name VARCHAR(50), Major VARCHAR(50));
CREATE TABLE IF NOT EXISTS COURSE (Course_ID INT PRIMARY KEY, Course_name VARCHAR(100), Credits INT);
CREATE TABLE IF NOT EXISTS ENROLLS_IN (Student_ID INT, Course_ID INT, Grade VARCHAR(2), PRIMARY KEY (Student_ID, Course_ID));
INSERT INTO STUDENT VALUES (1, 'Milan', 'CS'), (2, 'Sangeeta', 'IT'), (3, 'Binod', 'CS');
INSERT INTO COURSE VALUES (101, 'Database', 3), (102, 'Advanced Physics', 4), (103, 'Computing', 3);
INSERT INTO ENROLLS_IN VALUES (1, 101, 'A'), (2, 101, 'B'), (1, 102, 'B'), (3, 103, 'A');
```

---

### Chapter 3: Structured Query Language

#### 2017 (A) | Label: 2(b)

```markdown
2. b) Write the SQL statements for the following queries by reference of the `Liquors_Info` relation: (7)

**Liquors_Info relation:**

| Serial No | Liquors | Start year | Bottles | Ready year |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Gorkha | 1997 | 10 | 1998 |
| 2 | Divine Wine | 1998 | 5 | 2000 |
| 3 | Old Durbar | 1997 | 12 | 2001 |
| 4 | Khukuri Rum | 1991 | 10 | 1992 |
| 5 | Xing | 1994 | 5 | 1995 |

**Queries:**
i. Create the `Liquors_Info` relation.
ii. Insert the records in `Liquors_Info` as above.
iii. List all the records which were ready by 2000.
iv. Remove all records from database that required more than 2 years to get ready.

---
```

```sql
-- Liquors Info Setup
CREATE TABLE IF NOT EXISTS Liquors_Info (Serial_No INT PRIMARY KEY, Liquors VARCHAR(50), Start_year INT, Bottles INT, Ready_year INT);
INSERT INTO Liquors_Info VALUES (1, 'Gorkha', 1997, 10, 1998), (2, 'Divine Wine', 1998, 5, 2000), (3, 'Old Durbar', 1997, 12, 2001), (4, 'Khukuri Rum', 1991, 10, 1992), (5, 'Xing', 1994, 5, 1995);
```

---

#### 2017 (B) | Label: 2(a)

```markdown
2. a) Define relation schema and views. Consider the following relations for a database that keeps track of student enrollment in courses and the books adopted for each course:
      - `STUDENT(SSN, Name, Major, Bdate)`
      - `COURSE(Course#, Cname, Dept)`
      - `ENROLL(SSN, Course#, Quarter, Grade)`
      - `BOOK_ADOPTION(Course#, Quarter, Book_ISBN)`
      - `TEXT(Book_ISBN, Book_Title, Publisher, Author)`
      
      Draw a relational schema diagram specifying the foreign keys for this schema. (8)
```

```sql
-- Student, Course, Enrolls_In Setup
CREATE TABLE IF NOT EXISTS STUDENT (Student_ID INT PRIMARY KEY, Student_name VARCHAR(50), Major VARCHAR(50));
CREATE TABLE IF NOT EXISTS COURSE (Course_ID INT PRIMARY KEY, Course_name VARCHAR(100), Credits INT);
CREATE TABLE IF NOT EXISTS ENROLLS_IN (Student_ID INT, Course_ID INT, Grade VARCHAR(2), PRIMARY KEY (Student_ID, Course_ID));
INSERT INTO STUDENT VALUES (1, 'Milan', 'CS'), (2, 'Sangeeta', 'IT'), (3, 'Binod', 'CS');
INSERT INTO COURSE VALUES (101, 'Database', 3), (102, 'Advanced Physics', 4), (103, 'Computing', 3);
INSERT INTO ENROLLS_IN VALUES (1, 101, 'A'), (2, 101, 'B'), (1, 102, 'B'), (3, 103, 'A');
```

---

#### 2018 (B) | Label: 3(a)

```markdown
3. a) Differentiate between SQL and MYSQL. Why access to database from a general purpose programming language is required? Explain. (7)
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

#### 2019 | Label: 2(b)

```markdown
2. b) Write the SQL statements for the following queries by reference of `Hotel_details` relation: (7)

**Hotel_details relation:**

| hotel_id | hotel_name | estb_year | hotel_star | hotel_worth |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Hyatt | 2047 | Five | 15M |
| 2 | Hotel Ktm | 2043 | Three | 5M |
| 3 | Fulbari | 2058 | Five | 20M |
| 4 | Yak and Yeti | 2052 | Four | 11M |
| 5 | Hotel Chitwan | 2055 | Three | 7M |

i. Create a database named `hotel` & table relation.
ii. Create a view named `Price` which shows hotel name & its worth.
iii. Modify the data so that `Hotel Chitwan` is now four star level.
iv. Delete the records of all hotels having worth more than 9M.
```

```sql
-- Hotel Details Setup
CREATE TABLE IF NOT EXISTS Hotel_details (hotel_id INT PRIMARY KEY, hotel_name VARCHAR(100), est_year INT, hotel_star INT, hotel_worth DECIMAL(15, 2));
INSERT INTO Hotel_details VALUES (1, 'Hyatt', 2047, 5, 15000000), (2, 'Hotel Ktm', 2043, 3, 5000000), (3, 'Fulbari', 2058, 5, 20000000), (4, 'Yak and Yeti', 2052, 4, 11000000), (5, 'Hotel Chitwan', 2055, 3, 7000000);
```

---

#### 2022 | Label: 2(a)

```markdown
2. a) Suppose we have the following relation: (8)
   - `Employee(person_name, street, city)`
   - `Works(person_name, company_name, salary)`
   - `Company(company_name, city)`

   Write relational algebra expressions for the following queries:
   i. Find names of all employees who live in 'Butwal' and whose salary is less than Rs. 50,000.
   ii. Find the names of all employees who work for 'Nabil Bank Limited'.
   iii. Find the names and cities of residence of all employees who work for "Global bank".
   iv. Update the salary of all employees by 10%.
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2022 | Label: 3(a)

```markdown
3. a) Consider the relation `Actress_Details` and write the SQL statements for the following queries: (8)

| Players_id | Actress_name | Debut_year | Recent_release | Actress_fee |
|---|---|---|---|---|
| 1 | Renu | 2010 | Samay | 400000 |
| 2 | Sita | 2022 | Radha | 300000 |
| 3 | Geeta | 2001 | Mato | 600000 |
| 4 | Amita | 1990 | Man | 700000 |
| 5 | Karishma | 1989 | Prem | 100000 |
```

```sql
-- Actress Details Setup
CREATE TABLE IF NOT EXISTS Actress_Details (Player_id INT PRIMARY KEY, Actress_name VARCHAR(50), Debut_year INT, Recent_release VARCHAR(50), Actress_fee DECIMAL(15, 2));
INSERT INTO Actress_Details VALUES (1, 'Renu', 2010, 'Samay', 400000), (2, 'Sita', 2022, 'Radha', 300000), (3, 'Geeta', 2001, 'Mato', 600000), (4, 'Amita', 1990, 'Man', 700000), (5, 'Karishma', 1989, 'Prem', 100000);
```

---

#### 2023 | Label: 2(b)

```markdown
2. b) What are the views? Consider the table `tbl_emp` as follows: (8)

| Emp_id | Emp_name | Salary | Department | Date_of_joining |
|---|---|---|---|---|
| 101 | Anish | 20000 | Packing | 2070-02-01 |
| 102 | Rojina | 18000 | Cleaning | 2075-04-06 |
| 103 | Sita | 35000 | Polishing | 2078-09-12 |

Write the SQL statements for the following:
i. Create the above table by considering `Emp_id` as primary key and insert the above records.
ii. Change the Department of Anish to marketing.
iii. Increase the salary of employees whose department is Cleaning by 12%.
iv. Find the name of employees having salary greater than 16000 and who joined after 2072-11-25.
v. Add a new column `Address` to the above table.
vi. Delete the entire table.
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2023 | Label: 2 OR

```markdown
2. Why is joining in SQL necessary? Explain Inner Join, Natural Join and Outer Join with suitable examples. (8)
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

#### 2024 (A) | Label: 2(a)

```markdown
2. a) Consider the following schema:
`STUDENT(Student_ID, Student_name, Major)`  
`COURSE(Course_ID, Course_name, Credits)`  
`ENROLLS_IN(Student_ID, Course_ID, Grade)`  

Write the relational algebra expressions for the following cases:
i. Find the names of all students who are enrolled in courses with names that start with "C".
ii. Update the grades of students to 'A' whose current grade is 'B'.
iii. Find the average credits of courses each student is enrolled in.
iv. Update the name of the course "Physics" to "Advanced Physics".
```

```sql
-- Student, Course, Enrolls_In Setup
CREATE TABLE IF NOT EXISTS STUDENT (Student_ID INT PRIMARY KEY, Student_name VARCHAR(50), Major VARCHAR(50));
CREATE TABLE IF NOT EXISTS COURSE (Course_ID INT PRIMARY KEY, Course_name VARCHAR(100), Credits INT);
CREATE TABLE IF NOT EXISTS ENROLLS_IN (Student_ID INT, Course_ID INT, Grade VARCHAR(2), PRIMARY KEY (Student_ID, Course_ID));
INSERT INTO STUDENT VALUES (1, 'Milan', 'CS'), (2, 'Sangeeta', 'IT'), (3, 'Binod', 'CS');
INSERT INTO COURSE VALUES (101, 'Database', 3), (102, 'Advanced Physics', 4), (103, 'Computing', 3);
INSERT INTO ENROLLS_IN VALUES (1, 101, 'A'), (2, 101, 'B'), (1, 102, 'B'), (3, 103, 'A');
```

---

#### 2024 (A) | Label: 2(b)

```markdown
2. b) Let us consider the following relation: (8)
`Sailors (sid, sname, rating, age)`  
`Boats (bid, bname, color)`  
`Reserves (sid, bid, day)`  

Write a SQL statements for the following:
i. Find the records of sailors who have reserved boat number 75 (bid=75).



ii. Update the color of the yellow boat to green.
iii. Delete the records of sailors whose rating is less than 5.
iv. Find the name and rating of sailors who have reserved a black or blue boat.
v. Find the age of sailors who have reserved boat number 25 on day 3.
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

#### 2024 (B) | Label: 2(a)

```markdown
2. a) Consider the following schema:
`EMPLOYEE (Employee_ID, Employee_Name, Department)`  
`PROJECT (Project_ID, Project_Title, Budget)`  
`WORKS_ON (Employee_ID, Project_ID, Hours_Worked)`  

Write the relational algebra expression to:
i. Find the names of all employees who are working on a project with a project title that contains the word 'Development'.
ii. Update the budget of projects to 1,000,000 where the budget is currently less than 500,000.
iii. Find the total hours worked by each employee across all projects.
iv. Update the name of the 'HR' department to 'Human_Resources'.
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2024 (B) | Label: 2(b)

```markdown
2. b) Write the SQL statements for the following queries by reference of Hotel_details relation. (7)
```

```sql
-- Hotel Details Setup
CREATE TABLE IF NOT EXISTS Hotel_details (hotel_id INT PRIMARY KEY, hotel_name VARCHAR(100), est_year INT, hotel_star INT, hotel_worth DECIMAL(15, 2));
INSERT INTO Hotel_details VALUES (1, 'Hyatt', 2047, 5, 15000000), (2, 'Hotel Ktm', 2043, 3, 5000000), (3, 'Fulbari', 2058, 5, 20000000), (4, 'Yak and Yeti', 2052, 4, 11000000), (5, 'Hotel Chitwan', 2055, 3, 7000000);
```

---

#### 2024 (C) | Label: 2(a)

```markdown
2. a) Using the following schema represent the following queries using Relational algebra: (8)
`Doctors (DoctorID, DoctorName, Department, Address, Salary)`  
`Patients (PatientID, Patient Name, Address, Age, Gender)`  
`Hospitals (PatientID, Doctor ID, HospitalName, Location)`

i. Display name of female Patient admitted to hospital at Pokhara.
ii. Delete the record of Doctors whose salary is greater than average salary of doctors.
iii. Increase the salary of doctors by 18.5% who are not from Kathmandu.
iv. Find the average salary of Doctors for each address who have average salary more than 55K.
```

```sql
-- Doctors, Patients, Hospitals Setup
CREATE TABLE IF NOT EXISTS Doctors (DoctorID INT PRIMARY KEY, DoctorName VARCHAR(50), Department VARCHAR(50), Address VARCHAR(100), Salary DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS Patients (PatientID INT PRIMARY KEY, PatientName VARCHAR(50), Address VARCHAR(100), Age INT, Gender VARCHAR(10));
CREATE TABLE IF NOT EXISTS Hospitals (PatientID INT, DoctorID INT, HospitalName VARCHAR(100), Location VARCHAR(100), PRIMARY KEY (PatientID, DoctorID));
INSERT INTO Doctors VALUES (1, 'Dr. Sharma', 'Surgery', 'Kathmandu', 60000), (2, 'Dr. Bhatta', 'Cardiology', 'Pokhara', 45000);
INSERT INTO Patients VALUES (1, 'Rita', 'Pokhara', 25, 'Female'), (2, 'Mina', 'Kathmandu', 40, 'Female');
INSERT INTO Hospitals VALUES (1, 2, 'Ciwat', 'Pokhara'), (2, 1, 'Teaching', 'Kathmandu');
```

---

#### 2024 (C) | Label: 2(b)

```markdown
2. b) Write the SQL statements for the following queries by reference of Hotel-details relation: (7)

| hotel_id | hotel_name    | est_year | hotel_star | hotel_worth |
| :------- | :----------- | :------- | :--------- | :---------- |
| 1        | Hyatt         | 2047     | 5          | 1500000     |
| 2        | Hotel Ktm     | 2043     | 3          | 500000      |
| 3        | Fulbari       | 2058     | 5          | 2000000     |
| 4        | Yak and Yeti  | 2052     | 4          | 1100000     |
| 5        | Hotel Chitwan | 2055     | 3          | 700000      |

i. Create a database named hotel and table relation.
ii. Create a view named Price which shows hotel name and its worth.
iii. Modify the data so that Hotel Chitwan is now four star level.
iv. Delete the records of all hotels having worth more than 900000.

---

### Page 2
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

#### 2025 | Label: 3(a)

```markdown
3. a) Let us consider the following relation: (8)
`Sailors (sid, sname, rating, age)`  
`Boats (bid, bname, color)`  
`Reserves (sid, bid, day)`

Write a SQL statements for the following:
i. Find the records of sailors who have reserved boat number 20 (bid=20).
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

### Chapter 4: Relational Database Design

#### 2021 (B) | Label: 3(b)

```markdown
3. b) What is the role of Triggers? Write an SQL trigger to carry out the following action: On delete of an account, for each owner of the account, check if the owner has any remaining amount, and if she does not, delete her from the depositor relation. (7)
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

#### 2025 (B) | Label: 3(b)

```markdown
3. b) ii. Find the name and rating of sailors who have reserved a black or blue boat.
iii. Find the age of sailors who have reserved boat number 27 on day 7.
iv. Update the color of the orange boat to red.
v. Delete the records of sailors whose rating is less than 7.
Explain Domain, Entity, and Referential Integrity Constraints with suitable SQL examples. (7)
```

```sql
-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);
```

---

### Chapter 10: Emerging Trend in Databases

#### 2022 (B) | Label: 3(b)

```markdown
3. b) i. Create the table `Actress_details` relation. (7)
   ii. Delete the data of actress whose recent release is `Prem`.
   iii. Modify the database so that Renu's new release is "Win the Race" film.
   iv. Insert a new record in the above table.
Consider the following relation where `{M_ID and P_ID}` are primary keys. State in which normal form the relation is. What anomalies can occur in this relation? How can these anomalies be removed? (8)

| M_ID | M_Date | P_ID | Quantity |
|---|---|---|---|
| M11 | 16 June, 2022 | I1 | 20 |
| M11 | 26 June, 2022 | I6 | 30 |
| M22 | 3 September, 2022 | I5 | 20 |
| M22 | 13 September, 2022 | I6 | 60 |
| M22 | 23 September, 2022 | I2 | 35 |
```

```sql
-- Actress Details Setup
CREATE TABLE IF NOT EXISTS Actress_Details (Player_id INT PRIMARY KEY, Actress_name VARCHAR(50), Debut_year INT, Recent_release VARCHAR(50), Actress_fee DECIMAL(15, 2));
INSERT INTO Actress_Details VALUES (1, 'Renu', 2010, 'Samay', 400000), (2, 'Sita', 2022, 'Radha', 300000), (3, 'Geeta', 2001, 'Mato', 600000), (4, 'Amita', 1990, 'Man', 700000), (5, 'Karishma', 1989, 'Prem', 100000);
```

---

#### 2022 (B) | Label: 5(a)

```markdown
5. a) Consider the relation schema in 2(a), Write the relational algebra expression for the query "Find the names of all employees who lives in Pokhara". Construct the initial operator tree and final efficient operator tree after applying transformation rules. (8)
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

#### 2025 | Label: 1(b)

```markdown
1. b) Draw an E-R diagram for a banking enterprise that keeps the information about employee, customer, loan, account and payment. (8)
```

```sql
-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);
```

---

