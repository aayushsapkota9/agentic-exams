import pypdf

pdf_path = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm/Numerical Methods.pdf"
reader = pypdf.PdfReader(pdf_path)
num_pages = len(reader.pages)
print(f"Number of pages: {num_pages}")

# Print first 2000 chars of page 1 and page 2
print("--- Page 1 ---")
print(reader.pages[0].extract_text()[:1000])
print("--- Page 2 ---")
print(reader.pages[1].extract_text()[:1000])

# Search for "2024" or "Pokhara University" in the PDF
found_pages = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if "Pokhara University" in text or "POKHARA UNIVERSITY" in text:
        found_pages.append(idx + 1)

print(f"Found 'Pokhara University' on pages: {found_pages}")
