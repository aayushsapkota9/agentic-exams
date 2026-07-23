import os

toc_dir = "toc"

# Function to construct a question block
def qblock(heading, paper, qtext):
    return f"##### {paper}\n{qtext}\n\n```markdown\n{qtext}\n```\n\n---\n\n"

# ----------------- CHAP 1 -----------------
chap1_nav = "[1(a)](#1a) | [1(b)](#1b)"
chap1_content = f"""# Chapter 1: Introduction - Past Questions
### Quick Navigation
{chap1_nav}

---

## 1(a)

"""

chap1_qns_1a = [
    ("2018 Fall - Pokhara University", "a) Define set, relation, and function. What are the different types of functions? Explain with suitable examples. **[8]**"),
    ("2020 Fall - Pokhara University", "a) What is a set? Show the different types of set operations with examples. **[7]**"),
    ("2020 Fall - Pokhara University", "c) Cartesian Product, Relation and Function (Short Note) **[5]**"),
    ("2022 Fall - Pokhara University", "a) What is a function? Explain different types of functions with examples. **[8]**"),
    ("2023 Spring - Pokhara University", "a) Define alphabet, string, and language with examples. **[5]**"),
    ("2024 Spring - Pokhara University", "a) What is function? Explain its types with examples. **[7]**")
]

for paper, text in chap1_qns_1a:
    chap1_content += qblock("## 1(a)", paper, text)

chap1_content += "## 1(b)\n\n"

chap1_qns_1b = [
    ("2018 Spring - Pokhara University", "a) Explain proof techniques: proof by contradiction, mathematical induction, and pigeonhole principle with examples. **[8]**"),
    ("2024 Spring (New Course) - Pokhara University", "a) State and prove the pigeonhole principle. Prove by mathematical induction that $n^2 - 3n + 4$ is even and true for all positive integers. **[7]**")
]

for paper, text in chap1_qns_1b:
    chap1_content += qblock("## 1(b)", paper, text)


# ----------------- CHAP 2 -----------------
chap2_nav = "[1(a)](#1a) | [1(b)](#1b) | [2(a)](#2a) | [2(b)](#2b)"
chap2_content = f"""# Chapter 2: Finite Automata and Regular Language - Past Questions
### Quick Navigation
{chap2_nav}

---

## 1(a)

"""

chap2_qns_1a = [
    ("2018 Fall - Pokhara University", "b) Differentiate between DFA and NFA. Construct a DFA that accepts the set of strings over $\\Sigma = \\{a, b\\}$ containing an even number of $a$'s and odd number of $b$'s. Test your design with a valid string. **[7]**"),
    ("2018 Spring - Pokhara University", "b) Define Deterministic Finite Automata (DFA). Construct a DFA that accepts strings over $\\Sigma = \\{0, 1\\}$ that start with $01$ and end with $10$. Test your design with an input string. **[7]**"),
    ("2020 Fall - Pokhara University", "b) Explain finite automata along with its uses and applications. Construct a DFA that recognizes language $L$ accepting the set of strings containing exactly four 1's over alphabet $\\Sigma = \\{0, 1\\}$ and test your design with a valid string. **[8]**"),
    ("2021 Fall - Pokhara University", "a) Differentiate between DFA and NFA. Design a DFA that accepts the set of strings over $\\Sigma = \\{0, 1\\}$ containing neither \"00\" nor \"11\" as substring. Test your design for $101001$. **[8]**"),
    ("2021 Spring - Pokhara University", "a) Explain finite automata along with its uses and applications. Construct a DFA that recognizes language accepting the set of strings that neither has \"aa\" nor \"bb\" as substring over $\\Sigma = \\{a, b\\}$ and test your design with a valid string. **[8]**"),
    ("2022 Fall - Pokhara University", "b) Define DFA. The C programming language has three keywords `while`, `for`, and `do` that are used to write loop statements. Construct a Deterministic Finite Automaton (DFA) that recognizes these three loop keywords. **[7]**"),
    ("2023 Spring - Pokhara University", "b) Design a DFA for the language $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ ends with } bb\\}$. **[5]**"),
    ("2024 Fall - Pokhara University", "a) Define Finite State Automata. Construct a DFA to recognize a language $L$ that accepts the set of strings which contains neither \"ba\" nor \"ab\" as substring over $\\Sigma = \\{a, b\\}$ and test your design with a valid string. **[8]**"),
    ("2024 Spring - Pokhara University", "b) Differentiate between DFA and NFA. Design a DFA that accepts the language given by $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ contains neither } 'aa' \\text{ nor } 'bb' \\text{ as substring}\\}$. Hence test your design for $abaabb$. **[8]**")
]

for paper, text in chap2_qns_1a:
    chap2_content += qblock("## 1(a)", paper, text)

chap2_content += "## 1(b)\n\n"

chap2_qns_1b = [
    ("2018 Fall - Pokhara University", "a) Convert the given NFA into an equivalent DFA. **[8]**"),
    ("2018 Spring - Pokhara University", "a) State Arden's Theorem. Convert the given NFA with $\\varepsilon$-transitions to an equivalent DFA. **[8]**"),
    ("2019 Spring - Pokhara University", "a) Find the regular expression for the given Finite Automata. Convert the NDFA to equivalent DFA. **[8]**"),
    ("2021 Fall - Pokhara University", "b) Construct a DFA equivalent to the given NFA. **[7]**"),
    ("2021 Spring - Pokhara University", "b) Convert a DFA equivalent to NFA as shown in figure. **[7]**"),
    ("2022 Fall - Pokhara University", "a) Construct a DFA equivalent to NFA as shown in figure. **[8]**"),
    ("2023 Spring - Pokhara University", "a) What is the significance of minimizing a DFA? Minimize the given DFA and analyze your finding. **[8]**"),
    ("2024 Fall - Pokhara University", "a) Convert the following NFA to its equivalent DFA. **[8]**"),
    ("2024 Spring - Pokhara University", "a) Convert the given NFA to its equivalent DFA. **[7]**")
]

for paper, text in chap2_qns_1b:
    chap2_content += qblock("## 1(b)", paper, text)

chap2_content += "## 2(a)\n\n"

chap2_qns_2a = [
    ("2018 Spring - Pokhara University", "b) Define regular expression. Construct a regular expression for the set of all strings over $\\Sigma = \\{a, b\\}$ containing at most two $a$'s. **[7]**"),
    ("2020 Fall - Pokhara University", "a) Find the regular expression from NFA $M = (K, \\Sigma, \\delta, s, F)$, where $K = \\{q_0, q_1, q_2, q_3, q_4, q_5\\}$, $\\Sigma = \\{a, b\\}$, $s = q_0$, $F = \\{q_5\\}$. **[8]**"),
    ("2021 Fall - Pokhara University", "b) Construct an $\\varepsilon$-NFA for the Regular Expression $(0+1)^*(0+1)$. **[7]**"),
    ("2022 Fall - Pokhara University", "b) Explain Arden's Theorem. Find the regular expression for the given Finite State Automaton using Arden's method. **[7]**"),
    ("2023 Spring - Pokhara University", "b) \"We can convert Finite Automata to Regular Expression and also Regular Expression to Finite Automata\". Justify this statement with suitable examples. **[7]**"),
    ("2024 Fall - Pokhara University", "b) What are Regular Expressions (RE)? Construct an NFA for the RE $(a+b)^* a b c (a+b)^*$. **[7]**")
]

for paper, text in chap2_qns_2a:
    chap2_content += qblock("## 2(a)", paper, text)

chap2_content += "## 2(b)\n\n"

chap2_qns_2b = [
    ("2018 Fall - Pokhara University", "b) State and prove Pumping Lemma for Regular Languages. Show that the language $L = \\{a^n b^n \\mid n \\ge 0\\}$ is not regular using pumping lemma. **[7]**"),
    ("2021 Spring - Pokhara University", "a) Define Pumping Lemma. Show that $L = \\{a^n b^{2n} \\mid n \\ge 1\\}$ is not regular using pumping lemma for regular language. **[8]**"),
    ("2024 Spring - Pokhara University", "b) Define Pumping Lemma for regular language. Show that $L = \\{a^n b^{2n} \\mid n > 1\\}$ is not regular using pumping lemma for regular language. **[8]**")
]

for paper, text in chap2_qns_2b:
    chap2_content += qblock("## 2(b)", paper, text)


# ----------------- CHAP 3 -----------------
chap3_nav = "[1(a)](#1a) | [1(b)](#1b) | [2(a)](#2a) | [2(b)](#2b)"
chap3_content = f"""# Chapter 3: Context-Free Language and Pushdown Automata - Past Questions
### Quick Navigation
{chap3_nav}

---

## 1(a)

"""

chap3_qns_1a = [
    ("2018 Spring - Pokhara University", "b) Define ambiguous grammar with an example. Prove that the grammar $S \\to S + S \\mid S \\times S \\mid a$ is ambiguous. **[7]**"),
    ("2019 Spring - Pokhara University", "a) Using the principles of Context-Free Grammar, capture the expression $(x_1 + x_2) * (x_3 * x_2 + x_1)$ and draw its parse tree. **[8]**"),
    ("2019 Spring - Pokhara University", "b) Define ambiguous grammar. Explain with an example. Remove the $\\varepsilon$-productions (Null productions) from the given grammar. **[7]**"),
    ("2020 Fall - Pokhara University", "a) What is CFG? Design a CFG for language $L = \\{w c w^R \\mid w \\in \\{a, b\\}^*\\}$. Test the grammar for derivation of $baacaab$ and draw the equivalent parse tree. **[8]**"),
    ("2021 Fall - Pokhara University", "b) For the grammar $S \\to aSb \\mid a$, show the leftmost derivation and rightmost derivation trees for input string $aaabbb$. **[7]**"),
    ("2021 Spring - Pokhara University", "b) Define Derivation Tree. When is a grammar called ambiguous? Explain with an example. **[7]**"),
    ("2022 Fall - Pokhara University", "a) What is Context-Free Grammar? Design a CFG for language $L = \\{a^m b^n \\mid m \\ge 1, n \\ge 1\\}$. Test the grammar for derivation of $aaabbb$ and draw equivalent parse tree. **[8]**"),
    ("2023 Spring - Pokhara University", "a) Can production rules realize Context-Free Grammar for the language given by $L = \\{a^m b^n \\mid m > 0 \\text{ and } n > 0\\}$? How? **[7]**"),
    ("2023 Spring - Pokhara University", "b) Explain the process of simplifying Context-Free Grammar. Simplify the given CFG. **[8]**"),
    ("2023 Spring - Pokhara University", "c) Define an ambiguous grammar. Check if below grammar is ambiguous. **[5]**"),
    ("2024 Fall - Pokhara University", "a) What is a Parse tree (Derivation tree)? How is it useful to show the grammar is ambiguous? Give an example. **[8]**"),
    ("2024 Spring - Pokhara University", "a) What is CFG? Design a CFG for language $L = \\{a^m b^n \\mid m \\ge 1, n \\ge 1\\}$. Test the grammar for derivation of $aaaabbb$ and also draw equivalent parse tree. **[8]**")
]

for paper, text in chap3_qns_1a:
    chap3_content += qblock("## 1(a)", paper, text)

chap3_content += "## 1(b)\n\n"

chap3_qns_1b = [
    ("2018 Fall - Pokhara University", "a) Describe the normal forms for Context-Free Grammars (CFG) with suitable examples. Convert the given CFG to Chomsky Normal Form (CNF). **[8]**"),
    ("2018 Spring - Pokhara University", "a) What is Context-Free Grammar (CFG)? Convert the given grammar into Greibach Normal Form (GNF). **[8]**"),
    ("2020 Fall - Pokhara University", "b) What is CNF? Convert following CFG into CNF. **[7]**"),
    ("2021 Fall - Pokhara University", "a) Illustrate the simplification algorithm for a Context-Free Grammar. Convert the grammar into Chomsky Normal Form (CNF). **[8]**"),
    ("2021 Spring - Pokhara University", "a) Reduce the given CFG to CNF. **[8]**"),
    ("2024 Fall - Pokhara University", "b) What is an empty language? Convert the following context-free grammar (CFG) into its equivalent Chomsky's Normal Form (CNF). **[7]**"),
    ("2024 Spring - Pokhara University", "b) Convert the following grammar into Chomsky Normal Form (CNF). **[7]**")
]

for paper, text in chap3_qns_1b:
    chap3_content += qblock("## 1(b)", paper, text)

chap3_content += "## 2(a)\n\n"

chap3_qns_2a = [
    ("2018 Fall - Pokhara University", "a) How to construct a Pushdown Automaton (PDA) from a Context-Free Grammar (CFG)? Construct a PDA for the grammar. **[8]**"),
    ("2018 Spring - Pokhara University", "a) Define Pushdown Automata (PDA) with a formal block diagram. Design a PDA for the language $L = \\{w w^R \\mid w \\in \\{a, b\\}^*\\}$. **[8]**"),
    ("2019 Spring - Pokhara University", "a) What is instantaneous description of a PDA? Design a PDA which accepts the language $L = \\{w \\in \\{0, 1\\}^* \\mid w \\text{ has equal number of 0s and 1s}\\}$. **[8]**"),
    ("2020 Fall - Pokhara University", "b) Design a Pushdown Automaton (PDA) for given grammar. **[7]**"),
    ("2021 Fall - Pokhara University", "a) Define PDA with a block diagram. Design a PDA which accepts the language $L = \\{a^n b^{2n} \\mid n \\ge 1\\}$ and test for strings $aabbbb$ and $aab$. **[8]**"),
    ("2021 Fall - Pokhara University", "b) Prove that each context-free language is accepted by some pushdown automaton. **[7]**"),
    ("2021 Spring - Pokhara University", "a) Design a PDA for the given grammar $G = (V, \\Sigma, R, S)$. **[7]**"),
    ("2021 Spring - Pokhara University", "b) Define PDA. Design a PDA which accepts the set of all palindromes over alphabet $\\Sigma = \\{0, 1\\}$. **[7]**"),
    ("2022 Fall - Pokhara University", "a) Design a PDA which accepts the language $L = \\{w \\in \\{a, b\\}^* \\mid w \\text{ has equal number of a's and b's}\\}$. **[8]**"),
    ("2022 Fall - Pokhara University", "b) \"For every CFG there is an equivalent Pushdown Automaton\". Justify this statement with an example. **[7]**"),
    ("2023 Spring - Pokhara University", "a) Explain the concept of \"epsilon transitions\" in a Pushdown Automaton. How do they affect the computation? **[7]**"),
    ("2023 Spring - Pokhara University", "b) Define PDA with block diagram. Design a PDA which accepts the language $L = \\{a^n b^n \\mid n \\ge 1\\}$ and test for strings $aabb$ and $aab$. **[8]**"),
    ("2024 Fall - Pokhara University", "a) Design a Pushdown Automaton (PDA) for language $L = \\{w w^R \\mid w \\in \\{a, b\\}^*\\}$. **[8]**"),
    ("2024 Fall - Pokhara University", "b) \"For every CFG there is an equivalent Pushdown Automata\". Justify this statement with an example. **[7]**"),
    ("2024 Spring - Pokhara University", "a) Define PDA with block diagram. Design a PDA which accepts the language $L = \\{a^n \\mid n \\ge 1\\}$ and test for strings $aaaaaaaa$ and $aaaaaa$. **[8]**")
]

for paper, text in chap3_qns_2a:
    chap3_content += qblock("## 2(a)", paper, text)

chap3_content += "## 2(b)\n\n"

chap3_qns_2b = [
    ("2018 Fall - Pokhara University", "b) Explain the closure properties of context-free languages. **[7]**"),
    ("2018 Spring - Pokhara University", "b) State the Pumping Lemma for Context-Free Languages. Prove that $L = \\{a^n b^n c^n \\mid n \\ge 1\\}$ is not context-free. **[7]**"),
    ("2019 Spring - Pokhara University", "b) State the Pumping Lemma for Context-Free Languages. Prove that the language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$ is not context-free. **[7]**"),
    ("2019 Spring - Pokhara University", "b) Write about the closure properties of context-free languages. **[7]**"),
    ("2020 Fall - Pokhara University", "a) In what aspects is a PDA stronger than a finite automaton? State the closure properties of context-free grammar. **[7]**"),
    ("2020 Fall - Pokhara University", "b) State the Pumping Lemma for Context-Free Languages. Prove that $L = \\{0^n 1^n 2^n \\mid n \\ge 0\\}$ is not context-free. **[8]**"),
    ("2021 Fall - Pokhara University", "a) What is pumping lemma for CFL? Show that language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$ is not a CFL using pumping lemma for CFL. **[8]**"),
    ("2021 Spring - Pokhara University", "b) Briefly explain about properties of CFL. **[7]**"),
    ("2022 Fall - Pokhara University", "b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**"),
    ("2024 Fall - Pokhara University", "b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**"),
    ("2024 Spring - Pokhara University", "b) Show that the language $L = \\{a^n b^n c^n \\mid n > 0\\}$ is not context-free using the concept of pumping lemma. **[7]**")
]

for paper, text in chap3_qns_2b:
    chap3_content += qblock("## 2(b)", paper, text)


# ----------------- CHAP 4 -----------------
chap4_nav = "[1(a)](#1a) | [1(b)](#1b)"
chap4_content = f"""# Chapter 4: Turing Machines - Past Questions
### Quick Navigation
{chap4_nav}

---

## 1(a)

"""

chap4_qns_1a = [
    ("2018 Fall - Pokhara University", "b) Define Turing Machine. Design a Turing Machine that accepts the language $L = \\{1^n 2^n 3^n \\mid n \\ge 0\\}$. **[7]**"),
    ("2018 Spring - Pokhara University", "a) Define Turing Machine formally. **[8]**"),
    ("2019 Spring - Pokhara University", "b) Design a Turing Machine as a right shift machine which transforms $\#w\#$ into $\#\#w\#$ over alphabet $\\Sigma = \\{a, b, \\#\\}$. **[7]**"),
    ("2020 Fall - Pokhara University", "a) Design a Turing Machine that transforms $\#w\#$ to $\#\#w\#$ where $\#$ represents blank symbol and $w \\in \\{a, b\\}^*$. **[8]**"),
    ("2021 Fall - Pokhara University", "b) Design a deterministic Turing Machine to accept the language $L = \\{0^n 1^n 2^n \\mid n \\ge 0\\}$. **[7]**"),
    ("2021 Spring - Pokhara University", "b) Define a Turing Machine. Design a TM that accepts the language $L = \\{1^n 2^n 3^n \\mid n \\ge 0\\}$. **[8]**"),
    ("2022 Fall - Pokhara University", "a) Define Turing Machine. Design a Turing Machine to decide whether or not any input string $w \\in \\{a, b\\}^*$ is a palindrome. Test your design for strings $ababa$ and $bbaab$. **[8]**"),
    ("2023 Spring - Pokhara University", "b) Define Turing Machine. Construct a Turing Machine that accepts the language of strings over $\\{a, b\\}$ with each string of even length. Also show it accepts string $abab$. **[7]**"),
    ("2024 Fall - Pokhara University", "b) Briefly explain the idea of designing the Turing Machine that accepts the language $L = \\{a^n b^n \\mid n > 0\\}$. Show the state transition diagram. **[7]**"),
    ("2024 Spring - Pokhara University", "a) Define Turing Machine. Design a Turing Machine that accepts the language $L = \\{a^n b^n c^n \\mid n \\ge 0\\}$. **[8]**")
]

for paper, text in chap4_qns_1a:
    chap4_content += qblock("## 1(a)", paper, text)

chap4_content += "## 1(b)\n\n"

chap4_qns_1b = [
    ("2018 Fall - Pokhara University", "a) How can you represent a Turing Machine for computing a function? Show that the function $f(n) = n + 1$ is Turing computable. **[8]**"),
    ("2018 Spring - Pokhara University", "a) Design a Turing Machine to perform unary addition $f(x, y) = x + y$. **[8]**"),
    ("2019 Spring - Pokhara University", "a) How can you represent a Turing Machine? Show that the function $f(n) = n + 1$ is Turing computable. **[8]**"),
    ("2020 Fall - Pokhara University", "b) What is a configuration of a Turing Machine? Show that $f(x) = x + 1$ is Turing computable. **[7]**"),
    ("2021 Fall - Pokhara University", "a) How can you represent a Turing Machine for computing a function? Show that the function $f(n) = n + 1$ is Turing computable. **[8]**"),
    ("2021 Spring - Pokhara University", "a) Design a TM which computes the function $f(m) = m + 1$ for each $m \\in \\mathbb{N}$. **[8]**"),
    ("2022 Fall - Pokhara University", "b) Turing machines are functionally stronger than Pushdown Automata. Justify. Also show TM are function computable. **[7]**"),
    ("2023 Spring - Pokhara University", "a) Describe the concept of an \"accepting state\" and a \"halting state\" in a Turing Machine. Show that the function $f(n) = n + 1$ is Turing computable. **[8]**"),
    ("2024 Fall - Pokhara University", "a) Design a Turing Machine for computing function $f(x, y) = x + y$ and show your validation for $x = 2$ and $y = 4$. **[8]**"),
    ("2024 Spring - Pokhara University", "b) How does a Turing Machine compute a function of natural numbers? Describe. Show that the function $f(n) = n + 2$ is computable. **[7]**")
]

for paper, text in chap4_qns_1b:
    chap4_content += qblock("## 1(b)", paper, text)


# ----------------- CHAP 5 -----------------
chap5_nav = "[1(a)](#1a) | [1(b)](#1b)"
chap5_content = f"""# Chapter 5: Undecidability - Past Questions
### Quick Navigation
{chap5_nav}

---

## 1(a)

"""

chap5_qns_1a = [
    ("2018 Fall - Pokhara University", "a) Write short notes on Church-Turing thesis and Universal Turing Machine. **[8]**"),
    ("2018 Spring - Pokhara University", "a) Describe the Church-Turing thesis. Compare Recursive and Recursively Enumerable languages. **[8]**"),
    ("2018 Spring - Pokhara University", "b) Explain the Halting Problem of Turing Machine. Why is it undecidable? **[7]**"),
    ("2019 Spring - Pokhara University", "b) Write about Church-Turing thesis and universal Turing machine. **[7]**"),
    ("2020 Fall - Pokhara University", "a) Write about Church-Turing thesis and Universal Turing Machine. **[8]**"),
    ("2021 Fall - Pokhara University", "b) Write about Church-Turing thesis and Universal Turing Machine. **[7]**"),
    ("2021 Spring - Pokhara University", "a) Describe Church's Hypothesis. Also illustrate your understanding of Halting Problem. **[8]**"),
    ("2022 Fall - Pokhara University", "a) State Church-Turing Thesis. Compare and contrast the relationship between Recursive and Recursively Enumerable Language. **[8]**"),
    ("2024 Fall - Pokhara University", "b) Explain the Halting Paradox in Turing Machine. What are Space and Time complexity? **[7]**"),
    ("2024 Spring - Pokhara University", "a) State the halting theorem and give the outline of its proof. **[7]**")
]

for paper, text in chap5_qns_1a:
    chap5_content += qblock("## 1(a)", paper, text)

chap5_content += "## 1(b)\n\n"

chap5_qns_1b = [
    ("2018 Fall - Pokhara University", "b) Discuss Recursive Function Theory. Prove that the union of two recursive languages is recursive. **[7]**"),
    ("2019 Spring - Pokhara University", "a) What are recursive and recursively enumerable languages? Show that the union of two recursive languages is also recursive. **[8]**"),
    ("2021 Spring - Pokhara University", "b) Describe briefly about recursive and recursively enumerable language. **[7]**"),
    ("2023 Spring - Pokhara University", "a) Define the concept of \"Recursive Functions\" and explain their significance in the theory of computation. **[8]**")
]

for paper, text in chap5_qns_1b:
    chap5_content += qblock("## 1(b)", paper, text)


# ----------------- CHAP 6 -----------------
chap6_nav = "[1(a)](#1a) | [1(b)](#1b)"
chap6_content = f"""# Chapter 6: Computational Complexity - Past Questions
### Quick Navigation
{chap6_nav}

---

## 1(a)

"""

chap6_qns_1a = [
    ("2018 Spring - Pokhara University", "b) Explain computational complexity. Differentiate between tractable and intractable problems with suitable examples. **[7]**"),
    ("2019 Spring - Pokhara University", "a) How does computability differ from complexity theory? Describe time and space complexity. **[8]**"),
    ("2021 Spring - Pokhara University", "b) Explain computational complexity. What are Space and Time complexity? **[7]**"),
    ("2023 Spring - Pokhara University", "b) Is $P = NP$? Explain. Also differentiate between Tractable and Intractable problems with examples. **[7]**")
]

for paper, text in chap6_qns_1a:
    chap6_content += qblock("## 1(a)", paper, text)

chap6_content += "## 1(b)\n\n"

chap6_qns_1b = [
    ("2018 Fall - Pokhara University", "b) Define computability theory. Differentiate between P problems and NP-complete problems with examples. Is $P = NP$? Discuss. **[7]**"),
    ("2019 Spring - Pokhara University", "b) Explain class P, NP, and NP-complete problems with examples. **[7]**"),
    ("2020 Fall - Pokhara University", "b) Explain in brief Class P and NP-complete problems with suitable examples. **[7]**"),
    ("2021 Fall - Pokhara University", "a) When are problems said to be NP-Complete? Illustrate with suitable examples. **[8]**"),
    ("2022 Fall - Pokhara University", "b) Explain Computational Complexity Theory. What are P, NP and NP-Complete problems? Explain with examples. **[7]**"),
    ("2024 Fall - Pokhara University", "a) What is computational complexity of a problem? Explain P, NP and NP-Complete problems. **[8]**"),
    ("2024 Spring - Pokhara University", "b) What are P, NP and NP-Complete problems? Explain with examples. **[8]**")
]

for paper, text in chap6_qns_1b:
    chap6_content += qblock("## 1(b)", paper, text)


# Write all files
qns_files = [
    ("chap1", chap1_content),
    ("chap2", chap2_content),
    ("chap3", chap3_content),
    ("chap4", chap4_content),
    ("chap5", chap5_content),
    ("chap6", chap6_content),
]

for chap, content in qns_files:
    cpath = os.path.join(toc_dir, chap)
    os.makedirs(cpath, exist_ok=True)
    with open(os.path.join(cpath, f"{chap}-qns.md"), "w") as f:
        f.write(content)

print("Created all chapX-qns.md files successfully.")
