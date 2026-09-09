# Chapter 3: Context-Free Languages & Pushdown Automata — Quick Revision Note

> **Revision Target:** 20–25 minutes  
> **Coverage:** CFG, Ambiguity, Simplification Pipeline, Normal Forms (CNF & GNF), PDA Formalisms, Transition Function Anatomy, Pumping Lemma for CFL, Direct Comparison Tables (Regular vs CFL).

---

## 1. CFG & Derivations

### The Formal 4-Tuple
$$G = (V, T, P, S)$$
- $V$: Finite set of Variables / Non-terminals
- $T$: Finite set of Terminals ($V \cap T = \emptyset$)
- $P$: Production rules of the form $A \to \alpha$ where $A \in V, \alpha \in (V \cup T)^*$
- $S \in V$: Start symbol

### Ambiguity (Guaranteed Exam Topic!)
A grammar $G$ is **ambiguous** if there exists at least one string $w \in L(G)$ that has:
- **Two or more distinct parse trees**, OR
- **Two or more distinct Leftmost Derivations (LMD)**, OR
- **Two or more distinct Rightmost Derivations (RMD)**.

> [!TIP]
> **Exam Trap / Scoring Requirement:** Stating "the grammar is ambiguous" gets 0 marks. You **MUST** choose one single string and write out **TWO distinct derivation trees** or **TWO distinct LMD sequences** side by side!
> - *Classic Exam String for Dangling Else ($S \to iCtS \mid iCtSeS \mid a, C \to b$):* $w = \text{ibtibtaea}$.
> - *Classic Exam String for Expression Grammar ($S \to S+S \mid S*S \mid a$):* $w = a + a * a$.

---

## 2. Simplification Pipeline & Normal Forms

### Strict Order of Simplification (Do NOT change order!)
1. **Eliminate $\varepsilon$-Productions:** Find all nullable variables ($A \Rightarrow^* \varepsilon$). Replace productions containing nullable variables with combinations where they are present/absent.
2. **Eliminate Unit Productions ($A \to B$):** If $A \Rightarrow^* B$ and $B \to \alpha$, add $A \to \alpha$. Remove unit pairs.
3. **Eliminate Useless Symbols:**
   - *Phase 1 (Generating):* Find symbols that derive strings of terminals ($X \Rightarrow^* w \in T^*$). Eliminate non-generating symbols.
   - *Phase 2 (Reachable):* Find symbols reachable from start symbol $S$ ($S \Rightarrow^* \alpha X \beta$). Eliminate unreachable symbols.

---

### Chomsky Normal Form (CNF) vs Greibach Normal Form (GNF)
| Feature | Chomsky Normal Form (CNF) | Greibach Normal Form (GNF) |
| :--- | :--- | :--- |
| **Allowed Production Format** | **$A \to BC$** OR **$A \to a$**<br>*(Strictly 2 non-terminals OR 1 terminal)* | **$A \to a\alpha$** where $a \in T, \alpha \in V^*$<br>*(Strictly 1 terminal followed by $\ge 0$ variables)* |
| **Derivation Length for $|w| = n$** | Exactly **$2n - 1$ steps** | Exactly **$n$ steps** |
| **Parse Tree Structure** | Strictly binary tree | Flat, branched structure |
| **Primary Use in Theory** | **CYK Algorithm** (Membership decision) & CFL Pumping Lemma proof | Direct equivalence to PDA single-state conversion |

---

## 3. Pushdown Automata (PDA) Anatomy

### Formal 7-Tuple
$$M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$$
- $Q$: Finite set of states
- $\Sigma$: Input alphabet
- $\Gamma$: Stack alphabet
- $q_0 \in Q$: Start state
- $Z_0 \in \Gamma$: Initial bottom-of-stack marker
- $F \subseteq Q$: Set of accepting states
- **$\delta$:** Transition function:
  $$\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \to \mathcal{P}(Q \times \Gamma^*)$$

---

### Understanding the Transition Function $\delta(q, a, X) = (p, \gamma)$
```
  Inputs: (Current State, Input Symbol, Current Stack Top)
  Output: (Next State, String that REPLACES the Stack Top)
```

$$\delta(\underbrace{q}_{\text{current state}}, \underbrace{a}_{\text{input or } \varepsilon}, \underbrace{X}_{\text{top of stack}}) = \{(\underbrace{p}_{\text{new state}}, \underbrace{\gamma}_{\text{stack replacement}})\}$$

- **POP Operation:** $\gamma = \varepsilon$  
  *(The top symbol $X$ is erased; the item below it becomes the new top).*  
  *Example:* $\delta(q_1, b, a) = (q_1, \varepsilon)$
- **NO-OP / Read-Only Operation:** $\gamma = X$  
  *(The top symbol $X$ is replaced by itself; stack remains unchanged).*  
  *Example:* $\delta(q_0, \varepsilon, Z_0) = (q_f, Z_0)$
- **PUSH Operation:** $\gamma = YX$  
  *(Leftmost character is new top! $Y$ is pushed on top of existing $X$).*  
  *Example:* $\delta(q_0, a, Z_0) = (q_0, aZ_0)$
- **DOUBLE-PUSH (e.g. for $a^n b^{2n}$):** $\gamma = aaX$  
  *(Pushes two $a$'s for a single input $a$).*  
  *Example:* $\delta(q_0, a, Z_0) = (q_0, aaZ_0)$

---

### Deterministic PDA (DPDA) vs Non-Deterministic PDA (NPDA)
- **DPDA:** At most one transition is possible from any configuration. If $\delta(q, \varepsilon, X)$ is non-empty, then $\delta(q, a, X)$ must be empty for all $a \in \Sigma$.
- **Crucial Fact:** $\mathcal{L}(\text{DPDA}) \subsetneq \mathcal{L}(\text{NPDA}) = \text{CFL}$.  
  *(Unlike Finite Automata, non-determinism strictly increases the power of pushdown automata!)*
  - $L = \{w c w^R\}$ has a center marker $c \implies$ **Deterministic (DPDA)**.
  - $L = \{w w^R\}$ has NO center marker $\implies$ **Non-Deterministic (NPDA)** (must guess the midpoint via an $\varepsilon$-move).

---

## 4. Pumping Lemma for Context-Free Languages (CFL)

### Formal Statement (Standard $p$ notation)
If $L$ is a context-free language, there exists a constant $p \ge 1$ (the pumping length) such that any string $w \in L$ with $|w| \ge p$ can be written as:
$$w = uvwxy$$
satisfying the **Three Mandatory Conditions:**
1. **$|vx| \ge 1$** (At least one of the pumpable segments $v$ or $x$ is non-empty).
2. **$|vwx| \le p$** (The middle section containing both pumps is at most length $p$).
3. **$\forall i \ge 0, \quad u v^i w x^i y \in L$** (Pumping $v$ and $x$ synchronously maintains membership).

---

### Proof Template: Proving $L = \{a^n b^n c^n \mid n \ge 1\}$ is NOT Context-Free
1. **Assume $L$ is CFL.** Let $p$ be its pumping length.
2. **Choose String:** $w = a^p b^p c^p \in L$. Length $|w| = 3p \ge p$.
3. **Apply Condition 2 ($|vwx| \le p$):** Because the span of $vwx$ cannot exceed $p$, the substring $vwx$ **cannot contain occurrences of all three symbols $a, b,$ and $c$**. It can at most contain symbols from two adjacent groups (either $a$'s and $b$'s, or $b$'s and $c$'s).
4. **Pump Down ($i = 0$):** In $w' = u v^0 w x^0 y = uwy$, the count of at most two letters is decreased, while the count of the third letter remains unchanged ($= p$).
5. **Contradiction:** $w'$ has unequal numbers of $a$'s, $b$'s, and $c$'s $\implies w' \notin L$.
6. **Conclusion:** $L$ is not a Context-Free Language.

---

## 5. Master Comparison Tables (Chapter 2 vs Chapter 3)

### Table 1: Pumping Lemma Comparison
| Feature | Regular Languages (Chapter 2) | Context-Free Languages (Chapter 3) |
| :--- | :--- | :--- |
| **Partition** | **$w = xyz$** (3 pieces, 1 pump: $y$) | **$w = uvwxy$** (5 pieces, 2 pumps: $v$ and $x$) |
| **Non-emptiness** | $|y| \ge 1$ | $|vx| \ge 1$ |
| **Length Bound** | **$|xy| \le p$** (bounded at the *front*) | **$|vwx| \le p$** (bounded in the *middle*) |
| **Pumping Condition** | $\forall i \ge 0, \quad xy^i z \in L$ | $\forall i \ge 0, \quad uv^i wx^i y \in L$ |
| **Underlying Origin** | Pigeonhole principle on **DFA states** | Pigeonhole principle on **Parse Tree variables** |

---

### Table 2: Closure Properties Comparison (The Big Traps!)
| Operation | Regular Sets | Context-Free Languages (CFL) | Reason / Counterexample for CFL Failure |
| :--- | :---: | :---: | :--- |
| **Union ($L_1 \cup L_2$)** | **YES** | **YES** | Rule: $S \to S_1 \mid S_2$ |
| **Concatenation ($L_1 L_2$)** | **YES** | **YES** | Rule: $S \to S_1 S_2$ |
| **Kleene Star ($L^*$)** | **YES** | **YES** | Rule: $S \to S S_1 \mid \varepsilon$ |
| **Intersection ($L_1 \cap L_2$)** | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> | **Stack cannot count 2 independent balances!**<br>$L_1 = \{a^n b^n c^m\}, L_2 = \{a^m b^n c^n\} \implies L_1 \cap L_2 = \{a^n b^n c^n\} \notin \text{CFL}$. |
| **Complement ($\overline{L}$)** | **YES** | <span style="color:red; font-weight:bold;">NO ❌</span> | By De Morgan's: $L_1 \cap L_2 = \overline{\overline{L_1} \cup \overline{L_2}}$. If complement were closed, intersection would be closed too! |
| **Intersection with Regular** | **YES** | **YES** | Product construction of PDA stack $\times$ DFA finite states. |
| **Reversal ($L^R$)** | **YES** | **YES** | Reverse the RHS of all production rules. |

> **Mnemonic for CFL Closure:** *"CFLs are selfish: they can balance ONE thing, but FAIL at sharing (No Intersection, No Complement)."*

---

### Table 3: Decision Algorithms Comparison
| Decision Problem | Regular Languages | Context-Free Languages (CFL) | Algorithm / Status for CFL |
| :--- | :---: | :---: | :--- |
| **Membership ($w \in L$?)** | **Decidable** | **Decidable** | **CYK Algorithm** (runs in $O(n^3)$ time on CNF). |
| **Emptiness ($L = \emptyset$?)** | **Decidable** | **Decidable** | Generating symbols check: Is start symbol $S$ generating? |
| **Finiteness (Is $L$ finite?)** | **Decidable** | **Decidable** | Check for directed cycles among useful variables in CNF graph. |
| **Equivalence ($L_1 = L_2$?)** | **Decidable** | <span style="color:red; font-weight:bold;">UNDECIDABLE ❌</span> | No algorithm exists; cannot compare infinite derivation structures. |
| **Intersection-Emptiness ($L_1 \cap L_2 = \emptyset$?)**| **Decidable** | <span style="color:red; font-weight:bold;">UNDECIDABLE ❌</span> | Reduces directly to Post Correspondence Problem (PCP). |
| **Universality ($L = \Sigma^*$?)** | **Decidable** | <span style="color:red; font-weight:bold;">UNDECIDABLE ❌</span> | Undecidable via valid TM computation histories. |
| **Ambiguity (Is CFG ambiguous?)** | **N/A** | <span style="color:red; font-weight:bold;">UNDECIDABLE ❌</span> | Cannot verify all infinite derivation paths. |

> **Mnemonic for CFL Decision:** **"Only MEF is Decidable"** $\implies$ **M**embership, **E**mptiness, **F**initeness. Everything else is **UNDECIDABLE**!
