# Agentic Exams Repository

This repository is dedicated to organizing and mapping past examination questions for various engineering courses (starting with Pokhara University syllabus). Each subject is broken down by chapter, mapping individual exam questions (e.g., 1a, 1b) across multiple years to their specific syllabus units.

---

## Instructions for the Next Subject (AI Agent Prompt)

If the user wants to add a new subject, use the following "Mega Prompt" to ensure perfect continuity and formatting.

### **The Mega Prompt**

> [!IMPORTANT]
> **SUBJECT INITIATION PROMPT**
>
> I am adding a new subject called `{SubjectName}`. Follow these steps to process the new subject folder `/repos/agentic-exams/{SubjectName}/`.
>
> **Phase 1: Image Processing**
> 1.  Navigate to `{SubjectName}/past-qns/` where I've uploaded several `.heic` images of exam papers.
> 2.  Use the `sips` terminal command to convert all `.heic` files to `.jpg`.
> 3.  **Delete** all original `.heic` files once the conversion is confirmed.
>
> **Phase 2: Syllabus Setup**
> 1.  Locate `{SubjectName}/syllabus-text.md` (which I provided).
> 2.  Create a clean `{SubjectName}/syllabus.md` and create individual chapter folders (e.g., `chap1/`, `chap2/`...) within the subject directory.
> 3.  Create `chap{n}-syllabus.md` files for each chapter based on the units in the source syllabus.
>
> **Phase 3: OCR & Mapping**
> 1.  Transcribe the text from all `.jpg` exam images into `{SubjectName}/past-qns-text/` folder as individual `.md` files (one per photo).
> 2.  Merge the front and back of the same year (e.g., 2024A Front and Back) into a single `.md` file for that year.
> 3.  **CRITICAL MAPPING:** Analyze the transcribed questions and the syllabus. Map each sub-question (e.g., 2a, 2b) to its respective chapter.
>
> **Phase 4: Chapter Compilations**
> 1.  In each `chap{n}/` folder, create a `chap{n}-qns.md` file.
> 2.  **GROUPING BY LABEL:** Within the `chap{n}-qns.md` file, do **NOT** list by year. Instead, group all similar question labels together across all years.
>     *   Example: List all `1a` questions from all years, then all `1b` questions from all years, and so on.
> 3.  Use the following styling:
>     *   Main header: `## 1(a)`
>     *   Sub-header for specific question: `### 1(a) <small>YEAR</small> <small>[MARKS]</small>`
>     *   Include a code block with the exact original transcription for reference.
>
> **Phase 5: Final Verification**
> 1.  Check each chapter file to ensure no question was missed.
> 2.  Verify the folder structure matches the existing `micro/` or `calculus-ii/` examples.
