# Chapter 7: Advanced Topics in Java — Exam Quick Revision

> **Exam Focus**: ORM & Object-Relational Impedance Mismatch, Hibernate 4-Layer Architecture (`Configuration`, `SessionFactory`, `Session`, `Transaction`), `hibernate.cfg.xml`, JPA Annotations, HQL, Spring Boot Basics (`@SpringBootApplication`, Starters, `@RestController`), Concurrency & Multithreading (`Thread` vs `Runnable`, `start()` vs `run()`, Thread Lifecycle, `synchronized`, `wait()`/`notify()`), Design Patterns (Singleton, Factory Method, Abstract Factory).

---

## 1. 🚨 Exact Classes, Interfaces & Annotations You Must Know

| Symbol / Class / Annotation | Exact Package / Import | Type | Purpose / Exam Trigger |
| :--- | :--- | :--- | :--- |
| `SessionFactory`, `Session` | `org.hibernate.*` | Interfaces | Heavyweight factory & lightweight CRUD bridge |
| `Transaction` | `org.hibernate.Transaction` | Interface | Atomic unit of database work (`tx.commit()`) |
| `@Entity`, `@Table`, `@Id` | `javax.persistence.*` / `jakarta.persistence.*` | Annotations | Maps class $\rightarrow$ table and primary key |
| `@GeneratedValue`, `@Column`| `javax.persistence.*` | Annotations | Auto-increment key & column customization |
| `@SpringBootApplication` | `org.springframework.boot.autoconfigure.*`| Annotation | Bundles Config + AutoConfig + ComponentScan |
| `@RestController`, `@RequestMapping`| `org.springframework.web.bind.annotation.*`| Annotations | RESTful controller & endpoint routing |
| `@GetMapping`, `@PathVariable`| `org.springframework.web.bind.annotation.*`| Annotations | GET handler & URL path parameter binding |
| `Thread`, `Runnable` | `java.lang.*` | Class / SAM | Core Java multithreading primitives |
| `synchronized`, `wait()`, `notify()`| `java.lang.Object` / Keyword | Monitor / Sync | Mutual exclusion & inter-thread communication |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **`SessionFactory` vs. `Session`**:
   - `SessionFactory`: Heavyweight, thread-safe, **created once per application/database**.
   - `Session`: Lightweight, **NOT thread-safe**, created and destroyed per request/transaction.
2. **HQL is Case-Sensitive for Java Names**:
   - `SELECT * FROM students` ❌ **INVALID HQL!**
   - ✅ **CORRECT HQL**: `FROM Student s WHERE s.gpa > :minGpa` (Java class `Student` and field `s.gpa` must match exact Java casing; SQL keywords like `FROM`, `WHERE` are case-insensitive).
3. **`@SpringBootApplication` Combines 3 Annotations**:
   - 1) `@SpringBootConfiguration`
   - 2) `@EnableAutoConfiguration`
   - 3) `@ComponentScan`
4. **`t.start()` vs `t.run()`**:
   - `t.start()`: Allocates OS native thread, registers with scheduler, and calls `run()` **asynchronously**.
   - `t.run()`: Calls `run()` synchronously like a normal method on the **current thread** (NO new thread spawned!).
   - Calling `start()` twice on the same thread throws **`IllegalThreadStateException`**!
5. **Thread Creation: Why `Runnable` is Preferred**:
   - Java does NOT support multiple class inheritance; extending `Thread` uses up your single parent class slot. `implements Runnable` keeps inheritance open and separates the task from the thread runner.
6. **Singleton Pattern 3 Mandatory Code Rules**:
   - 1) `private static ClassName instance;`
   - 2) `private ClassName() {}` (Private constructor prevents `new`)
   - 3) `public static synchronized ClassName getInstance()` (Global access point).

---

## 3. ⚖️ Crucial Comparisons & Architecture Tables

### A. JDBC vs. ORM (Hibernate)

| Feature | Raw JDBC | ORM (Hibernate) |
| :--- | :--- | :--- |
| **Data Representation** | Flat tables, rows, `ResultSet` | **Pure Java Objects** (`Student`, `Order`) |
| **Boilerplate Code** | High (Tedious manual column mapping) | **Minimal** (Framework generates SQL automatically) |
| **Portability** | Low (Vendor-specific SQL queries) | **High** (Switch dialect in config: `MySQLDialect`) |
| **Caching** | None (Manual cache required) | Built-in 1st Level (Session) & 2nd Level Cache |

### B. Factory Method vs. Abstract Factory Pattern

| Feature | Factory Method Pattern | Abstract Factory Pattern |
| :--- | :--- | :--- |
| **Intent** | Creates **one single product** instance | Creates **families of related/dependent products** |
| **Mechanism** | Relies on a single method / switch block | Relies on factory object composition & inheritance |
| **Example** | `NotificationFactory.create("SMS")` | `WindowsFactory` produces (`WinButton` + `WinCheckbox`) |

---

## 4. 🧠 The 5 Thread Lifecycle States

```
+---------+  start()  +----------+  Scheduler  +---------+  run() exits  +------------+
|   NEW   | ────────> | RUNNABLE | ──────────> | RUNNING | ────────────> | TERMINATED |
+---------+           +----------+             +---------+               +------------+
                            ^                        │
                            │   sleep/wait/lock      │
                            +────────────────────────+
                                 WAITING / BLOCKED
```

---

## 5. 📋 Must-Memorize Code Boilerplates

### Snippet 1: Hibernate Annotated Entity & CRUD Transaction
```java
// 1. Entity Definition (Student.java)
package com.college;
import javax.persistence.*;

@Entity
@Table(name = "students")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "full_name", nullable = false)
    private String name;
    private double gpa;

    public Student() {}
    public Student(String name, double gpa) { this.name = name; this.gpa = gpa; }
    // Getters and Setters...
}

// 2. CRUD Execution Block
Session session = sessionFactory.openSession();
Transaction tx = null;
try {
    tx = session.beginTransaction();

    // CREATE
    Student s = new Student("Aayush", 3.9);
    session.save(s);

    // READ & UPDATE
    Student retrieved = session.get(Student.class, s.getId());
    if (retrieved != null) {
        retrieved.setGpa(4.0);
        session.update(retrieved);
    }

    // HQL Named Parameter Query
    List<Student> toppers = session
        .createQuery("FROM Student s WHERE s.gpa >= :minGpa", Student.class)
        .setParameter("minGpa", 3.8)
        .list();

    tx.commit(); // Save permanently
} catch (Exception e) {
    if (tx != null) tx.rollback();
    e.printStackTrace();
} finally {
    session.close();
}
```

### Snippet 2: Spring Boot REST Controller
```java
package com.college.controller;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args); // Boots embedded Tomcat
    }
}

@RestController
@RequestMapping("/api/students")
class StudentController {
    // GET /api/students
    @GetMapping
    public List<String> getStudents() {
        return Arrays.asList("Aayush", "Sita", "Ramesh"); // Automatically serialized to JSON
    }

    // GET /api/students/1
    @GetMapping("/{id}")
    public String getStudentById(@PathVariable("id") int id) {
        return "Student details for ID: " + id;
    }
}
```

### Snippet 3: Multithreading Synchronization (Even-Odd / Counter)
```java
class SharedPrinter {
    private boolean isOddTurn = true;

    public synchronized void printOdd(int num) {
        while (!isOddTurn) {
            try { wait(); } catch (InterruptedException e) {}
        }
        System.out.println("Odd: " + num);
        isOddTurn = false;
        notify(); // Wake up even thread
    }

    public synchronized void printEven(int num) {
        while (isOddTurn) {
            try { wait(); } catch (InterruptedException e) {}
        }
        System.out.println("Even: " + num);
        isOddTurn = true;
        notify(); // Wake up odd thread
    }
}

public class AlternateThreadDemo {
    public static void main(String[] args) {
        SharedPrinter printer = new SharedPrinter();

        Thread oddThread = new Thread(() -> {
            for (int i = 1; i <= 5; i += 2) printer.printOdd(i);
        });

        Thread evenThread = new Thread(() -> {
            for (int i = 2; i <= 6; i += 2) printer.printEven(i);
        });

        oddThread.start();
        evenThread.start();
    }
}
```

### Snippet 4: Singleton Design Pattern (Thread-Safe Lazy Initialization)
```java
public class DatabaseConnectionPool {
    // 1. Private static instance
    private static DatabaseConnectionPool instance;

    // 2. Private constructor
    private DatabaseConnectionPool() {
        System.out.println("Initializing DB connection pool...");
    }

    // 3. Public static synchronized accessor
    public static synchronized DatabaseConnectionPool getInstance() {
        if (instance == null) {
            instance = new DatabaseConnectionPool();
        }
        return instance;
    }
}
```

### Snippet 5: Abstract Factory Pattern (Notification Suite)
```java
// 1. Abstract Products
interface SmsSender { void sendSms(String msg); }
interface EmailSender { void sendEmail(String msg); }

// 2. Concrete Product Families
class TwilioSms implements SmsSender {
    public void sendSms(String msg) { System.out.println("[PROD SMS]: " + msg); }
}
class SendGridEmail implements EmailSender {
    public void sendEmail(String msg) { System.out.println("[PROD EMAIL]: " + msg); }
}
class MockSms implements SmsSender {
    public void sendSms(String msg) { System.out.println("[DEV MOCK SMS]: " + msg); }
}
class MockEmail implements EmailSender {
    public void sendEmail(String msg) { System.out.println("[DEV MOCK EMAIL]: " + msg); }
}

// 3. Abstract Factory Interface
interface NotificationFactory {
    SmsSender createSms();
    EmailSender createEmail();
}

// 4. Concrete Factories
class ProductionFactory implements NotificationFactory {
    public SmsSender createSms() { return new TwilioSms(); }
    public EmailSender createEmail() { return new SendGridEmail(); }
}
class DevFactory implements NotificationFactory {
    public SmsSender createSms() { return new MockSms(); }
    public EmailSender createEmail() { return new MockEmail(); }
}
```

---

## 6. 🎯 30-Second Rapid Recall Quiz

- **Q: What is Object-Relational Impedance Mismatch?** $\rightarrow$ Conceptual mismatch between OOP (classes, inheritance, references) and RDBMS (tables, foreign keys, flat rows).
- **Q: Does `Thread.sleep()` release object monitor locks?** $\rightarrow$ **NO** (`sleep()` pauses execution but retains locks; `wait()` releases the lock).
- **Q: What is the default Spring bean scope?** $\rightarrow$ **Singleton**.
- **Q: Purpose of `hbm2ddl.auto=update` in Hibernate?** $\rightarrow$ Automatically creates or updates table schema based on entity mappings without dropping existing data.
