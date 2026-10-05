def build_structured_experience(
    experience_entries,
    total_experience,
    gaps,
    overlaps,
    relevance_scores,
    target_role
):
    """
    Build the final structured experience object.
    """

    return {
        "target_role": target_role,
        "experience": experience_entries,
        "total_experience": total_experience,
        "gaps": gaps,
        "overlaps": overlaps,
        "relevance": relevance_scores
    }