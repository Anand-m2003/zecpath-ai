import re


SECTION_HEADINGS = {
    "PROFILE": "PROFILE",
    "SUMMARY": "SUMMARY",
    "PROFESSIONAL SUMMARY": "SUMMARY",
    "OBJECTIVE": "OBJECTIVE",
    "EDUCATION": "EDUCATION",
    "ACADEMIC QUALIFICATIONS": "EDUCATION",
    "SKILLS": "SKILLS",
    "TECHNICAL SKILLS": "SKILLS",
    "EXPERIENCE": "EXPERIENCE",
    "WORK EXPERIENCE": "EXPERIENCE",
    "PROFESSIONAL EXPERIENCE": "EXPERIENCE",
    "CERTIFICATIONS": "CERTIFICATIONS",
    "PROJECTS": "PROJECTS",
    "ACHIEVEMENTS": "ACHIEVEMENTS"
}


def normalize_bullets(text):
    """Convert common bullet symbols into a standard '- ' format."""
    text = re.sub(r"[•●▪◦‣►]", "-", text)
    return text


def normalize_headings(text):
    """Normalize common resume section headings."""
    lines = []

    for line in text.splitlines():
        cleaned = line.strip()
        heading = cleaned.upper().rstrip(":")

        if heading in SECTION_HEADINGS:
            lines.append(SECTION_HEADINGS[heading])
        else:
            lines.append(cleaned)

    return "\n".join(lines)


def clean_resume_text(text):
    """
    Clean and normalize extracted resume text.
    """
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Normalize bullet points
    text = normalize_bullets(text)

    # Remove unwanted control characters
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)

    # Normalize section headings
    text = normalize_headings(text)

    # Remove trailing spaces from each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove repeated blank lines
    cleaned_lines = []
    previous_blank = False

    for line in lines:
        if not line:
            if not previous_blank:
                cleaned_lines.append("")
            previous_blank = True
        else:
            cleaned_lines.append(line)
            previous_blank = False

    # Normalize excessive spaces
    result = "\n".join(cleaned_lines)
    result = re.sub(r"[ \t]+", " ", result)

    return result.strip()