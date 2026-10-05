from parsers.resume_section_classifier import classify_resume_sections


def test_resume_section_classification():
    resume_text = """
    CANDIDATE NAME: Arjun Menon

    EDUCATION:
    Bachelor of Computer Applications (BCA)
    University of Kerala

    EXPERIENCE:
    Python Developer - TechSoft Solutions
    Developed REST APIs using Python and Flask.

    SKILLS:
    Python, Flask, SQL, Git

    CERTIFICATIONS:
    Python Programming Certification

    PROJECTS:
    Employee Management System using Flask.
    """

    sections = classify_resume_sections(resume_text)

    assert "Bachelor of Computer Applications (BCA)" in sections["education"]
    assert "Python Developer - TechSoft Solutions" in sections["work_experience"]
    assert "Python, Flask, SQL, Git" in sections["skills"]
    assert "Python Programming Certification" in sections["certifications"]
    assert "Employee Management System using Flask." in sections["projects"]