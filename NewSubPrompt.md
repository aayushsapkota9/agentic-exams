In the `<FOLDER_NAME>` folder, we have a `syllabus.txt` file and a `past-qn-images` folder containing screenshots of past exams. Please perform the following steps:

1. **OCR Extraction**: Run OCR on all screenshot images in `<FOLDER_NAME>/past-qn-images/` to extract their text.
2. **Syllabus Conversion**: Convert the plain text `<FOLDER_NAME>/syllabus.txt` to a clean, formatted Markdown file at `<FOLDER_NAME>/syllabus.md`.
3. **Reconstruct Exam Papers**: Clean up the raw OCR text to reconstruct the individual year-wise past exam papers in markdown format. Save them under `<FOLDER_NAME>/past-qns/md/` (naming them like `<SUBJECT_NAME>_<Year>_PU_<Season>.md`).
4. **Chapter-wise Syllabus & Questions**:
   - Create chapter folders (`<FOLDER_NAME>/chap1/`, `<FOLDER_NAME>/chap2/`, etc.) corresponding to each unit in the syllabus.
   - Generate `chapX-syllabus.md` for each chapter containing the specific unit's outline.
   - Categorize and distribute the past questions into their respective `chapX-qns.md` files, grouped under their original question headings (e.g., `## 1(a)`, `## 2(b)`).

Refer to the layout, styling, and file/folder structures used in `applied-maths` (or `java`) as a reference guide. Each question in `chapX-qns.md` should be listed as regular text followed immediately by a markdown code block containing the exact same question. Add a quick navigation menu at the top of each question file.
