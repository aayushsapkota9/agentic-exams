# Master Java Class & Interface Hierarchy Trees — Exam Quick Reference

> **Legend**:
> - `(C)` = Concrete Class
> - `(A)` = Abstract Class
> - `(I)` = Interface
> - `(E)` = Enum
> - `(@)` = Annotation

---

## 📑 Quick Navigation

- [Chapter 1: Exceptions & Collections Hierarchy](#-chapter-1-exceptions--collections-hierarchy)
- [Chapter 2: OOP & Core Object Hierarchy](#-chapter-2-oop--core-object-hierarchy)
- [Chapter 3: GUI — AWT, Swing, Events & JavaFX Trees](#-chapter-3-gui--awt-swing-events--javafx-trees)
- [Chapter 4: Distributed Networking, JavaMail, RMI & CORBA Trees](#-chapter-4-distributed-networking-javamail-rmi--corba-trees)
- [Chapter 5: Database Programming (JDBC API) Trees](#-chapter-5-database-programming-jdbc-api-trees)
- [Chapter 6: Web Applications — Servlet API & State Trees](#-chapter-6-web-applications--servlet-api--state-trees)
- [Chapter 7: Hibernate, Spring Boot, Concurrency & Design Patterns](#-chapter-7-hibernate-spring-boot-concurrency--design-patterns)

---

## 🌳 Chapter 1: Exceptions & Collections Hierarchy

### 1.1 The Complete Exception & Error Family Tree

```
java.lang.Object
└── java.lang.Throwable (C)
    │
    ├── java.lang.Error (C) [FATAL SYSTEM ERRORS - UNCHECKED]
    │   ├── java.lang.VirtualMachineError (A)
    │   │   ├── OutOfMemoryError (C)
    │   │   └── StackOverflowError (C)
    │   └── java.lang.LinkageError (C)
    │       └── NoClassDefFoundError (C)
    │
    └── java.lang.Exception (C) [APPLICATION LEVEL EXCEPTIONS]
        │
        ├── 🛡️ CHECKED EXCEPTIONS [Must handle via try-catch or throws]
        │   ├── java.io.IOException (C)
        │   │   ├── java.io.FileNotFoundException (C)
        │   │   └── java.io.EOFException (C)
        │   ├── java.sql.SQLException (C)
        │   ├── java.lang.ClassNotFoundException (C)
        │   ├── java.lang.InterruptedException (C)
        │   ├── java.rmi.RemoteException (C)
        │   ├── jakarta.servlet.ServletException (C)
        │   └── jakarta.mail.MessagingException (C)
        │
        └── ⚠️ UNCHECKED EXCEPTIONS (Inherits RuntimeException) [Logic Bugs]
            └── java.lang.RuntimeException (C)
                ├── NullPointerException (C)
                ├── ArithmeticException (C) [/ by zero]
                ├── ArrayIndexOutOfBoundsException (C)
                ├── StringIndexOutOfBoundsException (C)
                ├── ClassCastException (C) [Invalid downcast]
                ├── IllegalArgumentException (C)
                │   └── NumberFormatException (C) [Integer.parseInt("abc")]
                └── IllegalStateException (C)
                    └── IllegalThreadStateException (C) [start() called twice]
```

---

### 1.2 Java Collections Framework (JCF) Hierarchy

```
                               java.lang.Iterable<T> (I)
                                         │
                               java.util.Collection<E> (I)
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
 java.util.List<E> (I)           java.util.Set<E> (I)           java.util.Queue<E> (I)
 [Ordered, Duplicates]          [No Duplicates, Unique]          [FIFO Processing]
         │                               │                               │
 ┌───────┴────────┐              ┌───────┴────────┐                      ├─ PriorityQueue<E> (C)
 │                │              │                │                      │
ArrayList (C) LinkedList (C)  HashSet (C)  SortedSet<E> (I)             Deque<E> (I) [Double-ended]
[O(1) Access] [O(1) Add/Del]  [O(1) Hash]         │                      │
                                           NavigableSet<E> (I)           └─ LinkedList<E> (C)
                                                  │
                                             TreeSet<E> (C)
                                             [Red-Black Tree, O(log n) Sorted]
```

```
                                java.util.Map<K,V> (I)
                           [Key-Value Store, NOT Collection]
                                         │
         ┌───────────────────────────────┴───────────────────────────────┐
         │                                                               │
java.util.HashMap<K,V> (C)                                    java.util.SortedMap<K,V> (I)
[O(1) Hash Table, Unordered]                                                     │
         │                                                    java.util.NavigableMap<K,V> (I)
LinkedHashMap<K,V> (C)                                                           │
[Maintains Insertion Order]                                           java.util.TreeMap<K,V> (C)
                                                              [Red-Black Tree, Sorted by Key, O(log n)]
```

---

## 🌳 Chapter 2: OOP & Core Object Hierarchy

```
java.lang.Object [The Root Ancestor of ALL Java Classes]
├── Methods:
│   ├── toString(): String
│   ├── equals(Object obj): boolean
│   ├── hashCode(): int
│   ├── getClass(): Class<?>
│   ├── clone(): Object (protected)
│   └── wait(), notify(), notifyAll() [Concurrency locks]
│
└── Type Casting Reference Lineage:
    Animal a = new Dog();       // ⬆️ UPCASTING: Implicit & 100% Safe (Only Animal methods visible)
    Dog d = (Dog) a;            // ⬇️ DOWNCASTING: Explicit & Risky (Throws ClassCastException)
    if (a instanceof Dog d) { } // 🛡️ PATTERN MATCHING INSTANCEOF (Safe downcast check)
```

---

## 🌳 Chapter 3: GUI — AWT, Swing, Events & JavaFX Trees

### 3.1 AWT & Swing Component Hierarchy

```
java.lang.Object
└── java.awt.Component (A) [Base AWT visual element]
    │
    └── java.awt.Container (C) [Can contain other components]
        │
        ├── java.awt.Panel (C)
        │   └── java.applet.Applet (C) ──► javax.swing.JApplet (C)
        │
        ├── java.awt.Window (C) [Top-level window, no borders/menubar]
        │   ├── java.awt.Frame (C) ──► javax.swing.JFrame (C) [Main Application Window]
        │   └── java.awt.Dialog (C) ──► javax.swing.JDialog (C) [Custom Popup Dialog]
        │
        └── javax.swing.JComponent (A) [Root for all Swing Lightweight Components]
            ├── javax.swing.JPanel (C) [Container canvas, default FlowLayout]
            ├── javax.swing.JLabel (C) [Static text / image]
            ├── javax.swing.JMenuBar (C) [Menu container attached to JFrame]
            ├── javax.swing.JComboBox<T> (C) [Dropdown selector]
            │
            ├── javax.swing.text.JTextComponent (A)
            │   ├── javax.swing.JTextField (C) [Single-line input]
            │   │   └── javax.swing.JPasswordField (C) [Masked text input]
            │   └── javax.swing.JTextArea (C) [Multi-line text area]
            │
            └── javax.swing.AbstractButton (A)
                ├── javax.swing.JButton (C) [Standard push button]
                ├── javax.swing.JMenuItem (C) [Menu option] ──► javax.swing.JMenu (C)
                └── javax.swing.JToggleButton (C)
                    ├── javax.swing.JCheckBox (C) [Independent on/off toggle]
                    └── javax.swing.JRadioButton (C) [Exclusive toggle using ButtonGroup]
```

### 3.2 Swing Event Listener & Adapter Tree

```
java.util.EventListener (I)
│
├── java.awt.event.ActionListener (I) [SAM - 1 Method: actionPerformed(ActionEvent e)]
│   └── 💡 No adapter class exists! (Use clean Lambda: e -> { ... })
│
├── java.awt.event.MouseListener (I) [5 Methods: clicked, pressed, released, entered, exited]
│   └── java.awt.event.MouseAdapter (C) [Pre-implements all 5 methods with empty bodies]
│
├── java.awt.event.MouseMotionListener (I) [2 Methods: mouseMoved, mouseDragged]
│   └── java.awt.event.MouseMotionAdapter (C) [Pre-implements both methods]
│
├── java.awt.event.KeyListener (I) [3 Methods: keyPressed, keyReleased, keyTyped]
│   └── java.awt.event.KeyAdapter (C) [Pre-implements all 3 methods]
│
└── java.awt.event.WindowListener (I) [7 Methods: windowOpened, windowClosing, ...]
    └── java.awt.event.WindowAdapter (C)
```

### 3.3 JavaFX Scene Graph Hierarchy

```
javafx.application.Application (A) [Lifecycle: init() -> start(Stage) -> stop()]
│
javafx.stage.Stage (C) [Top-level window frame]
└── javafx.scene.Scene (C) [Physical canvas container]
    └── javafx.scene.Node (A) [Base node for all visual elements]
        └── javafx.scene.Parent (A)
            │
            ├── javafx.scene.layout.Region (C)
            │   └── javafx.scene.layout.Pane (C) [Layout Containers - uses getChildren()]
            │       ├── javafx.scene.layout.VBox (C) [Vertical column]
            │       ├── javafx.scene.layout.HBox (C) [Horizontal row]
            │       ├── javafx.scene.layout.BorderPane (C) [Top, Bottom, Left, Right, Center]
            │       ├── javafx.scene.layout.GridPane (C) [Flexible grid cells: add(node, c, r)]
            │       ├── javafx.scene.layout.StackPane (C) [Z-ordered card overlay]
            │       └── javafx.scene.layout.FlowPane (C)
            │
            └── javafx.scene.control.Control (C) [UI Controls - uses setOnAction()]
                ├── Button, Label, TextField, PasswordField, TextArea
                ├── CheckBox, RadioButton (Grouped via ToggleGroup), ComboBox<T>
                └── MenuBar, Menu, MenuItem
```

---

## 🌳 Chapter 4: Distributed Networking, JavaMail, RMI & CORBA Trees

### 4.1 Networking & JavaMail Class Trees

```
java.net
├── TCP Streaming Tier:
│   ├── ServerSocket (C) [serverSocket.accept() -> Socket]
│   └── Socket (C) [socket.getInputStream(), socket.getOutputStream()]
│
├── UDP Datagram Tier:
│   ├── DatagramSocket (C) [socket.send(packet), socket.receive(packet)]
│   └── DatagramPacket (C) [Raw byte[] payload + InetAddress + Port]
│
├── Addressing Tier:
│   └── InetAddress (C) [InetAddress.getByName("localhost")]
│
└── Web Protocol Tier:
    ├── URI (C) ──► toURL()
    ├── URL (C) ──► url.openConnection()
    └── URLConnection (C) ──► HttpURLConnection (C)

jakarta.mail / javax.mail (JavaMail API)
├── Session (C) [Session.getInstance(Properties, Authenticator)]
├── Authenticator (A) ──► returns PasswordAuthentication (C)
├── Message (A) ──► jakarta.mail.internet.MimeMessage (C)
├── Address (A) ──► jakarta.mail.internet.InternetAddress (C)
└── Transport (C) [Transport.send(Message)]
```

### 4.2 RMI & CORBA Architecture Trees

```
java.rmi (Remote Method Invocation)
├── java.rmi.Remote (I) [Root Marker Interface for all RMI Services]
│   └── YourRemoteService (I) [Every method throws RemoteException]
│
├── java.rmi.server.RemoteObject (C)
│   └── java.rmi.server.RemoteServer (C)
│       └── java.rmi.server.UnicastRemoteObject (C) [Exports point-to-point stubs]
│           └── YourRemoteServiceImpl (C) [Implements YourRemoteService]
│
└── java.rmi.registry.LocateRegistry (C)
    └── Returns ──► java.rmi.registry.Registry (I) [rebind(), lookup()]

org.omg.CORBA / org.omg.PortableServer (CORBA)
├── org.omg.CORBA.ORB (C) [Central Object Request Broker Middleware]
├── org.omg.PortableServer.POA (I) [Portable Object Adapter manager]
├── org.omg.PortableServer.Servant (A)
│   └── GeneratedPOA (A) [Auto-generated by idlj compiler]
│       └── ServantImpl (C) [Native business logic]
└── org.omg.CosNaming.NamingContextExt (I) [CORBA Directory Lookup Service]
```

---

## 🌳 Chapter 5: Database Programming (JDBC API) Trees

```
java.sql (The Core JDBC Standard API)
├── DriverManager (C) [Loads drivers & creates connections via getConnection()]
│
├── Connection (I) [Physical network socket session to DB engine]
│   ├── createStatement() ──────────► Statement (I) [Static SQL]
│   ├── prepareStatement(sql) ──────► PreparedStatement (I) [Pre-compiled '?']
│   └── prepareCall(sql) ───────────► CallableStatement (I) [Stored Procedures]
│
├── ResultSet (I) [Tabular row cursor returned by executeQuery()]
│   ├── Concurrency: CONCUR_READ_ONLY (default), CONCUR_UPDATABLE
│   └── Scrollability: TYPE_FORWARD_ONLY (default), TYPE_SCROLL_INSENSITIVE, TYPE_SCROLL_SENSITIVE
│
├── Savepoint (I) [Checkpoint for partial transaction rollbacks]
└── SQLException (C) [Captures getSQLState(), getErrorCode(), getNextException()]

javax.sql.rowset (Disconnected RowSet Subsystem)
├── javax.sql.RowSet (I)
│   └── javax.sql.rowset.CachedRowSet (I) [In-Memory, Disconnected, Serializable]
└── javax.sql.rowset.RowSetProvider (C) [RowSetProvider.newFactory().createCachedRowSet()]
```

---

## 🌳 Chapter 6: Web Applications — Servlet API & State Trees

```
jakarta.servlet (The Web Framework Engine)
├── Servlet (I) [Root Interface: init(), service(), destroy()]
│   └── GenericServlet (A) [Protocol-Independent base implementation]
│       └── jakarta.servlet.http.HttpServlet (A) [HTTP Protocol Specialist]
│           └── YourCustomServlet (C) [Decorated with @WebServlet("/path")]
│
├── ServletRequest (I) ──► jakarta.servlet.http.HttpServletRequest (I)
│   ├── getParameter(name): String
│   ├── getParameterValues(name): String[]
│   ├── getSession(): HttpSession
│   └── getCookies(): Cookie[]
│
├── ServletResponse (I) ──► jakarta.servlet.http.HttpServletResponse (I)
│   ├── setContentType("text/html"): void
│   ├── getWriter(): PrintWriter
│   ├── addCookie(Cookie): void
│   └── sendRedirect(location): void
│
├── RequestDispatcher (I) [forward(req, resp), include(req, resp)]
├── ServletConfig (I) [Per-servlet init parameters]
└── ServletContext (I) [Application-wide shared context parameters]

jakarta.servlet.http (State Management)
├── Cookie (C) [Client-side 4KB text file: getName(), getValue(), setMaxAge(sec)]
└── HttpSession (I) [Server-side RAM storage: setAttribute(k, v), getAttribute(k), invalidate()]
```

---

## 🌳 Chapter 7: Hibernate, Spring Boot, Concurrency & Design Patterns

### 7.1 Hibernate Framework Core Hierarchy

```
org.hibernate
├── cfg.Configuration (C) [Reads hibernate.cfg.xml at boot time]
│   └── buildSessionFactory() ──► SessionFactory (I) [Heavyweight, Thread-Safe, 1 per DB]
│                                      │
│                                      └── openSession() ──► Session (I) [Lightweight, Non-thread-safe]
│                                                                ├── save(obj) / get(Class, id)
│                                                                ├── update(obj) / delete(obj)
│                                                                ├── createQuery(hql) -> Query<T> (I)
│                                                                └── beginTransaction() -> Transaction (I)
│
JPA Annotations (javax.persistence.* / jakarta.persistence.*)
├── @Entity [Declares class as managed persistent entity]
├── @Table(name = "...") [Maps to specific database table]
├── @Id [Designates Primary Key]
├── @GeneratedValue(strategy = GenerationType.IDENTITY) [Auto-increment strategy]
├── @Column(name = "...", nullable = false) [Custom column mapping]
└── @Transient [Ignores field from database mapping]
```

### 7.2 Spring Boot Web Architecture

```
@SpringBootApplication [Main Application Starter]
├── @SpringBootConfiguration [Designates configuration class]
├── @EnableAutoConfiguration [Enables classpath auto-wiring]
└── @ComponentScan [Scans sub-packages for managed components]

Spring MVC Web Controller Hierarchy:
@Component (Base annotation for all Spring managed beans)
└── @Controller (Presentation layer MVC controller returning view templates)
    └── @RestController (@Controller + @ResponseBody -> returns JSON directly)
        ├── @RequestMapping("/basePath")
        ├── @GetMapping, @PostMapping, @PutMapping, @DeleteMapping
        └── @PathVariable("id"), @RequestBody, @RequestParam
```

### 7.3 Concurrency & Multithreading Hierarchy

```
java.lang.Thread (C) [implements java.lang.Runnable]
├── Methods: start(), run(), sleep(long ms), join(), isAlive(), currentThread(), interrupt()
└── Thread States (java.lang.Thread.State Enum):
    NEW ──► RUNNABLE ──► TIMED_WAITING / WAITING / BLOCKED ──► TERMINATED

java.lang.Runnable (I) [SAM: void run()] ──► 💡 Preferred over extending Thread!
java.util.concurrent.Callable<V> (I) [V call() throws Exception]
java.util.concurrent.Future<V> (I) [get(), isDone(), cancel()]
java.util.concurrent.ExecutorService (I) [Thread Pool Execution Engine]

Thread Synchronization & Monitor Locks (java.lang.Object):
├── synchronized keyword [Method or code-block mutual exclusion lock]
└── Monitor Methods: wait() [Releases lock], notify(), notifyAll()
```

### 7.4 Design Patterns Structural Trees

```
1. SINGLETON PATTERN (Creational)
   AppConfig (C)
   ├── - instance: AppConfig (static private)
   ├── - AppConfig() [private constructor prevents 'new']
   └── + getInstance(): AppConfig [public static synchronized global accessor]

2. FACTORY METHOD PATTERN (Creational)
   Notification (I)
   ├── EmailNotification (C)
   └── SMSNotification (C)
   NotificationFactory (C)
   └── + createNotification(type: String): Notification

3. ABSTRACT FACTORY PATTERN (Factory of Factories)
   Abstract Products:
   ├── Button (I) ──► WinButton (C), MacButton (C)
   └── Checkbox (I) ──► WinCheckbox (C), MacCheckbox (C)
   Abstract Factory:
   └── GUIFactory (I) [createButton(), createCheckbox()]
       ├── WindowsFactory (C) ──► creates (WinButton + WinCheckbox)
       └── MacFactory (C) ─────► creates (MacButton + MacCheckbox)
```
