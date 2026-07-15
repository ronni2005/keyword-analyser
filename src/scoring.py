def calculate_skill_score(matched: set[str], jd_skills: set[str]) -> float:
    """
    Calculate the fraction of required job skills
    that are present in the resume.
    """
    if not jd_skills:
        return 0.0

    return len(matched) / len(jd_skills)


def calculate_final_score(
    similarity_score: float,
    skill_score: float,
    similarity_weight: float = 0.7,
    skill_weight: float = 0.3,
) -> float:
    """
    Calculate the final resume match score using
    weighted similarity and skill matching.
    """

    if abs((similarity_weight + skill_weight) - 1.0) > 1e-9:
        raise ValueError("Weights must sum to 1.")

    return (
        similarity_score * similarity_weight
        + skill_score * skill_weight
    )