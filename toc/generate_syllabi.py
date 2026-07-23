import os

toc_dir = "toc"

# Chapter 1: Introduction
chap1_syllabus = """# Unit 1: Introduction
**Total Hours: 4**

- **1.1 Review of set, relation and function**
- **1.2 Proof techniques** – proof by contradiction, pigeon hole principle, induction and diagonalization.
- **1.3 Alphabets and language**
- **1.4 Chomsky’s hierarchy**
"""

# Chapter 2: Finite Automata and Regular Language
chap2_syllabus = """# Unit 2: Finite Automata and Regular Language
**Total Hours: 10**

- **2.1 Deterministic Finite Automata, Non-Deterministic Finite Automata**
- **2.2 Regular expressions and regular language, equivalence of regular language and finite automata**
- **2.3 Properties of regular language**
- **2.4 Pumping lemma for regular sets**
- **2.5 Closure properties of regular sets**
- **2.6 Decision algorithms for regular sets**
"""

# Chapter 3: Context-Free Language and Pushdown Automata
chap3_syllabus = """# Unit 3: Context-Free Language and Pushdown Automata
**Total Hours: 13**

- **3.1 Context-free grammar**
- **3.2 Derivation trees and simplification of context-free grammar**
- **3.3 Normal forms (CNF, GNF)**
- **3.4 Pushdown automata** (formal description and final state PDA design)
- **3.5 Equivalence of pushdown automata and context-free grammar**
- **3.6 Properties of context-free languages (CFL)**
- **3.7 Pumping lemma for CFL’s**
- **3.8 Closure properties of CFL’s**
- **3.9 Decision algorithms for CFL’s**
"""

# Chapter 4: Turing Machines
chap4_syllabus = """# Unit 4: Turing Machines
**Total Hours: 10**

- **4.1 Introduction to Turing machine**
- **4.2 Computing with Turing machine**
- **4.3 Extensions of Turing machine**
- **4.4 Unrestricted grammar**
- **4.5 Recursively enumerable languages**
"""

# Chapter 5: Undecidability
chap5_syllabus = """# Unit 5: Undecidability
**Total Hours: 4**

- **5.1 The Church-Turing thesis**
- **5.2 Halting Problem**
- **5.3 Universal Turing machines**
- **5.4 Undecidable problems about Turing machines**
- **5.5 Properties of Recursive and Recursively enumerable languages**
"""

# Chapter 6: Computational Complexity
chap6_syllabus = """# Unit 6: Computational Complexity
**Total Hours: 4**

- **6.1 Introduction to Complexity theory, tractable and intractable problems**
- **6.2 Class P and Class NP problems**
- **6.3 NP-complete problems**
"""

syllabi = [
    ("chap1", chap1_syllabus),
    ("chap2", chap2_syllabus),
    ("chap3", chap3_syllabus),
    ("chap4", chap4_syllabus),
    ("chap5", chap5_syllabus),
    ("chap6", chap6_syllabus),
]

for chap, content in syllabi:
    cpath = os.path.join(toc_dir, chap)
    os.makedirs(cpath, exist_ok=True)
    with open(os.path.join(cpath, f"{chap}-syllabus.md"), "w") as f:
        f.write(content)

print("Created all chapX-syllabus.md files.")
