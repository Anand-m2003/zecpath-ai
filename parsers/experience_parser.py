import re
from datetime import datetime


DATE_PATTERN = r"""
(
    (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}
    |
    \d{1,2}[/-]\d{4}
    |
    \d{4}
)
"""


def parse_date(date_text):
    date_text = date_text.strip()

    formats = [
        "%B %Y",
        "%b %Y",
        "%m/%Y",
        "%m-%Y",
        "%Y"
    ]

    for date_format in formats:
        try:
            return datetime.strptime(date_text, date_format)
        except ValueError:
            continue

    return None


def calculate_duration(start_date, end_date):
    if not start_date:
        return 0

    if not end_date:
        end_date = datetime.today()

    months = (
        (end_date.year - start_date.year) * 12
        + (end_date.month - start_date.month)
    )

    return max(months, 0)


def extract_experience_entries(text):
    """
    Extract company names, job titles and employment durations
    from the Experience section of a resume.
    """

    entries = []

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    experience_started = False
    current_entry = None

    pending_job_title = ""
    pending_company = ""

    section_headers = {
        "summary",
        "profile",
        "objective",
        "education",
        "skills",
        "certifications",
        "projects",
        "achievements",
        "languages",
        "references"
    }

    for line in lines:

        normalized = line.lower().strip(" :-")

        # Start of experience section
        if normalized in {
            "experience",
            "work experience",
            "professional experience",
            "employment history",
            "work history"
        }:
            experience_started = True
            continue

        # Stop at another resume section
        if experience_started and normalized in section_headers:
            break

        if not experience_started:
            continue

        # Detect job title and company before the date
        if "|" in line:
            parts = [part.strip() for part in line.split("|")]

            if len(parts) >= 2:
                pending_job_title = parts[0]
                pending_company = parts[1]
                continue

        # Detect "Job Title at Company"
        at_match = re.match(
            r"(.+?)\s+at\s+(.+)",
            line,
            re.IGNORECASE
        )

        if at_match:
            pending_job_title = at_match.group(1).strip()
            pending_company = at_match.group(2).strip()
            continue

        # Detect employment duration
        date_range = re.search(
            rf"({DATE_PATTERN})\s*(?:-|–|—|to)\s*(Present|Current|{DATE_PATTERN})",
            line,
            re.IGNORECASE | re.VERBOSE
        )

        if date_range:

            start_text = date_range.group(1)
            end_text = date_range.group(2)

            start_date = parse_date(start_text)

            if end_text.lower() in {"present", "current"}:
                end_date = datetime.today()
            else:
                end_date = parse_date(end_text)

            duration_months = calculate_duration(
                start_date,
                end_date
            )

            if current_entry:
                entries.append(current_entry)

            current_entry = {
                "company": pending_company,
                "job_title": pending_job_title,
                "start_date": start_text,
                "end_date": end_text,
                "duration_months": duration_months
            }

            pending_job_title = ""
            pending_company = ""

            continue

        # Handle job title/company appearing after the date
        if current_entry:

            if not current_entry["job_title"]:
                current_entry["job_title"] = line

            elif not current_entry["company"]:
                current_entry["company"] = line

    if current_entry:
        entries.append(current_entry)

    return entries


def calculate_total_experience(experience_entries):
    total_months = sum(
        entry["duration_months"]
        for entry in experience_entries
    )

    total_years = round(total_months / 12, 2)

    return {
        "total_months": total_months,
        "total_years": total_years
    }


def detect_gaps_and_overlaps(experience_entries):
    valid_entries = []

    for entry in experience_entries:

        start = parse_date(entry["start_date"])

        if entry["end_date"].lower() in {"present", "current"}:
            end = datetime.today()
        else:
            end = parse_date(entry["end_date"])

        if start and end:
            valid_entries.append({
                "company": entry["company"],
                "job_title": entry["job_title"],
                "start": start,
                "end": end
            })

    valid_entries.sort(key=lambda x: x["start"])

    gaps = []
    overlaps = []

    for i in range(len(valid_entries) - 1):

        current = valid_entries[i]
        next_entry = valid_entries[i + 1]

        if next_entry["start"] > current["end"]:

            gap_months = (
                (next_entry["start"].year - current["end"].year) * 12
                + (next_entry["start"].month - current["end"].month)
            )

            gaps.append({
                "after_company": current["company"],
                "before_company": next_entry["company"],
                "gap_months": gap_months
            })

        elif next_entry["start"] < current["end"]:

            overlaps.append({
                "company_1": current["company"],
                "company_2": next_entry["company"]
            })

    return {
        "gaps": gaps,
        "overlaps": overlaps
    }


def build_experience_object(text):
    experience_entries = extract_experience_entries(text)

    total_experience = calculate_total_experience(
        experience_entries
    )

    gap_overlap_data = detect_gaps_and_overlaps(
        experience_entries
    )

    return {
        "experience": experience_entries,
        "total_experience": total_experience,
        "gaps": gap_overlap_data["gaps"],
        "overlaps": gap_overlap_data["overlaps"]
    }