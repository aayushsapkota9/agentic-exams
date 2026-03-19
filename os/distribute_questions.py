import json
import re
import os

# Define keywords for each unit based on the syllabus
SYLLABUS_KEYWORDS = {
    1: ["introduction", "monolithic", "layered", "microkernel", "evolution", "history"],
    2: ["process", "thread", "pcb", "context switch", "ipc", "synchronization", "mutual exclusion", "semaphore", "monitor", "scheduling", "fcfs", "sjf", "rr", "quantum", "priority", "hrrn", "producer", "consumer", "reader", "writer", "dining philosopher", "tsl"],
    3: ["memory", "allocation", "fragmentation", "paging", "segmentation", "virtual memory", "page replacement", "fifo", "lru", "clock"],
    4: ["kernel architecture", "types of kernel", "kernel", "context switching"], # Be careful with context switching as it overlaps with chap 2. Chap 2 is usually more detailed.
    5: ["i/o management", "dma", "interrupt", "deadlock", "banker's", "raid", "prevention", "avoidance", "detection", "recovery"],
    6: ["file system", "directory", "access method", "protection", "contiguous", "linked", "index node"],
    7: ["real-time", "distributed", "cloud", "mobile operating"]
}

def identify_chapter(question_text):
    text_lower = question_text.lower()
    scores = {i: 0 for i in range(1, 8)}
    
    for chapter, keywords in SYLLABUS_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[chapter] += 1
                
    # Default to chapter 2 if we found scheduling table numbers without words but that's hard to catch.
    # Let's find the max score.
    max_score = max(scores.values())
    if max_score == 0:
        return None # Could not identify
        
    # Get chapter with max score
    best_chapter = max(scores, key=scores.get)
    return best_chapter

def parse_and_distribute(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        
    chapters = {i: [] for i in range(1, 8)}
    unclassified = []
    
    for img_name, text in data.items():
        # Split text into rough questions or chunks based on numbering like "1.", "a)", "Q."
        # This is a simple heuristic as OCR output varies
        lines = text.split('\n')
        current_question = ""
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Very basic check for a new question start (e.g., "1.", "1)", "a)", "Q1")
            if re.match(r"^(\d+[\.\)]|[a-zA-Z][\.\)]|Q\d+|\d+)\s+", line):
                if current_question:
                    chapter = identify_chapter(current_question)
                    if chapter:
                        chapters[chapter].append((current_question, img_name))
                    else:
                        unclassified.append((current_question, img_name))
                current_question = line
            else:
                current_question += " " + line
                
        # Last question
        if current_question:
            chapter = identify_chapter(current_question)
            if chapter:
                chapters[chapter].append((current_question, img_name))
            else:
                unclassified.append((current_question, img_name))

    # Write to files
    base_dir = "/Users/aayushsapkota9/repos/agentic-exams/os"
    for ch_num, qns in chapters.items():
        if not qns: continue
        ch_dir = f"chap{ch_num}"
        if ch_num == 2: ch_dir = "chap2"
        os.makedirs(os.path.join(base_dir, ch_dir), exist_ok=True)
        
        # Append to existing or create new
        output_file = os.path.join(base_dir, ch_dir, f"chap{ch_num}_questions.md")
        # We know we already have some in chap2, so we'll just write whatever we found.
        # But we don't want to overwrite manual curations if they exist.
        mode = 'w'
        
        with open(output_file, mode) as f:
            f.write(f"# Chapter {ch_num} Past Questions (Extracted)\n\n")
            # De-duplicate basic strings
            seen = set()
            for q, img in qns:
                clean_q = re.sub(r'^\d+\.\s*', '', q.strip())
                if clean_q not in seen and len(clean_q) > 10: # avoid tiny fragments
                    seen.add(clean_q)
                    f.write(f"- {clean_q} ({img})\n")
                    
    print(f"Extraction complete. Unclassified chunks: {len(unclassified)}")
    with open("unclassified_questions.txt", "w") as f:
        for u, img in unclassified:
            f.write(f"[{img}] {u}\n")

if __name__ == "__main__":
    parse_and_distribute("extracted_text_all.json")
