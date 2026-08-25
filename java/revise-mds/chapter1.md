# Chapter 1: Basics of Java Programming — Exam Quick Revision

> **Exam Focus**: JVM Architecture, Classpath rules, `public static void main`, Data Types & Suffixes, Access Modifiers, Exception Handling Hierarchy, Custom Exceptions, Wrapper Classes, and Collections Framework.

---

## 1. 📦 Package & Classes Quick Reference Table

| Package / Module | Classes, Interfaces & Components | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.lang.*`** *(Auto-imported)* | `Object`, `System`, `Math`, `String`, `StringBuilder`, `StringBuffer`, `Integer`, `Double`, `Float`, `Long`, `Boolean`, `Character`<br><br>**Exceptions / Errors**:<br>`Throwable`, `Error` (`OutOfMemoryError`, `StackOverflowError`), `Exception`, `RuntimeException` (`NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`, `ClassCastException`, `NumberFormatException`, `IllegalArgumentException`), `ClassNotFoundException`, `InterruptedException` | `Integer.parseInt(str)` $\rightarrow$ `int`<br>`Double.parseDouble(str)` $\rightarrow$ `double`<br>`Math.max(a, b)`, `Math.min()`, `Math.PI`<br>`System.out.println()`, `System.err.println()`<br>`e.getMessage()`, `e.printStackTrace()`<br>`throw new CustomException("error msg");`<br>`float f = 3.14f;` *(f required!)*<br>`long l = 9999999999L;` *(L required!)* |
| **`java.util.*`** | **Input**: `Scanner`<br>**Lists**: `List` *(I)*, `ArrayList`, `LinkedList`, `Vector`, `Stack`<br>**Sets**: `Set` *(I)*, `HashSet`, `TreeSet` *(Sorted)*, `LinkedHashSet`<br>**Queues**: `Queue` *(I)*, `Deque` *(I)*, `PriorityQueue`<br>**Maps**: `Map` *(I)*, `HashMap`, `TreeMap` *(Sorted by Key)*, `LinkedHashMap`, `Map.Entry` *(I)*<br>**Utilities**: `Arrays`, `Collections`, `Properties` | `scanner.nextLine()`, `scanner.nextInt()`, `scanner.hasNextLine()`<br>`list.add(e)`, `list.get(index)`, `list.remove(index)`, `list.size()`<br>`deque.addFirst(e)`, `deque.addLast(e)`, `deque.removeFirst()`<br>`set.add(e)`, `set.contains(e)` *(rejects duplicates silently)*<br>`map.put(key, value)`, `map.get(key)`, `map.containsKey(k)`<br>`for (Map.Entry<K,V> e : map.entrySet()) { e.getKey(); e.getValue(); }`<br>`Arrays.equals(arr1, arr2)`, `Arrays.asList(arr)`<br>`Collections.sort(list)` |
| **`java.io.*`** | `IOException`, `FileNotFoundException`, `EOFException`, `BufferedReader`, `InputStreamReader`, `PrintWriter`, `FileReader`, `FileWriter`, `File`, `Serializable` *(Marker Interface)* | `new BufferedReader(new InputStreamReader(is))` $\rightarrow$ `reader.readLine()`<br>`new PrintWriter(os, true)` $\rightarrow$ `out.println()`<br>`file.exists()`, `file.length()`, `file.createNewFile()` |

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
