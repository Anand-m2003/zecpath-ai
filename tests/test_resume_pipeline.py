from parsers.resume_parser import extract_resume_text
from parsers.text_output import save_extracted_text


def test_docx_pipeline():
    file_path = "data/test_resumes/test_resume.docx"

    text = extract_resume_text(file_path)
    output_file = save_extracted_text(text, file_path)

    assert text
    assert output_file.exists()


def test_pdf_pipeline():
    file_path = "data/test_resumes/test_resume.pdf"

    text = extract_resume_text(file_path)
    output_file = save_extracted_text(text, file_path)

    assert text
    assert output_file.exists()