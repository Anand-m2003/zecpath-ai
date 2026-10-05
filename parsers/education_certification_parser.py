import re


DEGREE_SYNONYMS = {
    "b.tech": "Bachelor of Technology",
    "btech": "Bachelor of Technology",
    "b.e": "Bachelor of Engineering",
    "be": "Bachelor of Engineering",
    "b.sc": "Bachelor of Science",
    "bsc": "Bachelor of Science",
    "bca": "Bachelor of Computer Applications",
    "m.tech": "Master of Technology",
    "mtech": "Master of Technology",
    "m.e": "Master of Engineering",
    "me": "Master of Engineering",
    "m.sc": "Master of Science",
    "msc": "Master of Science",
    "mca": "Master of Computer Applications",
    "mba": "Master of Business Administration",
    "phd": "Doctor of Philosophy"
}


CERTIFICATION_CATEGORIES = {
    "technical": [
        "python",
        "java",
        "aws",
        "azure",
        "google cloud",
        "docker",
        "kubernetes",
        "machine learning",
        "data science",
        "cybersecurity",
        "power bi",
        "sql"
    ],
    "business": [
        "project management",
        "business analysis",
        "digital marketing",
        "sales",
        "finance"
    ],
    "creative": [
        "graphic design",
        "ui design",
        "ux design",
        "video editing",
        "content writing"
    ]
}


def normalize_degree(degree):
    key = degree.strip().lower()
    return DEGREE_SYNONYMS.get(key, degree.strip())


def extract_graduation_year(text):
    years = re.findall(r"\b(?:19|20)\d{2}\b", text)

    if years:
        return int(years[0])

    return None


def extract_education(text):
    education = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    education_started = False

    section_headers = {
        "experience",
        "work experience",
        "skills",
        "certifications",
        "projects",
        "achievements",
        "languages",
        "references"
    }

    for line in lines:

        normalized = line.lower().strip(" :-")

        if normalized in {
            "education",
            "academic background",
            "educational qualifications",
            "academic qualifications"
        }:
            education_started = True
            continue

        if education_started and normalized in section_headers:
            break

        if not education_started:
            continue

        degree = None

        for key, value in DEGREE_SYNONYMS.items():
            if key in normalized:
                degree = value
                break

        if degree:

            graduation_year = extract_graduation_year(line)

            parts = [
                part.strip()
                for part in re.split(
                    r"\||,|\s+-\s+",
                    line
                )
                if part.strip()
            ]

            field_of_study = ""
            institution = ""

            if len(parts) >= 2:
                field_of_study = parts[1]

            if len(parts) >= 3:
                institution = parts[2]

            education.append({
                "degree_type": degree,
                "field_of_study": field_of_study,
                "institution": institution,
                "graduation_year": graduation_year
            })

    return education


def extract_certifications(text):
    certifications = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    certification_started = False

    section_headers = {
        "summary",
        "profile",
        "objective",
        "education",
        "experience",
        "work experience",
        "skills",
        "projects",
        "achievements",
        "languages",
        "references"
    }

    for line in lines:

        normalized = line.lower().strip(" :-")

        if normalized in {
            "certifications",
            "certificates",
            "professional certifications"
        }:
            certification_started = True
            continue

        if certification_started and normalized in section_headers:
            break

        if not certification_started:
            continue

        certifications.append(line)

    return certifications


def categorize_certification(certification):
    certification_lower = certification.lower()

    for category, keywords in CERTIFICATION_CATEGORIES.items():

        for keyword in keywords:

            if keyword in certification_lower:
                return category

    return "general"


def build_certification_profile(certifications):
    return [
        {
            "name": certification,
            "category": categorize_certification(certification)
        }
        for certification in certifications
    ]