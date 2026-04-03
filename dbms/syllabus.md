# Pokhara University
## Faculty of Science and Technology

| | |
| :--- | :--- |
| **Course Code** | CMP 222 |
| **Course Title** | Database Management System (3-1-3) |
| **Nature of Course** | Theory and Practical |
| **Full Marks** | 100 |
| **Pass Marks** | 45 |
| **Total Lectures** | 45 hours |
| **Level** | Bachelor |
| **Program** | BE |

---

## 1. Course Description
This course is designed to encompass the fundamental concepts of database management systems. These concepts include the aspects of database design, database languages, and database system implementation. This course presents the introductory concepts of database security, query processing and optimization, transactions and their concurrency control, and recovery policies. This course also introduces emerging new trended databases such as NoSQL and Blockchain databases. After completion of this course, students can design and implement a database system to develop a software application.

## 2. General Objectives
- To acquaint the students with the knowledge of relational database design using ER Model.
- To develop the skills in students to design normalized relational database required for a specified application.
- To acquaint the students with the knowledge of database security, query processing and optimization, files and record organizations, transaction, concurrency control, and data recovery mechanisms.
- To acquaint the students with basic concepts of NoSQL databases and Blockchain Databases.

## 3. Methods of Instruction
- Lecture, Tutorial/Discussion/Readings, Practical works, and Project works.

---

## 4. Contents in Detail

| Unit | Objectives | Topics |
| :--- | :--- | :--- |
| **Unit 1: Introduction** (4 hrs) | Familiarize with basic concepts of database systems and its architecture. | - DBMS purpose and applications<br>- Database Systems vs File Systems<br>- View of Data: Data Abstraction (Physical, logical, and view level; Data Independence)<br>- Instances and Schemas<br>- Database Languages (DDL, DML, and DCL)<br>- Database and Application Architecture: Two-tier and Three-tier |
| **Unit 2: ER and Relational Model** (8 hrs) | - Familiarize with ER Model, Relational Model, and relational algebra.<br>- Design the relational database using ER model. | - **ER Model**: Entity sets, attributes and values, Relationship sets, Mapping Cardinalities, ER Diagrams, Specialization, Generalization, and Aggregation<br>- **Key**: Super key, Candidate key, Primary key; Strong and Weak Entity Sets<br>- **Relational Model**: Reducing ER diagrams to Relational Schema, Structure of Relational Databases, Database Schema, Keys, Schema Diagrams<br>- **Relational Algebra** |
| **Unit 3: Structured Query Language** (5 hrs) | Implement and write DDL and DML queries in SQL. | - SQL DDL and DML<br>- Basic Structure of SQL Queries: Rename, String, Attribute Specification, Order by, Where-clause<br>- Set Operations, Null values, Aggregate Functions<br>- Nested Queries<br>- Join Expressions: Natural Join, Join Conditions, Outer Joins<br>- Modification of Database: Delete, Insert into, Update<br>- Views, Stored Procedures |
| **Unit 4: Relational Database Design** (6 hrs) | - Apply integrity constraints to implement database securities.<br>- Normalize the database to a defined normal form. | - **Integrity constraints**: Domain, Entity, and Referential Integrity Constraints; Assertions and Triggers<br>- Features of Good Relational Designs<br>- Functional dependencies and Armstrong’s Axioms<br>- Closure of a Set of Functional Dependencies and Attribute Sets<br>- **Normalization**: 1NF, 2NF, 3NF, and BCNF<br>- Denormalization for Performance |
| **Unit 5: Security** (3 hrs) | Understand the need for database security and the role of access control, authorization, and encryption. | - Security and integrity violations<br>- Access control<br>- Authorization<br>- Security and Views |
| **Unit 6: Query Processing & Optimization** (5 hrs) | Understand the mechanism of query processing and the need for query optimization. | - Introduction to Query Processing<br>- Equivalence of Expressions<br>- Query Cost Estimation<br>- Query Optimization<br>- Query evaluation and execution plan |
| **Unit 7: Storage Management & Indexing** (3 hrs) | Familiarize with different file organization methods. | - **File Organization**: Fixed and variable length records<br>- **Record Organization**: Heap, Sequential, and Indexed sequential file organizations<br>- B+ Tree Index Files<br>- Hash Indices |
| **Unit 8: Transactions & Concurrency Control** (4 hrs) | - Understand transactions, ACID properties, and serial schedules.<br>- Familiarize with Concurrency control. | - Transaction Concepts, Model, and State Diagram<br>- ACID properties<br>- Serializability: Conflict and View serializability<br>- SQL Standard Isolation Levels<br>- Concurrency Control: Lock-Based and Graph-Based Protocols |
| **Unit 9: Crash Recovery** (3 hrs) | Understand recovery algorithms to protect and recover data from failures. | - Failure classification<br>- **Recovery & Atomicity**: Log records, Database modification, Redo/Undo Transactions, Check Points<br>- **Recovery Algorithm**: Transaction Rollback, System Crash Recovery, Optimizing Commit Processing<br>- High Availability Using Remote Backup System |
| **Unit 10: Emerging Trends** (4 hrs) | Understand NoSQL, ODBMS, and Distributed Databases. | - **NoSQL Databases**: Characteristics, Categories, Advantages<br>- Object-Oriented Database and ORM<br>- **Distributed Databases**<br>- **Blockchain**: Distributed Ledger Technology, Cryptocurrency, Blockchain Properties |

---

## 5. Practical Works (45 hrs)
Laboratory work covers database design, use of database languages, and implementation using RDBMS (MS SQL, MySQL, or Oracle).

| S.N. | Task |
| :--- | :--- |
| 1 | Introduction to RDBMS (MS SQL/MySQL/Oracle), data types, and installation. |
| 2 | SQL DDL operations: Create database, Create tables, Delete database, Drop table, Alter, etc. |
| 3 | SQL DML operations: Insert into, Delete, Update, etc. |
| 4 | Implementing Join Expressions (Natural, Join Conditions, Outer Joins). |
| 5 | Implementing Stored Procedures. |
| 6 | Illustration and implementation of Views. |
| 7 | Implementing Integrity constraints (Domain, Entity, Referential Integrity). |
| 8 | Implementing Assertions and Triggers. |
| 9 | Implementation of Database Security and Privileges: Grant/Revoke, Commit/Rollback. |
| 10 | Connecting database with connection string using a programming language and executing queries. |

### Project Work
Students must submit a project work implementing a database system.
- Design database using ER model (presented via ER diagram).
- Reduce to relational schema.
- Apply constraints and triggers.
- Database should be in at least 3NF.
- Evaluation is based on the final project work.

---

## 6. List of Tutorials (15 hrs)
Tutorials involve discussion, problem-solving, and Q&A sessions.

### A. Discussion-based (3 hrs)
- Evolution of database systems vs traditional file systems.
- Semi-Structured and Object-Based Data Models.
- Concurrency Control: Lock-Based and Timestamp-Based Protocols (Oral Presentation).

### B. Problem Solving-based (6 hrs)
- Design a real-world database (University, College, etc.) using ER model.
- Reduce to relational schema and normalize.
- Implement constraints, security (Grant/Revoke), and develop a mini-project.

### C. Review & Q/A (6 hrs)
- Case study on NoSQL Databases.
- Case study on Blockchain Databases.
- Review of course content and exam preparation.

---

## 7. Evaluation System

### Internal Evaluation (50 Marks)
| Category | Component | Weight |
| :--- | :--- | :--- |
| **Theory** (30) | Attendance & Class Participation | 10% |
| | Assignments | 20% |
| | Presentations/Quizzes | 10% |
| | Internal Assessment | 60% |
| **Practical** (20) | Attendance & Class Participation | 10% |
| | Lab Report/Project Report | 20% |
| | Practical Exam/Project Work | 40% |
| | Viva Voce | 30% |

### External Evaluation (50 Marks)
- **Semester-End Examination**: 50 Marks (Theory)

> [!IMPORTANT]
> - Students must secure at least **45% marks** separately in internal assessment and practical evaluation.
> - **80% attendance** is mandatory to appear in the Semester-End Examination.

---

## 8. Prescribed Books and References

### Text Books
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2011). *Database System Concepts*. McGraw Hill.

### References
- Majumdar, A. K., & Bhattacharyya, P. (1996). *Database Management Systems*. McGraw-Hill.
- Elmasri, R., & Navathe, S. B. (1994). *Fundamentals of Database Systems*. Benjamin Cummings. Redwood City, CA.
- Everest, G. C. (1986). *Database Management*. McGraw-Hill, Inc.
