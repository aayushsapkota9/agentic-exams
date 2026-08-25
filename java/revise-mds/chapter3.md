# Chapter 3: GUI Programming (Swing, JavaFX & Applets) — Exam Quick Revision

> **Exam Focus**: Swing hierarchy, Dialogs (`JOptionPane` vs `JDialog`), Menus (`JMenuBar`, `JMenu`, `JMenuItem`), Event Handling (`ActionListener`, `MouseAdapter`, `KeyAdapter`), Layout Managers (`BorderLayout`, `GridLayout`, `FlowLayout`, `GridBagLayout`), Frame Background Color trap (`getContentPane()`), Applet Lifecycle & `paint(Graphics g)`, JavaFX Architecture (`Stage` $\rightarrow$ `Scene` $\rightarrow$ Panes $\rightarrow$ Nodes), Swing vs JavaFX Comparison.

---

## 1. 🚨 Exact Classes, Interfaces & Imports You Must Know

| Class / Interface / Adapter | Exact Package / Import | Type | Purpose / Exam Trigger |
| :--- | :--- | :--- | :--- |
| `JFrame`, `JPanel`, `JLabel`, `JButton` | `javax.swing.*` | Classes | Standard Swing window, container, text, button |
| `JTextField`, `JPasswordField`, `JTextArea` | `javax.swing.*` | Classes | Single-line, password masked, multi-line text |
| `JRadioButton`, `ButtonGroup` | `javax.swing.*` | Classes | Radio option (`genderGroup.add(male)`) |
| `JCheckBox`, `JComboBox<T>` | `javax.swing.*` | Classes | Checkbox, dropdown selection list |
| `JMenuBar`, `JMenu`, `JMenuItem` | `javax.swing.*` | Classes | Top menu system (`frame.setJMenuBar(mb)`) |
| `JOptionPane` | `javax.swing.JOptionPane` | Class | Static popups (`showMessageDialog`, `showInputDialog`, `showConfirmDialog`) |
| `JDialog` | `javax.swing.JDialog` | Class | Custom popup window (`new JDialog(frame, "Title", true)`) |
| `BorderLayout`, `FlowLayout`, `GridLayout` | `java.awt.*` | Classes | Layout managers for panels/frames |
| `Color`, `Font`, `Dimension`, `Graphics` | `java.awt.*` | Classes | AWT styling, drawing canvas, dimensions |
| `ActionEvent`, `ActionListener` | `java.awt.event.*` | Event / SAM | Button clicks, Enter key in text fields |
| `MouseEvent`, `MouseListener`, `MouseMotionListener` | `java.awt.event.*` | Event / Intf | Clicks/enters (5 methods) / moves/drags (2 methods) |
| `MouseAdapter`, `MouseMotionAdapter`, `KeyAdapter` | `java.awt.event.*` | Classes | Pre-built adapters to override single mouse/key methods |
| `KeyEvent`, `KeyListener` | `java.awt.event.*` | Event / Intf | Key typing/pressing (`e.getKeyCode() == KeyEvent.VK_ENTER`) |
| `Applet` | `java.applet.Applet` | Class | Embedded web GUI (`paint(Graphics g)`) |
| `Application`, `Stage`, `Scene` | `javafx.application.*`, `javafx.stage.*`, `javafx.scene.*` | Classes | JavaFX core window and canvas framework |
| `VBox`, `HBox`, `BorderPane`, `GridPane`, `StackPane`| `javafx.scene.layout.*` | Classes | JavaFX layout panes (use `.getChildren().addAll()`) |
| `Button`, `Label`, `TextField`, `PasswordField` | `javafx.scene.control.*` | Classes | JavaFX UI controls (use `.setOnAction(e -> )`) |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **JFrame Background Color (10-Mark Board Exam Trap)**:
   - `frame.setBackground(Color.RED);` ❌ **DOES NOT WORK VISUALLY!**
   - ✅ **MUST WRITE**: `frame.getContentPane().setBackground(Color.RED);`
2. **Radio Buttons Need a `ButtonGroup`**:
   - `JRadioButton` alone allows selecting BOTH Male and Female.
   - ✅ **MUST GROUP**: `ButtonGroup bg = new ButtonGroup(); bg.add(male); bg.add(female);`
   - *Note*: Add the `JRadioButton` to the `JPanel` visually, but add it to the `ButtonGroup` logically!
3. **`ActionListener` vs `MouseAdapter` (Why Lambda vs Adapter?)**:
   - `ActionListener` has only **1 method** (`actionPerformed`), so you can write a clean lambda: `btn.addActionListener(e -> { ... });`.
   - `MouseListener` has **5 methods** (`mouseClicked`, `mousePressed`, `mouseReleased`, `mouseEntered`, `mouseExited`). Lambdas fail! You **must use `new MouseAdapter() { public void mouseEntered(MouseEvent e) { ... } }`**.
4. **Keyboard Events Need Focus**:
   - `frame.addKeyListener(...)` will NOT fire unless you call `frame.setFocusable(true);` first!
5. **Applet `paint()` Signature**:
   - Must be: `public void paint(Graphics g)` (import `java.awt.Graphics`, NOT `Graphics2D`).
6. **JavaFX Elements are Added via `getChildren()`**:
   - Swing: `panel.add(button);`
   - JavaFX: `vbox.getChildren().add(button);` or `grid.add(node, col, row);`
7. **JavaFX Main Entry**:
   - Class must `extends Application`, override `public void start(Stage stage)`, and `main()` calls `launch(args);`.

---

## 3. ⚖️ Swing vs. JavaFX Comparison Table (High-Yield 5-10 Marks)

| Feature | Java Swing (Classic) | JavaFX (Modern Standard) |
| :--- | :--- | :--- |
| **Release Era** | 1998 (Bundled with JDK) | 2008 (Current UI toolkit) |
| **Architecture** | Monolithic (UI & Logic combined) | **MVC Architecture** (FXML view + Controller + Model) |
| **Rendering Engine**| **CPU-bound** (Software 2D rendering) | **GPU-bound** (Hardware accelerated via DirectX/OpenGL) |
| **Styling** | Rigid Pluggable Look & Feel (PLAF) | **Web standard CSS** (`-fx-background-color: red;`) |
| **Top Window** | `JFrame` (`new JFrame()`) | `Stage` (Provided in `start(Stage stage)`) |
| **Canvas Container**| `JPanel` + `setLayout(mgr)` | `Scene` + Layout Panes (`VBox`, `HBox`, `GridPane`) |
| **Naming Prefix** | Prefixed with **J** (`JButton`, `JLabel`) | Semantic names (`Button`, `Label`, `TextField`) |

---

## 4. 📋 Must-Memorize Code Boilerplates

### Snippet 1: Complete Swing Form with Menu, Dialog & Color Change
```java
import javax.swing.*;
import java.awt.*;

public class SwingCompleteDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Swing Exam Demo");
        frame.setSize(400, 350);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // 1. Menu Bar
        JMenuBar mb = new JMenuBar();
        JMenu menu = new JMenu("Options");
        JMenuItem itemFeedback = new JMenuItem("Feedback");
        menu.add(itemFeedback);
        mb.add(menu);
        frame.setJMenuBar(mb);

        // 2. Center Panel with GridLayout
        JPanel panel = new JPanel(new GridLayout(3, 2, 5, 5));
        JTextField num1 = new JTextField();
        JTextField num2 = new JTextField();
        JButton btnAdd = new JButton("Add & Red");
        JLabel lblResult = new JLabel("Result: ");

        panel.add(new JLabel("Number 1:")); panel.add(num1);
        panel.add(new JLabel("Number 2:")); panel.add(num2);
        panel.add(btnAdd);                  panel.add(lblResult);

        // 3. Event Handling: Calculation + Background Color + Dialogs
        btnAdd.addActionListener(e -> {
            int a = Integer.parseInt(num1.getText());
            int b = Integer.parseInt(num2.getText());
            lblResult.setText("Result: " + (a + b));
            
            // Frame ContentPane Color Change (Crucial!)
            frame.getContentPane().setBackground(Color.RED);
            JOptionPane.showMessageDialog(frame, "Calculated: " + (a + b));
        });

        // 4. Custom JDialog on Menu Click
        itemFeedback.addActionListener(e -> {
            JDialog dialog = new JDialog(frame, "Feedback Form", true); // modal = true
            dialog.setLayout(new FlowLayout());
            dialog.setSize(250, 150);
            dialog.add(new JTextField(15));
            JButton btnClose = new JButton("Close");
            btnClose.addActionListener(ev -> dialog.dispose());
            dialog.add(btnClose);
            dialog.setVisible(true);
        });

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);
    }
}
```

### Snippet 2: Mouse & Key Listeners with Adapters
```java
import javax.swing.*;
import java.awt.FlowLayout;
import java.awt.event.*;

public class EventAdapterDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Adapter Demo");
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());
        
        JLabel lblStatus = new JLabel("Status: -");
        JTextField txtField = new JTextField(15);
        frame.add(txtField); frame.add(lblStatus);

        // MouseAdapter for enter/exit hover
        frame.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                lblStatus.setText("Mouse Entered at: " + e.getX() + "," + e.getY());
            }
            @Override
            public void mouseExited(MouseEvent e) {
                lblStatus.setText("Mouse Left Window");
            }
        });

        // KeyAdapter for Enter key
        txtField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    lblStatus.setText("Typed: " + txtField.getText());
                }
            }
        });

        frame.setVisible(true);
    }
}
```

### Snippet 3: Applet Lifecycle & Drawing Shapes
```java
import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;

/*
<applet code="MyApplet.class" width="300" height="300">
</applet>
*/
public class MyApplet extends Applet {
    // Lifecycle: init() -> start() -> paint() -> stop() -> destroy()
    @Override
    public void init() {
        setBackground(Color.WHITE);
    }

    @Override
    public void paint(Graphics g) {
        g.drawString("Applet Graphics Demo", 20, 20);
        
        g.setColor(Color.RED);
        g.fillRect(50, 50, 80, 40); // x, y, width, height

        g.setColor(Color.BLUE);
        g.fillOval(150, 50, 60, 60);

        g.setColor(Color.GREEN);
        g.fillArc(50, 120, 80, 80, 0, 120); // Pie chart slice
    }
}
```

### Snippet 4: Complete JavaFX Application
```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class JavaFXQuickApp extends Application {
    @Override
    public void start(Stage stage) {
        VBox vbox = new VBox(10); // 10px spacing
        vbox.setStyle("-fx-padding: 20px; -fx-alignment: center;");

        TextField txtName = new TextField();
        txtName.setPromptText("Enter your name");
        Label lblGreeting = new Label();
        Button btn = new Button("Say Hello");

        // Event Handling
        btn.setOnAction(e -> {
            lblGreeting.setText("Hello, " + txtName.getText());
            lblGreeting.setStyle("-fx-text-fill: green; -fx-font-size: 16px;");
        });

        // Mouse hover on node
        vbox.setOnMouseMoved(e -> {
            System.out.println("Coordinates: X=" + e.getX() + " Y=" + e.getY());
        });

        vbox.getChildren().addAll(txtName, btn, lblGreeting);

        Scene scene = new Scene(vbox, 300, 250);
        stage.setTitle("JavaFX Exam App");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

---

## 5. 🎯 30-Second Rapid Recall Quiz

- **Q: Which method closes a `JDialog` programmatically?** $\rightarrow$ `dialog.dispose()`.
- **Q: What does `JOptionPane.showConfirmDialog()` return?** $\rightarrow$ `int` (0 for YES, 1 for NO, 2 for CANCEL).
- **Q: What is the default layout of `JFrame`?** $\rightarrow$ `BorderLayout`.
- **Q: What is the default layout of `JPanel`?** $\rightarrow$ `FlowLayout`.
- **Q: Which JavaFX method displays the window?** $\rightarrow$ `stage.show()`.
