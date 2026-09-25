import fitz


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """
    text = ""

    document = fitz.open(file_path)

    for page in document:
        text += page.get_text("text") + "\n"

    document.close()

    return text