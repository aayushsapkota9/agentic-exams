import os

md_dir = "toc/past-qns/md"
os.makedirs(md_dir, exist_ok=True)

# 3. TOC_2019_PU_Spring.md
with open(os.path.join(md_dir, "TOC_2019_PU_Spring.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2019
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Find the regular expression for the given Finite Automata. Convert the NDFA to equivalent DFA. **[8]**

b) Define ambiguous grammar. Explain with an example. Remove the $\\varepsilon$-productions (Null productions) from the following grammar:  
$S \\to ABAC$  
$A \\to aA \\mid \\varepsilon$  
$B \\to bB \\mid \\varepsilon$  
$C \\to c$ **[7]**

---

#### 2.
a) Using the principles of Context-Free Grammar, capture the expression $(x_1 + x_2) * (x_3 * x_2 + x_1)$ and draw its parse tree. **[8]**

b) State the Pumping Lemma for Context-Free Languages. Prove that the language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$ is not context-free. **[7]**

---

#### 3.
a) What is instantaneous description of a PDA? Design a PDA which accepts the language $L = \\{w \\in \\{0, 1\\}^* \\mid w \\text{ has equal number of 0s and 1s}\\}$. **[8]**

b) Write about the closure properties of context-free languages. **[7]**

---

#### 4.
a) How can you represent a Turing Machine? Show that the function $f(n) = n + 1$ is Turing computable. **[8]**

b) Design a Turing Machine as a right shift machine which transforms $\#w\#$ into $\#\#w\#$ over alphabet $\\Sigma = \\{a, b, \#\\}$. **[7]**

---

#### 5.
a) What are recursive and recursively enumerable languages? Show that the union of two recursive languages is also recursive. **[8]**

b) Write about Church-Turing thesis and universal Turing machine. **[7]**

---

#### 6.
a) How does computability differ from complexity theory? Describe time and space complexity. **[8]**

b) Explain class P, NP, and NP-complete problems with examples. **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Undecidability  
b) Universal Turing Machines  
c) Relations and Functions  
""")

# 4. TOC_2020_PU_Fall.md
with open(os.path.join(md_dir, "TOC_2020_PU_Fall.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2020
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) What is a set? Show the different types of set operations with examples. **[7]**

b) Explain finite automata along with its uses and applications. Construct a DFA that recognizes language $L$ accepting the set of strings containing exactly four 1's over alphabet $\\Sigma = \\{0, 1\\}$ and test your design with a valid string. **[8]**

---

#### 2.
a) Find the regular expression from NFA $M = (K, \\Sigma, \\delta, s, F)$, where $K = \\{q_0, q_1, q_2, q_3, q_4, q_5\\}$, $\\Sigma = \\{a, b\\}$, $s = q_0$, $F = \\{q_5\\}$. **[8]**

b) For the grammar given by $G = (V, \\Sigma, R, S)$ where $V = \\{S, X\\}$, $\\Sigma = \\{a, b, c\\}$, design a Pushdown Automaton (PDA). **[7]**

---

#### 3.
a) What is CFG? Design a CFG for language $L = \\{w c w^R \\mid w \\in \\{a, b\\}^*\\}$. Test the grammar for derivation of $baacaab$ and draw the equivalent parse tree. **[8]**

b) What is CNF? Convert following CFG into CNF:  
$S \\to aAB \\mid AaB \\mid B$  
$A \\to aA \\mid \\varepsilon$  
$B \\to ab \\mid bA$ **[7]**

---

#### 4.
a) In what aspects is a PDA stronger than a finite automaton? State the closure properties of context-free grammar. **[7]**

b) State the Pumping Lemma for Context-Free Languages. Prove that $L = \\{0^n 1^n 2^n \\mid n \\ge 0\\}$ is not context-free. **[8]**

---

#### 5.
a) Design a Turing Machine that transforms $\#w\#$ to $\#\#w\#$ where $\#$ represents blank symbol and $w \\in \\{a, b\\}^*$. **[8]**

b) What is a configuration of a Turing Machine? Show that $f(x) = x + 1$ is Turing computable. **[7]**

---

#### 6.
a) Write about Church-Turing thesis and Universal Turing Machine. **[8]**

b) Explain in brief Class P and NP-complete problems with suitable examples. **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Relations and Functions  
b) K-tape Turing Machine  
c) Cartesian Product, Relation and Function  
""")

# 5. TOC_2021_PU_Fall.md
with open(os.path.join(md_dir, "TOC_2021_PU_Fall.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2021
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Differentiate between DFA and NFA. Design a DFA that accepts the set of strings over $\\Sigma = \\{0, 1\\}$ containing neither "00" nor "11" as substring. Test your design for $101001$. **[8]**

b) Construct a DFA equivalent to the given NFA. **[7]**

---

#### 2.
a) Illustrate the simplification algorithm for a Context-Free Grammar. Convert the grammar $S \\to abSb \\mid a \\mid aAb$, $A \\to bS \\mid aAAb$ into Chomsky Normal Form (CNF). **[8]**

b) For the grammar $S \\to aSb \\mid a$, show the leftmost derivation and rightmost derivation trees for input string $aaabbb$. **[7]**

---

#### 3.
a) Define PDA with a block diagram. Design a PDA which accepts the language $L = \\{a^n b^{2n} \\mid n \\ge 1\\}$ and test for strings $aabbbb$ and $aab$. **[8]**

b) Prove that each context-free language is accepted by some pushdown automaton. **[7]**

---

#### 4.
a) What is pumping lemma for CFL? Show that language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$ is not a CFL using pumping lemma for CFL. **[8]**

b) Design a deterministic Turing Machine to accept the language $L = \\{0^n 1^n 2^n \\mid n \\ge 0\\}$. **[7]**

---

#### 5.
a) How can you represent a Turing Machine for computing a function? Show that the function $f(n) = n + 1$ is Turing computable. **[8]**

b) Construct an $\\varepsilon$-NFA for the Regular Expression $(0+1)^*(0+1)$. **[7]**

---

#### 6.
a) When are problems said to be NP-Complete? Illustrate with suitable examples. **[8]**

b) Write about Church-Turing thesis and Universal Turing Machine. **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Knapsack Problem / NP-complete problems  
b) Universal Turing Machine  
c) Languages and Alphabets  
""")

# 6. TOC_2021_PU_Spring.md
with open(os.path.join(md_dir, "TOC_2021_PU_Spring.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2021
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Explain finite automata along with its uses and applications. Construct a DFA that recognizes language accepting the set of strings that neither has "aa" nor "bb" as substring over $\\Sigma = \\{a, b\\}$ and test your design with a valid string. **[8]**

b) Convert a DFA equivalent to NFA as shown in figure. **[7]**

---

#### 2.
a) Define Pumping Lemma. Show that $L = \\{a^n b^{2n} \\mid n \\ge 1\\}$ is not regular using pumping lemma for regular language. **[8]**

b) Define Derivation Tree. When is a grammar called ambiguous? Explain with an example. **[7]**

---

#### 3.
a) Reduce the following CFG to CNF:  
$A \\to B ad \\mid bSX \\mid a$  
$X \\to SB \\mid aBx \\mid ad \\mid B$ **[8]**

b) Define PDA. Design a PDA which accepts the set of all palindromes over alphabet $\\Sigma = \\{0, 1\\}$. **[7]**

---

#### 4.
a) Design a PDA for the grammar $G = (V, \\Sigma, R, S)$ where $V = \\{S\\}$, $\\Sigma = \\{a, b, c\\}$ and $R = \\{S \\to aSa \\mid bSb \\mid c\\}$. **[7]**

b) Define a Turing Machine. Design a TM that accepts the language $L = \\{1^n 2^n 3^n \\mid n \\ge 0\\}$. **[8]**

---

#### 5.
a) Design a TM which computes the function $f(m) = m + 1$ for each $m \\in \\mathbb{N}$. **[8]**

b) Briefly explain about properties of CFL. Describe briefly about recursive and recursively enumerable language. **[7]**

---

#### 6.
a) Describe Church's Hypothesis. Also illustrate your understanding of Halting Problem. **[8]**

b) Explain computational complexity. What are Space and Time complexity? **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Multi-tape Turing Machine  
b) Integer bin-packing problems  
c) Regular expressions  
""")

# 7. TOC_2022_PU_Fall.md
with open(os.path.join(md_dir, "TOC_2022_PU_Fall.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2022
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) What is a function? Explain different types of functions with examples. **[8]**

b) Define DFA. The C programming language has three keywords `while`, `for`, and `do` that are used to write loop statements. Construct a Deterministic Finite Automaton (DFA) that recognizes these three loop keywords. **[7]**

---

#### 2.
a) Construct a DFA equivalent to NFA as shown in figure. **[8]**

b) Explain Arden's Theorem. Find the regular expression for the given Finite State Automaton using Arden's method. **[7]**

---

#### 3.
a) What is Context-Free Grammar? Design a CFG for language $L = \\{a^m b^n \\mid m \\ge 1, n \\ge 1\\}$. Test the grammar for derivation of $aaabbb$ and draw equivalent parse tree. **[8]**

b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**

---

#### 4.
a) Design a PDA which accepts the language $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ has equal number of a's and b's}\\}$. Consider $Z_0$ as the bottom of the stack. Show verification for an accepted string. **[8]**

b) "For every CFG there is an equivalent Pushdown Automaton". Justify this statement with an example. **[7]**

---

#### 5.
a) Define Turing Machine. Design a Turing Machine to decide whether or not any input string $w \\in \\{a, b\\}^*$ is a palindrome. Test your design for strings $ababa$ and $bbaab$. **[8]**

b) Turing machines are functionally stronger than Pushdown Automata. Justify. Also show TM are function computable. **[7]**

---

#### 6.
a) State Church-Turing Thesis. Compare and contrast the relationship between Recursive and Recursively Enumerable Language. **[8]**

b) Explain Computational Complexity Theory. What are P, NP and NP-Complete problems? Explain with examples. **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Importance and scope of Theory of Computation  
b) Decision algorithm of CFLs  
c) The halting problem  
""")

# 8. TOC_2023_PU_Spring.md
with open(os.path.join(md_dir, "TOC_2023_PU_Spring.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2023
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Define alphabet, string, and language with examples. **[5]**

b) Design a DFA for the language $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ ends with } bb\\}$. **[5]**

c) Define an ambiguous grammar. Check if below grammar is ambiguous:  
$S \\to aB \\mid ab$  
$A \\to aAB \\mid a$  
$B \\to ABb \\mid b$ **[5]**

---

#### 2.
a) What is the significance of minimizing a DFA? Minimize the given DFA and analyze your finding. **[8]**

b) "We can convert Finite Automata to Regular Expression and also Regular Expression to Finite Automata". Justify this statement with suitable examples. **[7]**

---

#### 3.
a) Can production rules realize Context-Free Grammar for the language given by $L = \\{a^m b^n \\mid m > 0 \\text{ and } n > 0\\}$? How? **[7]**

b) Explain the process of simplifying Context-Free Grammar. Simplify the following CFG $G = (V, \\Sigma, R, S)$:  
$V = \\{S, A, B\\}$, $\\Sigma = \\{a, b\\}$  
$R = \\{S \\to aAB \\mid AaB \\mid B, B \\to ab \\mid bA\\}$ **[8]**

---

#### 4.
a) Explain the concept of "epsilon transitions" in a Pushdown Automaton. How do they affect the computation? **[7]**

b) Define PDA with block diagram. Design a PDA which accepts the language $L = \\{a^n b^n \\mid n \\ge 1\\}$ and test for strings $aabb$ and $aab$. **[8]**

---

#### 5.
a) Describe the concept of an "accepting state" and a "halting state" in a Turing Machine. Show that the function $f(n) = n + 1$ is Turing computable. **[8]**

b) Define Turing Machine. Construct a Turing Machine that accepts the language of strings over $\\{a, b\\}$ with each string of even length. Also show it accepts string $abab$. **[7]**

---

#### 6.
a) Define the concept of "Recursive Functions" and explain their significance in the theory of computation. **[8]**

b) Is $P = NP$? Explain. Also differentiate between Tractable and Intractable problems with examples. **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Pumping lemma for CFL  
b) Universal Turing Machine  
c) The Halting problem  
""")

# 9. TOC_2024_PU_Fall.md
with open(os.path.join(md_dir, "TOC_2024_PU_Fall.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2024
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Define Finite State Automata. Construct a DFA to recognize a language $L$ that accepts the set of strings which contains neither "ba" nor "ab" as substring over $\\Sigma = \\{a, b\\}$ and test your design with a valid string. **[8]**

b) What are Regular Expressions (RE)? Construct an NFA for the RE $(a+b)^* a b c (a+b)^*$. **[7]**

---

#### 2.
a) Convert the following NFA to its equivalent DFA. **[8]**

b) What is an empty language? Convert the following context-free grammar (CFG) into its equivalent Chomsky's Normal Form (CNF):  
$S \\to a \\mid aA \\mid B$  
$B \\to Aa \\mid b$ **[7]**

---

#### 3.
a) What is a Parse tree (Derivation tree)? How is it useful to show the grammar is ambiguous? Give an example. **[8]**

b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**

---

#### 4.
a) Design a Pushdown Automaton (PDA) for language $L = \\{w w^R \\mid w \\in \\{a, b\\}^*\\}$ where $w^R$ represents reverse of $w$, and test for strings $bbaabb$ and $ababa$. **[8]**

b) "For every CFG there is an equivalent Pushdown Automata". Justify this statement with an example. **[7]**

---

#### 5.
a) Design a Turing Machine for computing function $f(x, y) = x + y$ and show your validation for $x = 2$ and $y = 4$. **[8]**

b) Briefly explain the idea of designing the Turing Machine that accepts the language $L = \\{a^n b^n \\mid n > 0\\}$. Show the state transition diagram. **[7]**

---

#### 6.
a) What is computational complexity of a problem? Explain P, NP and NP-Complete problems. **[8]**

b) Explain the Halting Paradox in Turing Machine. What are Space and Time complexity? **[7]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Power set and Kleene Closure  
b) Recursive and Recursively Enumerable Language  
c) Universal Turing Machine  
""")

# 10. TOC_2024_PU_Spring.md
with open(os.path.join(md_dir, "TOC_2024_PU_Spring.md"), "w") as f:
    f.write("""# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2024
**Programme:** B.E.  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) What is a function? Explain its types with examples. **[7]**

b) Differentiate between DFA and NFA. Design a DFA that accepts the language given by $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ contains neither } \'aa\' \\text{ nor } \'bb\' \\text{ as substring}\\}$. Hence test your design for $abaabb$. **[8]**

---

#### 2.
a) Convert the given NFA to its equivalent DFA. **[7]**

b) Define Pumping Lemma for regular language. Show that $L = \\{a^n b^{2n} \\mid n > 1\\}$ is not regular using pumping lemma for regular language. **[8]**

---

#### 3.
a) What is CFG? Design a CFG for language $L = \\{a^m b^n \\mid m \\ge 1, n \\ge 1\\}$. Test the grammar for derivation of $aaaabbb$ and also draw equivalent parse tree. **[8]**

b) Convert the following grammar into Chomsky Normal Form (CNF):  
$S \\to bAD$  
$A \\to aB \\mid bAB$  
$B \\to b$  
$D \\to \\varepsilon \\text{ (Null)}$ **[7]**

---

#### 4.
a) Define PDA with block diagram. Design a PDA which accepts the language $L = \\{a^n \\mid n \\ge 1\\}$ and test for strings $aaaaaaaa$ and $aaaaaa$. **[8]**

b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**

---

#### 5.
a) Define Turing Machine. Design a Turing Machine that accepts the language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$. **[8]**

b) How does a Turing Machine compute a function of natural numbers? Describe. Show that the function $f(n) = n + 2$ is computable. **[7]**

---

#### 6.
a) State the halting theorem and give the outline of its proof. **[7]**

b) What are P, NP and NP-Complete problems? Explain with examples. **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Simplification of CFG  
b) Recursive and Recursively Enumerable Language  
c) Decision algorithm for CFL  
""")

print("Successfully wrote all 10 reconstructed exam files under toc/past-qns/md/")
