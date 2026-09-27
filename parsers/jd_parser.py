import re

from parsers.jd_cleaner import normalize_jd_text
from parsers.jd_synonyms import normalize_skill, normalize_role


def extract_role(text):
    """
    Extract the job role from the first meaningful line.
    """
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if line and not line.endswith(":"):
            return normalize_role(line)

    return ""


def extract_experience(text):
    """
    Extract minimum years of experience.
    """
    patterns = [
        r"minimum\s+(\d+)\s*\+?\s*years?",
        r"(\d+)\s*\+\s*years?\s+of\s+experience",
        r"(\d+)\s*-\s*(\d+)\s*years?\s+of\s+experience"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return int(match.group(1))

    return 0


def extract_education(text):
    """
    Extract common bachelor's/master's degree requirements.
    """
    education = []

    patterns = [
        r"(Bachelor'?s)\s+degree\s+in\s+([^.\n]+)",
        r"(Master'?s)\s+degree\s+in\s+([^.\n]+)"
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)

        for degree, field in matches:
            education.append({
                "degree": degree,
                "field_of_study": field.strip()
            })

    return education


def extract_skills(text):
    """
    Extract skills using the synonym dictionary.
    """
    skills = []

    skill_patterns = [
        "python",
        "flask",
        "django",
        "fastapi",
        "rest api",
        "rest apis",
        "restful api",
        "sql",
        "sql databases",
        "git",
        "github",
        "docker",
        "machine learning",
        "ml",
        "artificial intelligence",
        "ai"
    ]

    text_lower = text.lower()

    for skill in skill_patterns:
        if skill in text_lower:
            normalized = normalize_skill(skill)

            if normalized not in skills:
                skills.append(normalized)

    return skills


def extract_preferred_skills(text):
    """
    Extract skills mentioned under the Preferred Skills section.
    """
    preferred = []

    match = re.search(
        r"Preferred Skills:(.*?)(?:Responsibilities:|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        section = match.group(1)
        preferred = extract_skills(section)

    return preferred


def extract_responsibilities(text):
    """
    Extract responsibilities from the Responsibilities section.
    """
    responsibilities = []

    match = re.search(
        r"Responsibilities:(.*)$",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        section = match.group(1)

        for line in section.splitlines():
            line = line.strip()

            if line.startswith("-"):
                responsibilities.append(line[1:].strip())

    return responsibilities


def build_job_profile(text):
    """
    Convert raw job description text into a structured job profile.
    """

    cleaned_text = normalize_jd_text(text)

    skills = extract_skills(cleaned_text)
    preferred_skills = extract_preferred_skills(cleaned_text)

    required_skills = [
        skill for skill in skills
        if skill not in preferred_skills
    ]

    job_profile = {
        "job_profile": {
            "job_id": "",
            "job_title": extract_role(cleaned_text),
            "department": "",
            "job_type": "",
            "location": "",
            "description": cleaned_text,
            "required_education": extract_education(cleaned_text),
            "required_experience": {
                "minimum_years": extract_experience(cleaned_text),
                "maximum_years": None
            },
            "required_skills": [
                {
                    "name": skill,
                    "category": "",
                    "importance": "required"
                }
                for skill in required_skills
            ],
            "preferred_skills": [
                {
                    "name": skill,
                    "category": ""
                }
                for skill in preferred_skills
            ],
            "responsibilities": extract_responsibilities(cleaned_text),
            "certifications": [],
            "salary_range": {
                "minimum": None,
                "maximum": None,
                "currency": ""
            }
        }
    }

    return job_profile


