# Chapter 5: Database Programming with JDBC — Exam Quick Revision

> **Exam Focus**: 4-Layer JDBC Architecture, 4 Driver Types, `DriverManager.getConnection()`, `Statement` vs. `PreparedStatement` vs. `CallableStatement`, SQL Injection Prevention, Query Execution Methods (`executeQuery`, `executeUpdate`, `execute`), Auto-Generated Keys, `ResultSet` Navigation & 1-based indexing, Transactions (`commit`, `rollback`, `Savepoint`), `CachedRowSet` Disconnected Model, and SQL Escape Syntax.

---

## 1. 📦 Package & Classes Quick Reference Table

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.sql.*`** | `DriverManager`, `Connection` *(I)*, `Statement` *(I)*, `PreparedStatement` *(I)*, `CallableStatement` *(I)*, `ResultSet` *(I)*, `ResultSetMetaData` *(I)*, `Savepoint` *(I)*, `SQLException`, `Types`, `Driver` | `Connection conn = DriverManager.getConnection(url, user, pass);` *(Never new Connection!)*<br>`Statement stmt = conn.createStatement();`<br>`PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);`<br>`pstmt.setInt(1, 100); pstmt.setString(2, "Alice");` *(1-based indexing!)*<br>`CallableStatement cstmt = conn.prepareCall("{call sp_name(?, ?)}");`<br>`cstmt.registerOutParameter(2, Types.DOUBLE); cstmt.execute(); cstmt.getDouble(2);`<br>`stmt.executeQuery(sql)` $\rightarrow$ Returns `ResultSet` *(SELECT)*<br>`stmt.executeUpdate(sql)` $\rightarrow$ Returns `int` *(Rows affected for INSERT, UPDATE, DELETE)*<br>`stmt.execute(sql)` $\rightarrow$ Returns `boolean` *(true if ResultSet, false if update/DDL)*<br>`ResultSet rs = pstmt.getGeneratedKeys(); if (rs.next()) long id = rs.getLong(1);`<br>`while (rs.next()) { rs.getInt("id"); rs.getString(1); }`<br>`conn.setAutoCommit(false); conn.commit(); conn.rollback();`<br>`Savepoint sp = conn.setSavepoint("sp1"); conn.rollback(sp);`<br>`e.getSQLState()`, `e.getErrorCode()`, `e.getNextException()` |
| **`javax.sql.rowset.*`** | `RowSet` *(I)*, `CachedRowSet` *(I)*, `RowSetProvider` | `CachedRowSet crs = RowSetProvider.newFactory().createCachedRowSet();`<br>`crs.setUrl("jdbc:mysql://localhost:3306/db"); crs.setUsername("root"); crs.setPassword("pass");`<br>`crs.setCommand("SELECT * FROM students"); crs.execute();`<br>*(Disconnected model: Loads into RAM and closes DB connection immediately; Serializable)* |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **`Connection` is an Interface**:
   - `Connection conn = new Connection();` ❌ **FATAL ERROR!**
   - ✅ **MUST USE**: `Connection conn = DriverManager.getConnection(url, user, password);`
2. **JDBC Indexing is 1-Based**:
   - Array/String in Java starts at index `0`.
   - **JDBC indices start at `1`!**
   - `pstmt.setString(1, "Alice");` (Replaces first `?`).
   - `rs.getString(1);` (Retrieves first column).
3. **Choosing the Right Execution Method**:
   - `executeQuery(sql)` $\rightarrow$ Returns **`ResultSet`** (For `SELECT` queries only).
   - `executeUpdate(sql)` $\rightarrow$ Returns **`int`** (Count of affected rows; for `INSERT`, `UPDATE`, `DELETE`).
   - `execute(sql)` $\rightarrow$ Returns **`boolean`** (`true` if `ResultSet` returned; `false` if DDL/update count).
4. **Auto-Generated Keys**:
   - Must request keys when preparing statement: `conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);`.
   - Retrieve via: `ResultSet rs = pstmt.getGeneratedKeys(); if (rs.next()) long id = rs.getLong(1);`.
5. **Transactions Require Disabling Auto-Commit**:
   - By default, `conn.getAutoCommit() == true` (every statement commits instantly!).
   - To group statements: `conn.setAutoCommit(false);` $\rightarrow$ execute statements $\rightarrow$ `conn.commit();`. On error $\rightarrow$ `conn.rollback();`.
6. **CachedRowSet is Disconnected**:
   - `ResultSet` requires an active DB connection.
   - `CachedRowSet` loads data into RAM, closes the connection immediately, and is **Serializable** (can travel over RMI / Web services).

---

## 3. ⚖️ Crucial Driver Types & Statements Comparison

### A. The 4 JDBC Driver Types

| Type | Name | Architecture / Description | Pros / Cons | Status |
| :---: | :--- | :--- | :--- | :--- |
| **Type 1** | **JDBC-ODBC Bridge** | Translates JDBC calls $\rightarrow$ ODBC calls $\rightarrow$ DB | Slow, requires native ODBC setup on client | **Dead** (Removed in Java 8) |
| **Type 2** | **Native-API Driver** | Converts JDBC calls $\rightarrow$ Native C/C++ DB client API | Faster than Type 1, but platform-dependent binaries | Legacy |
| **Type 3** | **Network Protocol Driver** | All-Java client $\rightarrow$ Middleware server $\rightarrow$ DB | Flexible, but introduces extra network tier | Specialized |
| **Type 4** | **Thin Driver (Pure Java)**| Pure Java converts JDBC $\rightarrow$ Direct DB socket protocol | **Fastest, 100% portable, no install needed** | **Industry Standard** |

### B. Statement vs. PreparedStatement vs. CallableStatement

| Feature | `Statement` | `PreparedStatement` | `CallableStatement` |
| :--- | :--- | :--- | :--- |
| **Best For** | Static DDL / Simple queries | Parameterized repeated DML/DQL | Stored Procedures / DB Functions |
| **SQL Injection** | ❌ Vulnerable (via string concatenation)| 🛡️ **100% Protected** (Parameterization)| 🛡️ Protected |
| **Performance** | Compiles SQL on every execution | **Pre-compiles & caches query plan** | Executed directly on database engine |
| **Syntax** | `conn.createStatement()` | `conn.prepareStatement(sql)` | `conn.prepareCall("{call sp(?, ?)}")` |

---

## 4. 📋 Must-Memorize Code Boilerplates

### Snippet 1: Complete CRUD with `PreparedStatement` & Auto-Generated Keys
```java
import java.sql.*;

public class JDBCCompleteDemo {
    private static final String URL = "jdbc:mysql://localhost:3306/school_db";
    private static final String USER = "root";
    private static final String PASS = "password123";

    public static void main(String[] args) {
        String insertSql = "INSERT INTO students (name, gpa) VALUES (?, ?)";
        String selectSql = "SELECT id, name, gpa FROM students WHERE gpa >= ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            // 1. INSERT (DML) with Generated Keys
            try (PreparedStatement pstmt = conn.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS)) {
                pstmt.setString(1, "Aayush");
                pstmt.setDouble(2, 3.85);
                int rows = pstmt.executeUpdate();
                System.out.println("Inserted rows: " + rows);

                try (ResultSet keys = pstmt.getGeneratedKeys()) {
                    if (keys.next()) {
                        long generatedId = keys.getLong(1);
                        System.out.println("Generated Primary Key ID: " + generatedId);
                    }
                }
            }

            // 2. SELECT (DQL) Query Processing
            try (PreparedStatement pstmt = conn.prepareStatement(selectSql)) {
                pstmt.setDouble(1, 3.5);
                try (ResultSet rs = pstmt.executeQuery()) {
                    while (rs.next()) {
                        int id = rs.getInt("id"); // or rs.getInt(1)
                        String name = rs.getString("name");
                        double gpa = rs.getDouble("gpa");
                        System.out.println("Student: " + id + " | " + name + " | " + gpa);
                    }
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### Snippet 2: Transactions & Savepoints (ACID Transfer)
```java
import java.sql.*;

public class TransactionDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/bank_db";
        Connection conn = null;

        try {
            conn = DriverManager.getConnection(url, "root", "secret");
            
            // 1. Begin Transaction (Turn off auto-commit)
            conn.setAutoCommit(false);

            try (PreparedStatement deduct = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
                 PreparedStatement add = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?")) {

                // Deduct $500 from Account 101
                deduct.setDouble(1, 500.0); deduct.setInt(2, 101);
                deduct.executeUpdate();

                // Add $500 to Account 102
                add.setDouble(1, 500.0); add.setInt(2, 102);
                add.executeUpdate();

                // 2. Commit transaction permanently
                conn.commit();
                System.out.println("Bank Transfer Committed Successfully!");
            }
        } catch (SQLException e) {
            // 3. Rollback on ANY failure
            if (conn != null) {
                try {
                    conn.rollback();
                    System.err.println("Transaction Rolled Back!");
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        } finally {
            if (conn != null) {
                try { conn.setAutoCommit(true); conn.close(); } catch (SQLException ignored) {}
            }
        }
    }
}
```

### Snippet 3: `CachedRowSet` (Disconnected Data Access)
```java
import javax.sql.rowset.CachedRowSet;
import javax.sql.rowset.RowSetProvider;
import java.sql.SQLException;

public class CachedRowSetDemo {
    public static void main(String[] args) throws SQLException {
        // 1. Factory Creation
        CachedRowSet crs = RowSetProvider.newFactory().createCachedRowSet();

        // 2. Configure connection and SQL command
        crs.setUrl("jdbc:mysql://localhost:3306/school_db");
        crs.setUsername("root");
        crs.setPassword("password123");
        crs.setCommand("SELECT id, name FROM students");

        // 3. Populate and disconnect from network
        crs.execute();

        // Connection is completely closed now! Iterate offline in RAM:
        while (crs.next()) {
            System.out.println("ID: " + crs.getInt("id") + " | Name: " + crs.getString("name"));
        }
    }
}
```

### Snippet 4: Stored Procedure & SQL Escapes
```java
// CallableStatement for Stored Procedure:
CallableStatement cstmt = conn.prepareCall("{call get_bonus(?, ?)}");
cstmt.setInt(1, 101); // IN parameter
cstmt.registerOutParameter(2, java.sql.Types.DOUBLE); // OUT parameter
cstmt.execute();
double bonus = cstmt.getDouble(2);

// SQL Escapes Examples:
// Date Literal: {d '2026-08-25'}
// Function:     SELECT {fn current_date()} FROM dual
// Outer Join:   SELECT * FROM {oj tableA LEFT OUTER JOIN tableB ON ...}
// Like Escape:  SELECT * FROM users WHERE code LIKE '%!_' {escape '!'}
```

---

## 5. 🎯 30-Second Rapid Recall Quiz

- **Q: Why does `PreparedStatement` prevent SQL Injection?** $\rightarrow$ It separates the query structure (pre-compiled template) from user input parameters, treating input strictly as literal data rather than executable SQL syntax.
- **Q: What is the initial position of a `ResultSet` cursor?** $\rightarrow$ Immediately **before the first row** (requires `rs.next()` to move to row 1).
- **Q: Default port for MySQL vs. PostgreSQL?** $\rightarrow$ MySQL: `3306` | PostgreSQL: `5432`.
- **Q: Which interface provides disconnected dataset operations?** $\rightarrow$ `CachedRowSet`.
