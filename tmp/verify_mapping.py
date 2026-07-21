import os
import re

base_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm"

# 1. Read all chapter questions contents
chapter_texts = {}
for i in range(1, 7):
    path = os.path.join(base_dir, f"chap{i}", f"chap{i}-qns.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            chapter_texts[i] = f.read()

# 2. Define questions from reconstructed papers to check
papers = [
    "NumericalMethods_2023_PU_Spring.md",
    "NumericalMethods_2024_PU_Spring.md",
    "NumericalMethods_2025_PU_Spring.md"
]

all_found = True

for paper in papers:
    paper_path = os.path.join(base_dir, "past-qns/md", paper)
    print(f"\nVerifying questions in {paper}...")
    
    with open(paper_path, "r") as f:
        content = f.read()
        
    # Find all questions in the paper
    # These are lines starting with "a)", "b)", "c)" or "OR" or "i." etc.
    # We will search for sentences of length > 20
    lines = content.split("\n")
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # Match lines like "a) Explain...", "b) Find...", "OR", "i. One...", "ii. One..."
        if re.match(r"^([a-z]\)|OR|i{1,3}\.|[1-7]\.)\s+", line_clean):
            # Check if this question text exists in any of the chapter files
            # Extract a key sub-phrase of the question to search
            # We strip markdown formatting first
            phrase = re.sub(r"\*\*\[\d+(?:\s*x\s*\d+)?\]\*\*", "", line_clean)
            phrase = phrase.replace("a)", "").replace("b)", "").replace("c)", "").strip()
            phrase = re.sub(r"\s+", " ", phrase)
            
            if len(phrase) < 15:
                continue # Skip short headers/notes
                
            # Search in chapters
            found_in_chapters = []
            for ch_num, ch_text in chapter_texts.items():
                # Clean multiple spaces to match
                ch_text_clean = re.sub(r"\s+", " ", ch_text)
                # Search for the phrase
                if phrase in ch_text_clean:
                    found_in_chapters.append(ch_num)
                    
            if not found_in_chapters:
                print(f"  [MISSING] Question not found in any chapter file: \"{line_clean[:50]}...\"")
                all_found = False
            elif len(found_in_chapters) > 1:
                print(f"  [DUPLICATED] Question found in multiple chapters {found_in_chapters}: \"{line_clean[:50]}...\"")
                all_found = False
            else:
                print(f"  [OK] Question mapped to Chapter {found_in_chapters[0]}")

if all_found:
    print("\nVerification SUCCESSFUL: All questions are uniquely mapped!")
else:
    print("\nVerification FAILED: Some questions are missing or duplicated.")
