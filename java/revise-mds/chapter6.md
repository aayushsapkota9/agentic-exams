# Chapter 6: Web Applications with Servlets and JSP — Exam Quick Revision

> **Exam Focus**: Client-Server & Web Container (Tomcat), HTTP Methods (GET vs POST), HTTP Status Codes (200, 302, 404, 405, 500), Servlet Lifecycle (`init`, `service`, `destroy`), Multi-threading & Thread Safety in Servlets, `@WebServlet`, Form Processing (`getParameter` vs `getParameterValues`), Servlet $\rightarrow$ DB (JDBC), Cookies vs `HttpSession` (`JSESSIONID` handshake), Redirect (`sendRedirect`) vs Forward (`RequestDispatcher`), JSP Tags & Implicit Objects.

---

## 1. 📦 Package & Classes Quick Reference Table

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`jakarta.servlet.*`** | `Servlet` *(I)*, `GenericServlet` *(A)*, `ServletRequest` *(I)*, `ServletResponse` *(I)*, `ServletConfig` *(I)*, `ServletContext` *(I)*, `RequestDispatcher` *(I)*, `ServletException` | Lifecycle: `init(ServletConfig config)`, `service(ServletRequest, ServletResponse)`, `destroy()`<br>`RequestDispatcher rd = req.getRequestDispatcher("home.jsp");`<br>`rd.forward(req, resp);` *(Server-side transfer, URL unchanged)*<br>`rd.include(req, resp);` |
| **`jakarta.servlet.http.*`** | `HttpServlet` *(A)*, `HttpServletRequest` *(I)*, `HttpServletResponse` *(I)*, `Cookie`, `HttpSession` *(I)* | `protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException`<br>`protected void doPost(HttpServletRequest req, HttpServletResponse resp)`<br>`String val = req.getParameter("txtName");` *(Returns String - parse manually!)*<br>`String[] hobbies = req.getParameterValues("chkHobby");`<br>`resp.setContentType("text/html");` *(MUST BE CALLED BEFORE getWriter!)*<br>`PrintWriter out = resp.getWriter(); out.println("<html>...</html>");`<br>`resp.sendRedirect("login.html");` *(Client-side 302 redirect, URL changes)*<br>`Cookie c = new Cookie("user", "Alex"); c.setMaxAge(24*60*60); resp.addCookie(c);`<br>`Cookie[] cookies = req.getCookies(); if (cookies != null) for (Cookie c : cookies) c.getValue();`<br>`HttpSession session = req.getSession();` *(or getSession(false))`<br>`session.setAttribute("user", userObj);`<br>`User u = (User) session.getAttribute("user");`<br>`session.invalidate();` *(Terminates session & wipes RAM)*<br>⚠️ *Web Container creates only ONE servlet instance shared across threads; do NOT store user state in class fields!* |
| **`jakarta.servlet.annotation.*`** | `@WebServlet` | `@WebServlet("/register")` *(Class-level annotation replacing web.xml)* |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **`response.setContentType()` MUST Come BEFORE `getWriter()`**:
   - Calling `PrintWriter out = response.getWriter();` first causes the browser to default to plain text; subsequent `setContentType("text/html")` will be **ignored**!
2. **`getParameter()` Always Returns a `String`**:
   - `int age = request.getParameter("age");` ❌ **COMPILE ERROR!**
   - ✅ **MUST PARSE**: `int age = Integer.parseInt(request.getParameter("age"));`
3. **Single Servlet Instance Multi-Threading Trap**:
   - The Web Container creates **only ONE instance** of each servlet.
   - When 500 users visit at once, 500 threads execute `service()` on that single shared instance.
   - ⚠️ **DO NOT store user-specific data in class instance variables!** (Thread safety violation / data leak between users). Keep state inside local method variables or `HttpSession`.
4. **HTTP Status 405 (Method Not Allowed)**:
   - Happens when an HTML form uses `method="POST"` but your Servlet only overrides `doGet()`.
5. **Redirect vs. Forward**:
   - **`response.sendRedirect("home.html")`**: Client-side (HTTP 302), URL changes in browser, creates a brand **NEW request** (old request data lost).
   - **`request.getRequestDispatcher("home.jsp").forward(request, response)`**: Server-side, URL stays the same, **preserves request/response attributes**.
6. **Reading Cookies Returns an Array**:
   - `request.getCookie("name")` ❌ **DOES NOT EXIST!**
   - ✅ `Cookie[] cookies = request.getCookies();` (Must loop through array and check `c.getName().equals(...)`).

---

## 3. ⚖️ Crucial Web Comparisons

### A. GET vs. POST Request Methods

| Feature | GET Request | POST Request |
| :--- | :--- | :--- |
| **Data Payload** | Attached to URL Query String (`?user=alex&id=5`) | Encapsulated inside HTTP Request Body |
| **Data Visibility** | **Public** (Visible in URL, browser history, logs)| **Hidden** (Not stored in history/logs) |
| **Data Size Limit**| Limited (~2048 characters URL limit) | **Unlimited** (Ideal for file uploads / forms) |
| **Idempotency** | **Yes** (Safe to refresh/bookmark repeatedly) | **No** (Refreshing prompts "Resubmit form?") |
| **Servlet Handler**| `doGet(request, response)` | `doPost(request, response)` |

### B. Cookies vs. Sessions (State Management)

| Feature | Cookies (`Cookie`) | Sessions (`HttpSession`) |
| :--- | :--- | :--- |
| **Storage Location**| **Client-Side** (Browser disk/memory) | **Server-Side** (Web container RAM) |
| **Capacity** | Tiny (Max 4KB per cookie) | Large (Limited only by server RAM) |
| **Data Types** | **Strings/Text only** | **Any Java Object** (`List`, `User`, `Map`) |
| **Security** | Low (User can view/tamper) | **High** (Data never leaves the server) |
| **Handshake Bridge**| Browser receives & sends `JSESSIONID` cookie automatically to look up the session locker! |

---

## 4. 🧠 The 5 Stages of a Servlet's Life Cycle

```
1. Loading & Instantiation  ──► Class loaded & default constructor called ONCE
2. Initialization           ──► init(ServletConfig) called ONCE (sets up DB pools/config)
3. Request Servicing        ──► service(req, resp) called for EVERY request (spawns thread -> calls doGet/doPost)
4. Destruction              ──► destroy() called ONCE on server shutdown / undeployment
5. Garbage Collection       ──► Memory reclaimed by JVM GC
```

---

## 5. 📋 Must-Memorize Code Boilerplates

### Snippet 1: Complete Form Handling & Redirect Servlet
```java
import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {
    // 1. GET: Render the HTML Form
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<html><body>");
        out.println("<form action='register' method='POST'>");
        out.println("Name: <input type='text' name='txtName'><br>");
        out.println("Age: <input type='text' name='txtAge'><br>");
        out.println("<input type='submit' value='Submit'>");
        out.println("</form></body></html>");
    }

    // 2. POST: Process Submitted Data
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        String name = req.getParameter("txtName");
        int age = Integer.parseInt(req.getParameter("txtAge"));

        // Store user in Session
        HttpSession session = req.getSession();
        session.setAttribute("userName", name);

        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<h2>Welcome, " + name + " (Age: " + age + ")</h2>");
        out.println("<a href='dashboard'>Go to Dashboard</a>");
    }
}
```

### Snippet 2: Database Persistence inside Servlet (JDBC + Servlet)
```java
import java.io.*;
import java.sql.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/saveStudent")
public class StudentDBServlet extends HttpServlet {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/school_db";

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        String name = req.getParameter("name");
        double gpa = Double.parseDouble(req.getParameter("gpa"));

        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String sql = "INSERT INTO students (name, gpa) VALUES (?, ?)";
            try (Connection conn = DriverManager.getConnection(DB_URL, "root", "secret");
                 PreparedStatement pstmt = conn.prepareStatement(sql)) {
                
                pstmt.setString(1, name);
                pstmt.setDouble(2, gpa);
                int rows = pstmt.executeUpdate();

                if (rows > 0) {
                    out.println("<h3>Student saved successfully in database!</h3>");
                }
            }
        } catch (Exception e) {
            out.println("<h3>Error: " + e.getMessage() + "</h3>");
        }
    }
}
```

### Snippet 3: Cookies & Session Management in Action
```java
// === SETTING COOKIE & SESSION ===
Cookie userCookie = new Cookie("userTheme", "dark");
userCookie.setMaxAge(24 * 60 * 60); // 24 hours in seconds
resp.addCookie(userCookie);

HttpSession session = req.getSession(); // get or create
session.setAttribute("authLevel", "ADMIN");

// === READING COOKIE & SESSION ===
// 1. Reading Cookies
Cookie[] cookies = req.getCookies();
if (cookies != null) {
    for (Cookie c : cookies) {
        if ("userTheme".equals(c.getName())) {
            String theme = c.getValue(); // "dark"
        }
    }
}

// 2. Reading Session
HttpSession currentSession = req.getSession(false); // false = do not create new
if (currentSession != null && currentSession.getAttribute("authLevel") != null) {
    String auth = (String) currentSession.getAttribute("authLevel");
}

// 3. Logout / Invalidate
if (currentSession != null) {
    currentSession.invalidate(); // Destroy session
}
```

### Snippet 4: JSP Core Tags Quick Syntax
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<%! int hitCount = 0; %>                  <!-- Declaration: class field/method -->
<html>
<body>
    <% hitCount++; %>                     <!-- Scriptlet: arbitrary Java code -->
    <h3>Page Hit Count: <%= hitCount %></h3>  <!-- Expression: evaluated & printed (NO semicolon!) -->
    
    <!-- 9 Implicit Objects Available Directly: -->
    <!-- request, response, out, session, application, config, pageContext, page, exception -->
    <p>Session ID: <%= session.getId() %></p>
    <p>Client IP: <%= request.getRemoteAddr() %></p>
</body>
</html>
```

---

## 6. 🎯 30-Second Rapid Recall Quiz

- **Q: Which method is called only once when a servlet is loaded?** $\rightarrow$ `init(ServletConfig config)`.
- **Q: What is the cookie name used by Tomcat to track sessions?** $\rightarrow$ `JSESSIONID`.
- **Q: What is the return type of `request.getParameterValues()`?** $\rightarrow$ `String[]`.
- **Q: Difference between `getSession()` and `getSession(false)`?** $\rightarrow$ `getSession()` creates a new session if none exists; `getSession(false)` returns `null` if no active session exists.
