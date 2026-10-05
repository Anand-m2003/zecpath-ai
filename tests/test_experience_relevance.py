from parsers.experience_relevance import (
    normalize_role,
    calculate_role_similarity,
    calculate_experience_relevance,
    calculate_overall_relevance
)


def test_role_normalization():
    assert normalize_role("Python Programmer") == "python developer"
    assert normalize_role("ML Engineer") == "machine learning engineer"


def test_role_similarity():
    score = calculate_role_similarity(
        "Python Developer",
        "Python Developer"
    )

    assert score == 100.0


def test_experience_relevance():
    experiences = [
        {
            "company": "TechSoft Solutions",
            "job_title": "Python Developer",
            "duration_months": 24
        },
        {
            "company": "ABC Technologies",
            "job_title": "Software Developer",
            "duration_months": 18
        }
    ]

    results = calculate_experience_relevance(
        experiences,
        "Python Developer"
    )

    assert len(results) == 2
    assert results[0]["relevance_score"] == 100.0


def test_overall_relevance():
    experiences = [
        {
            "company": "TechSoft Solutions",
            "job_title": "Python Developer",
            "duration_months": 24
        }
    ]

    score = calculate_overall_relevance(
        experiences,
        "Python Developer"
    )

    assert score == 100.0


def test_structured_experience_output():
    from parsers.experience_output import build_structured_experience

    experience_entries = [
        {
            "company": "TechSoft Solutions",
            "job_title": "Python Developer",
            "duration_months": 24
        }
    ]

    total_experience = {
        "total_months": 24,
        "total_years": 2.0
    }

    gaps = []

    overlaps = []

    relevance_scores = [
        {
            "company": "TechSoft Solutions",
            "job_title": "Python Developer",
            "relevance_score": 100.0
        }
    ]

    result = build_structured_experience(
        experience_entries,
        total_experience,
        gaps,
        overlaps,
        relevance_scores,
        "Python Developer"
    )

    assert result["target_role"] == "Python Developer"
    assert result["experience"] == experience_entries
    assert result["total_experience"] == total_experience
    assert result["gaps"] == gaps
    assert result["overlaps"] == overlaps
    assert result["relevance"] == relevance_scores