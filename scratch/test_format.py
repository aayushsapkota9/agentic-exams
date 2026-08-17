import sys
sys.path.append('/Users/aayushsapkota9/repos/oxford/agentic-exams/applied-maths/scratch')
import format_latex
import difflib

filepath = '/Users/aayushsapkota9/repos/oxford/agentic-exams/applied-maths/past-qns/md/PU_AppliedMaths_31_Computer.md'
with open(filepath, 'r') as f:
    orig = f.read()

new = format_latex.process_file_content(orig)

print("Original length:", len(orig))
print("New length:", len(new))

diff = list(difflib.unified_diff(orig.splitlines(), new.splitlines()))
print("Diff lines count:", len(diff))
for line in diff[:10]:
    print(line)
