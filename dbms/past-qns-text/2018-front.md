# Pokhara University - Database Management System (Fall 2018)

**Level:** Bachelor  
**Year:** 2018  
**Semester:** Fall  
**Programme:** BE  
**Full Marks:** 100  
**Pass Marks:** 45  
**Course:** Database Management System  
**Time:** 3 hrs.

---

Candidates are required to give their answers in their own words as far as practicable.  
The figures in the margin indicate full marks.  
*Attempt all the questions.*

---

1. a) Explain the difference between physical and logical data independence. List the major steps that you would take in setting up a database for a particular enterprise. (7)
   b) Suppose you are given the following requirements for a simple database for the Employee Management System: (8)
      i. An employee may work in up to two departments or may not be assigned to any department.
      ii. Each department must have one and may have up to three phone numbers.
      iii. Each department can have anywhere between 1 and 30 employees.
      iv. Each phone is used by one, and only one, department.
      v. Each phone is assigned to at least one, and may be assigned to up to 30 employees.
      vi. Each employee is assigned at least one, but no more than 5 phones.
      
      Construct a clean and concise ER diagram for the database. Clearly indicate the cardinality mappings.

2. a) Consider the following relational Schema: (8)
      - `Department (DepartmentID, DepartmentName)`
      - `Designation (DesignationID, DesignationName, Salary)`
      - `Employee (EmpID, EmpName, Gender, DesignationID, DepartmentID)`
      - `Allowance (AllowanceID, AllowanceName)`
      - `Allowance Details (DetailID, EmpID, AllowanceID, Amount)`
