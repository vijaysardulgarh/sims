import re

# -------------------------------
# Subjects ignored for CBSE enrollment
# -------------------------------
IGNORED_SUBJECTS = {
    "GENERAL AWARENESS & LIFE SKILLS",
    "SPORTS AND GAMES",
    "CULTURAL LITERACY SCIENTIFIC ACTIVITIES NCC SCOUTS AND GUIDES",
}

# -------------------------------
# CBSE Medium of Instruction Codes
# -------------------------------
MEDIUM_CODE_MAP = {
    "ENGLISH": "1",
    "HINDI": "2",
    "URDU": "3",
    "PUNJABI": "4",
    "BENGALI": "5",
    "TAMIL": "6",
    "TELUGU": "7",
    "MARATHI": "8",
    "GUJARATI": "9",
    "KANNADA": "10",
    "MALAYALAM": "11",
    "ORIYA": "12",
    "ASSAMESE": "13",
    "NEPALI": "14",
    "SANSKRIT": "15",
    "OTHER": "99",
}

# -------------------------------
# CBSE Slot Subject Mapping
# -------------------------------
SUBJECT_CODE_MAP = {
    "sub1": {"ENGLISH": "English"},
    "sub2": {"HINDI": "Hindi", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"},
    "sub3": {
        "MATHEMATICS": "Mathematics",
        "PHYSICS": "Physics",
        "CHEMISTRY": "Chemistry",
        "BIOLOGY": "Biology",
        "ECONOMICS": "Economics",
        "ACCOUNTANCY": "Accountancy",
        "BUSINESS": "Business Studies",
        "POLITICAL SCIENCE": "Political Science",
        "GEOGRAPHY": "Geography",
        "PSYCHOLOGY": "Psychology",
        "HIND MUSIC.VOCAL": "Hind Music Vocal",
        "PAINTING": "Painting",
        "PHYSICAL EDUCATION": "Physical Education",
        "HOME SCIENCE": "Home Science",
    },
    "sub4": {  # Additional academic subjects
        "MATHEMATICS": "Mathematics",
        "PHYSICS": "Physics",
        "CHEMISTRY": "Chemistry",
        "BIOLOGY": "Biology",
        "ECONOMICS": "Economics",
        "ACCOUNTANCY": "Accountancy",
        "BUSINESS": "Business Studies",
        "POLITICAL SCIENCE": "Political Science",
        "GEOGRAPHY": "Geography",
        "PSYCHOLOGY": "Psychology",
        "HIND MUSIC.VOCAL": "Hind Music Vocal",
        "PAINTING": "Painting",
        "PHYSICAL EDUCATION": "Physical Education",
        "HOME SCIENCE": "Home Science",
    },
    "sub5": {  # Optional/extra
        "MATHEMATICS": "Mathematics",
        "PHYSICS": "Physics",
        "CHEMISTRY": "Chemistry",
        "BIOLOGY": "Biology",
        "ECONOMICS": "Economics",
        "ACCOUNTANCY": "Accountancy",
        "BUSINESS": "Business Studies",
        "POLITICAL SCIENCE": "Political Science",
        "GEOGRAPHY": "Geography",
        "PSYCHOLOGY": "Psychology",
        "HIND MUSIC.VOCAL": "Hind Music Vocal",
        "PAINTING": "Painting",
        "PHYSICAL EDUCATION": "Physical Education",
        "HOME SCIENCE": "Home Science",
    },
    "sub6": {"AUTOMOTIVE": "Automotive", "BEAUTY & WELLNESS": "Beauty & Wellness"},
    "sub7": {
        "PUNJABI": "Punjabi",
        "SANSKRIT": "Sanskrit",
        "DRAWING": "Painting",
        "PAINTING": "Painting",
        "HOME SCIENCE": "Home Science",
        "MUSIC HINDUSTANI VOCAL (MHV)": "Music Hindustani Vocal",
    },
}

# -------------------------------
# Helper: Clean subject names
# -------------------------------
def extract_subject_name(raw_subject: str) -> str:
    if not raw_subject:
        return ""
    parts = raw_subject.split(":", 1)
    subject = parts[1] if len(parts) == 2 else raw_subject
    return subject.strip().upper()

# -------------------------------
# Convert student's subjects to CBSE slots
# -------------------------------
def convert_subjects_to_cbse_slots(student_subjects):
    """
    Assign **only one subject per CBSE slot** for PDF and CSV.
    """
    slots = {f"sub{i}": "" for i in range(1, 8)}
    if not student_subjects:
        return slots

    cleaned_subjects = [extract_subject_name(s) for s in student_subjects]
    used_subjects = set()

    # Sub1: English
    for s in cleaned_subjects:
        if s == "ENGLISH" and s not in used_subjects:
            slots["sub1"] = "English"
            used_subjects.add(s)
            break

    # Sub2: Hindi / Punjabi / Sanskrit
    for s in cleaned_subjects:
        if s in ("HINDI", "PUNJABI", "SANSKRIT") and s not in used_subjects:
            slots["sub2"] = SUBJECT_CODE_MAP["sub2"][s]
            used_subjects.add(s)
            break

    # Sub3–Sub5: Academic / Core subjects
    for slot in ["sub3", "sub4", "sub5"]:
        for s in cleaned_subjects:
            if s in SUBJECT_CODE_MAP[slot] and s not in used_subjects:
                slots[slot] = SUBJECT_CODE_MAP[slot][s]
                used_subjects.add(s)
                break

    # Sub6: Vocational
    for s in cleaned_subjects:
        if s in SUBJECT_CODE_MAP["sub6"] and s not in used_subjects:
            slots["sub6"] = SUBJECT_CODE_MAP["sub6"][s]
            used_subjects.add(s)
            break

    # Sub7: Optional / Art / Home Science / Music
    for s in cleaned_subjects:
        if s in SUBJECT_CODE_MAP["sub7"] and s not in used_subjects:
            slots["sub7"] = SUBJECT_CODE_MAP["sub7"][s]
            used_subjects.add(s)
            break

    return slots

# -------------------------------
# Get medium code from section
# -------------------------------
def get_medium_from_section(section_name: str) -> str:
    if not section_name:
        return "1"
    match = re.search(r"\((.*?)\)", section_name)
    if match:
        medium_text = match.group(1).strip().upper()
        return MEDIUM_CODE_MAP.get(medium_text, "1")
    return "1"
