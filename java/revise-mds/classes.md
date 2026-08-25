# Master Java Classes & Packages Reference — Chapter-Wise Quick Tables

> **Exam Strategy**: Organized strictly by **Package $\rightarrow$ Classes/Components $\rightarrow$ Crucial Methods & Traps**.

---

## 📑 Quick Navigation

- [Chapter 1: Basics, Exceptions & Collections](#chapter-1-basics-exceptions--collections)
- [Chapter 2: Object-Oriented Principles](#chapter-2-object-oriented-principles)
- [Chapter 3: GUI (Swing, AWT, Events, Applets & JavaFX)](#chapter-3-gui-swing-awt-events-applets--javafx)
- [Chapter 4: Distributed Networking, JavaMail, RMI & CORBA](#chapter-4-distributed-networking-javamail-rmi--corba)
- [Chapter 5: Database Programming (JDBC API)](#chapter-5-database-programming-jdbc-api)
- [Chapter 6: Web Applications (Servlets & JSP)](#chapter-6-web-applications-servlets--jsp)
- [Chapter 7: Hibernate, Spring Boot, Concurrency & Design Patterns](#chapter-7-hibernate-spring-boot-concurrency--design-patterns)

---

## Chapter 1: Basics, Exceptions & Collections

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.lang.*`** *(Auto-imported)* | `Object`, `System`, `Math`, `String`, `StringBuilder`, `StringBuffer`, `Integer`, `Double`, `Float`, `Long`, `Boolean`, `Character`<br><br>**Exceptions / Errors**:<br>`Throwable`, `Error` (`OutOfMemoryError`, `StackOverflowError`), `Exception`, `RuntimeException` (`NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`, `ClassCastException`, `NumberFormatException`, `IllegalArgumentException`), `ClassNotFoundException`, `InterruptedException` | `Integer.parseInt(str)` $\rightarrow$ `int`<br>`Double.parseDouble(str)` $\rightarrow$ `double`<br>`Math.max(a, b)`, `Math.min()`, `Math.PI`<br>`System.out.println()`, `System.err.println()`<br>`e.getMessage()`, `e.printStackTrace()`<br>`throw new CustomException("error msg");`<br>`float f = 3.14f;` *(f required!)*<br>`long l = 9999999999L;` *(L required!)* |
| **`java.util.*`** | **Input**: `Scanner`<br>**Lists**: `List` *(I)*, `ArrayList`, `LinkedList`, `Vector`, `Stack`<br>**Sets**: `Set` *(I)*, `HashSet`, `TreeSet` *(Sorted)*, `LinkedHashSet`<br>**Queues**: `Queue` *(I)*, `Deque` *(I)*, `PriorityQueue`<br>**Maps**: `Map` *(I)*, `HashMap`, `TreeMap` *(Sorted by Key)*, `LinkedHashMap`, `Map.Entry` *(I)*<br>**Utilities**: `Arrays`, `Collections`, `Properties` | `scanner.nextLine()`, `scanner.nextInt()`, `scanner.hasNextLine()`<br>`list.add(e)`, `list.get(index)`, `list.remove(index)`, `list.size()`<br>`deque.addFirst(e)`, `deque.addLast(e)`, `deque.removeFirst()`<br>`set.add(e)`, `set.contains(e)` *(rejects duplicates silently)*<br>`map.put(key, value)`, `map.get(key)`, `map.containsKey(k)`<br>`for (Map.Entry<K,V> e : map.entrySet()) { e.getKey(); e.getValue(); }`<br>`Arrays.equals(arr1, arr2)`, `Arrays.asList(arr)`<br>`Collections.sort(list)` |
| **`java.io.*`** | `IOException`, `FileNotFoundException`, `EOFException`, `BufferedReader`, `InputStreamReader`, `PrintWriter`, `FileReader`, `FileWriter`, `File`, `Serializable` *(Marker Interface)* | `new BufferedReader(new InputStreamReader(is))` $\rightarrow$ `reader.readLine()`<br>`new PrintWriter(os, true)` $\rightarrow$ `out.println()`<br>`file.exists()`, `file.length()`, `file.createNewFile()` |

---

## Chapter 2: Object-Oriented Principles

| Package / Keyword | Classes, Keywords & Modifiers | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.lang.*`** | `Object`, `Comparable<T>` *(I)*, `Cloneable` *(I)* | `toString()`, `equals(Object o)`, `hashCode()`, `getClass()`<br>`int compareTo(T o)` *(Natural ordering)*<br>`clone()` *(Protected copy)* |
| **`java.util.*`** | `Comparator<T>` *(I)* | `int compare(T o1, T o2)` *(Custom sort strategy)* |
| **`Keywords & OOP Modifiers`** | `extends`, `implements`, `super`, `this`, `final`, `abstract`, `@Override`, `default`, `static`, `instanceof` | `super(args);` *(MUST be on Line 1 of subclass constructor)*<br>`super.methodName()` *(Calls parent overridden method)*<br>`super.fieldName` *(Accesses shadowed parent variable)*<br>`final class X` *(Cannot be subclassed)*, `final void m()` *(Cannot be overridden)*<br>`abstract class X` *(Cannot use new)*, `abstract void m();` *(No body)*<br>`default void log(String s) {}` *(Concrete method in interface, Java 8+)*<br>`if (animal instanceof Dog d)` *(Pattern matching downcast check)*<br>⚠️ *Interface methods implemented in a class MUST be explicitly declared `public`!* |

---

## Chapter 3: GUI (Swing, AWT, Events, Applets & JavaFX)

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`javax.swing.*`** | **Windows & Containers**: `JFrame`, `JPanel`, `JDialog`<br>**Popups**: `JOptionPane`<br>**Buttons & Groups**: `JButton`, `JCheckBox`, `JRadioButton`, `ButtonGroup`<br>**Text**: `JLabel`, `JTextField`, `JPasswordField`, `JTextArea`<br>**Menus & Lists**: `JMenuBar`, `JMenu`, `JMenuItem`, `JComboBox<T>` | `frame.getContentPane().setBackground(Color.RED);` *(10-mark exam trap!)*<br>`frame.setSize(w, h)`, `frame.setVisible(true)`, `frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)`<br>`frame.setJMenuBar(menuBar)`<br>`JOptionPane.showMessageDialog(frame, "msg")`<br>`String val = JOptionPane.showInputDialog(frame, "Prompt")`<br>`int choice = JOptionPane.showConfirmDialog(frame, "Sure?")` *(0=Yes, 1=No, 2=Cancel)*<br>`JDialog d = new JDialog(frame, "Title", true);` $\rightarrow$ `d.dispose();`<br>`ButtonGroup bg = new ButtonGroup(); bg.add(male); bg.add(female);`<br>`radio.isSelected()`, `checkBox.isSelected()`<br>`tf.getText()`, `tf.setText("text")` |
| **`java.awt.*`** | **Layouts**: `BorderLayout`, `FlowLayout`, `GridLayout`, `GridBagLayout`, `GridBagConstraints`, `CardLayout`<br>**Styling & 2D**: `Color`, `Font`, `Graphics`, `Dimension` | `new BorderLayout()`, `frame.add(comp, BorderLayout.NORTH)`<br>`new GridLayout(rows, cols, hgap, vgap)`<br>`new FlowLayout()`<br>`g.setColor(Color.RED)`<br>`g.drawString("text", x, y)`<br>`g.fillRect(x, y, w, h)`, `g.fillOval(x, y, w, h)`<br>`g.fillArc(x, y, w, h, startAngle, arcAngle)` *(Pie chart slice)* |
| **`java.awt.event.*`** | **Action**: `ActionEvent`, `ActionListener` *(SAM)*<br>**Mouse**: `MouseEvent`, `MouseListener` $\rightarrow$ `MouseAdapter`, `MouseMotionListener` $\rightarrow$ `MouseMotionAdapter`<br>**Key**: `KeyEvent`, `KeyListener` $\rightarrow$ `KeyAdapter`<br>**Window**: `WindowEvent`, `WindowListener` $\rightarrow$ `WindowAdapter` | `btn.addActionListener(e -> { ... })`<br>`if (e.getSource() == redBtn) { ... }` or `switch(e.getActionCommand())`<br>`canvas.addMouseListener(new MouseAdapter() { public void mouseEntered(MouseEvent e) {} })`<br>`e.getX()`, `e.getY()`, `e.getXOnScreen()`, `e.getYOnScreen()`<br>`tf.addKeyListener(new KeyAdapter() { public void keyPressed(KeyEvent e) { if (e.getKeyCode() == KeyEvent.VK_ENTER) {} } })`<br>`frame.setFocusable(true);` *(Required for keyboard events!)* |
| **`java.applet.*`** | `Applet` | Lifecycle: `public void init()`, `start()`, `paint(Graphics g)`, `stop()`, `destroy()`<br>`<applet code="MyApplet.class" width="300" height="300"></applet>` |
| **`javafx.application.*` & `javafx.stage.*`** | `Application`, `Stage` | `public class App extends Application`<br>`@Override public void start(Stage stage) { stage.setScene(scene); stage.show(); }`<br>`public static void main(String[] args) { launch(args); }` |
| **`javafx.scene.*` & `javafx.scene.layout.*`** | `Scene`, `Node`, `Parent`<br>**Panes**: `VBox`, `HBox`, `BorderPane`, `GridPane`, `StackPane`, `FlowPane` | `new Scene(rootPane, width, height)`<br>`vbox.getChildren().addAll(node1, node2)`<br>`borderPane.setTop(header)`, `borderPane.setCenter(content)`<br>`grid.add(node, col, row)`<br>`pane.setStyle("-fx-background-color: #333; -fx-padding: 10px;")` |
| **`javafx.scene.control.*` & `javafx.scene.input.*`** | `Button`, `Label`, `TextField`, `PasswordField`, `CheckBox`, `RadioButton`, `ToggleGroup`, `ComboBox<T>`, `MouseEvent`, `KeyEvent`, `KeyCode` | `btn.setOnAction(e -> { ... })`<br>`radio.setToggleGroup(toggleGroup)`<br>`combo.getItems().addAll("A", "B")`, `combo.getValue()`<br>`node.setOnMouseMoved(e -> { e.getX(); })`<br>`tf.setOnKeyPressed(e -> { if (e.getCode() == KeyCode.ENTER) {} })` |

---

## Chapter 4: Distributed Networking, JavaMail, RMI & CORBA

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.net.*`** | **TCP**: `ServerSocket`, `Socket`<br>**UDP**: `DatagramSocket`, `DatagramPacket`<br>**Addressing**: `InetAddress`<br>**URLs**: `URI`, `URL`, `URLConnection`, `HttpURLConnection` | **TCP Server**: `ServerSocket server = new ServerSocket(port); Socket client = server.accept();`<br>**TCP Client**: `Socket s = new Socket("localhost", port);`<br>**Streams**: `s.getInputStream()`, `s.getOutputStream()`<br>**UDP Server**: `DatagramSocket sock = new DatagramSocket(port);`<br>**UDP Client**: `DatagramSocket sock = new DatagramSocket();`<br>**UDP Receive Packet**: `new DatagramPacket(buf, buf.length);` *(2 args)*<br>**UDP Send Packet**: `new DatagramPacket(buf, buf.length, inetAddr, port);` *(4 args)*<br>`socket.send(packet)`, `socket.receive(packet)`<br>`new String(packet.getData(), 0, packet.getLength())`<br>`packet.getAddress()`, `packet.getPort()`<br>`InetAddress.getByName("localhost")`<br>`URI uri = new URI("https://..."); URL url = uri.toURL();`<br>`URLConnection conn = url.openConnection(); conn.getContentType(); conn.getInputStream()` |
| **`jakarta.mail.*`** / **`javax.mail.*`** | `Session`, `Authenticator`, `PasswordAuthentication`, `Message` *(A)*, `Transport`, `MessagingException` | `Session session = Session.getInstance(props, new Authenticator() { protected PasswordAuthentication getPasswordAuthentication() { return new PasswordAuthentication(user, pass); } });`<br>`Transport.send(message);` *(Throws MessagingException)* |
| **`jakarta.mail.internet.*`** | `MimeMessage`, `InternetAddress` | `Message msg = new MimeMessage(session);`<br>`msg.setFrom(new InternetAddress("sender@gmail.com"));`<br>`msg.setRecipients(Message.RecipientType.TO, InternetAddress.parse("to@gmail.com"));`<br>`msg.setSubject("Subject line");`<br>`msg.setText("Body text");` |
| **`java.rmi.*`** | `Remote` *(Marker Interface)*, `RemoteException` *(Checked Exc)* | `public interface ComputeService extends Remote { int add(int a, int b) throws RemoteException; }` |
| **`java.rmi.server.*`** | `UnicastRemoteObject` | `public class ComputeServiceImpl extends UnicastRemoteObject implements ComputeService { public ComputeServiceImpl() throws RemoteException { super(); } }` |
| **`java.rmi.registry.*`** | `LocateRegistry`, `Registry` *(I)* | `Registry reg = LocateRegistry.createRegistry(1099); reg.rebind("Calc", serviceObj);`<br>`Registry reg = LocateRegistry.getRegistry("localhost", 1099); ComputeService comp = (ComputeService) reg.lookup("Calc");` |
| **`org.omg.CORBA.*` & `org.omg.PortableServer.*`** | `ORB`, `POA`, `POAHelper`, `Servant` $\rightarrow$ `GeneratedPOA`, `NamingContextExt`, `NamingContextExtHelper` | `ORB orb = ORB.init(args, null);`<br>`POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));`<br>`rootpoa.the_POAManager().activate();`<br>`Adder href = AdderHelper.narrow(ncRef.resolve_str("AdderService"));` |

---

## Chapter 5: Database Programming (JDBC API)

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.sql.*`** | `DriverManager`, `Connection` *(I)*, `Statement` *(I)*, `PreparedStatement` *(I)*, `CallableStatement` *(I)*, `ResultSet` *(I)*, `ResultSetMetaData` *(I)*, `Savepoint` *(I)*, `SQLException`, `Types`, `Driver` | `Connection conn = DriverManager.getConnection(url, user, pass);` *(Never new Connection!)*<br>`Statement stmt = conn.createStatement();`<br>`PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);`<br>`pstmt.setInt(1, 100); pstmt.setString(2, "Alice");` *(1-based indexing!)*<br>`CallableStatement cstmt = conn.prepareCall("{call sp_name(?, ?)}");`<br>`cstmt.registerOutParameter(2, Types.DOUBLE); cstmt.execute(); cstmt.getDouble(2);`<br>`stmt.executeQuery(sql)` $\rightarrow$ Returns `ResultSet` *(SELECT)*<br>`stmt.executeUpdate(sql)` $\rightarrow$ Returns `int` *(Rows affected for INSERT, UPDATE, DELETE)*<br>`stmt.execute(sql)` $\rightarrow$ Returns `boolean` *(true if ResultSet, false if update/DDL)*<br>`ResultSet rs = pstmt.getGeneratedKeys(); if (rs.next()) long id = rs.getLong(1);`<br>`while (rs.next()) { rs.getInt("id"); rs.getString(1); }`<br>`conn.setAutoCommit(false); conn.commit(); conn.rollback();`<br>`Savepoint sp = conn.setSavepoint("sp1"); conn.rollback(sp);`<br>`e.getSQLState()`, `e.getErrorCode()`, `e.getNextException()` |
| **`javax.sql.rowset.*`** | `RowSet` *(I)*, `CachedRowSet` *(I)*, `RowSetProvider` | `CachedRowSet crs = RowSetProvider.newFactory().createCachedRowSet();`<br>`crs.setUrl("jdbc:mysql://localhost:3306/db"); crs.setUsername("root"); crs.setPassword("pass");`<br>`crs.setCommand("SELECT * FROM students"); crs.execute();`<br>*(Disconnected model: Loads into RAM and closes DB connection immediately; Serializable)* |

---

## Chapter 6: Web Applications (Servlets & JSP)

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`jakarta.servlet.*`** | `Servlet` *(I)*, `GenericServlet` *(A)*, `ServletRequest` *(I)*, `ServletResponse` *(I)*, `ServletConfig` *(I)*, `ServletContext` *(I)*, `RequestDispatcher` *(I)*, `ServletException` | Lifecycle: `init(ServletConfig config)`, `service(ServletRequest, ServletResponse)`, `destroy()`<br>`RequestDispatcher rd = req.getRequestDispatcher("home.jsp");`<br>`rd.forward(req, resp);` *(Server-side transfer, URL unchanged)*<br>`rd.include(req, resp);` |
| **`jakarta.servlet.http.*`** | `HttpServlet` *(A)*, `HttpServletRequest` *(I)*, `HttpServletResponse` *(I)*, `Cookie`, `HttpSession` *(I)* | `protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException`<br>`protected void doPost(HttpServletRequest req, HttpServletResponse resp)`<br>`String val = req.getParameter("txtName");` *(Returns String - parse manually!)*<br>`String[] hobbies = req.getParameterValues("chkHobby");`<br>`resp.setContentType("text/html");` *(MUST BE CALLED BEFORE getWriter!)*<br>`PrintWriter out = resp.getWriter(); out.println("<html>...</html>");`<br>`resp.sendRedirect("login.html");` *(Client-side 302 redirect, URL changes)*<br>`Cookie c = new Cookie("user", "Alex"); c.setMaxAge(24*60*60); resp.addCookie(c);`<br>`Cookie[] cookies = req.getCookies(); if (cookies != null) for (Cookie c : cookies) c.getValue();`<br>`HttpSession session = req.getSession();` *(or getSession(false))`<br>`session.setAttribute("user", userObj);`<br>`User u = (User) session.getAttribute("user");`<br>`session.invalidate();` *(Terminates session & wipes RAM)*<br>⚠️ *Web Container creates only ONE servlet instance shared across threads; do NOT store user state in class fields!* |
| **`jakarta.servlet.annotation.*`** | `@WebServlet` | `@WebServlet("/register")` *(Class-level annotation replacing web.xml)* |

---

## Chapter 7: Hibernate, Spring Boot, Concurrency & Design Patterns

| Package / Category | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`org.hibernate.*` & `org.hibernate.cfg.*`** | `Configuration`, `SessionFactory` *(I - Heavyweight, 1 per DB)*, `Session` *(I - Lightweight CRUD bridge)*, `Transaction` *(I)*, `Query<T>` *(I)* | `Configuration cfg = new Configuration().configure();`<br>`SessionFactory factory = cfg.buildSessionFactory();`<br>`Session session = factory.openSession();`<br>`Transaction tx = session.beginTransaction();`<br>`session.save(entityObj);`<br>`Student s = session.get(Student.class, 1);`<br>`session.update(s); session.delete(s);`<br>`List<Student> list = session.createQuery("FROM Student s WHERE s.gpa > :gpa", Student.class).setParameter("gpa", 3.5).list();`<br>`tx.commit(); tx.rollback(); session.close();`<br>⚠️ *HQL class & property names are case-sensitive (`Student s`, `s.gpa`)!* |
| **`javax.persistence.*` / `jakarta.persistence.*`** | `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@GenerationType`, `@Column`, `@Transient` | `@Entity`<br>`@Table(name = "students")`<br>`@Id`<br>`@GeneratedValue(strategy = GenerationType.IDENTITY)`<br>`@Column(name = "full_name", nullable = false)`<br>`@Transient` *(Ignores field from DB)* |
| **`org.springframework.boot.*` & `org.springframework.web.bind.annotation.*`** | `@SpringBootApplication`, `SpringApplication`, `@RestController`, `@Controller`, `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PathVariable`, `@RequestBody`, `@RequestParam` | `@SpringBootApplication` *(Combines @SpringBootConfiguration + @EnableAutoConfiguration + @ComponentScan)*<br>`SpringApplication.run(Application.class, args);`<br>`@RestController`<br>`@RequestMapping("/api/students")`<br>`@GetMapping("/{id}")`<br>`public Student getById(@PathVariable("id") int id) { ... }` *(Auto-serialized to JSON)* |
| **`java.lang.*` & `java.util.concurrent.*`** | `Thread` *(C)*, `Runnable` *(I - SAM)*, `Callable<V>` *(I)*, `Future<V>` *(I)*, `ExecutorService` *(I)*, `Executors`, `synchronized`, `wait()`, `notify()`, `notifyAll()` | `Thread t = new Thread(runnableTask);`<br>`t.start();` *(Spawns new OS thread; t.run() does NOT!)*<br>`t.join();` *(Waits for thread termination)*<br>`Thread.sleep(1000);` *(Pauses thread but DOES NOT release monitor lock!)*<br>`synchronized void increment() { count++; }`<br>`synchronized(lockObj) { while(!ready) { lockObj.wait(); } lockObj.notify(); }` *(wait() RELEASES monitor lock!)* |
| **`Design Patterns`** | `Singleton`, `Factory Method`, `Abstract Factory` | **Singleton**: `private static Instance instance;`, `private Constructor() {}`, `public static synchronized getInstance()`<br>**Factory**: `Notification n = NotificationFactory.create("SMS"); n.send(msg);`<br>**Abstract Factory**: `GUIFactory f = new WinFactory(); Button b = f.createButton(); Checkbox c = f.createCheckbox();` |
