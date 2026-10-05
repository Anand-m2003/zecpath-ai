from pathlib import Path

from parsers.experience_parser import (
    extract_experience_entries,
    calculate_total_experience,
    detect_gaps_and_overlaps,
    build_experience_object
)


def test_experience_parser():
    text = """
    EXPERIENCE

    Python Developer | TechSoft Solutions
    Jan 2022 - Dec 2023

    Developed Python applications and REST APIs.

    Backend Developer | ABC Technologies
    Jan 2024 - Present

    Developed backend applications using Flask and SQL.
    """

    experiences = extract_experience_entries(text)

    assert len(experiences) == 2

    assert experiences[0]["job_title"] == "Python Developer"
    assert experiences[0]["company"] == "TechSoft Solutions"

    assert experiences[1]["job_title"] == "Backend Developer"
    assert experiences[1]["company"] == "ABC Technologies"


def test_total_experience():
    experiences = [
        {
            "company": "Company A",
            "job_title": "Python Developer",
            "start_date": "Jan 2022",
            "end_date": "Dec 2023",
            "duration_months": 23
        },
        {
            "company": "Company B",
            "job_title": "Backend Developer",
            "start_date": "Jan 2024",
            "end_date": "Dec 2024",
            "duration_months": 11
        }
    ]

    result = calculate_total_experience(experiences)

    assert result["total_months"] == 34
    assert result["total_years"] == 2.83


def test_gap_and_overlap_detection():
    experiences = [
        {
            "company": "Company A",
            "job_title": "Developer",
            "start_date": "Jan 2020",
            "end_date": "Dec 2021",
            "duration_months": 23
        },
        {
            "company": "Company B",
            "job_title": "Developer",
            "start_date": "Jan 2023",
            "end_date": "Dec 2024",
            "duration_months": 23
        }
    ]

    result = detect_gaps_and_overlaps(experiences)

    assert isinstance(result["gaps"], list)
    assert isinstance(result["overlaps"], list)


def test_structured_experience_object():
    text = """
    EXPERIENCE

    Python Developer | TechSoft Solutions
    Jan 2022 - Dec 2023

    Backend Developer | ABC Technologies
    Jan 2024 - Present
    """

    result = build_experience_object(text)

    assert "experience" in result
    assert "total_experience" in result
    assert "gaps" in result
    assert "overlaps" in result

    assert len(result["experience"]) == 2