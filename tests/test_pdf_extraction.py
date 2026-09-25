from parsers.resume_parser import extract_resume_text


def test_pdf_extraction():
    file_path = "data/test_resumes/test_resume.pdf"

    text = extract_resume_text(file_path)

    print("\n--- Extracted PDF Resume Text ---")
    print(text)

    assert text
    assert "JOHN DOE" in text
    assert "SUMMARY" in text
    assert "SKILLS" in text
    assert "EXPERIENCE" in text
    assert "EDUCATION" in text
    assert "PROJECTS" in text