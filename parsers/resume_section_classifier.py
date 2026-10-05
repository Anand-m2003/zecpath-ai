import re


SECTION_ALIASES = {
    "skills": [
        "skills",
        "technical skills",
        "key skills",
        "core skills",
        "technical expertise"
    ],
    "work_experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history"
    ],
    "education": [
        "education",
        "academic background",
        "educational qualifications",
        "academic qualifications"
    ],
    "certifications": [
        "certifications",
        "certificates",
        "professional certifications"
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "professional projects"
    ]
}


NON_TARGET_SECTIONS = [
    "summary",
    "profile",
    "objective",
    "career objective",
    "achievements",
    "awards",
    "languages",
    "interests",
    "references"
]


def normalize_heading(line):
    """Normalize a possible section heading."""
    line = line.strip().lower()
    line = re.sub(r"[:\-]+$", "", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def detect_section_heading(line):
    """
    Detect whether a line represents a known resume section.
    Returns the normalized section name or None.
    """
    heading = normalize_heading(line)

    for section, aliases in SECTION_ALIASES.items():
        if heading in aliases:
            return section

    return None


def classify_resume_sections(text):
    """
    Divide resume text into structured sections.
    """
    sections = {
        "skills": [],
        "work_experience": [],
        "education": [],
        "certifications": [],
        "projects": []
    }

    current_section = None

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        detected_section = detect_section_heading(line)

        if detected_section:
            current_section = detected_section
            continue

        normalized_line = normalize_heading(line)

        if normalized_line in NON_TARGET_SECTIONS:
            current_section = None
            continue

        if current_section:
            sections[current_section].append(line)

    return sections


def get_section_text(sections, section_name):
    """Return section content as a single string."""
    return "\n".join(sections.get(section_name, []))