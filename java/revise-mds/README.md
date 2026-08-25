# Java Finals — Morning Cram & Master Revision Guide

> **1.5-Hour High-Speed Strategy**: Review the **"Things You WILL Forget"** and **"Must-Memorize Code Boilerplates"** in each chapter file. Use this index as your jump table.

---

## 📚 Chapter Breakdown & Quick Jump Links

| Chapter | Core Focus & Memory Triggers | Link |
| :--- | :--- | :---: |
| **Chapter 1: Basics of Java** | JVM Architecture, Classpath, Data Types (`float 3.14f`, `long 10L`), Custom Exceptions, Collections (`ArrayList`, `LinkedList`, `TreeSet`, `TreeMap`) | [Open Chapter 1](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter1.md) |
| **Chapter 2: OOP in Java** | `super()` / `this()`, `final` (class/method/var), `abstract class` vs `interface`, Overloading vs Overriding, Upcasting vs Downcasting (`instanceof`), `default` methods | [Open Chapter 2](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter2.md) |
| **Chapter 3: GUI Programming** | Swing vs JavaFX, `frame.getContentPane().setBackground(Color.RED)`, `JOptionPane` popups vs `JDialog`, `MouseAdapter` / `KeyAdapter`, Applet `paint(Graphics g)`, JavaFX `Stage` $\rightarrow$ `Scene` $\rightarrow$ Panes | [Open Chapter 3](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter3.md) |
| **Chapter 4: Network Programming**| TCP (`ServerSocket`/`Socket`), UDP (`DatagramSocket`/`DatagramPacket`), `URL`/`URLConnection`, JavaMail (`MimeMessage`, `Session`, `Transport`), RMI 4-file setup, CORBA `ORB`/`IDL` | [Open Chapter 4](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter4.md) |
| **Chapter 5: Database (JDBC)** | 4 Driver Types, `DriverManager.getConnection()`, `PreparedStatement` (`?`, SQLi prevention), `executeQuery` vs `executeUpdate`, 1-based indexing, Transactions (`commit`/`rollback`), `CachedRowSet` | [Open Chapter 5](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter5.md) |
| **Chapter 6: Servlets & JSP** | Servlet Lifecycle (`init`, `service`, `destroy`), Thread Safety (1 instance!), `@WebServlet`, GET vs POST, Cookies (`JSESSIONID`) vs `HttpSession`, Redirect vs Forward, JSP tags | [Open Chapter 6](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter6.md) |
| **Chapter 7: Advanced Java** | ORM & Impedance Mismatch, Hibernate (`SessionFactory`, `Session`, `Transaction`, HQL), Spring Boot (`@SpringBootApplication`, REST), Multithreading (`Runnable`, `synchronized`), Singleton, Factory, Abstract Factory | [Open Chapter 7](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/chapter7.md) |
| 🌳 **Master Class Hierarchy Trees** | **All Java classes, interfaces, exceptions & adapters in ASCII Tree form** across all chapters | [Open Classes Guide](file:///Users/aayushsapkota9/repos/oxford/java/finals/revise-mds/classes.md) |

---

## 🚨 Master "DO NOT WRITE THIS IN EXAM" Cheat Sheet

| Common Exam Mistake ❌ | Correct Code / Syntax ✅ | Why? |
| :--- | :--- | :--- |
| `Connection conn = new Connection();` | `Connection conn = DriverManager.getConnection(url, u, p);` | `Connection` is an interface; `DriverManager` instantiates the driver implementation. |
| `frame.setBackground(Color.RED);` | `frame.getContentPane().setBackground(Color.RED);` | In Swing, `JFrame`'s surface is covered by its `ContentPane`. |
| `rs.getString(0);` | `rs.getString(1);` | JDBC column indices start at **1**, NOT 0! |
| `response.getWriter();` then `response.setContentType();` | `response.setContentType("text/html");` **BEFORE** `response.getWriter();` | Browser headers must be set before opening the character response stream. |
| `float x = 3.14;` | `float x = 3.14f;` | Decimal literals default to 64-bit `double` in Java. |
| `t.run();` to start a thread | `t.start();` | `run()` executes synchronously on the current thread; `start()` spawns a new OS thread. |
| Storing user data in Servlet fields | Store in `HttpSession` or local method variables | Web Container creates only **ONE** servlet instance shared across all threads! |
| `new Session(...)` for JavaMail | `Session.getInstance(props, authenticator)` | Factory method required to initialize environment properties. |
| `SELECT * FROM students` in HQL | `FROM Student s WHERE s.gpa > :minGpa` | HQL operates on Java entity classes and properties (case-sensitive). |
