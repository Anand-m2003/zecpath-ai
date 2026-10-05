from parsers.education_certification_parser import (
    normalize_degree,
    extract_graduation_year,
    extract_education,
    extract_certifications,
    categorize_certification,
    build_certification_profile
)


def test_degree_normalization():
    assert normalize_degree("B.Tech") == "Bachelor of Technology"
    assert normalize_degree("MCA") == "Master of Computer Applications"


def test_graduation_year_extraction():
    year = extract_graduation_year(
        "Bachelor of Technology | Computer Science | 2024"
    )

    assert year == 2024


def test_education_extraction():
    text = """
    EDUCATION

    B.Tech | Computer Science | ABC University | 2024

    MCA | Computer Applications | XYZ University | 2026

    EXPERIENCE

    Python Developer
    """

    education = extract_education(text)

    assert len(education) == 2

    assert education[0]["degree_type"] == "Bachelor of Technology"
    assert education[0]["field_of_study"] == "Computer Science"
    assert education[0]["institution"] == "ABC University"
    assert education[0]["graduation_year"] == 2024

    assert education[1]["degree_type"] == "Master of Computer Applications"
    assert education[1]["field_of_study"] == "Computer Applications"
    assert education[1]["institution"] == "XYZ University"
    assert education[1]["graduation_year"] == 2026


def test_certification_extraction():
    text = """
    CERTIFICATIONS

    Python Certification
    AWS Certified Cloud Practitioner
    Power BI Certification

    PROJECTS

    Resume Parser
    """

    certifications = extract_certifications(text)

    assert len(certifications) == 3
    assert "Python Certification" in certifications
    assert "AWS Certified Cloud Practitioner" in certifications
    assert "Power BI Certification" in certifications


def test_certification_categorization():
    assert categorize_certification(
        "Python Certification"
    ) == "technical"

    assert categorize_certification(
        "Project Management Certification"
    ) == "business"

    assert categorize_certification(
        "Graphic Design Certification"
    ) == "creative"

    assert categorize_certification(
        "General Professional Certificate"
    ) == "general"


def test_structured_certification_profile():
    certifications = [
        "Python Certification",
        "Project Management Certification"
    ]

    profile = build_certification_profile(certifications)

    assert len(profile) == 2

    assert profile[0]["name"] == "Python Certification"
    assert profile[0]["category"] == "technical"

    assert profile[1]["name"] == "Project Management Certification"
    assert profile[1]["category"] == "business"