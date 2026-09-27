from parsers.jd_synonyms import normalize_skill, normalize_role


def test_skill_synonyms():
    assert normalize_skill("python programming") == "Python"
    assert normalize_skill("rest apis") == "REST API"
    assert normalize_skill("ml") == "Machine Learning"


def test_role_synonyms():
    assert normalize_role("python programmer") == "Python Developer"
    assert normalize_role("back end developer") == "Backend Developer"
    assert normalize_role("ml engineer") == "Machine Learning Engineer"