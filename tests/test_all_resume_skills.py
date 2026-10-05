from pathlib import Path

from parsers.skill_extractor import extract_skills


def test_all_resume_skill_extraction():
    resume_folder = Path("data/sample_resumes")
    resumes = list(resume_folder.glob("*.txt"))

    assert len(resumes) == 10

    for resume in resumes:
        text = resume.read_text(encoding="utf-8")
        skills = extract_skills(text)

        assert skills