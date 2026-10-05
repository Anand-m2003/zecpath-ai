from parsers.nlp_skill_recognizer import extract_entities


def test_nlp_entity_recognition():
    text = """
    Anand is a Python Developer working at TechSoft Solutions.
    He has experience with Flask, SQL and Machine Learning.
    """

    entities = extract_entities(text)

    assert isinstance(entities, list)
    assert len(entities) > 0