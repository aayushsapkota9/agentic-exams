# Programming Questions (ALP) for 8085 and 8086

This document contains a consolidated list of Assembly Language Programming (ALP) questions for the 8085 and 8086 microprocessors, extracted from past exam papers.

---

## 8085 ALP Questions

### Array & Data Manipulation
- **Smallest Number:** Write an ALP in 8085 to find the smallest number among ten 8-bit data stored in memory locations D000H to D009H. Also, store the result in F000H and display it on output device 48H.
- **Greatest Number:** Write an ALP in 8085 to find out the greatest number among ten 8-bit data stored in memory locations C000H to C009H. Also store that value in D000H.
- **Data Transfer:** Write an ALP in 8085 to transfer 10 bytes of data from memory address starting from 5000H to 6000H.
- **Positive/Negative Check:** Write an ALP in 8085 to check whether the number stored in memory location D001H is positive or negative.

### Arithmetic & Series
- **Addition of 32-bit Numbers:** Write an ALP in 8085 to add two 32-bit numbers stored in memory locations starting from 2000H and 3000H respectively.
- **Sum of Even Numbers:** Write an ALP in 8085 to find the sum of even numbers located from address D050H-D059H and store the result in E055H.
- **Sum of Odd Numbers:** Write an ALP in 8085 to find the sum of odd numbers located from memory address C000H to C005H and store the result in C006H.
- **Sum of Squares:** Write an ALP in 8085 to perform the following addition: $1^2 + 2^2 + 3^2 + ... + 9^2$.
- **Fibonacci Series:** Write 8085 assembly programming language to generate the Fibonacci series of the first 10 terms starting from 1.

### Logical & Mathematical Checks
- **Prime Number Check:** Write an ALP in 8085 to check whether the number stored in memory location 2060H is prime or not. If the number is prime, store FFH in memory location C00FH, else store 00H.

---

## 8086 ALP Questions

### Interfacing & I/O
- **8255 PPI Status:** Write an 8085 program to take input from 4 switches connected to PC0-PC3 and display the status of the switches to 4 LEDs connected to PC4-PC7 of 8255 PPI.

---

## 8086 ALP Questions

### String manipulation
- **Palindrome Check:** Write an 8086 ALP to check whether the given string is a palindrome or not.
- **Reverse String Display:** Write an 8086 ALP to display the string "POKHARA UNIVERSITY" in reverse order.
- **Display String (Console):** Write an 8086 ALP to display the string "Computer Engineering" at the console.
- **Reverse User Input:** Write an ALP for 8086 to take a string input from the keyboard and display its reverse form on the screen.
- **Print Word by Word:** Write an 8086 ALP for MASM in DOS mode to print each word of a string on different lines.
- **Case Conversion:** Write a program in 8086 to display "MICROPROCESSOR IS EASY TO LEARN" in lower case.

### Arithmetic & Functions
- **Square Root:** Write an 8086 program to find the square root of a given number. (Assume the number is a perfect square of two digits).
- **Positive/Negative Check:** Write a program in 8086 to find whether a number is positive or negative.
- **Display without 09H:** Write an ALP in 8086 to display "POKHARA UNIVERSITY" without using the 09H function of INT 21H.

---

## Common ALP Commands (Instruction Set)

### 8085 Microprocessor Commands
| Command | Example | Description |
| :--- | :--- | :--- |
| **MOV** | `MOV A, B` | Moves data from register B to register A. |
| **MVI** | `MVI A, 05H` | Moves immediate 8-bit data to register A. |
| **LXI** | `LXI H, 2000H` | Loads a 16-bit address into a register pair (e.g., HL). |
| **LDA** | `LDA 3000H` | Loads the accumulator directly with data from a memory address. |
| **STA** | `STA 3001H` | Stores the content of the accumulator at a memory address. |
| **LHLD** | `LHLD 2500H` | Loads HL pair directly from memory locations 2500H and 2501H. |
| **SHLD** | `SHLD 2500H` | Stores HL pair content directly to memory locations 2500H and 2501H. |
| **ADD / SUB** | `ADD B` | Adds / Subtracts the content of register B to/from the accumulator. |
| **INR / DCR** | `INR A` | Increments / Decrements the registration by 1. |
| **INX / DCX** | `INX H` | Increments / Decrements a 16-bit register pair by 1. |
| **CMP** | `CMP B` | Compares register B with A (sets flags without changing A). |
| **ANA / ORA** | `ANA B` | Logical AND / OR of register B with register A. |
| **XRA** | `XRA B` | Logical XOR of register B with register A. |
| **DAA** | `DAA` | Decimal Adjust Accumulator (used for BCD addition). |
| **XCHG** | `XCHG` | Exchanges the contents of HL and DE register pairs. |
| **RIM / SIM** | `RIM` | Read / Set Interrupt Mask (used for serial I/O and interrupts). |
| **JMP** | `JMP 2050H` | Unconditional jump to specified address. |
| **JZ / JNZ** | `JZ 2080H` | Jump if Zero flag is set / not set. |
| **JC / JNC** | `JC 2090H` | Jump if Carry flag is set / not set. |
| **CALL / RET**| `CALL 4000H` | Call a subroutine / Return from subroutine. |
| **HLT** | `HLT` | Halts the microprocessor. |

### 8086 Microprocessor Commands
| Command | Example | Description |
| :--- | :--- | :--- |
| **MOV** | `MOV AX, BX` | Moves 16-bit data from register BX to AX. |
| **ADD / SUB** | `ADD AX, CX` | Adds / Subtracts content of register/memory to/from AX. |
| **INC / DEC** | `INC SI` | Increment or decrement register/memory content by 1. |
| **MUL / DIV** | `MUL BL` | Unsigned multiplication or division (uses AL/AX). |
| **CMP** | `CMP AX, BX` | Compares AX and BX by subtraction (affects flags). |
| **AND / OR** | `AND AL, 0FH` | Logical AND / OR operations. |
| **XOR** | `XOR AX, AX` | Logical XOR (commonly used to clear a register). |
| **JMP** | `JMP Label` | Unconditional jump to a label. |
| **JE / JNE** | `JE Label` | Jump if Equal (Zero flag=1) / Not Equal (Zero flag=0). |
| **JG / JL** | `JG Label` | Jump if Greater / Less (for signed numbers). |
| **LOOP** | `LOOP Label` | Decrements CX and jumps if CX is not zero. |
| **INT** | `INT 21H` | Invokes a software interrupt (e.g., DOS API). |
| **PUSH / POP** | `PUSH AX` | Pushes content of AX onto stack / Pops from stack. |
| **LEA** | `LEA DX, Str` | Load Effective Address of 'Str' into DX. |
| **MOVSB** | `MOVSB` | Move string byte from DS:SI to ES:DI. |
| **CMPSB** | `CMPSB` | Compare string byte from DS:SI with ES:DI. |
| **SCASB** | `SCASB` | Scan string byte (compares AL with ES:DI). |
| **STOSB** | `STOSB` | Store AL into string (ES:DI). |
| **CLD / STD** | `CLD` | Clear / Set Direction flag (for string operations). |
| **OFFSET** | `MOV SI, OFFSET S`| Directive to get the offset address of a variable. |
