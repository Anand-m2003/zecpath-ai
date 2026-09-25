from parsers.resume_parser import extract_resume_text


def test_docx_extraction():
    file_path = "data/test_resumes/test_resume.docx"

    text = extract_resume_text(file_path)

    print("\n--- Extracted Resume Text ---")
    print(text)

    assert text
    assert "JOHN DOE" in text
    assert "Python Developer" in text
    assert "EDUCATION" in text
    assert "PROJECTS" in text