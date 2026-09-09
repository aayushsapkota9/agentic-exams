# Chapter 6: Computational Complexity — Quick Revision Note

> **Revision Target:** 10–15 minutes  
> **Coverage:** Computability vs Complexity, Time & Space Bounds, Tractable vs Intractable Problems, Class P, Class NP, NP-Hard, NP-Complete, Cook-Levin Theorem, Classic NP-Complete Problems.

---

## 1. Computability vs Computational Complexity

| Dimension | Computability Theory (Unit 5) | Computational Complexity Theory (Unit 6) |
| :--- | :--- | :--- |
| **Core Question** | *"Can this problem be solved by an algorithm at all?"* | *"How efficiently can this problem be solved?"* |
| **Primary Metric** | Decidable vs Undecidable | Time ($O(f(n))$) and Space ($O(f(n))$) requirements |
| **Boundary** | Finite Halting vs Infinite Looping | Polynomial Time ($O(n^k)$) vs Exponential Time ($O(2^n)$) |
| **Key Benchmark** | Halting Problem, Church-Turing Thesis | $P$ vs $NP$ Question, Cook-Levin Theorem |

---

## 2. Tractable vs Intractable Problems

- **Tractable Problems:** Problems that can be solved by a deterministic algorithm in **polynomial time** ($O(n^k)$ for some constant $k$).
  - Belong to **Class P**.
  - Considered computationally feasible for practical real-world inputs (e.g., Shortest Path via Dijkstra, Sorting, Minimum Spanning Tree).
- **Intractable Problems:** Problems that require **super-polynomial or exponential time** ($O(2^n), O(n!)$) in the worst case to solve deterministically, or are completely undecidable.
  - Infeasible for large $n$. Even with the fastest supercomputers, an exponential algorithm ($2^n$) quickly exceeds the age of the universe for $n \approx 100$.

---

## 3. Class P and Class NP

```
      +-----------------------------------------+
      |               CLASS NP                  |
      |  (Verifiable in Polynomial Time)        |
      |                                         |
      |   +-------------------+  +-----------+  |
      |   |      CLASS P      |  |    NP-    |  |
      |   |   (Solvable in    |  | COMPLETE  |  |
      |   | Polynomial Time)  |  | (Hardest) |  |
      |   +-------------------+  +-----------+  |
      +-----------------------------------------+
                    Is P = NP?
```

### The Definitions You Must Write in Exams

#### Class P (Polynomial Time)
The class of all decision problems that can be **solved** by a **Deterministic Turing Machine (DTM)** in polynomial time $O(n^k)$:
$$P = \bigcup_{k \ge 1} \text{TIME}(n^k)$$

#### Class NP (Nondeterministic Polynomial Time)
Can be defined in **two equivalent ways**:
1. **Verifier Definition:** The class of decision problems for which a proposed "Yes" answer (a certificate / witness) can be **verified** by a Deterministic Turing Machine in **polynomial time**.
2. **NTM Definition:** The class of decision problems that can be **solved** by a **Non-Deterministic Turing Machine (NTM)** in polynomial time:
   $$NP = \bigcup_{k \ge 1} \text{NTIME}(n^k)$$

> [!CAUTION]
> **The #1 Student Exam Trap:**
> **NP DOES NOT MEAN "NON-POLYNOMIAL"!**  
> It strictly stands for **Nondeterministic Polynomial time**. Writing "non-polynomial" will lose you full marks immediately!

---

### The $P$ vs $NP$ Question
- **Known Fact:** $P \subseteq NP$ (Because any problem that can be *solved* in polynomial time can trivially be *verified* in polynomial time by ignoring the certificate and just solving it).
- **The Unsolved Question:** Is $P = NP$ or is $P \ne NP$?
  - If $P = NP$, every problem that can be verified easily can also be solved easily (destroying modern cryptography, RSA, blockchain).
  - Most computer scientists strongly suspect $P \ne NP$.

---

## 4. NP-Hard vs NP-Complete

### Polynomial-Time Reduction ($A \le_P B$)
Problem $A$ reduces to problem $B$ in polynomial time ($A \le_P B$) if any instance of $A$ can be transformed into an instance of $B$ in polynomial time such that the answer to $B$ is "Yes" if and only if the answer to $A$ is "Yes".
- **Meaning:** $B$ is **at least as hard as** $A$!

---

### Defining the Classes
- **NP-Hard:** A problem $X$ is NP-Hard if **every problem in NP is polynomial-time reducible to $X$**:
  $$\forall Y \in NP, \quad Y \le_P X$$
  *(Note: An NP-Hard problem does NOT need to be in NP; it can even be undecidable, like the Halting Problem!).*
- **NP-Complete:** A problem $X$ is NP-Complete if it satisfies **BOTH** conditions:
  1. **$X \in NP$** (Its solutions can be verified in polynomial time).
  2. **$X$ is NP-Hard** ($\forall Y \in NP, Y \le_P X$).

---

### The Monumental Property of NP-Completeness
> *"If ANY single NP-Complete problem can be solved in polynomial time ($X \in P$), then EVERY problem in NP can be solved in polynomial time, proving that $P = NP$."*

---

## 5. Cook-Levin Theorem & Classic NP-Complete Problems

### The Cook-Levin Theorem (1971)
- **Theorem:** The **Boolean Satisfiability Problem (SAT)** is **NP-Complete**.
- **Historical Significance:** This was the very first problem proven to be NP-Complete. Cook and Levin proved it directly from scratch without reducing from another problem: they encoded the step-by-step polynomial-time computation of an arbitrary Non-Deterministic Turing Machine into a massive boolean formula in Conjunctive Normal Form (CNF).

---

### 7 Classic NP-Complete Problems to Memorize (Exam Cheat Sheet)
1. **SAT / 3-SAT:** Given a boolean formula in 3-CNF, is there a truth assignment that makes the entire formula TRUE?
2. **Vertex Cover:** Given a graph $G = (V, E)$ and integer $k$, does there exist a subset of vertices $V' \subseteq V$ of size $|V'| \le k$ such that every edge in $E$ has at least one endpoint in $V'$?
3. **Clique Problem:** Given graph $G$ and integer $k$, does $G$ contain a complete subgraph (clique) of size $\ge k$?
4. **Hamiltonian Cycle:** Does a graph $G$ contain a closed cycle that visits **every vertex exactly once**?
5. **Travelling Salesperson Problem (TSP - Decision Version):** Given a set of cities, distances, and bound $K$, is there a round-trip tour visiting every city exactly once with total distance $\le K$?
6. **Subset Sum:** Given a set of integers and a target $T$, does any subset sum up to exactly $T$?
7. **Graph Coloring (3-Colorability):** Can the vertices of a graph $G$ be colored using at most 3 colors such that no two adjacent vertices share the same color?

---

## 6. Professor Tricks & Traps

> [!WARNING]
> ### 1. Decision Problem vs Optimization Problem
> - NP-Completeness is formally defined **strictly for Decision Problems** (problems that yield a binary **YES/NO** answer).
> - **Trap:** *"Is TSP NP-Complete?"*
>   - Finding the *shortest possible tour* is an **Optimization Problem** ($\implies$ NP-Hard).
>   - Asking *"Does there exist a tour of length $\le K$?"* is a **Decision Problem** ($\implies$ **NP-Complete**). Always specify the decision version!

> [!WARNING]
> ### 2. Solving vs Verifying (The Sudoku Analogy)
> - **Verification:** Given an already-filled $9 \times 9$ Sudoku grid, checking whether rows, columns, and $3 \times 3$ boxes contain numbers 1–9 takes under a second $\implies$ **Polynomial Time Verification ($NP$)**.
> - **Solving:** Given an empty or sparse generalized $n \times n$ Sudoku grid, finding the valid solution by testing branches can take exponential time $\implies$ **NP-Complete**.
