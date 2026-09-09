# Chapter 5: Undecidability — Quick Revision Note

> **Revision Target:** 15–20 minutes  
> **Coverage:** Church-Turing Thesis, Halting Problem Proof, Universal Turing Machine (UTM), Rice's Theorem, Post Correspondence Problem (PCP), Recursive (Decidable) vs Recursively Enumerable (RE) Languages, Post's Theorem.

---

## 1. The Church-Turing Thesis

### The Core Statement
> *"Any algorithmic process or effective procedure that can be carried out by a human mathematician or a mechanical computer can be carried out by a Turing Machine."*

### Why Is It a "Thesis" and NOT a "Theorem"? (Crucial Exam Question!)
| Concept | Definition |
| :--- | :--- |
| **Theorem** | A formal proposition derived strictly from mathematical axioms using formal logical proofs (e.g., Pythagorean theorem, Pumping Lemma). |
| **Thesis** | A working scientific hypothesis connecting an **informal, intuitive concept** with a **formal, mathematical model**. |

- **The Reason:** The human notion of an *"effective procedure"* or *"algorithm"* is an intuitive, informal concept without a prior mathematical definition.
- You **cannot mathematically prove** that an informal concept is identical to a formal mathematical object (a Turing machine).
- Hence, it remains a **Thesis** (universally accepted because every computing model invented—Lambda Calculus, Post Machines, Cellular Automata, Quantum Computers—has proven equivalent in computability to a Turing Machine).

---

## 2. Decidable (Recursive) vs Recognizable (RE) Languages

```
+-------------------------------------------------------------+
| ALL LANGUAGES OVER Σ* (Uncountable: 2^|Σ*|)                |
|  +-------------------------------------------------------+  |
|  | RECURSIVELY ENUMERABLE (RE) / Recognizable            |  |
|  |  +-------------------------------------------------+  |  |
|  |  | RECURSIVE (REC) / Decidable                     |  |  |
|  |  | (TM halts on ALL inputs: Accept or Reject)      |  |  |
|  |  +-------------------------------------------------+  |  |
|  |  (TM halts & accepts if w in L; LOOPS if w not in L)|  |
|  +-------------------------------------------------------+  |
|  (Non-RE Languages: No TM can even recognize them, e.g. ~A_TM)
+-------------------------------------------------------------+
```

### Comprehensive Comparison Table
| Feature | Recursive Language (REC / Decidable) | Recursively Enumerable Language (RE / Recognizable) |
| :--- | :--- | :--- |
| **Machine Model** | **Turing Decider** (Halts on **ALL** inputs). | **Turing Recognizer** (May **loop forever**). |
| **If $w \in L$** | Machine halts in state $q_{accept}$. | Machine halts in state $q_{accept}$. |
| **If $w \notin L$** | Machine halts in state $q_{reject}$. | Machine halts in $q_{reject}$ **OR LOOPS FOREVER**. |
| **Chomsky Type** | Intermediate between Type 1 and Type 0. | Strictly **Type 0** (Unrestricted Grammar). |
| **Complement ($\overline{L}$)**| **Always Recursive** (swap accept/reject). | **NOT closed!** If $L$ is RE but not REC, $\overline{L}$ is Non-RE. |

---

### Post's Complementarity Theorem
$$L \text{ is Recursive (Decidable)} \iff L \in \text{RE} \quad \text{AND} \quad \overline{L} \in \text{RE}$$
- *Proof Intuition:* Run the recognizer for $L$ ($M_1$) and the recognizer for $\overline{L}$ ($M_2$) in parallel on two tracks (or alternating steps). For any input $w$, exactly one of them MUST halt and accept! When it does, you give the definitive YES or NO. Thus, $L$ is decidable.

---

### Proof Template: Intersection of Two Recursive Languages is Recursive *(2025 Spring New Q5(b))*
1. Let $L_1$ and $L_2$ be two recursive languages.
2. By definition, there exist Turing deciders $M_1$ and $M_2$ that decide $L_1$ and $L_2$ respectively (both halt on all inputs).
3. **Construct Decider $M'$ for $L_1 \cap L_2$:**
   - Input: string $w$.
   - Step 1: Run $M_1$ on input $w$. Since $M_1$ is a decider, it halts in finite time. If $M_1$ rejects, $M'$ **rejects and halts**.
   - Step 2: If $M_1$ accepts, run $M_2$ on input $w$. Since $M_2$ is a decider, it halts in finite time.
   - Step 3: If $M_2$ accepts, $M'$ **accepts and halts**; if $M_2$ rejects, $M'$ **rejects and halts**.
4. Since $M'$ halts on every input and accepts $w$ if and only if $w \in L_1$ and $w \in L_2$, $M'$ is a decider for $L_1 \cap L_2$.
5. Therefore, the intersection of two recursive languages is also **recursive**.

---

## 3. The Halting Problem ($H_{TM}$) & Undecidability Proof

### The Problem
$$H_{TM} = \{ \langle M, w \rangle \mid M \text{ is a TM that halts on input } w \}$$
Can we build a single universal algorithm $H$ that takes any program $M$ and input $w$, and tells us whether $M$ will halt on $w$ without getting stuck in an infinite loop?

### The Proof by Contradiction (Diagonalization)
1. **Assume a Decider $H$ exists:**
   $$H(\langle M, w \rangle) = \begin{cases} \text{Accept} & \text{if } M \text{ halts on } w \\ \text{Reject} & \text{if } M \text{ loops forever on } w \end{cases}$$
2. **Construct an Adversary Machine $D$:**
   $D$ takes the encoding of a Turing Machine $\langle M \rangle$ as input:
   - $D$ calls $H$ with input $\langle M, \langle M \rangle \rangle$ (feeding machine $M$ its own code as input).
   - If $H$ returns "Accept" ($M$ halts), **$D$ deliberately enters an infinite loop**.
   - If $H$ returns "Reject" ($M$ loops), **$D$ halts immediately**.
3. **Feed $D$ to Itself (Diagonalization Step):**
   What happens when we run $D$ with its own description $\langle D \rangle$?
   $$D(\langle D \rangle) \text{ halts} \iff H(\langle D, \langle D \rangle \rangle) \text{ rejects} \iff D(\langle D \rangle) \text{ loops forever!}$$
4. **Contradiction:** $D(\langle D \rangle)$ halts if and only if it loops forever. This is a logical impossibility.
5. **Conclusion:** Decider $H$ cannot exist. The Halting Problem is **Undecidable**.

---

## 4. Universal Turing Machine (UTM)

- **Definition:** A Turing Machine $U$ capable of simulating **any** arbitrary Turing Machine $M$ on any arbitrary input string $w$.
- **Input on Tape:** $\langle M, w \rangle$ (a standardized binary encoding of $M$'s states, alphabet, and $\delta$ transitions, concatenated with input $w$).
- **Standard 3-Tape Simulation Architecture:**
  - **Tape 1 (Program Tape):** Holds the encoded description of the target machine $\langle M \rangle$.
  - **Tape 2 (Work/Data Tape):** Holds the contents of $M$'s tape with input $w$.
  - **Tape 3 (State Register):** Stores the current state of $M$ (initialized to $q_0$).
- **Simulation Loop:**
  1. Read current state from Tape 3 and scanned symbol from Tape 2.
  2. Search Tape 1 for matching transition $\delta(q, X) = (p, Y, D)$.
  3. Overwrite symbol on Tape 2 with $Y$, update state on Tape 3 to $p$, move Tape 2 head in direction $D$.
  4. If $p \in F$, halt and accept!

---

## 5. Other Undecidable Problems & Rice's Theorem

### Rice's Theorem
> *"Any non-trivial semantic property of the language of a Turing Machine is UNDECIDABLE."*
- **Semantic Property:** A property about the *language* recognized by the machine ($L(M)$), not the syntax of its code.
- **Non-Trivial:** The property is true for some TMs and false for others.
- **Direct Consequence:** Under Rice's Theorem, all of the following questions are **automatically undecidable**:
  - Is $L(M)$ empty? ($L(M) = \emptyset$?)
  - Is $L(M)$ finite?
  - Is $L(M)$ regular?
  - Is $L(M)$ context-free?
  - Does $L(M)$ contain the string "00"?

---

### Post Correspondence Problem (PCP)
- **Problem Statement:** Given a finite set of domino pairs $\left\{ \left[\frac{t_1}{b_1}\right], \left[\frac{t_2}{b_2}\right], \dots, \left[\frac{t_k}{b_k}\right] \right\}$, does there exist a sequence of indices $i_1, i_2, \dots, i_m$ such that:
  $$t_{i_1} t_{i_2} \dots t_{i_m} = b_{i_1} b_{i_2} \dots b_{i_m}$$
- **Status:** **Undecidable** for $|\Sigma| \ge 2$.
- **Role in TOC:** Used as the master reduction tool to prove that **CFG Ambiguity** and **CFL Intersection-Emptiness ($L_1 \cap L_2 = \emptyset$)** are undecidable without needing to construct complex Turing machines!

---

## 6. Professor Tricks & Traps

> [!WARNING]
> ### 1. Complement of an RE Language
> - If $L$ is Recursive $\implies \overline{L}$ is always Recursive.
> - If $L$ is RE but **NOT** Recursive (e.g. $A_{TM}$, $H_{TM}$) $\implies \overline{L}$ is strictly **NON-RE**! (If $\overline{L}$ were RE, by Post's theorem $L$ would become Recursive, a contradiction).

> [!WARNING]
> ### 2. Decidable vs Recognizable Wording
> - When an exam asks: *"Show that $L$ is Turing computable / decidable"*, you must prove that the machine **always halts** on every input.
> - If you only show it halts on accepted strings, you have only proven it is **Recursively Enumerable**, losing half the marks!
