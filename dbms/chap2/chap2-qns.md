# Chapter 2: ER and Relational Model

### Quick Navigation
[1 OR](#1-or) | [1(b)](#1b) | [2(a)](#2a) | [5(b)](#5b) | [7(c)](#7c)

---

## 1 OR

##### 2024 (A) [?]

```markdown
1. Draw an ER diagram of an "Exam System of Pokhara University" using extended features. Explain Primary key and Foreign key.
```

---

## 1(b)

##### 2024 (C) [?]

```markdown
1. b) Draw an E-R diagram for an online shopping system. Assume necessary entities and attributes. Also, the system should model the following: (8)
- A customer can place many orders, and each order contains many items.
- An order can be shipped to different addresses, and each shipping address can be linked to multiple orders.
- The system tracks payment status and the payment method for each order.
```

---

##### 2024 (B) [?]

```markdown
1. b) Explain the benefits of data model. Construct an ER diagram for keeping records for Library Management System. (8)
```

---

##### 2024 (A) [?]

```markdown
1. b) Draw E-R diagram for airline reservation system. The system must keep track of customers and their reservations, flights and their status, seat assignments on individual flights. Include appropriate relationship and cardinality. (8)
```

---

##### 2023 [?]

```markdown
1. b) Consider you are asked to design a database for the Exam section of your college. Draw its ER diagram assuming required entities and their attributes. (8)
```

---

##### 2022 [?]

```markdown
1. b) Why do you need E-R diagram? Draw an E-R diagram for online shop management system. Assume relevant entities and attributes for the given system. (8)
```

---

##### 2021 [?]

```markdown
1. b) Differentiate between Data model and E-R model. Draw an E-R diagram for a Library Management System including primary key, weak entity, composite attribute, derived attribute and multivalued attributes in your ER diagram. (8)
```

---

##### 2019 [?]

```markdown
1. b) Construct an ER diagram for keeping records for Library Management Systems. (8)
```

---

##### 2018 [?]

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

---

##### 2017 (B) [?]

```markdown
1. b) What do you mean by data model? What are the basic data modelling components? Briefly explain different types of data models. (7)
```

---

##### 2017 (A) [?]

```markdown
1. b) Draw an ER diagram for the following scenario.  
      A university contains many faculties. The faculties in turn are divided into several colleges. Each college offers numerous programs and each program contains many courses. Teachers can teach many different courses and even the same course numerous times. Courses can also be taught by many teachers. A student is enrolled in only one program but a program can contain many students. Students can be enrolled in many courses at the same time and the courses have many students enrolled. (8)
```

---

## 2(a)

##### 2025 [?]

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

---

##### 2023 [?]

```markdown
2. a) Convert the ER diagram that you designed in question no 1 b) into relational schema. (7)
```

---

##### 2021 [?]

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

---

##### 2019 [?]

```markdown
2. a) Using the following schema represent the following queries using Relational algebra: (8)
   - `PROJECT (Project_num, ProjectName, ProjectType, ProjectManager)`
   - `EMPLOYEE (Empnum, Empname)`
   - `ASSIGNED_TO (Projectnum, Empnum)`
```

---

##### 2017 (A) [?]

```markdown
2. a) Consider the following schema:
      - `employee (person_name, street, city)`
      - `works (person_name, company_name, salary)`
      - `company (company_name, city)`
      - `manages (person_name, manager_name)`
      
      Give an expression in relational algebra to express each of the following queries:
```

---

## 5(b)

##### 2018 (Extra) [?]

```markdown
5. b) Design an E-R diagram for keeping track of the exploits of your favourite sports team. You should store the matches played, the scores in each match, the players in each match and individual player statistics for each match. Summary statistics should be modeled as derived attributes.
```

---

## 7(c)

##### 2018 (Extra) [?]

```markdown
7. c) Write short notes on: (Any two)**
Network Data Model Vs Hierarchical Data Model

---
*(Page 3 of DBMS-2018)*
```

---

