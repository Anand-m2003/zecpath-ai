import re


ROLE_SYNONYMS = {
    "python programmer": "python developer",
    "python engineer": "python developer",
    "backend developer": "backend developer",
    "backend engineer": "backend developer",
    "software developer": "software developer",
    "software engineer": "software engineer",
    "data analyst": "data analyst",
    "data scientist": "data scientist",
    "machine learning engineer": "machine learning engineer",
    "ml engineer": "machine learning engineer",
    "frontend developer": "frontend developer",
    "front end developer": "frontend developer",
}


def normalize_role(role):
    """
    Normalize a job role using role synonyms.
    """
    role = role.strip().lower()

    return ROLE_SYNONYMS.get(role, role)


def tokenize_role(role):
    """
    Convert a role into normalized keywords.
    """
    normalized_role = normalize_role(role)

    words = re.findall(r"[a-zA-Z]+", normalized_role)

    return set(words)


def calculate_role_similarity(candidate_role, target_role):
    """
    Calculate role-to-role similarity using common role keywords.
    """

    candidate_words = tokenize_role(candidate_role)
    target_words = tokenize_role(target_role)

    if not candidate_words or not target_words:
        return 0.0

    common_words = candidate_words.intersection(target_words)

    similarity = (
        len(common_words) /
        len(target_words)
    ) * 100

    return round(similarity, 2)


def calculate_experience_relevance(
    experience_entries,
    target_role
):
    """
    Calculate relevance scores for candidate experience
    against a target job role.
    """

    results = []

    for entry in experience_entries:

        similarity = calculate_role_similarity(
            entry["job_title"],
            target_role
        )

        results.append({
            "company": entry["company"],
            "job_title": entry["job_title"],
            "relevance_score": similarity
        })

    return results


def calculate_overall_relevance(
    experience_entries,
    target_role
):
    """
    Calculate the overall experience relevance score.
    """

    relevance_results = calculate_experience_relevance(
        experience_entries,
        target_role
    )

    if not relevance_results:
        return 0.0

    total_score = sum(
        item["relevance_score"]
        for item in relevance_results
    )

    return round(
        total_score / len(relevance_results),
        2
    )