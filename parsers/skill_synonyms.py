SKILL_SYNONYMS = {
    # Python
    "python programming": "Python",
    "python development": "Python",
    "py": "Python",

    # JavaScript
    "js": "JavaScript",
    "javascript programming": "JavaScript",

    # Machine Learning
    "ml": "Machine Learning",
    "machine-learning": "Machine Learning",

    # Artificial Intelligence
    "ai": "Artificial Intelligence",
    "artificial-intelligence": "Artificial Intelligence",

    # NLP
    "natural language processing": "NLP",

    # Power BI
    "powerbi": "Power BI",
    "power-bi": "Power BI",

    # Scikit-learn
    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",

    # Node.js
    "nodejs": "Node.js",
    "node js": "Node.js"
}


SKILL_STACKS = {
    "mern": [
        "MongoDB",
        "Express.js",
        "React",
        "Node.js"
    ],
    "mean": [
        "MongoDB",
        "Express.js",
        "Angular",
        "Node.js"
    ],
    "lamp": [
        "Linux",
        "Apache",
        "MySQL",
        "PHP"
    ]
}


def normalize_skill(skill):
    """Normalize a skill using the synonym dictionary."""
    key = skill.strip().lower()

    if key in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[key]

    return skill.strip()


def expand_skill_stack(skill):
    """Expand a recognized technology stack into individual skills."""
    key = skill.strip().lower()

    if key in SKILL_STACKS:
        return SKILL_STACKS[key]

    return [skill.strip()]