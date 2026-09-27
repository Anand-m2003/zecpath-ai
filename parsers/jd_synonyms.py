SKILL_SYNONYMS = {
    "python": "Python",
    "python programming": "Python",
    "python developer": "Python",
    "flask": "Flask",
    "django": "Django",
    "fastapi": "FastAPI",
    "rest api": "REST API",
    "rest apis": "REST API",
    "restful api": "REST API",
    "sql": "SQL",
    "sql databases": "SQL",
    "git": "Git",
    "github": "GitHub",
    "docker": "Docker",
    "machine learning": "Machine Learning",
    "ml": "Machine Learning",
    "artificial intelligence": "Artificial Intelligence",
    "ai": "Artificial Intelligence"
}


ROLE_SYNONYMS = {
    "python programmer": "Python Developer",
    "python developer": "Python Developer",
    "backend developer": "Backend Developer",
    "back end developer": "Backend Developer",
    "software developer": "Software Developer",
    "software engineer": "Software Engineer",
    "data scientist": "Data Scientist",
    "machine learning engineer": "Machine Learning Engineer",
    "ml engineer": "Machine Learning Engineer",
    "frontend developer": "Frontend Developer",
    "front end developer": "Frontend Developer"
}


def normalize_skill(skill):
    """
    Normalize a skill using the synonym dictionary.
    """
    key = skill.strip().lower()

    return SKILL_SYNONYMS.get(skill.lower(), skill.strip())


def normalize_role(role):
    """
    Normalize a job role using the synonym dictionary.
    """
    key = role.strip().lower()

    return ROLE_SYNONYMS.get(key, role.strip())