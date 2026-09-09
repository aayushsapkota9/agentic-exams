# Chapter 2: Finite Automata and Regular Languages — Quick Revision Note

> **Revision Target:** 15–20 minutes  
> **Coverage:** DFA, NFA, $\varepsilon$-NFA, Subset Construction, DFA Minimization, Arden's Theorem, Regular Expressions, Pumping Lemma for Regular Languages, Closure Properties, Decision Algorithms.

---

## 1. Automata Anatomy & Transition Functions

### The Formal 5-Tuple
Both DFA and NFA are formally defined as:
$$M = (Q, \Sigma, \delta, q_0, F)$$
- $Q$: Finite set of states
- $\Sigma$: Finite input alphabet
- $q_0 \in Q$: Initial / start state
- $F \subseteq Q$: Set of final / accepting states
- $\delta$: Transition function (THE CRITICAL DIFFERENCE!)

### Transition Function Comparison
| Property | Deterministic Finite Automaton (DFA) | Non-Deterministic Finite Automaton (NFA) |
| :--- | :--- | :--- |
| **Transition Function $\delta$** | **$\delta : Q \times \Sigma \to Q$** | **$\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$ (or $\mathcal{P}(Q)$)** |
| **Next State** | Exactly **one** unique deterministic state. | A **subset / set of states** (can be $\emptyset$). |
| **$\varepsilon$-Transitions** | **Never allowed.** Must consume an input symbol. | **Allowed.** Can change state without reading input. |
| **Computational Power** | Identical: $\mathcal{L}(\text{DFA}) = \mathcal{L}(\text{NFA}) = \mathcal{L}(\varepsilon\text{-NFA}) = \text{Regular Languages}$. | |
| **Max States on Conversion** | A DFA converted from an $n$-state NFA can have up to **$2^n$ states**. | |

---

## 2. Conversions & Algorithms

### A. NFA to DFA (Subset Construction)
1. **$\varepsilon$-Closure($q$):** The set of all states reachable from $q$ following only $\varepsilon$-transitions (including $q$ itself).
2. **Start State of DFA:** $Q_0' = \varepsilon\text{-closure}(q_0)$.
3. **Transition Table Entry:** For each DFA state subset $S \subseteq Q$ and input $a \in \Sigma$:
   $$\delta'(S, a) = \varepsilon\text{-closure}\left( \bigcup_{q \in S} \delta(q, a) \right)$$
4. **Final States of DFA ($F'$):** Any subset $S$ that contains **at least one** state belonging to $F_{NFA}$ ($S \cap F_{NFA} \ne \emptyset$).

---

### B. DFA Minimization (Table-Filling / Myhill-Nerode)
1. **Remove Unreachable States:** Eliminate any states that cannot be reached from $q_0$.
2. **Step 1 (Base Partition):** Draw a lower-triangular grid for all state pairs $(p, q)$. Mark $(p, q)$ with an 'X' if one state is final ($p \in F$) and the other is non-final ($q \notin F$).
3. **Step 2 (Iterative Propagation):** For all unmarked pairs $(p, q)$:
   - For every input $a \in \Sigma$, inspect the target pair $(\delta(p, a), \delta(q, a))$.
   - If the target pair is **already marked**, mark $(p, q)$!
   - Repeat until a full pass makes no new marks.
4. **Step 3 (Merge):** Unmarked pairs are **equivalent** ($p \equiv q$) and are collapsed into a single merged state.

---

### C. Arden's Theorem (FA to Regular Expression)
- **Statement:** If $P$ and $Q$ are regular expressions over $\Sigma$ and $\varepsilon \notin P$, the equation:
  $$R = Q + RP \quad \implies \quad R = QP^* \quad (\text{Unique solution})$$
- **Exam Recipe:**
  1. Write an equation for each state $q_i$:
     $$q_i = \sum (\text{States transitioning into } q_i \times \text{transition symbol}) + (\varepsilon \text{ only if } q_i \text{ is the start state } q_0)$$
  2. Substitute equations into each other until you obtain $q_i = Q + q_i P$.
  3. Apply Arden's Theorem: $q_i = QP^*$.
  4. Final Regular Expression = Sum of expressions for all final states ($\sum_{q_f \in F} q_f$).

---

## 3. Pumping Lemma for Regular Languages

### Formal Statement (Standard $p$ notation)
If language $L$ is regular, there exists an integer constant $p \ge 1$ (the **pumping length**) such that any string $w \in L$ with $|w| \ge p$ can be divided into three substrings:
$$w = xyz$$
satisfying the **Three Mandatory Conditions:**
1. **$|y| \ge 1$** (The pumpable middle $y$ is non-empty, $|y| > 0$).
2. **$|xy| \le p$** ($xy$ is constrained within the first $p$ characters).
3. **$\forall i \ge 0, \quad x y^i z \in L$** (Pumping $y$ up or down must stay in $L$).

---

### Step-by-Step Proof Template: Proving $L = \{a^n b^{2n} \mid n > 0\}$ is NOT Regular
*(Past Exam Favorite: 2021 Spring, 2024 Spring, 2025 Spring New)*

1. **Assumption:** Assume $L$ is regular. By the Pumping Lemma, there exists a pumping length $p \ge 1$.
2. **Choose String $w$:** Choose $w = a^p b^{2p}$. Clearly $w \in L$ and $|w| = 3p \ge p$.
3. **Partition:** By Condition 2 ($|xy| \le p$), the substring $xy$ lies entirely within the leading $a$'s.
   Therefore:
   $$x = a^r, \quad y = a^k, \quad z = a^{p-r-k} b^{2p}$$
   where $k \ge 1$ (by Condition 1: $|y| \ge 1$) and $r + k \le p$.
4. **Pump Down ($i = 0$):**
   $$w' = x y^0 z = xz = a^r a^{p-r-k} b^{2p} = a^{p-k} b^{2p}$$
5. **Contradiction:** In string $w'$, the number of $a$'s is $p - k$, while the number of $b$'s is $2p$.
   For $w'$ to be in $L$, the number of $b$'s must be twice the number of $a$'s:
   $$2(p - k) = 2p - 2k \ne 2p \quad (\text{since } k \ge 1)$$
   Therefore, $x y^0 z \notin L$, which directly contradicts Condition 3!
6. **Conclusion:** The initial assumption that $L$ is regular is false. Hence, $L$ is not regular.

---

## 4. Closure & Decision Properties for Regular Sets

### Closure Properties (Regular is Closed under EVERYTHING!)
| Operation | Closed? | Construction / Justification |
| :--- | :---: | :--- |
| **Union ($L_1 \cup L_2$)** | **YES** | Add new start state with $\varepsilon$-moves to $q_{01}, q_{02}$ OR product DFA. |
| **Intersection ($L_1 \cap L_2$)** | **YES** | Product Automaton: State $(p, q)$ is final if $p \in F_1 \mathbf{\text{ AND }} q \in F_2$. |
| **Complement ($\overline{L}$)** | **YES** | Swap accepting and non-accepting states in complete DFA: $F' = Q - F$. |
| **Concatenation ($L_1 L_2$)** | **YES** | Connect final states of $M_1$ via $\varepsilon$-transitions to start state of $M_2$. |
| **Kleene Star ($L^*$)** | **YES** | Add new start/final state with $\varepsilon$-transitions to/from existing final states. |
| **Set Difference ($L_1 - L_2$)** | **YES** | $L_1 - L_2 = L_1 \cap \overline{L_2}$ (both intersection and complement are closed). |
| **Reversal ($L^R$)** | **YES** | Reverse all transitions in FA, make start state final and final states start. |

---

### Decision Algorithms for Regular Sets (ALL DECIDABLE!)
| Problem | Decidable? | Algorithm / Verification Method |
| :--- | :---: | :--- |
| **Membership ($w \in L$?)** | **YES** | Simulate string $w$ on DFA. Halts in $|w|$ steps. If final $\implies$ YES. |
| **Emptiness ($L = \emptyset$?)** | **YES** | Breadth-First / Depth-First search on DFA graph. Test if any state in $F$ is reachable from $q_0$. |
| **Finiteness (Is $L$ finite?)** | **YES** | Check for directed cycles on any path from $q_0$ that can reach an accepting state $F$. Cycle $\implies$ Infinite. |
| **Equivalence ($L_1 = L_2$?)** | **YES** | Construct symmetric difference $L_{sym} = (L_1 \cap \overline{L_2}) \cup (\overline{L_1} \cap L_2)$. Test if $L_{sym} = \emptyset$. |
| **Subset ($L_1 \subseteq L_2$?)** | **YES** | Test if $L_1 \cap \overline{L_2} = \emptyset$. |

---

## 5. Professor Tricks & Traps (From Past Exam Papers)

> [!WARNING]
> ### 1. "Neither 'aa' nor 'bb'" vs "Does not contain 'aa' or 'bb'" *(2024 Fall Q1(a))*
> - Students mistakenly build an NFA for "contains $aa$ or $bb$" and forget to invert, or get confused by substrings.
> - **Trick:** Build a DFA with 4 active states:
>   - $q_0$ (Start / Empty, or last saw nothing)
>   - $q_a$ (Last symbol was $a$)
>   - $q_b$ (Last symbol was $b$)
>   - $q_{dead}$ (Trap state reached if $aa$ or $bb$ is read)
>   - States $q_0, q_a, q_b$ are all **FINAL** states! Only $q_{dead}$ is non-accepting.

> [!WARNING]
> ### 2. The Arden's Theorem Trap *(2022 Fall & 2025 Spring)*
> - $R = Q + RP \implies R = QP^*$.
> - **Trap 1:** The self-loop must be on the **right** ($RP$). If you write $PR$, the formula fails unless commutative.
> - **Trap 2:** If $P$ contains $\varepsilon$, the solution is **not unique**. Arden's theorem strictly requires $\varepsilon \notin P$.

> [!WARNING]
> ### 3. Pumping Lemma: Choosing a Concrete String is Automatic Failure!
> - Never choose $w = a^3 b^6$ or $w = a^2 b^4$. The pumping length $p$ is an **unknown fixed constant**.
> - You **MUST** define $w$ strictly using parameter $p$ (e.g., $w = a^p b^{2p}$, $w = 0^p 1^p$).
