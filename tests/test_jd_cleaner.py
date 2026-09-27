from parsers.jd_cleaner import normalize_jd_text


def test_normalize_jd_text():
    raw_text = """
    PYTHON   DEVELOPER

    • Python
    • Flask
    • REST APIs
    """

    cleaned = normalize_jd_text(raw_text)

    assert "PYTHON DEVELOPER" in cleaned
    assert "- Python" in cleaned
    assert "- Flask" in cleaned
    assert "- REST APIs" in cleaned