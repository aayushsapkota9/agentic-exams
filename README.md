# Agentic Exams Repository

This repository organizes and maps past examination questions for engineering courses (Pokhara University syllabus). Each subject is broken down by chapter, mapping individual exam questions across multiple years to their specific syllabus units.

## Adding a New Subject — Mega Prompt

Copy the entire block below and paste it to your AI agent. Replace `{SUBJECT_NAME}` and `{SUBJECT_DIR}` before sending.

---

````
I am adding a new subject called {SUBJECT_NAME}. The subject folder is at {SUBJECT_DIR} (e.g. /repos/agentic-exams/operating-system/). Follow all phases in order. Before starting any phase, CHECK if it has already been completed — if yes, skip it and move on. Do not redo work that is already done.

---

PHASE 1 — IMAGE CONVERSION

Before doing anything: check if {SUBJECT_DIR}/past-qns/ already contains .jpg files and no .heic files. If so, skip this phase entirely and move to Phase 2.

1. List all files in {SUBJECT_DIR}/past-qns/.
2. If .heic files exist, convert each one to .jpg using:
   sips -s format jpeg filename.heic --out filename.jpg
   Rename the output to match the original name exactly (e.g. "2024 A front.heic" → "2024 A front.jpg").
3. Verify each .jpg was created and is not empty.
4. Delete all .heic files.
5. List the final .jpg files and confirm the count matches the original .heic count.

---

PHASE 2 — SYLLABUS PROCESSING

Before doing anything: check if {SUBJECT_DIR}/syllabus.md already exists AND if chap1/, chap2/, etc. folders already exist with chap{n}-syllabus.md files inside. If all of these exist, skip this phase entirely and move to Phase 3.

1. Read {SUBJECT_DIR}/syllabus-text.md (the raw syllabus provided).
2. Parse it into chapters. For each chapter, create a folder: {SUBJECT_DIR}/chap1/, chap2/, etc.
3. Inside each chapter folder, create chap{n}-syllabus.md containing only that chapter's topics as written in the source syllabus.
4. Create {SUBJECT_DIR}/syllabus.md listing all chapters with links to their chap{n}-syllabus.md files.

---

PHASE 3 — OCR & TRANSCRIPTION

Before doing anything: check if {SUBJECT_DIR}/past-qns-text/ already exists and contains .md files. If files already exist there, skip transcription for those files and only process any .jpg files that do not yet have a corresponding .md in past-qns-text/.

1. Create {SUBJECT_DIR}/past-qns-text/ if it does not exist.
2. For each .jpg in past-qns/, extract all visible text via OCR.
3. Save each as a separate .md file named exactly after the photo (e.g. "2024 A front.jpg" → "2024 A front.md", "2024 A back.jpg" → "2024 A back.md"). One file per photo. Do NOT merge files.
4. Preserve the original question numbering and formatting exactly as it appears on the paper.

---

PHASE 4 — QUESTION MAPPING & CHAPTER COMPILATION

Before doing anything: check which chap{n}-qns.md files already exist. For those that exist, skip re-generating them unless you find a question that was missed.

MAPPING RULES:
- Read all transcribed .md files from past-qns-text/.
- Read all chap{n}-syllabus.md files to understand which topics belong to which chapter.
- For each sub-question (e.g. 1a, 1b, 2a), determine its chapter based on topic match with the syllabus.
- STRICT RULE: Do NOT guess. If you are not confident about a chapter mapping, do not place the question in any chapter file. Instead, add it to {SUBJECT_DIR}/not-identified.md (format below).
- STRICT RULE: No duplicates. Each sub-question from a given exam session must appear in exactly one place — either one chapter file or not-identified.md.

For each chap{n}/, create chap{n}-qns.md with this exact format:

---
# Chapter {n} — {Chapter Title}

## Quick Navigation
[1(a)](#1a) | [1(b)](#1b) | [2(a)](#2a) | ...

---

## 1(a)

##### 2024 A [7 marks]

```markdown
Exact transcribed question text here.
` ` `

##### 2023 B [7 marks]

```markdown
Exact transcribed question text here.
` ` `

---

## 1(b)

...
---

FORMATTING RULES:
- Group by question label (## 1(a) contains all years of that label), sorted newest year first.
- Year label uses the photo filename session identifier (e.g. "2024 A", "2023 B").
- Each question goes inside a fenced markdown code block. No plain text outside the code block.
- No duplicates across chapter files or within a file.

NOT-IDENTIFIED FILE FORMAT:
Create {SUBJECT_DIR}/not-identified.md for any question that could not be confidently mapped:

---
# Not Identified Questions

These questions could not be confidently mapped to a chapter. Do not guess — review manually.

## 2024 A — 3(b)

```markdown
Exact transcribed question text here.
` ` `

## 2023 B — 5(a)

```markdown
Exact transcribed question text here.
` ` `
---

---

PHASE 5 — VERIFICATION

1. Confirm every sub-question from every exam session appears in exactly one location (a chapter file or not-identified.md). No question should be missing or duplicated.
2. Confirm the folder structure matches this layout:

{SUBJECT_DIR}/
├── syllabus.md
├── syllabus-text.md          ← original, untouched
├── not-identified.md         ← unmapped questions only
├── past-qns/                 ← only .jpg files remain
├── past-qns-text/            ← one .md per photo (e.g. "2024 A front.md")
├── chap1/
│   ├── chap1-syllabus.md
│   └── chap1-qns.md
├── chap2/
│   ├── chap2-syllabus.md
│   └── chap2-qns.md
└── ...

3. Report:
   - Total questions processed
   - Questions mapped per chapter
   - Questions in not-identified.md and why they were not mapped
````
