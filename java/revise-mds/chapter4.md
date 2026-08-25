# Chapter 4: Distributed Network Programming — Exam Quick Revision

> **Exam Focus**: TCP (`ServerSocket` / `Socket`), UDP (`DatagramSocket` / `DatagramPacket`), `InetAddress`, `URL` & `URLConnection`, JavaMail API (`MimeMessage`, `Session`, `Transport`), RMI 4-File Architecture (`Remote`, `UnicastRemoteObject`, `LocateRegistry`), CORBA Architecture & IDL (`ORB`, `POA`, `IIOP`), RMI vs. CORBA.

---

## 1. 🚨 Exact Classes, Interfaces & Imports You Must Know

| Class / Interface | Exact Package / Import | Type | Purpose / Exam Trigger |
| :--- | :--- | :--- | :--- |
| `ServerSocket`, `Socket` | `java.net.*` | Classes | Connection-oriented TCP Server & Client |
| `DatagramSocket`, `DatagramPacket` | `java.net.*` | Classes | Connectionless UDP communication |
| `InetAddress` | `java.net.InetAddress` | Class | IP address lookup (`InetAddress.getByName("localhost")`) |
| `URI`, `URL`, `URLConnection` | `java.net.*` | Classes | Web URLs, HTTP headers & resource streaming |
| `Session`, `Authenticator` | `jakarta.mail.*` / `javax.mail.*` | Classes | Mail session creation with credentials |
| `MimeMessage`, `InternetAddress` | `jakarta.mail.internet.*` | Classes | MIME-compliant email header & body builder |
| `Transport` | `jakarta.mail.Transport` | Class | Static email dispatcher (`Transport.send(msg)`) |
| `Remote` | `java.rmi.Remote` | **Interface** | Marker interface that all RMI services MUST extend |
| `RemoteException` | `java.rmi.RemoteException` | Checked Exc | Mandatory exception thrown by all RMI methods |
| `UnicastRemoteObject` | `java.rmi.server.*` | Class | Base class for RMI servants to export point-to-point stubs |
| `LocateRegistry`, `Registry` | `java.rmi.registry.*` | Classes | RMI lookup registry (`createRegistry(1099)`, `rebind()`, `lookup()`) |
| `ORB`, `POA`, `NamingContextExt`| `org.omg.CORBA.*`, `org.omg.CosNaming.*` | Classes | CORBA Request Broker & Naming service |

---

## 2. ⚠️ Things You WILL Forget in the Exam (Gotchas & Traps)

1. **TCP vs UDP Classes**:
   - TCP: `ServerSocket` (server) + `Socket` (client). Uses **streams** (`getInputStream()`, `getOutputStream()`).
   - UDP: `DatagramSocket` (both sides) + `DatagramPacket` (data envelopes). Uses **raw byte arrays** (`byte[]`), NO streams!
2. **UDP Packet Constructors (Send vs Receive)**:
   - **Receive Packet**: `new DatagramPacket(buffer, buffer.length);` (Only 2 arguments!).
   - **Send Packet**: `new DatagramPacket(buffer, buffer.length, inetAddress, port);` (4 arguments!).
3. **RMI Interface & Constructor Requirements**:
   - Remote Interface MUST `extends Remote`.
   - Every method in the interface MUST declare `throws RemoteException`.
   - The implementation class constructor MUST explicitly declare `throws RemoteException` because `super()` from `UnicastRemoteObject` throws it!
4. **URL Instantiation (Modern Java)**:
   - `new URL("https://...")` is deprecated. Best practice: `new URI("https://...").toURL()`.
5. **JavaMail Session Creation**:
   - `Session.getInstance(properties, authenticator)` (Do NOT use `new Session()`).
   - Receiver field: `msg.setRecipients(Message.RecipientType.TO, InternetAddress.parse(toEmail));`.
6. **Default Port Numbers to Memorize**:
   - HTTP: `80` | HTTPS: `443` | SMTP: `25` or `587` (TLS) | RMI Registry: `1099` | CORBA NameService: `1050` | MySQL: `3306`.

---

## 3. ⚖️ Crucial Network Comparisons

### A. TCP vs. UDP

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection** | Connection-Oriented (3-way handshake) | Connectionless (Fire & Forget) |
| **Reliability** | **100% Reliable** (Retransmits lost packets) | **Unreliable** (Packets can be lost/duplicated) |
| **Ordering** | Guaranteed strict order | Packets can arrive out of order |
| **Speed** | Slower (protocol overhead & ACK packets) | **Blazing fast** (Zero overhead) |
| **Java Classes** | `ServerSocket`, `Socket` | `DatagramSocket`, `DatagramPacket` |
| **Best For** | Web (HTTP), Email (SMTP), File transfer (FTP)| Live Video/Audio streaming, Online Games, VoIP |

### B. RMI vs. CORBA

| Feature | RMI (Remote Method Invocation) | CORBA (Common Object Request Broker) |
| :--- | :--- | :--- |
| **Language Support** | **Java-only** (Client & Server must be JVM) | **Language-Independent** (C++, Java, Python, Ada)|
| **Contract Language**| Native Java Interface (`extends Remote`)| **Neutral IDL** (Interface Definition Language) |
| **Underlying Protocol**| **JRMP** (Java Remote Method Protocol) | **IIOP** (Internet Inter-ORB Protocol) |
| **Complexity** | Simple, clean, built into JDK | Heavyweight, complex IDL compilation step |

---

## 4. 📋 Must-Memorize Code Boilerplates

### Snippet 1: TCP Server & Client
```java
// === SERVER ===
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPServer {
    public static void main(String[] args) throws IOException {
        try (ServerSocket server = new ServerSocket(5000);
             Socket client = server.accept(); // Blocks until client connects
             Scanner in = new Scanner(client.getInputStream());
             PrintWriter out = new PrintWriter(client.getOutputStream(), true)) { // autoflush=true

            String msg = in.nextLine();
            out.println("Echo from Server: " + msg);
        }
    }
}

// === CLIENT ===
public class TCPClient {
    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket("localhost", 5000);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             Scanner in = new Scanner(socket.getInputStream())) {

            out.println("Hello TCP Server");
            System.out.println(in.nextLine());
        }
    }
}
```

### Snippet 2: UDP Server & Client
```java
// === UDP SERVER (Echo) ===
import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        try (DatagramSocket socket = new DatagramSocket(6000)) {
            byte[] buf = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(buf, buf.length);
            socket.receive(receivePacket); // Blocks

            String msg = new String(receivePacket.getData(), 0, receivePacket.getLength());
            byte[] sendBuf = ("Echo: " + msg).getBytes();

            // Reply using sender's address and port extracted from packet
            DatagramPacket sendPacket = new DatagramPacket(
                sendBuf, sendBuf.length, receivePacket.getAddress(), receivePacket.getPort()
            );
            socket.send(sendPacket);
        }
    }
}

// === UDP CLIENT ===
public class UDPClient {
    public static void main(String[] args) throws Exception {
        try (DatagramSocket socket = new DatagramSocket()) {
            InetAddress ip = InetAddress.getByName("localhost");
            byte[] sendBuf = "Hello UDP".getBytes();

            DatagramPacket sendPacket = new DatagramPacket(sendBuf, sendBuf.length, ip, 6000);
            socket.send(sendPacket);

            byte[] receiveBuf = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveBuf, receiveBuf.length);
            socket.receive(receivePacket);
            System.out.println(new String(receivePacket.getData(), 0, receivePacket.getLength()));
        }
    }
}
```

### Snippet 3: URL & URLConnection Reader
```java
import java.net.*;
import java.util.Scanner;

public class URLReader {
    public static void main(String[] args) throws Exception {
        URI uri = new URI("https://www.httpbin.org/robots.txt");
        URL url = uri.toURL();
        URLConnection conn = url.openConnection();

        System.out.println("Content-Type: " + conn.getContentType());
        System.out.println("Content-Length: " + conn.getContentLength());

        try (Scanner sc = new Scanner(conn.getInputStream())) {
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
        }
    }
}
```

### Snippet 4: JavaMail API (SMTP Sender)
```java
import jakarta.mail.*;
import jakarta.mail.internet.*;
import java.util.Properties;

public class MailSenderDemo {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.port", "587");

        Session session = Session.getInstance(props, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication("sender@gmail.com", "app-password");
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress("sender@gmail.com"));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("recipient@gmail.com"));
            message.setSubject("Exam Notification");
            message.setText("Distributed Network Programming revision successful!");

            Transport.send(message); // Dispatch email
            System.out.println("Email sent successfully!");
        } catch (MessagingException e) {
            e.printStackTrace();
        }
    }
}
```

### Snippet 5: Complete RMI Application (4-Component Architecture)
```java
// 1. Remote Interface (ComputeService.java)
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ComputeService extends Remote {
    int add(int a, int b) throws RemoteException;
}

// 2. Servant Implementation (ComputeServiceImpl.java)
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ComputeServiceImpl extends UnicastRemoteObject implements ComputeService {
    public ComputeServiceImpl() throws RemoteException {
        super(); // Exports the remote object
    }
    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }
}

// 3. RMI Server (RMIServer.java)
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) throws Exception {
        Registry registry = LocateRegistry.createRegistry(1099); // Start RMI Registry
        registry.rebind("CalculatorService", new ComputeServiceImpl());
        System.out.println("RMI Server Bound and Ready.");
    }
}

// 4. RMI Client (RMIClient.java)
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) throws Exception {
        Registry registry = LocateRegistry.getRegistry("localhost", 1099);
        ComputeService comp = (ComputeService) registry.lookup("CalculatorService");
        int result = comp.add(20, 30);
        System.out.println("Remote Calculation Result: " + result);
    }
}
```

### Snippet 6: CORBA IDL Sample (`Adder.idl`)
```idl
module AddApp {
    interface Adder {
        long add(in long a, in long b);
    };
};
// Compilation command: idlj -fall Adder.idl
```

---

## 5. 🎯 30-Second Rapid Recall Quiz

- **Q: What is a Stub in RMI?** $\rightarrow$ Client-side proxy that marshals method parameters into network packets.
- **Q: What is a Skeleton in RMI?** $\rightarrow$ Server-side proxy that unmarshals incoming network packets and invokes the real method on the servant.
- **Q: What protocol does CORBA use?** $\rightarrow$ **IIOP** (Internet Inter-ORB Protocol).
- **Q: How to create an RMI Registry inside Java code?** $\rightarrow$ `LocateRegistry.createRegistry(1099);`.
- **Q: Why does UDP not have `ConnectionRefusedException`?** $\rightarrow$ Because UDP is connectionless; packets are dispatched into the network without verifying recipient status.
