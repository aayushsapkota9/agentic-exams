
import json
import os
import re

with open("/tmp/cleaned_questions.json", "r") as f:
    questions = json.load(f)

# Group by chapter
chapters = {i: [] for i in range(1, 11)}
for q in questions:
    ch = q["chapter"]
    if ch in chapters:
        chapters[ch].append(q)

chapter_names = {
    1: "Introduction",
    2: "ER and Relational Model",
    3: "Structured Query Language",
    4: "Relational Database Design",
    5: "Security",
    6: "Query Processing and Optimization",
    7: "Storage Management and Indexing",
    8: "Transactions and Concurrency Control",
    9: "Crash Recovery",
    10: "Emerging Trend in Databases"
}

# --- SQL SCHEMA DEFINITIONS ---

SCHEMAS = {
    "sailors": """-- Sailors, Boats, Reserves Setup
CREATE TABLE IF NOT EXISTS Sailors (sid INT PRIMARY KEY, sname VARCHAR(50), rating INT, age INT);
CREATE TABLE IF NOT EXISTS Boats (bid INT PRIMARY KEY, bname VARCHAR(50), color VARCHAR(20));
CREATE TABLE IF NOT EXISTS Reserves (sid INT, bid INT, day INT, PRIMARY KEY (sid, bid, day), FOREIGN KEY (sid) REFERENCES Sailors(sid), FOREIGN KEY (bid) REFERENCES Boats(bid));
INSERT INTO Sailors VALUES (1, 'Ram', 7, 22), (2, 'Sita', 4, 25), (3, 'Hari', 8, 30), (4, 'Laxman', 9, 19);
INSERT INTO Boats VALUES (20, 'Interlake', 'Blue'), (25, 'Marine', 'Black'), (75, 'Speedy', 'Yellow');
INSERT INTO Reserves VALUES (1, 25, 3), (2, 75, 5), (4, 20, 1);""",

    "hotel_details": """-- Hotel Details Setup
CREATE TABLE IF NOT EXISTS Hotel_details (hotel_id INT PRIMARY KEY, hotel_name VARCHAR(100), est_year INT, hotel_star INT, hotel_worth DECIMAL(15, 2));
INSERT INTO Hotel_details VALUES (1, 'Hyatt', 2047, 5, 15000000), (2, 'Hotel Ktm', 2043, 3, 5000000), (3, 'Fulbari', 2058, 5, 20000000), (4, 'Yak and Yeti', 2052, 4, 11000000), (5, 'Hotel Chitwan', 2055, 3, 7000000);""",

    "doctors": """-- Doctors, Patients, Hospitals Setup
CREATE TABLE IF NOT EXISTS Doctors (DoctorID INT PRIMARY KEY, DoctorName VARCHAR(50), Department VARCHAR(50), Address VARCHAR(100), Salary DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS Patients (PatientID INT PRIMARY KEY, PatientName VARCHAR(50), Address VARCHAR(100), Age INT, Gender VARCHAR(10));
CREATE TABLE IF NOT EXISTS Hospitals (PatientID INT, DoctorID INT, HospitalName VARCHAR(100), Location VARCHAR(100), PRIMARY KEY (PatientID, DoctorID));
INSERT INTO Doctors VALUES (1, 'Dr. Sharma', 'Surgery', 'Kathmandu', 60000), (2, 'Dr. Bhatta', 'Cardiology', 'Pokhara', 45000);
INSERT INTO Patients VALUES (1, 'Rita', 'Pokhara', 25, 'Female'), (2, 'Mina', 'Kathmandu', 40, 'Female');
INSERT INTO Hospitals VALUES (1, 2, 'Ciwat', 'Pokhara'), (2, 1, 'Teaching', 'Kathmandu');""",

    "employee": """-- Employee, Project, Works_On Setup
CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID INT PRIMARY KEY, Employee_Name VARCHAR(50), Department VARCHAR(50));
CREATE TABLE IF NOT EXISTS PROJECT (Project_ID INT PRIMARY KEY, Project_Title VARCHAR(100), Budget DECIMAL(15, 2));
CREATE TABLE IF NOT EXISTS WORKS_ON (Employee_ID INT, Project_ID INT, Hours_Worked INT, PRIMARY KEY (Employee_ID, Project_ID));
INSERT INTO EMPLOYEE VALUES (101, 'Aayush', 'Database'), (102, 'Rohan', 'Management'), (103, 'Sapkota', 'HR');
INSERT INTO PROJECT VALUES (1, 'AI Development', 750000), (2, 'Legacy Migration', 600000), (3, 'System Upgrade', 300000);
INSERT INTO WORKS_ON VALUES (101, 1, 40), (102, 1, 20), (103, 3, 10);""",

    "student": """-- Student, Course, Enrolls_In Setup
CREATE TABLE IF NOT EXISTS STUDENT (Student_ID INT PRIMARY KEY, Student_name VARCHAR(50), Major VARCHAR(50));
CREATE TABLE IF NOT EXISTS COURSE (Course_ID INT PRIMARY KEY, Course_name VARCHAR(100), Credits INT);
CREATE TABLE IF NOT EXISTS ENROLLS_IN (Student_ID INT, Course_ID INT, Grade VARCHAR(2), PRIMARY KEY (Student_ID, Course_ID));
INSERT INTO STUDENT VALUES (1, 'Milan', 'CS'), (2, 'Sangeeta', 'IT'), (3, 'Binod', 'CS');
INSERT INTO COURSE VALUES (101, 'Database', 3), (102, 'Advanced Physics', 4), (103, 'Computing', 3);
INSERT INTO ENROLLS_IN VALUES (1, 101, 'A'), (2, 101, 'B'), (1, 102, 'B'), (3, 103, 'A');""",

    "liquors_info": """-- Liquors Info Setup
CREATE TABLE IF NOT EXISTS Liquors_Info (Serial_No INT PRIMARY KEY, Liquors VARCHAR(50), Start_year INT, Bottles INT, Ready_year INT);
INSERT INTO Liquors_Info VALUES (1, 'Gorkha', 1997, 10, 1998), (2, 'Divine Wine', 1998, 5, 2000), (3, 'Old Durbar', 1997, 12, 2001), (4, 'Khukuri Rum', 1991, 10, 1992), (5, 'Xing', 1994, 5, 1995);""",

    "actress_details": """-- Actress Details Setup
CREATE TABLE IF NOT EXISTS Actress_Details (Player_id INT PRIMARY KEY, Actress_name VARCHAR(50), Debut_year INT, Recent_release VARCHAR(50), Actress_fee DECIMAL(15, 2));
INSERT INTO Actress_Details VALUES (1, 'Renu', 2010, 'Samay', 400000), (2, 'Sita', 2022, 'Radha', 300000), (3, 'Geeta', 2001, 'Mato', 600000), (4, 'Amita', 1990, 'Man', 700000), (5, 'Karishma', 1989, 'Prem', 100000);"""
}

def get_sql_setup(text):
    text_l = text.lower()
    for key, sql in SCHEMAS.items():
        if key in text_l:
            return sql
    # Fallback for generic SQL questions if relevant
    if "sql" in text_l or "relational algebra" in text_l:
        # Default to sailors if it's a join/base question
        if any(x in text_l for x in ["join", "select", "where", "from"]):
             return SCHEMAS["sailors"]
    return None

# --- GENERATION ---

def slugify(text):
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug

def generate_chapter_md(ch_num, qns):
    title = chapter_names[ch_num]
    md = f"# Chapter {ch_num}: {title}\n\n"
    
    def label_key(l):
        m = re.match(r"(\d+)\(([a-z]+)\)", l)
        if m: return (int(m.group(1)), m.group(2))
        m = re.match(r"(\d+)", l)
        if m: return (int(m.group(1)), "")
        return (99, l)
    
    labels = sorted(list(set(q["label"] for q in qns)), key=label_key)
    
    # Quick Navigation
    if labels:
        md += "### Quick Navigation\n"
        nav_links = [f"[{label}](#{slugify(label)})" for label in labels]
        md += " | ".join(nav_links) + "\n\n---\n\n"
    
    for label in labels:
        md += f"## {label}\n\n"
        label_qns = [q for q in qns if q["label"] == label]
        label_qns.sort(key=lambda x: str(x["year"]), reverse=True)
        
        for q in label_qns:
            raw_text = q.get("raw", "").strip()
            marks_match = re.search(r'\((\d+)\)|\[(\d+)\]', raw_text)
            marks = marks_match.group(1) or marks_match.group(2) if marks_match else "?"
            
            md += f"##### {q['year']} [{marks}]\n\n"
            
            # Question Block
            md += "```markdown\n"
            md += f"{raw_text}\n"
            md += "```\n\n"
            
            # SQL Setup Block (NEW)
            sql_setup = get_sql_setup(raw_text)
            if sql_setup:
                md += "```sql\n"
                md += f"{sql_setup}\n"
                md += "```\n\n"
            
            md += "---\n\n"
            
    return md

for i in range(1, 11):
    content = generate_chapter_md(i, chapters[i])
    filepath = f"dbms/chap{i}/chap{i}-qns.md"
    with open(filepath, "w") as f:
        f.write(content)

print("Regenerated all chapters with embedded SQL setup blocks.")
