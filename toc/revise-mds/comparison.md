# TOC Master Comparison & Disambiguation Guide

> **File:** `toc/revise-mds/comparison.md`  
> **Purpose:** Single consolidated cheat-sheet directly comparing easily confused concepts across the entire Theory of Computation syllabus.

---

## 1. Master Automata & Machine Comparison

| Feature | DFA (Deterministic Finite Automaton) | NFA (Non-Deterministic Finite Automaton) | DPDA (Deterministic Pushdown Automaton) | NPDA (Non-Deterministic Pushdown Automaton) | LBA (Linear Bounded Automaton) | TM (Turing Machine - DTM/NTM) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Chomsky Type** | **Type 3 (Regular)** | **Type 3 (Regular)** | **Deterministic CFL (DCFL)** | **Type 2 (CFL)** | **Type 1 (CSL)** | **Type 0 (RE)** |
| **Formal Tuple** | **5-tuple:** $(Q, \Sigma, \delta, q_0, F)$ | **5-tuple:** $(Q, \Sigma, \delta, q_0, F)$ | **7-tuple:** $(Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ | **7-tuple:** $(Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ | **8-tuple:** $(Q, \Sigma, \Gamma, \delta, q_0, \text{¢}, \$, F)$ | **7-tuple:** $(Q, \Sigma, \Gamma, \delta, q_0, B, F)$ |
| **Memory / Storage** | **None** (only current state in $Q$) | **None** (only current states in $2^Q$) | **Single Stack** (LIFO, unbounded depth) | **Single Stack** (LIFO, unbounded depth) | **Tape bounded** by $k \cdot |w|$ cells (between $\text{¢}$ and $\$$) | **Infinite tape**, read/write, bidirectional |
| **Head Movement** | One-way (Left $\to$ Right only) | One-way (Left $\to$ Right only) | Input: One-way; Stack: Top only | Input: One-way; Stack: Top only | Two-way ($L, R$) within bounds | Two-way ($L, R$), unbounded |
| **Transition Function $\delta$** | **$\delta : Q \times \Sigma \to Q$** | **$\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$** | **$\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \to (Q \times \Gamma^*)$** *(at most 1 move)* | **$\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \to \mathcal{P}(Q \times \Gamma^*)$** | **$\delta : Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$** | **$\delta : Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$** |
| **Determinism vs Non-determinism** | **DFA $\equiv$ NFA** (Identical power, $2^{|Q|}$ state explosion) | | **DPDA $\subsetneq$ NPDA** (Non-determinism adds power!) | | **LBA $\equiv$ NLBA** (Immerman–Szelepcsényi) | **DTM $\equiv$ NTM** (Identical power, $O(2^{T})$ BFS simulation) |
| **Acceptance Criteria** | Reading stops at end of input; in state $q \in F$. | Reading stops; at least one branch in $q \in F$. | Final state OR Empty stack ($Z_0$ popped). | Final state OR Empty stack (both equivalent: $L(M) \equiv N(M)$). | Reaches accepting state within tape bounds. | Enters state $q_{accept}$ and halts (input does NOT need to be read). |
| **Canonical Languages** | $a^*b^*$, ending in $01$, even number of $a$'s | $(a+b)^*a(a+b)$ | $a^n b^n$, $w c w^R$, balanced parentheses | $w w^R$, $a^n b^{2n}$, equal $a$'s and $b$'s | $a^n b^n c^n d^n$ | $a^n b^n c^n$, copying $w \to ww$, palindrome |

---

## 2. Pumping Lemma: Regular Languages vs Context-Free Languages

| Pumping Lemma Aspect | Regular Languages (RL) — Chapter 2 | Context-Free Languages (CFL) — Chapter 3 |
| :--- | :--- | :--- |
| **String Partition** | **$w = xyz$** (3 pieces, 1 pumpable part: $y$) | **$w = uvwxy$** (5 pieces, 2 pumpable parts: $v$ and $x$) |
| **Pumping Length Parameter** | $p \ge 1$ (unknown fixed integer constant) | $p \ge 1$ (unknown fixed integer constant) |
| **Condition 1 (Non-empty pump)** | **$|y| \ge 1$** (or $|y| > 0$) | **$|vx| \ge 1$** ($v$ and $x$ cannot both be $\varepsilon$) |
| **Condition 2 (Length Bound)** | **$|xy| \le p$** (*Bounded at the start of string*) | **$|vwx| \le p$** (*Bounded in the middle span*) |
| **Condition 3 (Pumping Validity)**| **$\forall i \ge 0, \quad x y^i z \in L$** | **$\forall i \ge 0, \quad u v^i w x^i y \in L$** |
| **Pumping Down ($i = 0$)** | $w' = xz$ | $w' = uwy$ |
| **Pumping Up ($i = 2$)** | $w' = xyyz$ | $w' = uvvwxxy$ |
| **Pigeonhole Origin** | Repetition of **states in DFA** ($p = |Q|$) | Repetition of **variables in parse tree** ($p = b^{|V|+1}$) |
| **Typical Non-languages Proven**| $\{0^n 1^n \mid n \ge 0\}$, $\{a^n b^{2n} \mid n > 0\}$, $\{a^{n^2}\}$ | $\{a^n b^n c^n \mid n \ge 0\}$, $\{ww \mid w \in \{0, 1\}^*\}$, $\{a^{n^2}\}$ |

---

## 3. Grand Master Closure Properties Matrix

```
       Type 3 (Regular)  ⊆  Type 2 (CFL)  ⊆  Recursive (REC)  ⊆  Type 0 (RE)
```

| Operation | Regular Languages | Context-Free Languages (CFL) | Recursive (Decidable) | Recursively Enumerable (RE) |
| :--- | :---: | :---: | :---: | :---: |
| **Union ($L_1 \cup L_2$)** | **YES** | **YES** | **YES** | **YES** |
| **Concatenation ($L_1 L_2$)** | **YES** | **YES** | **YES** | **YES** |
| **Kleene Star ($L^*$)** | **YES** | **YES** | **YES** | **YES** |
| **Intersection ($L_1 \cap L_2$)** | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> | **YES** | **YES** |
| **Complement ($\overline{L}$)** | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> |
| **Set Difference ($L_1 - L_2$)** | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> |
| **Reversal ($L^R$)** | **YES** | **YES** | **YES** | **YES** |
| **Intersection with Regular** | **YES** | **YES** | **YES** | **YES** |

### Why Did They Fail? (The Traps Explained)
1. **Why CFL fails on Intersection:**
   A PDA has only **one stack**. $L_1 = \{a^n b^n c^m\}$ uses the stack to balance $a$ and $b$. $L_2 = \{a^m b^n c^n\}$ uses the stack to balance $b$ and $c$. The intersection $L_1 \cap L_2 = \{a^n b^n c^n\}$ requires balancing **three counts simultaneously**, which is impossible with one stack!
2. **Why CFL fails on Complement:**
   By De Morgan's Law: $L_1 \cap L_2 = \overline{\overline{L_1} \cup \overline{L_2}}$. Since CFL is closed under union, if it were closed under complement, it would automatically be closed under intersection (a contradiction).
3. **Why RE fails on Complement (Post's Theorem):**
   If $L \in \text{RE}$ and $\overline{L} \in \text{RE}$, then $L$ is **Recursive (Decidable)**. If RE were closed under complement, every RE language would have its complement in RE, making ALL RE languages decidable (which contradicts the undecidability of the Halting Problem!).

---

## 4. Grand Master Decision Algorithms & Decidability Matrix

> **Mnemonic for CFL Decision:** **"Only MEF is Decidable"**  
> (**M**embership, **E**mptiness, **F**initeness). Everything else is **UNDECIDABLE**!

| Decision Problem | Regular (Type 3) | Context-Free (Type 2) | Recursive (Decidable) | Recursively Enumerable (Type 0) |
| :--- | :---: | :---: | :---: | :---: |
| **Membership ($w \in L$?)** | **Decidable** (DFA simulation) | **Decidable** (CYK algorithm: $O(n^3)$) | **Decidable** (By definition: decider halts) | <span style="color:red; font-weight:bold;">Undecidable</span> (Recognizers may loop on $w \notin L$) |
| **Emptiness ($L = \emptyset$?)** | **Decidable** (Graph reachability) | **Decidable** (Generating symbols on $S$) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) |
| **Finiteness (Is $L$ finite?)** | **Decidable** (Cycle on path to $F$) | **Decidable** (Cycles in CNF graph) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) |
| **Equivalence ($L_1 = L_2$?)** | **Decidable** (Symmetric diff $= \emptyset$) | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) |
| **Intersection Emptiness ($L_1 \cap L_2 = \emptyset$?)**| **Decidable** | <span style="color:red; font-weight:bold;">Undecidable</span> (Reduces to PCP) | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> |
| **Universality ($L = \Sigma^*$?)** | **Decidable** (Test if $\overline{L} = \emptyset$) | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> |
| **Subset / Inclusion ($L_1 \subseteq L_2$?)** | **Decidable** (Test $L_1 \cap \overline{L_2} = \emptyset$) | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> |
| **Ambiguity (Is grammar ambiguous?)** | N/A | <span style="color:red; font-weight:bold;">Undecidable</span> (Reduces to PCP) | N/A | N/A |
| **Regularity (Is $L$ regular?)** | Trivial (Always YES) | <span style="color:red; font-weight:bold;">Undecidable</span> | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) | <span style="color:red; font-weight:bold;">Undecidable</span> (Rice's Theorem) |

---

## 5. Grammar Normal Forms Comparison

| Property | Chomsky Normal Form (CNF) | Greibach Normal Form (GNF) |
| :--- | :--- | :--- |
| **Production Format** | **$A \to BC$** OR **$A \to a$** | **$A \to a\alpha$** where $a \in T, \alpha \in V^*$ |
| **Grammar Shape** | Strictly 2 Variables OR 1 Terminal | Strictly 1 Terminal followed by 0 or more Variables |
| **Steps to Derive string $|w| = n$** | Exactly **$2n - 1$ derivation steps** | Exactly **$n$ derivation steps** |
| **Parse Tree Form** | Strictly binary tree | Wide, left-terminal branched tree |
| **Direct Application** | **CYK dynamic programming algorithm** for membership testing; CFL Pumping Lemma proof | Direct top-down construction of equivalent 1-state Pushdown Automaton |

---

## 6. Unit 4 vs Unit 5 Disambiguation

```
┌───────────────────────────────────────────────────┬───────────────────────────────────────────────────┐
│ UNIT 4: THE TURING MACHINE AS A COMPUTER          │ UNIT 5: UNDECIDABILITY & THE LIMITS OF COMPUTATION│
├───────────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ • Formal 7-tuple and instantaneous moves          │ • Church-Turing Thesis (Thesis vs Theorem)        │
│ • TM computing functions (f(n)=n+1, f(x,y)=x+y)   │ • Halting Problem (H_TM / A_TM proof by contra)   │
│ • Multi-tape, Multi-track, Storage in state       │ • Universal Turing Machine (UTM structure)        │
│ • Unrestricted Grammar (Type 0, α → β)            │ • Rice's Theorem (Semantic properties undecidable)│
│ • Recursive Function Theory (Z, S, P + C, P, M)   │ • Post Correspondence Problem (PCP)               │
│ • Focus: What machines CAN construct and compute  │ • Focus: What NO machine can ever decide          │
└───────────────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

---

## 7. Computational Complexity Classes Comparison

| Class | Full Name | Deterministic Machine Bound | Nondeterministic Machine Bound | Verification Time | Classic Example Problems |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P** | Polynomial Time | Solvable in **$O(n^k)$ steps** on DTM | Solvable in polynomial time | Solvable in polynomial time | Shortest path (Dijkstra), MST (Kruskal), Sorting, 2-SAT |
| **NP** | Nondeterministic Polynomial Time | Requires exponential time ($O(2^{n^k})$) | Solvable in **$O(n^k)$ steps** on NTM | **Verifiable in $O(n^k)$ steps** by DTM with certificate | 3-SAT, Clique, Hamiltonian Cycle, Sudoku, Subgraph Isomorphism |
| **NP-Complete** | NP-Complete | Hardest problems in NP; if one is in P $\implies P = NP$ | Solvable in polynomial time on NTM | Verifiable in polynomial time by DTM | SAT, 3-SAT, Vertex Cover, Clique, TSP (Decision), Subset Sum |
| **NP-Hard** | NP-Hard | At least as hard as any problem in NP ($\forall Y \in NP, Y \le_P X$) | Does NOT need to be in NP (can be undecidable!) | May not be verifiable in polynomial time | Halting Problem, TSP (Optimization: find exact minimum tour) |

---

## 8. High-Yield Mnemonics Cheat Sheet

1. **Chomsky Hierarchy Languages & Automata:**
   $$\text{\bf RE - CS - CF - REG} \quad \iff \quad \text{\bf TM - LBA - PDA - FA}$$
   *(Type 0 to Type 3)*

2. **Recursive Function Theory:**
   $$\text{\bf Z - S - P} \quad + \quad \text{\bf C - P - M}$$
   *(Base: Zero, Successor, Projection) + (Operations: Composition, Primitive Recursion, $\mu$-Minimization)*

3. **CFL Decidable Problems:**
   $$\text{\bf Only MEF is Decidable}$$
   *(**M**embership via CYK, **E**mptiness via generating start symbol, **F**initeness via CNF cycles. Everything else is **UNDECIDABLE**!)*

4. **CFG Simplification Strict Order:**
   $$\text{\bf N - U - U} \implies \text{\bf Null} \to \text{\bf Unit} \to \text{\bf Useless (Gen } \to \text{\bf Reach)}$$

5. **Post's Complementarity Theorem:**
   $$L \text{ is Recursive (Decidable)} \iff L \in \text{RE} \quad \text{\bf AND} \quad \overline{L} \in \text{RE}$$
