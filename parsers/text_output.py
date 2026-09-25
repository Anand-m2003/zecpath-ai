from pathlib import Path


def save_extracted_text(text, source_file):
    """
    Save cleaned resume text to a .txt file.

    Args:
        text: Cleaned resume text.
        source_file: Original resume file path.

    Returns:
        Path of the saved output file.
    """
    output_dir = Path("data/extracted_resumes")
    output_dir.mkdir(parents=True, exist_ok=True)

    source_path = Path(source_file)
    output_file = output_dir / f"{source_path.stem}_extracted.txt"

    output_file.write_text(text, encoding="utf-8")

    return output_file