# Chapter 3: Structured Query Language

### Quick Navigation
[2 OR](#2-or) | [2](#2) | [2(a)](#2a) | [2(b)](#2b) | [3(a)](#3a) | [7(b)](#7b)

---

## 2 OR

##### 2023 [?]

```markdown
2. Why is joining in SQL necessary? Explain Inner Join, Natural Join and Outer Join with suitable examples. (8)
```

---

## 2

##### 2021 (B) [?]

```markdown
2. iv. Remove all chef records whose name contains character 'r' in second position in his first name.
   v. Display the total experience hours of all chef.
   vi. Create a view from above table.
   vii. Display details of chef ordering on descending manner in last name and by first name when last name matches.
```

---

## 2(a)

##### 2024 (C) [?]

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

---

##### 2024 (B) [?]

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

---

##### 2024 (A) [?]

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

---

##### 2022 [?]

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

---

##### 2017 (B) [?]

```markdown
2. a) Define relation schema and views. Consider the following relations for a database that keeps track of student enrollment in courses and the books adopted for each course:
      - `STUDENT(SSN, Name, Major, Bdate)`
      - `COURSE(Course#, Cname, Dept)`
      - `ENROLL(SSN, Course#, Quarter, Grade)`
      - `BOOK_ADOPTION(Course#, Quarter, Book_ISBN)`
      - `TEXT(Book_ISBN, Book_Title, Publisher, Author)`
      
      Draw a relational schema diagram specifying the foreign keys for this schema. (8)
```

---

## 2(b)

##### 2025 [?]

```markdown
2. b) Explain the working mechanism of "GROUP BY" clause. Differentiate between WHERE and HAVING clause. (7)
```

---

##### 2024 (C) [?]

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

---

##### 2024 (B) [?]

```markdown
2. b) Write the SQL statements for the following queries by reference of Hotel_details relation. (7)
```

---

##### 2024 (A) [?]

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

---

##### 2023 [?]

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

---

##### 2022 [?]

```markdown
2. b) Define stored procedure. What is the advantage of the stored procedure? Explain how stored procedures are created in SQL. (7)
```

---

##### 2019 [?]

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

---

##### 2017 (B) [?]

```markdown
2. b) Explain several parts of Structured Query Language (SQL). What are the basic domain types? Describe them. (7)
```

---

##### 2017 (A) [?]

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

---

## 3(a)

##### 2025 [?]

```markdown
3. a) Let us consider the following relation: (8)
`Sailors (sid, sname, rating, age)`  
`Boats (bid, bname, color)`  
`Reserves (sid, bid, day)`

Write a SQL statements for the following:
i. Find the records of sailors who have reserved boat number 20 (bid=20).
```

---

##### 2022 [?]

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

---

##### 2019 (B) [?]

```markdown
3. a) What are store procedures? Explain equi join, natural join, left and right outer join with examples. (8)
```

---

##### 2018 (B) [?]

```markdown
3. a) Differentiate between SQL and MYSQL. Why access to database from a general purpose programming language is required? Explain. (7)
```

---

##### 2017 (B) [?]

```markdown
3. a) Describe the basic structure of SQL queries. Considering at least two relations, write SQL for illustrating different types of set operations. (8)
```

---

##### 2017 (A) [?]

```markdown
3. a) How does "GROUP BY" clause work? What is the difference between WHERE and HAVING clause? Explain each with examples. (8)
```

---

## 7(b)

##### 2024 (A) [?]

```markdown
7. b) Write short notes on: (Any two) (2x5)
Stored Procedures
```

---

##### 2021 (B) [?]

```markdown
7. b) Write short notes on: (Any two) (2 x 5 = 10)
Stored procedure
```

---

##### 2017 (B) [?]

```markdown
7. b) Write short notes on: (Any two)** (2 * 5)
QBE
```

---

