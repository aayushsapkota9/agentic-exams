# DBMS Exam Paper 2019 - Front Page

**POKHARA UNIVERSITY**
**Level:** Bachelor
**Semester:** Spring
**Year:** 2019
**Programme:** BE
**Full Marks:** 100
**Course:** Database Management System
**Pass Marks:** 45
**Time:** 3 hrs.

---

**1.**
a) Explain the concept of DBMS and its applications tracing the evolution. (7)
b) Construct an ER diagram for keeping records for Library Management Systems. (8)

**2.**
a) Using the following schema represent the following queries using Relational algebra: (8)
   - `PROJECT (Project_num, ProjectName, ProjectType, ProjectManager)`
   - `EMPLOYEE (Empnum, Empname)`
   - `ASSIGNED_TO (Projectnum, Empnum)`

   i) Find Employee details working on a project name starts with 'L'.
   ii) List all the employee details who are working under project manager "Rohan".
   iii) List the employees who are still not assigned with any project.
   iv) List the employees who are working in more than one project.

b) Write the SQL statements for the following queries by reference of `Hotel_details` relation: (7)

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
