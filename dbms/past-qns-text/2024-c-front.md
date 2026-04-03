# DBMS Exam Paper 2024 (c) - Front and Page 2

**POKHARA UNIVERSITY**  
**Level:** Bachelor  
**Semester:** Fall  
**Year:** 2024 (c)  
**Programme:** BE  
**Full Marks:** 100  
**Course:** Database Management System  
**Pass Marks:** 45  
**Time:** 3 hrs.

---

### Page 1

**1.**
a) Define Data Independency. Differentiate between Schema and Instance with the help of an example. (7)
b) Draw an E-R diagram for an online shopping system. Assume necessary entities and attributes. Also, the system should model the following: (8)
- A customer can place many orders, and each order contains many items.
- An order can be shipped to different addresses, and each shipping address can be linked to multiple orders.
- The system tracks payment status and the payment method for each order.

**2.**
a) Using the following schema represent the following queries using Relational algebra: (8)
`Doctors (DoctorID, DoctorName, Department, Address, Salary)`  
`Patients (PatientID, Patient Name, Address, Age, Gender)`  
`Hospitals (PatientID, Doctor ID, HospitalName, Location)`

i. Display name of female Patient admitted to hospital at Pokhara.
ii. Delete the record of Doctors whose salary is greater than average salary of doctors.
iii. Increase the salary of doctors by 18.5% who are not from Kathmandu.
iv. Find the average salary of Doctors for each address who have average salary more than 55K.

b) Write the SQL statements for the following queries by reference of Hotel-details relation: (7)

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

**3.**
a) Explain how you would normalize an e-commerce database that tracks customers, orders, and products. (7)
b) Explain Data Constraints and its types with examples. (8)

**4.**
a) What is multi-valued dependency? Illustrate the advantage of 4NF with suitable example. (8)
b) As a database administrator, discuss how Access control and Authentication can be implemented across database systems. (7)

**5.**
a) Define query optimization. What are the basic steps of query processing with the help of a diagram. (8)
b) What are different recovery scheme? Explain deferred database modification with suitable examples. (7)

**6.**
a) Construct a B+-tree for the following set of key values: (7)  
`(8, 10, 12, 14, 115, 16, 20, 24, 28, 34)`  
Assume that the tree is initially empty and values are added in ascending order. Construct B+ trees for the case where the number of pointers that will fit in one node is Four. Also show the form of the tree after deletion of '24'.
b) Explain the Two-Phase Locking (2PL) protocol and how it guarantees serializability in concurrent transactions. (8)

*Page 1 of 3 & Page 2 of 3*
