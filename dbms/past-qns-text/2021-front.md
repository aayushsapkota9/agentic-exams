# DBMS Exam Paper 2021 - Front Page

**POKHARA UNIVERSITY**
**Level:** Bachelor
**Semester:** Fall
**Year:** 2021
**Programme:** BE
**Full Marks:** 100
**Course:** Database Management System
**Pass Marks:** 45
**Time:** 3 hrs.

---

**1.**
a) Define Data Independence. Differentiate between Schema and Instance with the help of an example. (7)
b) Differentiate between Data model and E-R model. Draw an E-R diagram for a Library Management System including primary key, weak entity, composite attribute, derived attribute and multivalued attributes in your ER diagram. (8)

**2.**
a) Consider following relations, where the primary keys are underlined. Give an expression in the relational algebra to express each of the following queries: (8)
   - `Doctor(SSN, FirstName, LastName, Specialty, YearsOfExperience, PhoneNum)`
   - `Patient(SSN, FirstName, LastName, Address, DOB, PrimaryDoctor_SSN)`
   - `Medicine(TradeName, UnitPrice, GenericFlag)`
   - `Prescription(Id, Date, Doctor_SSN, Patient_SSN)`
   - `Prescription_Medicine(Prescription Id, TradeName, NumOfUnits)`

   i. List the trade name of generic medicine with unit price less than $50.
   ii. List the first and last name of patients whose primary doctor named 'John Smith'
   iii. List the first and last name of doctors who are not primary doctors to any patient.
   iv. List the SSN of distinct patients who have 'Aspirin' prescribed to them by doctor named 'John Smith'.

b) Write SQL statements for following: (7)
   i. Create a table named `Chef` with `chef_license` as primary key and following attributes:
      `chef_license`, `c_fname`, `c_lname`, `c_dob`, `c_gender`, `c_experience_hours`, `c_photograph`
   ii. Enter a full detailed information of a chef.
   iii. Change chef's experience hours by any value.
