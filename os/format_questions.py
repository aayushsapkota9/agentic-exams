import json
import re
import os

def clean_question(text):
    # Remove leading numbering like "1.", "a)", "Q.", "1. a)"
    # Also remove trailing marks like "2x5", "7", "8"
    t = re.sub(r'^\s*(\d+[\.\)]|[a-zA-Z][\.\)]|Q\d+|\d+)\s*', '', text)
    t = re.sub(r'^\s*([a-zA-Z][\.\)])\s*', '', t) # Apply twice for '1. a)'
    t = re.sub(r'\s+\d+(?:[xX\*]\d+)?\s*$', '', t) # Trailing marks
    return t.strip()

def format_all_questions():
    base_dir = "/Users/aayushsapkota9/repos/agentic-exams/os"
    
    # We will read all chapX/chapX_questions.md files and clean them up
    for i in range(1, 8):
        ch_dir = f"chap{i}"
        if i == 2: ch_dir = "chap2"
        file_path = os.path.join(base_dir, ch_dir, f"chap{i}_questions.md")
        
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        cleaned_lines = []
        for line in lines:
            if line.startswith("#"):
                cleaned_lines.append(line)
            elif line.startswith("- "):
                # Extract image source
                match = re.search(r'\((IMG_\d+\.jpg)\)$', line.strip())
                img_src = match.group(1) if match else ""
                
                # Extract question part
                q_part = line[2:].rsplit('(', 1)[0].strip()
                cleaned_q = clean_question(q_part)
                
                if len(cleaned_q) > 10: # Ignore fragments
                    cleaned_lines.append(f"- {cleaned_q} ({img_src})\n")
            else:
                cleaned_lines.append(line)
                
        with open(file_path, 'w') as f:
            f.writelines(cleaned_lines)

if __name__ == "__main__":
    format_all_questions()
    print("Formatting complete.")
