def build_skill_output(skills):
    """
    Build a structured skill output.
    """
    return {
        "skills": skills,
        "total_skills": len(skills)
    }