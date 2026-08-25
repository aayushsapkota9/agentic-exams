# Chapter 3: GUI Programming (Swing, JavaFX & Applets) — Exam Quick Revision

> **Exam Focus**: Swing hierarchy, Dialogs (`JOptionPane` vs `JDialog`), Menus (`JMenuBar`, `JMenu`, `JMenuItem`), Event Handling (`ActionListener`, `MouseAdapter`, `KeyAdapter`), Layout Managers (`BorderLayout`, `GridLayout`, `FlowLayout`, `GridBagLayout`), Frame Background Color trap (`getContentPane()`), Applet Lifecycle & `paint(Graphics g)`, JavaFX Architecture (`Stage` $\rightarrow$ `Scene` $\rightarrow$ Panes $\rightarrow$ Nodes), Swing vs JavaFX Comparison.

---

## 1. 📦 Package & Components Quick Reference Table

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
