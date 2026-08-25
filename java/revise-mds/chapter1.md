# Chapter 1: Basics of Java Programming — Exam Quick Revision

> **Exam Focus**: JVM Architecture, Classpath rules, `public static void main`, Data Types & Suffixes, Access Modifiers, Exception Handling Hierarchy, Custom Exceptions, Wrapper Classes, and Collections Framework.

---

## 1. 🚨 Exact Classes, Interfaces & Imports You Must Know

| Class / Interface / Enum | Exact Package / Import | Type | Purpose / Key Use |
| :--- | :--- | :--- | :--- |
| `Scanner` | `java.util.Scanner` | Class | Console & stream input (`scanner.nextLine()`, `scanner.nextInt()`) |
| `ArrayList<E>` | `java.util.ArrayList` | Class | Resizable dynamic array ($O(1)$ random access) |
| `LinkedList<E>` | `java.util.LinkedList` | Class | Doubly-linked list (`addFirst()`, `addLast()`, `removeFirst()`) |
| `HashSet<E>` | `java.util.HashSet` | Class | Unordered unique elements ($O(1)$ lookup) |
| `TreeSet<E>` | `java.util.TreeSet` | Class | Sorted unique elements ($O(\log n)$ Red-Black Tree) |
| `HashMap<K,V>` | `java.util.HashMap` | Class | Key-Value pairs, unordered ($O(1)$ average) |
| `TreeMap<K,V>` | `java.util.TreeMap` | Class | Key-Value pairs sorted by Key ($O(\log n)$) |
| `Map.Entry<K,V>` | `java.util.Map.Entry` | Interface | Single key-value pair for iterating over maps |
| `Throwable` | `java.lang.Throwable` | Class | Root superclass of all errors and exceptions in Java |
| `Exception` | `java.lang.Exception` | Class | Superclass for checked & application exceptions |
| `RuntimeException` | `java.lang.RuntimeException` | Class | Superclass for all **Unchecked** exceptions |
| `Error` | `java.lang.Error` | Class | Fatal JVM system problems (e.g., `OutOfMemoryError`) |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **`float` and `long` Literal Suffixes**:
   - `float f = 3.14;` ❌ **COMPILE ERROR** (Decimals default to 64-bit `double`). Must write `3.14f`.
   - `long n = 9999999999;` ❌ **COMPILE ERROR** (Whole numbers default to 32-bit `int`). Must write `9999999999L`.
2. **Boolean in Conditionals**:
   - `int x = 1; if (x) { ... }` ❌ **ILLEGAL IN JAVA** (C++ allows this, Java requires strict `boolean`: `if (x != 0)`).
3. **Array Comparison**:
   - `arr1 == arr2` checks memory reference, NOT values. Use `Arrays.equals(arr1, arr2)`.
4. **Default Access Modifier (Package-Private)**:
   - In C++, omitting modifier inside a class defaults to `private`. In Java, it defaults to **`default` (package-private)**: visible to all classes in the same package!
5. **Checked vs Unchecked Exceptions**:
   - **Checked** (inherits `Exception`, NOT `RuntimeException`): `IOException`, `SQLException`, `ClassNotFoundException` $\rightarrow$ **Must be caught or declared with `throws`**.
   - **Unchecked** (inherits `RuntimeException`): `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`, `ClassCastException` $\rightarrow$ Compiler does not force handling.
6. **Classpath Separators**:
   - Windows: `;` (e.g., `java -cp ".;lib/*" Main`)
   - Mac/Linux: `:` (e.g., `java -cp ".:lib/*" Main`)

---

## 3. 🧠 Memory & Architecture Breakdown

### A. JVM Architecture (3 Core Subsystems)
1. **Class Loader Subsystem**:
   - **Loading**: Bootstrap Loader (`rt.jar` / core Java) $\rightarrow$ Platform/Extension Loader $\rightarrow$ Application/System Loader (Classpath).
   - **Linking**: *Verify* (bytecode check) $\rightarrow$ *Prepare* (allocates memory for static fields with defaults) $\rightarrow$ *Resolve* (symbolic references $\rightarrow$ direct memory pointers).
   - **Initialization**: Executes `static` blocks and static variable assignments.
2. **Runtime Data Areas (Memory)**:
   - **Method Area** (Shared): Class metadata, static variables, runtime constant pool.
   - **Heap** (Shared): All objects (`new`) and instance fields. Managed by Garbage Collector.
   - **Java Thread Stack** (Per-thread private): Stack frames, method calls, local primitive variables, object references.
   - **PC Registers** (Per-thread): Current instruction address.
   - **Native Method Stack**: C/C++ native call frames.
3. **Execution Engine**: Interpreter (line-by-line), JIT (Just-In-Time) Compiler (compiles repeated "hotspots" to native machine code), Garbage Collector (GC).
4. **JNI**: Java Native Interface (bridge to native C/C++ libraries).

### B. Access Modifiers Matrix

| Modifier | Same Class | Same Package | Subclass (Diff Package) | World (Everywhere) |
| :--- | :---: | :---: | :---: | :---: |
| `public` | ✅ | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ✅ (via inheritance) | ❌ |
| *default* (no keyword) | ✅ | ✅ | ❌ | ❌ |
| `private` | ✅ | ❌ | ❌ | ❌ |

---

## 4. 📋 Must-Memorize Code Snippets

### Snippet 1: User-Defined Custom Exception
```java
// 1. Define custom checked exception
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

// 2. Throw and Handle
public class CustomExceptionDemo {
    static void checkEligibility(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age must be at least 18 to vote!");
        }
        System.out.println("Eligible to vote.");
    }

    public static void main(String[] args) {
        try {
            checkEligibility(15);
        } catch (InvalidAgeException e) {
            System.err.println("Caught Custom Exception: " + e.getMessage());
        } finally {
            System.out.println("Validation complete.");
        }
    }
}
```

### Snippet 2: Creating and Using User-Defined Packages
```java
// File: mypack/Calculator.java
package mypack;

public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}

// File: MainApp.java (in parent folder)
import mypack.Calculator;

public class MainApp {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("Sum = " + calc.add(10, 20));
    }
}
// Compilation: javac -d . mypack/Calculator.java
// Run: java MainApp
```

### Snippet 3: Collections Quick Operations (List, Set, Map)
```java
import java.util.*;

public class CollectionQuickRevise {
    public static void main(String[] args) {
        // List (Ordered, duplicates allowed)
        List<String> list = new ArrayList<>();
        list.add("Apple"); list.add("Banana");
        String item = list.get(0); // "Apple"

        // LinkedList (Fast end operations)
        LinkedList<String> deque = new LinkedList<>();
        deque.addFirst("Head");
        deque.addLast("Tail");
        String front = deque.removeFirst();

        // Set (Unique, TreeSet is sorted)
        Set<Integer> sortedSet = new TreeSet<>();
        sortedSet.add(45); sortedSet.add(12); sortedSet.add(45); // duplicate ignored
        // sortedSet is [12, 45]

        // Map (Key-Value, TreeMap sorts by key)
        Map<String, Integer> map = new TreeMap<>();
        map.put("Charlie", 80);
        map.put("Alice", 95);
        
        // Iterating Map.Entry
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
```

---

## 5. 🎯 30-Second Rapid Recall Quiz

- **Q: What is the return type of `main` method?** $\rightarrow$ `void` (program entrypoint, exits on completion).
- **Q: Size of `char` in Java?** $\rightarrow$ `2 bytes` (16-bit Unicode UTF-16, unlike C++ 1-byte ASCII).
- **Q: Can `finally` block run if an exception is NOT caught?** $\rightarrow$ **YES**, `finally` runs before the exception propagates up.
- **Q: What does `ClassNotFoundException` mean?** $\rightarrow$ Classpath missing the directory or JAR containing that class file.
