from parsers.skill_extractor import extract_skills
from parsers.skill_output import build_skill_output


def test_skill_extraction():
    resume_text = """
    Python developer with experience in Flask and SQL.
    Worked with machine learning and Power BI.
    """

    skills = extract_skills(resume_text)

    skill_names = [item["skill"] for item in skills]

    assert "Python" in skill_names
    assert "Flask" in skill_names
    assert "SQL" in skill_names
    assert "Machine Learning" in skill_names
    assert "Power BI" in skill_names


def test_skill_confidence():
    resume_text = "Experienced in Python and ML."

    skills = extract_skills(resume_text)

    skill_data = {item["skill"]: item["confidence"] for item in skills}

    assert skill_data["Python"] == 1.0
    assert skill_data["Machine Learning"] == 0.9


def test_skill_stack():
    resume_text = "Experienced in MERN stack."

    skills = extract_skills(resume_text)

    skill_names = [item["skill"] for item in skills]

    assert "MongoDB" in skill_names
    assert "Express.js" in skill_names
    assert "React" in skill_names
    assert "Node.js" in skill_names


def test_structured_skill_output():
    skills = [
        {
            "skill": "Python",
            "confidence": 1.0
        }
    ]

    output = build_skill_output(skills)

    assert output["total_skills"] == 1
    assert output["skills"][0]["skill"] == "Python"