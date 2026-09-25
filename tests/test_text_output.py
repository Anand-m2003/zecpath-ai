from parsers.resume_parser import extract_resume_text
from parsers.text_output import save_extracted_text


def test_save_extracted_text():
    file_path = "data/test_resumes/test_resume.docx"

    text = extract_resume_text(file_path)

    output_file = save_extracted_text(text, file_path)

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip()

    print(f"\nSaved extracted resume to: {output_file}")