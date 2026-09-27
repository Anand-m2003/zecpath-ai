import re


def normalize_jd_text(text):
    """
    Clean and normalize raw job description text.

    Args:
        text: Raw job description text.

    Returns:
        Normalized job description text.
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Normalize common bullet symbols
    text = re.sub(r"[•●▪◦‣►]", "-", text)

    # Remove unwanted control characters
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Clean individual lines
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    # Remove duplicate blank lines
    return "\n".join(lines).strip()