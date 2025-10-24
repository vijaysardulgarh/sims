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
# SUBJECT_PRIORITY merged with codes (Ninth & Eleventh streams)
# -------------------------------
SUBJECT_PRIORITY = {
    "Ninth": {
        "default": {
            "sub1": {"priority": ["ENGLISH"], "codes": {"ENGLISH": "English"}},
            "sub2": {"priority": ["HINDI", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI": "Hindi", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}},
            "sub3": {"priority": ["MATHEMATICS"], "codes": {"MATHEMATICS": "Mathematics"}},
            "sub4": {"priority": ["SCIENCE & TECHNOLOGY"], "codes": {"SCIENCE & TECHNOLOGY": "Science & Technology"}},
            "sub5": {"priority": ["SOCIAL SCIENCE"], "codes": {"SOCIAL SCIENCE": "Social Science"}},
            "sub6": {"priority": ["HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}},
            "sub7": {"priority": ["HINDI", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI": "Hindi", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}}
        }
    },
    "Eleventh": {
        "Science": {
            "sub1": {"priority": ["ENGLISH (CORE)"], "codes": {"ENGLISH (CORE)": "English (Core)"}},
            "sub2": {"priority": ["HINDI (CORE)", "CHEMISTRY", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI (CORE)": "Hindi (Core)", "CHEMISTRY": "Chemistry",
                               "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}},
            "sub3": {"priority": ["PHYSICS"], "codes": {"PHYSICS": "Physics"}},
            "sub4": {"priority": ["CHEMISTRY", "AUTOMOTIVE", "BEAUTY & WELLNESS"],
                     "codes": {"CHEMISTRY": "Chemistry", "AUTOMOTIVE": "Automotive", "BEAUTY & WELLNESS": "Beauty & Wellness"}},
            "sub5": {"priority": ["MATHEMATICS", "BIOLOGY"], "codes": {"MATHEMATICS": "Mathematics", "BIOLOGY": "Biology"}},
            "sub6": {"priority": ["MATHEMATICS", "BIOLOGY", "HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"MATHEMATICS": "Mathematics", "BIOLOGY": "Biology",
                               "HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}}
        },
        "Commerce": {
            "sub1": {"priority": ["ENGLISH (CORE)"], "codes": {"ENGLISH (CORE)": "English (Core)"}},
            "sub2": {"priority": ["HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}},
            "sub3": {"priority": ["ACCOUNTANCY"], "codes": {"ACCOUNTANCY": "Accountancy"}},
            "sub4": {"priority": ["BUSINESS STUDIES"], "codes": {"BUSINESS STUDIES": "Business Studies"}},
            "sub5": {"priority": ["ECONOMICS", "MATHEMATICS"],
                     "codes": {"ECONOMICS": "Economics", "MATHEMATICS": "Mathematics"}},
            "sub6": {"priority": ["HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}}
        },
        "Arts": {
            "sub1": {"priority": ["ENGLISH (CORE)"], "codes": {"ENGLISH (CORE)": "English (Core)"}},
            "sub2": {"priority": ["HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}},
            "sub3": {"priority": ["POLITICAL SCIENCE", "ECONOMICS", "PSYCHOLOGY", "PHYSICAL EDUCATION", "AUTOMOTIVE", "BEAUTY & WELLNESS"],
                     "codes": {"POLITICAL SCIENCE": "Political Science", "ECONOMICS": "Economics",
                               "PSYCHOLOGY": "Psychology", "PHYSICAL EDUCATION": "Physical Education",
                               "AUTOMOTIVE": "Automotive", "BEAUTY & WELLNESS": "Beauty & Wellness"}},
            "sub4": {"priority": ["GEOGRAPHY", "ECONOMICS", "PSYCHOLOGY", "PHYSICAL EDUCATION", "AUTOMOTIVE", "BEAUTY & WELLNESS"],
                     "codes": {"GEOGRAPHY": "Geography", "ECONOMICS": "Economics", "PSYCHOLOGY": "Psychology",
                               "PHYSICAL EDUCATION": "Physical Education", "AUTOMOTIVE": "Automotive",
                               "BEAUTY & WELLNESS": "Beauty & Wellness"}},
            "sub5": {"priority": ["FINE ARTS", "AUTOMOTIVE", "BEAUTY & WELLNESS", "ECONOMICS", "PSYCHOLOGY", "PHYSICAL EDUCATION"],
                     "codes": {"FINE ARTS": "Fine Arts", "AUTOMOTIVE": "Automotive",
                               "BEAUTY & WELLNESS": "Beauty & Wellness", "ECONOMICS": "Economics",
                               "PSYCHOLOGY": "Psychology", "PHYSICAL EDUCATION": "Physical Education"}},
            "sub6": {"priority": ["POLITICAL SCIENCE", "ECONOMICS", "PSYCHOLOGY", "PHYSICAL EDUCATION", "AUTOMOTIVE", "BEAUTY & WELLNESS", "GEOGRAPHY", "FINE ARTS", "HINDI (CORE)", "PUNJABI", "SANSKRIT"],
                     "codes": {"POLITICAL SCIENCE": "Political Science", "ECONOMICS": "Economics", "PSYCHOLOGY": "Psychology",
                               "PHYSICAL EDUCATION": "Physical Education", "AUTOMOTIVE": "Automotive", "BEAUTY & WELLNESS": "Beauty & Wellness",
                               "GEOGRAPHY": "Geography", "FINE ARTS": "Fine Arts", "HINDI (CORE)": "Hindi (Core)", "PUNJABI": "Punjabi", "SANSKRIT": "Sanskrit"}}
        }
    }
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
def convert_subjects_to_cbse_slots(student_class, stream, student_subjects):
    slots = {f"sub{i}": "" for i in range(1, 8)}
    if not student_subjects:
        return slots

    cleaned_subjects = [extract_subject_name(s) for s in student_subjects]
    used_subjects = set()

    # Determine slot mapping
    if student_class.upper() in ("NINTH", "9TH"):
        slot_map = SUBJECT_PRIORITY.get("Ninth", {}).get("default", {})
    else:
        slot_map = SUBJECT_PRIORITY.get("Eleventh", {}).get(stream, {})

    for slot, info in slot_map.items():
        priority_list = info.get("priority", [])
        codes = info.get("codes", {})

        # Pick first available from priority
        for subj in priority_list:
            for s in cleaned_subjects:
                if s.upper() == subj.upper() and s not in used_subjects:
                    slots[slot] = codes.get(subj.upper(), s)
                    used_subjects.add(s)
                    break
            if slots[slot]:
                break

        # If nothing matched, try any code
        if not slots[slot]:
            for s in cleaned_subjects:
                if s.upper() in codes and s not in used_subjects:
                    slots[slot] = codes[s.upper()]
                    used_subjects.add(s)
                    break

    return slots

# -------------------------------
# Mark invalid subjects as ❌
# -------------------------------
def mark_invalid_subjects(student_class, stream, subs):
    marked = {}
    if student_class.upper() in ("NINTH", "9TH"):
        rules = {k: v["priority"] for k, v in SUBJECT_PRIORITY.get("Ninth", {}).get("default", {}).items()}
    else:
        rules = {k: v["priority"] for k, v in SUBJECT_PRIORITY.get("Eleventh", {}).get(stream, {}).items()}

    for key, val in subs.items():
        if key not in rules or not rules[key]:
            marked[key] = val
        elif val.upper() not in [v.upper() for v in rules[key]]:
            marked[key] = f"{val} ❌"
        else:
            marked[key] = val
    return marked

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


def get_student_cbse_subjects(student, mark_invalid=False):
    """
    Returns CBSE slot mapping for a student ready for CSV/PDF export.
    If mark_invalid=True, invalid subjects are flagged with ❌
    """
    student_class = getattr(student, "studentclass", "")
    stream = getattr(student, "stream", "")  # For 11th
    student_subjects = (getattr(student, "subjects_opted", "") or "").split(",")

    # Convert subjects to CBSE slots
    slots = convert_subjects_to_cbse_slots(student_class, stream, student_subjects)

    # Mark invalid subjects if requested
    if mark_invalid:
        slots = mark_invalid_subjects(student_class, stream, slots)

    return slots