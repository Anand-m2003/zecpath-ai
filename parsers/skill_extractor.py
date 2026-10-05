import re

from parsers.skill_dictionary import MASTER_SKILL_DICTIONARY
from parsers.skill_synonyms import SKILL_SYNONYMS, normalize_skill, expand_skill_stack


def extract_skills(text):
    """
    Extract, normalize, deduplicate and score skills from resume text.
    """
    text_lower = text.lower()
    extracted_skills = {}

    # Direct skill matches
    for skill in MASTER_SKILL_DICTIONARY:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text_lower):
            normalized = MASTER_SKILL_DICTIONARY[skill]
            extracted_skills[normalized] = 1.0

    # Skill synonym matches
    for synonym in SKILL_SYNONYMS:
        pattern = r"\b" + re.escape(synonym) + r"\b"

        if re.search(pattern, text_lower):
            normalized = normalize_skill(synonym)

            if normalized not in extracted_skills:
                extracted_skills[normalized] = 0.9

    # Skill stack matches
    for stack in ["mern", "mean", "lamp"]:
        pattern = r"\b" + re.escape(stack) + r"\b"

        if re.search(pattern, text_lower):
            for skill in expand_skill_stack(stack):
                if skill not in extracted_skills:
                    extracted_skills[skill] = 0.85

    return [
        {
            "skill": skill,
            "confidence": confidence
        }
        for skill, confidence in extracted_skills.items()
    ]