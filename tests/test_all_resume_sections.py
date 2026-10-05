from pathlib import Path
from parsers.resume_section_classifier import classify_resume_sections


def test_all_resume_sections():
    resume_folder = Path("data/sample_resumes")

    resumes = list(resume_folder.glob("*.txt"))

    assert len(resumes) == 10

    for resume in resumes:
        text = resume.read_text(encoding="utf-8")
        sections = classify_resume_sections(text)

        assert sections["education"]
        assert sections["work_experience"]
        assert sections["skills"]
        assert sections["certifications"]
        assert sections["projects"]