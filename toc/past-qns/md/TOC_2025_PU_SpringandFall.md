# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2025
**Programme:** BE  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Define the terms alphabet, string, kleene closure, positive closure, language and regular expression with examples. **[7]**

b) Define DFA and NFA. Design a DFA that accepts the language given by $L=\{w: \{a,b\}^* : \text{the number of 'a' in w is multiple of 3}\}$. **[8]**

---

#### 2.
a) Convert the following NFA to its equivalent DFA. **[7]**
*(Refer to the NFA diagram with states $q_0, q_1, q_2, q_3$ in the original paper)*

b) Find Regular Expression of following Finite Automata using Arden's Theorem. **[8]**
*(Refer to the FA diagram with states A, B, C, D in the original paper)*

---

#### 3.
a) When is a grammar is ambiguous? For given grammar rule:  
$S \to aSa$  
$S \to bSb$  
$S \to c$  
Check Ambiguity for it. **[7]**

b) Define CNF. Convert the following grammar into CNF.  
$S \to ASB \mid \varepsilon, A \to aAS \mid a, B \to AB \mid b \mid \varepsilon$ **[8]**

---

#### 4.
a) Define PDA with block diagram? Design a PDA which accepts the language $L=\{w \in \{0,1\}^* : w \text{ has equal number of 0's and 1's}\}$. **[7]**

b) State pumping lemma for context free language. Prove that language $L = \{WW \mid W \in \{0, 1\}\}$ is not Context free. **[8]**

---

#### 5.
a) Design a Turing machine that accepts the language $L=\{a^nb^nc^n:n \ge 0\}$. **[7]**

b) How can multi-tape turing machine be simulated through single tape turing machine? Explain with an example. **[8]**
**OR**
Explain concept of having storage capability in state of Turing machine with suitable example.

---

#### 6.
a) What is 'Algorithm' according to Church Turing thesis? Why is it called thesis and not a theorem? Explain. **[7]**

b) Explain P and NP class problems with suitable example. How do they relate to NP complete problems? **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Simplification of CFG  
b) The halting problem  
c) Turing Machine Computing a function  

<br><br>

# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2025
**Programme:** BE  
**Course:** Theory of Computation (New)  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Explain Mathematical Induction. Using mathematical induction prove that sum of first n positive odd numbers $1+3+5+.......+2n-1 = n^2$. **[7]**

b) Differentiate Between DFA and NFA? Design a DFA that accepts the language given by $L=\{w \in \{0,1\}^* : w \text{ contains '00' or '11' as substring }\}$. Hence test your design for 101001 and 0101010. **[8]**

---

#### 2.
a) Minimize the following DFA (Draw initial diagram first). Specify performed operations in each step. **[7]**
| $\delta/\Sigma$ | 0 | 1 |
|---|---|---|
| $\to$Q0 | Q1 | Q2 |
| *Q1 | Q1 | Q3 |
| *Q2 | Q2 | Q2 |
| *Q3 | Q5 | Q2 |
| *Q4 | Q4 | Q2 |
| *Q5 | Q4 | Q2 |
| Q6 | Q5 | Q6 |
| Q7 | Q5 | Q6 |
*(Note: $\to$ for start state, * for final state)*

b) State Pumping Lemma for regular set. Use pumping lemma to prove that the language $L=\{0^n1^n : n>0\}$. **[8]**

---

#### 3.
a) What is GNF? Convert the following CFG into GNF. **[7]**  
$S \to XA \mid BB$  
$B \to b \mid SB$  
$X \to b$  
$A \to a$  

b) Design a PDA which accepts the language $L=\{w \in \{0,1\}^* : w \text{ has equal number of 0's and 1's}\}$ and also test your design for strings "010110" and "11010". **[8]**
**OR**
Design a PDA which accepts the language $L=\{a^ib^jc^k : k = i+j\}$ and also test your design for strings "aabccc" and "bbccc".

---

#### 4.
a) When is the grammar is said to be ambiguous? Prove the grammar is ambiguous: $S \to 0S1 \mid 1S0 \mid SS \mid \varepsilon$. **[7]**

b) What is Unrestricted Grammar? Design a Turing Machine to accept the language $L = \{0^n1^n : n \ge 1\}$. **[8]**
**OR**
Formally define a Turing Machine $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$ that accepts the language: $L = \{ w \in \{a, b\}^* \mid w \text{ is a palindrome}\}$. Trace the steps of the machine when processing the input string abba.abba.

---

#### 5.
a) How does Turing Machine compute a function? Design a Turing machine to compute a function $f(m)=m+1$ where m belongs to set of Natural numbers. **[7]**

b) What is recursive and recursively enumerable language? Show that the intersection of two recursive language is also recursive. **[8]**

---

#### 6.
a) Explain the Church-Turing thesis. How does the Post correspondence problem (PCP) demonstrate computational undecidability? **[7]**

b) What is meant by time and space complexity? Explain the classes P and NP in detail with examples. How are they related to real-world problem-solving? **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Pigeonhole principle  
b) Pumping Lemma for CFL  
c) Universal Turing Machine  

<br><br>

# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2025
**Programme:** BE  
**Course:** Theory of Computation  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) What is Function? Explain different types of functions with examples. **[7]**

b) "For every CFG there is an equivalent Push Down Automata". Justify this statement with an example. **[8]**

---

#### 2.
a) Define Finite Automata. Design a FA that accepts set of strings which doesn't starts with 0 and ends with 1 over the given alphabet $\Sigma = \{0, 1\}$. **[7]**

b) Convert the following NFA to its equivalent DFA. **[8]**
*(Refer to the NFA diagram with states $q_0, q_1, q_2$ in the original paper)*

---

#### 3.
a) What is Context Free Grammar? Design CFG for language $L = \{a^mb^n : m \ge 1, n \ge 1\}$. Test the grammar for derivation of $aaabbbb$ and also draw equivalent parse tree. **[7]**

b) Define Ambiguous Grammar. Prove that following grammar is ambiguous. **[8]**  
$S \to iCtS$  
$S \to iCtSeS$  
$S \to a$  
$C \to b$  

---

#### 4.
a) What is pumping lemma for CFL? Show that language $L = \{a^nb^nc^n : n > 0\}$ is not a CFL using pumping lemma for CFL. **[7]**

b) Define PDA with block diagram? Design a PDA which accepts the language $L = \{a^nb^{2n} : n \ge 1\}$ and test for strings aabbbb and aab. **[8]**

---

#### 5.
a) How can you represent Turing machine for computing a function? Show that the function $f(n) = n + 1$, is Turing computable. **[7]**

b) Define Turing machine. Design a Turing machine that accepts the language $L = \{a^nb^nc^n : n \ge 0\}$. Also explain your key idea. **[8]**

---

#### 6.
a) State Church-Turing Thesis. Compare and contrast the relationship of Recursive and Recursively Enumerable Language. **[7]**

b) Explain Computational Complexity Theory. What are P, NP and NP-Complete problems? Explain with examples. **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Applications of Regular expressions  
b) Normal Forms: CNF and GNF  
c) Decision Algorithm for CFL  
d) The halting problem  

<br><br>

# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2025
**Programme:** BE  
**Course:** Theory of Computation (New)  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) State the Pigeonhole Principle. Provide a formal proof for the following: "In any group of n people, there must be at least two people who have the same number of friends within that group." **[7]**

b) What is a regular expression? Construct a regular expression for the language of all strings over $\{a,b\}$ containing exactly two a's. Also draw a DFA for the expression. **[8]**

---

#### 2.
a) Explain Finite Automata? Design a DFA that accepts the language given by $L=\{w \in \{a,b\}^* : w \text{ does not contain three consecutive b's}\}$. Hence test your design for $abaabb$ and $babbba$. **[7]**

b) Construct a DFA equivalent to NFA as shown: **[8]**
*(Refer to the NFA diagram with states A, B, C, D, E in the original paper)*

---

#### 3.
a) Define a Context-Free Grammar (CFG). Construct a CFG for the language $L = \{a^n b^m c^n \mid n > 1, m > 1\}$. Provide the formal 4-tuple $\{V, T, P, S\}$ for your grammar. **[7]**

b) Apply the pumping lemma to prove $L = \{a^nb^nc^n \mid n \ge 0\}$ is not context-free. Show all steps of the proof. **[8]**
**OR**
Explain important properties of context-free languages (CFLs) with examples.

---

#### 4.
a) State decision properties of CFL. Show that CFL are not closed under complementation. **[7]**

b) Define PDA formally. Design a PDA for $L = \{ a^nb^{2n} : n > 0 \}$. **[8]**

---

#### 5.
a) How can multi-tape turing machine be simulated through single tape turing machine? Explain with an example. **[7]**

b) Design a Turing machine for the following language: $L = \{w \in \{a,b\}^* / w \text{ has equal number of a's and b's}\}$. **[8]**
**OR**
Design a Turing machine which works as copying machine for $w \in \{a, b\}^+$.

---

#### 6.
a) Define a Universal Turing Machine (UTM). Explain how it simulates other Turing Machines. **[7]**

b) Define tractable and intractable problems. Explain why finding a polynomial-time solution for any NP-complete problem would solve all NP problems. **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Chomsky Hierarchy  
b) Unrestricted grammar  
c) Halting Problem  
d) Complexity Analysis  
