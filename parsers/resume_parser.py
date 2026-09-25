from pathlib import Path

from parsers.pdf_reader import extract_text_from_pdf
from parsers.docx_reader import extract_text_from_docx
from parsers.text_cleaner import clean_resume_text


def extract_resume_text(file_path):
    """
    Extract and clean text from a PDF or DOCX resume.

    Args:
        file_path: Path to the resume file.

    Returns:
        Cleaned resume text.

    Raises:
        ValueError: If the file format is not supported.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        raw_text = extract_text_from_pdf(file_path)

    elif extension == ".docx":
        raw_text = extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported resume format. Only PDF and DOCX are supported."
        )

    return clean_resume_text(raw_text)