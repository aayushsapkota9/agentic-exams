# Chapter 1: Introduction — Quick Revision Note

> **Revision Target:** 10–15 minutes  
> **Coverage:** Sets, Relations, Functions, Proof Techniques (Contradiction, Induction, Pigeonhole, Diagonalization), Alphabets, Closures, Chomsky Hierarchy.

---

## 1. Quick Mathematical Primitives

### Sets & Power Set
- **Empty Set:** $\emptyset = \{\}$, $|\emptyset| = 0$.
- **Power Set $P(A)$:** Set of all subsets. If $|A| = n$, then $|P(A)| = 2^n$.
  - *Exam check:* If $A = \{a, b\}$, $P(A) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}$. Total elements = $2^2 = 4$.

### Relations on a Set $A$
A binary relation $R \subseteq A \times A$:
- **Reflexive:** $\forall a \in A, (a, a) \in R$
- **Symmetric:** $(a, b) \in R \implies (b, a) \in R$
- **Antisymmetric:** $(a, b) \in R \land (b, a) \in R \implies a = b$
- **Transitive:** $(a, b) \in R \land (b, c) \in R \implies (a, c) \in R$
- **Equivalence Relation:** Reflexive + Symmetric + Transitive (R + S + T).
- **Partial Order Relation (Poset):** Reflexive + Antisymmetric + Transitive (R + AS + T).

### Functions
$f: A \to B$ maps every element of domain $A$ to exactly one element of codomain $B$.
- **Injective (1-to-1):** $f(x_1) = f(x_2) \implies x_1 = x_2$.
- **Surjective (Onto):** $\text{Range}(f) = \text{Codomain } B$.
- **Bijective:** Injective + Surjective (Invertible).

---

## 2. The 4 Proof Techniques (High-Yield Summary)

| Technique | Core Mechanism | Canonical Exam Example | Relevance in TOC |
| :--- | :--- | :--- | :--- |
| **Contradiction** (*reductio ad absurdum*) | Assume $\neg P$ is TRUE. Follow valid logical deductions until a contradiction ($Q \land \neg Q$) arises. Conclude $P$ is TRUE. | Prove $\sqrt{2}$ is irrational ($a/b$ has factor 2). | Pumping Lemma proofs; Halting problem undecidability. |
| **Mathematical Induction** | 1. **Base:** Show true for $n = 1$ (or $n_0$).<br>2. **Hypothesis:** Assume true for $n = k$.<br>3. **Step:** Prove true for $n = k+1$. | $1+3+5+\dots+(2n-1) = n^2$.<br>Prove $n^2 - 3n + 4$ is always even. | Proving correctness of DFA loop invariants and grammar derivations. |
| **Pigeonhole Principle** | If $n$ pigeons occupy $m$ holes and $n > m$, $\ge 1$ hole has $\ge 2$ pigeons.<br>Generalized: $\ge \lceil n/m \rceil$. | In any group of $n$ people, at least 2 have the same number of friends. | **DFA Pumping Lemma foundation:** Any string $|w| \ge |Q|$ must repeat a state! |
| **Cantor's Diagonalization** | List all elements in a 2D table. Construct a new diagonal element by flipping each $i$-th element at $d_{ii}$. | Uncountability of real numbers $\mathbb{R} \in (0, 1)$. | Proves languages are uncountable, while TMs are countable $\implies$ undecidable languages exist. |

---

## 3. Alphabets, Strings, Closures (The Definitions You Forget)

- **Symbol:** An indivisible atomic token (e.g., $a, b, 0, 1$).
- **Alphabet ($\Sigma$):** A **finite, non-empty** set of symbols.
- **String / Word ($w$):** A finite sequence of symbols chosen from $\Sigma$.
- **Empty String ($\varepsilon$ or $\lambda$):** String of length zero: $|\varepsilon| = 0$.
- **Powers of Alphabet:**
  - $\Sigma^0 = \{\varepsilon\}$
  - $\Sigma^1 = \{a, b\}$
  - $\Sigma^2 = \{aa, ab, ba, bb\}$ (length 2)
  - $\Sigma^k$: all strings of length exactly $k$. Total strings = $|\Sigma|^k$.
- **Kleene Star ($\Sigma^*$):** Set of all possible finite strings, **including** $\varepsilon$:
  $$\Sigma^* = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \dots = \bigcup_{i=0}^{\infty} \Sigma^i$$
- **Positive Closure ($\Sigma^+$):** Set of all non-empty strings, **excluding** $\varepsilon$:
  $$\Sigma^+ = \Sigma^* - \{\varepsilon\} = \bigcup_{i=1}^{\infty} \Sigma^i$$
  $$\Sigma^* = \Sigma^+ \cup \{\varepsilon\}$$
- **Language ($L$):** Any subset of $\Sigma^*$ ($L \subseteq \Sigma^*$).

---

## 4. Chomsky Hierarchy Master Table

$$\text{Type 3 (Regular)} \subset \text{Type 2 (CFL)} \subset \text{Type 1 (CSL)} \subset \text{Type 0 (RE)}$$

| Type | Language Class | Automaton / Machine | Production Rule Form | Constraints |
| :---: | :--- | :--- | :--- | :--- |
| **Type 0** | **Recursively Enumerable (RE)** | **Turing Machine (TM)** | $\alpha \to \beta$ | $\alpha \in (V \cup T)^+$ with $\ge 1$ variable, $\beta \in (V \cup T)^*$. No length restriction! |
| **Type 1** | **Context-Sensitive (CSL)** | **Linear Bounded Automaton (LBA)** | $\alpha \to \beta$ | $|\alpha| \le |\beta|$ (Non-contracting rules, except $S \to \varepsilon$ if $S$ not on RHS). |
| **Type 2** | **Context-Free (CFL)** | **Pushdown Automaton (NPDA)** | $A \to \alpha$ | Left-hand side is **strictly one non-terminal** ($A \in V$); $\alpha \in (V \cup T)^*$. |
| **Type 3** | **Regular (RL)** | **Finite Automaton (DFA / NFA)** | $A \to aB \mid a$ (Right Linear) OR $A \to Ba \mid a$ (Left Linear) | Single non-terminal on LHS; RHS is one terminal or one terminal followed by one non-terminal. |

> **Mnemonic:** **"RE-CS-CF-REG"** (Real Computers Can Fail Regularly) $\implies$ **TM - LBA - PDA - FA**.

---

## 5. Professor Tricks & Traps (From Past Exam Questions)

> [!WARNING]
> ### 1. The Handshake / Friend Problem Trap *(2025 Fall New Course Q1(a))*
> **Question:** *"In any group of $n$ people, prove at least two have the same number of friends."*  
> **The Trap:** A person can have between $0$ and $n-1$ friends. That looks like $n$ possible values (pigeonholes) for $n$ people, which wouldn't force a collision!  
> **The Solution:** A person with $0$ friends (knows nobody) and a person with $n-1$ friends (knows everybody) **CANNOT coexist** in the same group.  
> - Case 1: If someone has $0$ friends, nobody can have $n-1$ friends $\implies$ possible degrees are $\{0, 1, \dots, n-2\}$ ($n-1$ holes).
> - Case 2: If nobody has $0$ friends, possible degrees are $\{1, 2, \dots, n-1\}$ ($n-1$ holes).  
> In both cases: $n$ people (pigeons) distributed into $n-1$ friend counts (holes) $\implies$ by Pigeonhole Principle, at least two must have the identical number of friends!

> [!WARNING]
> ### 2. Induction Base Case Oversight *(2024 Spring New & 2025 Spring New)*
> When proving $1 + 3 + 5 + \dots + (2n-1) = n^2$ or that $n^2 - 3n + 4$ is even:
> - Always explicitly write: **Base Step ($n=1$):** $(1)^2 - 3(1) + 4 = 2$, which is even.
> - **Inductive Step:** Substitute $k+1$: $(k+1)^2 - 3(k+1) + 4 = (k^2 - 3k + 4) + 2k$.  
> The first part is even by the inductive hypothesis; $2k$ is even by definition of multiples of 2. Even + Even = Even. Q.E.D.
