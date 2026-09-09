# Chapter 4: Turing Machines — Quick Revision Note

> **Revision Target:** 15–20 minutes  
> **Coverage:** Formal 7-Tuple, Transition Function Anatomy, Instantaneous Descriptions (IDs), Language Acceptors vs Function Computers, Extensions of TM, Unrestricted Grammars, Recursive Function Theory.

---

## 1. Unit 4 vs Unit 5 Disambiguation (Read This First!)

```
+-------------------------------------------------------------------------------+
| UNIT 4: THE MACHINE & COMPUTATION                                             |
| Focus: HOW the Turing Machine works, builds, computes functions, and matches   |
| Type-0 grammars. (Constructive: Languages, Functions, Extensions, Math Logic).|
+-------------------------------------------------------------------------------+
| UNIT 5: THE LIMITS & UNDECIDABILITY                                           |
| Focus: What the Turing Machine CANNOT DO.                                      |
| (Impossibility: Church-Turing Thesis, Halting Problem, UTM, Reductions, PCP).  |
+-------------------------------------------------------------------------------+
```

---

## 2. Turing Machine Formalism & Transitions

### The Formal 7-Tuple
$$M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$$
- $Q$: Finite set of states
- $\Sigma$: Input alphabet (does NOT contain the blank symbol $B$)
- $\Gamma$: Tape alphabet ($\Sigma \subset \Gamma$, includes blank $B$ and markers $X, Y, Z$)
- $q_0 \in Q$: Initial start state
- $B \in \Gamma$: Blank symbol ($B \notin \Sigma$)
- $F \subseteq Q$: Set of final / accepting halting states
- **$\delta$:** Transition function:
  $$\delta : Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$$

---

### Understanding the Transition Function $\delta(q, X) = (p, Y, D)$
```
  Inputs:  (Current State, Tape Symbol Scanned)
  Outputs: (Next State, Symbol Written to Tape, Head Movement L or R)
```

$$\delta(\underbrace{q}_{\text{current state}}, \underbrace{X}_{\text{scanned tape symbol}}) = (\underbrace{p}_{\text{new state}}, \underbrace{Y}_{\text{symbol to write}}, \underbrace{D \in \{L, R\}}_{\text{move head Left or Right}})$$

- *Example Move:* $\delta(q_0, a) = (q_1, X, R)$  
  $\implies$ In state $q_0$, seeing symbol $a$: overwrite with marker $X$, change state to $q_1$, and move the tape head one cell to the **Right**.
- **Instantaneous Description (ID):**
  $$\alpha_1 q \alpha_2$$
  - $\alpha_1$: Tape contents to the left of the head.
  - $q$: Current state of the finite control.
  - $\alpha_2$: Tape contents from the current head position to the rightmost non-blank symbol.  
  *(The head is scanning the FIRST symbol of $\alpha_2$)*.

---

## 3. Turing Machine as Language Acceptor vs Function Computer

### Mode 1: Language Acceptor (Decision Machine)
- Input string $w$ is written on tape: $\dots B B \underline{w}_1 w_2 \dots w_n B B \dots$
- If $w \in L$, machine reaches a state in $F$ and **halts & accepts**.
- If $w \notin L$, machine either halts in a non-accepting state OR **loops forever**.
- **Key Designs to Remember:**
  - $L = \{a^n b^n c^n \mid n \ge 0\}$: Mark $a \to X$, scan right to mark matching $b \to Y$, scan right to mark matching $c \to Z$. Return to leftmost $X$, repeat until all matched, verify only blanks/markers remain.
  - Palindromes $w \in \{a, b\}^*$: Match outer symbols (leftmost with rightmost), replace with blank, traverse back and forth.

---

### Mode 2: Function Computer (Transducer / Unary Arithmetic)
Unlike DFAs and PDAs, a Turing Machine can write output onto its tape!

> [!IMPORTANT]
> **Unary Notation Convention:**
> - Non-negative integer $n$ is represented as a block of $n$ ones ($1^n$) or $n+1$ ones ($0^n$ or $1^{n+1}$).
> - Function $f(n) = n + 1$:
>   - Tape initially contains: $B \underline{0}^n B$.
>   - Strategy: Move right past all $0$'s until reaching blank $B$. Overwrite $B$ with $0$. Move left and halt.
>   - Output on tape: $0^{n+1}$ (representing $n+1$).
> - Function $f(x, y) = x + y$:
>   - Tape initially contains: $B \underline{0}^x 1 0^y B$ (separated by a $1$).
>   - Strategy: Replace the separator $1$ with a $0$ (now we have $x+y+1$ zeros). Move to the rightmost zero and replace it with blank $B$. Result: exactly $x+y$ zeros!

---

## 4. Extensions of Turing Machines (Do They Add Power?)

| Extension | How It Works | Does It Increase Power? | Equivalence Proof Idea |
| :--- | :--- | :---: | :--- |
| **Multi-Tape TM** | $k$ independent tapes, each with its own read/write head. | <span style="color:red; font-weight:bold;">NO ❌</span> | A 1-tape TM with **$2k$ tracks** simulates $k$ tapes (track $2i-1$ stores tape content, track $2i$ stores head marker $\bullet$). Time slowdown is at most quadratic: $O(T^2)$. |
| **Multi-Track TM** | Single tape divided into $k$ parallel tracks; single read/write head. | <span style="color:red; font-weight:bold;">NO ❌</span> | Tape alphabet becomes $\Gamma' = \Gamma^k$ (tuples). Still a standard 1-tape TM. |
| **Storage in State** | State is augmented as a tuple: $[q, a]$ where $a \in \Gamma$ is stored data. | <span style="color:red; font-weight:bold;">NO ❌</span> | State set becomes $Q' = Q \times \Gamma$. Because $Q$ and $\Gamma$ are finite, $Q'$ remains strictly finite! |
| **Non-Deterministic TM (NTM)** | $\delta(q, X) \subseteq Q \times \Gamma \times \{L, R\}$ (multiple possible branch choices). | <span style="color:red; font-weight:bold;">NO ❌</span> | A 3-tape Deterministic TM simulates the NTM via **Breadth-First Search (BFS)** across the computation tree. |
| **Linear Bounded Automata (LBA)** | Tape head is strictly restricted to the $n$ cells containing the input string (between end-markers $\text{¢}$ and $\$$). | **LESS POWER** (Recognizes strictly Type-1 CSL, not general RE). | Bounded tape length restricts possible configurations to $O(|Q| \cdot n \cdot |\Gamma|^n)$. |

---

## 5. Unrestricted Grammars (Type 0) & Recursive Function Theory

### Unrestricted Grammar (Type 0 / Phase-Structure Grammar)
- **Form:**
  $$\alpha \to \beta \quad \text{where } \alpha \in (V \cup T)^+ \text{ and contains } \ge 1 \text{ variable}, \quad \beta \in (V \cup T)^*$$
- **Key Feature:** Completely unrestricted! Left-hand side can have multiple symbols ($|\alpha|$ can be $> |\beta|$), enabling contractions and complex contextual derivations.
- **Equivalence Theorem:** A language is generated by an unrestricted grammar **if and only if** it is accepted by a Turing Machine (i.e., it is **Recursively Enumerable**).

---

### Recursive Function Theory (The Mathematical View of Computability)
Before Turing built machines, mathematicians (Gödel, Church, Kleene) formalized computability purely through functions:

#### A. The 3 Initial / Base Functions:
1. **Zero Function ($Z$):** $Z(x) = 0$
2. **Successor Function ($S$):** $S(x) = x + 1$
3. **Projection / Selector Function ($P_i^n$):** $P_i^n(x_1, x_2, \dots, x_n) = x_i$

#### B. The 3 Operations to Build Complex Functions:
1. **Composition:** Plugging functions into other functions: $f(\vec{x}) = g(h_1(\vec{x}), \dots, h_m(\vec{x}))$.
2. **Primitive Recursion:** Defining functions inductively:
   - Base case: $f(\vec{x}, 0) = g(\vec{x})$
   - Inductive step: $f(\vec{x}, y+1) = h(\vec{x}, y, f(\vec{x}, y))$
   *(Builds addition, multiplication, exponentiation, factorial).*
3. **$\mu$-Operator (Minimalization / Unbounded Search):**
   $$\mu y [g(\vec{x}, y) = 0]$$
   Finds the smallest non-negative integer $y$ such that $g(\vec{x}, y) = 0$. May loop forever if no such $y$ exists!
   *(Minimalization introduces partial functions $\implies$ strictly equivalent to Turing Computability!).*

> **Mnemonic:** **"Z-S-P"** (Base) + **"C-P-M"** (Ops) $\implies$ Zero, Successor, Projection + Composition, Primitive recursion, Minimization.

---

## 6. Professor Tricks & Traps (From Past Exams)

> [!WARNING]
> ### 1. Copying Machine TM ($w \to ww$) *(2022 Fall & 2025 Fall New)*
> - **The Trap:** Students try to copy character by character without marking, resulting in an infinite loop because the machine cannot tell original input from copied characters!
> - **The Fix:** Mark each original symbol: $a \to X$, traverse all the way past original string and past intermediate blanks/separator to write $a$. Return to the first unmarked symbol. Repeat until all original symbols are marked ($X, Y$). Then perform a final rewind pass restoring $X \to a, Y \to b$.

> [!WARNING]
> ### 2. Halting vs Accepting States
> - In a DFA, reading stops when the string ends; you check if you are in a final state.
> - In a Turing Machine, **acceptance is by halting in an accepting state ($q_{acc}$)**! If an input is rejected, the TM can either halt in a rejecting state ($q_{rej}$) OR loop forever.
