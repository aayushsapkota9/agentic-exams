# Chapter 2: Object-Oriented Principles in Java — Exam Quick Revision

> **Exam Focus**: `extends` vs `implements`, `super()` & `this()`, Member Access Rules, Overloading vs Overriding, Virtual by default, `final` rules, `abstract` classes vs `interface`, Upcasting/Downcasting (`instanceof`), `default` & `static` methods in interfaces.

---

## 1. 📦 Package, Keywords & Modifiers Quick Reference Table

| Package / Keyword | Classes, Keywords & Modifiers | Crucial Methods, Signatures & Things You Forget |
| :--- | :--- | :--- |
| **`java.lang.*`** | `Object`, `Comparable<T>` *(I)*, `Cloneable` *(I)* | `toString()`, `equals(Object o)`, `hashCode()`, `getClass()`<br>`int compareTo(T o)` *(Natural ordering)*<br>`clone()` *(Protected copy)* |
| **`java.util.*`** | `Comparator<T>` *(I)* | `int compare(T o1, T o2)` *(Custom sort strategy)* |
| **`Keywords & OOP Modifiers`** | `extends`, `implements`, `super`, `this`, `final`, `abstract`, `@Override`, `default`, `static`, `instanceof` | `super(args);` *(MUST be on Line 1 of subclass constructor)*<br>`super.methodName()` *(Calls parent overridden method)*<br>`super.fieldName` *(Accesses shadowed parent variable)*<br>`final class X` *(Cannot be subclassed)*, `final void m()` *(Cannot be overridden)*<br>`abstract class X` *(Cannot use new)*, `abstract void m();` *(No body)*<br>`default void log(String s) {}` *(Concrete method in interface, Java 8+)*<br>`if (animal instanceof Dog d)` *(Pattern matching downcast check)*<br>⚠️ *Interface methods implemented in a class MUST be explicitly declared `public`!* |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **Implicit `super()` on Line 1**:
   - If parent has only parameterized constructor `Parent(int x)`, child MUST write `super(x);` on line 1, otherwise compiler fails seeking `Parent()`.
2. **Interface Methods MUST Be `public`**:
   - In interface: `void play();` (implicitly `public abstract`).
   - In implementing class: `void play() {}` ❌ **COMPILE ERROR** (Cannot reduce visibility to default). Must write `public void play() {}`!
3. **Interface Variables are Constants**:
   - `int AGE = 20;` inside interface is automatically **`public static final`**. You cannot have mutable instance state in an interface!
4. **All Java Methods are `virtual` by Default**:
   - The JVM decides which method to run based on the **actual object type on the heap**, NOT the reference variable type!
   - Non-virtual exceptions: `static` methods, `private` methods, and `final` methods.
5. **Downcasting Crash**:
   - `Animal a = new Animal(); Dog d = (Dog) a;` $\rightarrow$ Compiles OK, but throws **`ClassCastException` at runtime**!
   - Always protect with `instanceof`: `if (a instanceof Dog d) { d.bark(); }`.
6. **Multiple Inheritance in Java**:
   - Classes: ❌ Forbidden (resolves the *Diamond Problem*).
   - Interfaces: ✅ Allowed (`class Duck implements Flyable, Swimmable`).

---

## 3. ⚖️ Crucial Comparisons for 5-10 Mark Questions

### A. Method Overloading vs. Method Overriding

| Feature | Method Overloading | Method Overriding |
| :--- | :--- | :--- |
| **Binding Type** | **Compile-Time** (Static Polymorphism) | **Runtime** (Dynamic Method Dispatch) |
| **Location** | Within the **same class** | Across **Subclass & Superclass** |
| **Method Name** | Same | Same |
| **Parameters** | **MUST BE DIFFERENT** (type, number, order) | **MUST BE EXACTLY THE SAME** |
| **Return Type** | Can change freely | Must match (or be covariant) |
| **Private/Static**| Overloadable | **Cannot be overridden** |

### B. Abstract Class vs. Interface

| Feature | Abstract Class (`abstract class`) | Interface (`interface`) |
| :--- | :--- | :--- |
| **Inheritance** | Single (`extends ClassName`) | Multiple (`implements I1, I2`) |
| **Instance State** | ✅ Can have regular instance variables | ❌ Only `public static final` constants |
| **Constructors** | ✅ Can define constructors (called via `super()`) | ❌ No constructors allowed |
| **Methods** | Abstract, concrete, final, static | Abstract, `default` (Java 8), `static` (Java 8), private (Java 9) |
| **Design Meaning**| **IS-A** relationship (Identity & shared code) | **CAN-DO** contract (Capability) |

---

## 4. 📋 Must-Memorize Code Boilerplates

### Snippet 1: Dynamic Binding & `super` Usage
```java
class Vehicle {
    String type = "Generic Vehicle";
    int speed;

    Vehicle(int speed) {
        this.speed = speed;
    }

    void display() {
        System.out.println("Speed: " + speed);
    }
}

class Car extends Vehicle {
    String type = "Sports Car"; // Shadowed field

    Car(int speed) {
        super(speed); // Line 1: Parent constructor
    }

    @Override
    void display() {
        super.display(); // Call parent method
        System.out.println("Child Type: " + this.type);
        System.out.println("Parent Type: " + super.type);
    }
}

public class DispatchDemo {
    public static void main(String[] args) {
        Vehicle v = new Car(180); // Upcasting (Implicit)
        v.display(); // Runs Car's overridden display() at runtime!
    }
}
```

### Snippet 2: Abstract Class Hierarchy
```java
abstract class Shape {
    String color;
    Shape(String color) { this.color = color; }
    
    // Abstract method: no body
    abstract double getArea();
    
    void printColor() { System.out.println("Color: " + color); }
}

class Circle extends Shape {
    double radius;
    Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    double getArea() {
        return Math.PI * radius * radius;
    }
}
```

### Snippet 3: Multiple Interface Implementation with `default`
```java
interface Printable {
    void print(); // public abstract
}

interface Loggable {
    // Default method: concrete logic inside interface
    default void log(String msg) {
        System.out.println("[LOG]: " + msg);
    }
}

// Fulfilling multiple contracts
class Report implements Printable, Loggable {
    @Override
    public void print() { // MUST be public
        System.out.println("Printing Financial Report...");
    }
}
```

---

## 5. 🎯 30-Second Rapid Recall Quiz

- **Q: Why is `String` class declared `final` in Java?** $\rightarrow$ For security, thread safety, and immutability (cannot be altered via malicious subclassing).
- **Q: Can an abstract class have zero abstract methods?** $\rightarrow$ **YES**, but declaring it `abstract` prevents instantiation via `new`.
- **Q: What is the purpose of `@Override` annotation?** $\rightarrow$ Compile-time check verifying the method signature matches a superclass/interface method.
- **Q: How to prevent a method from being overridden?** $\rightarrow$ Mark it with `final`.
