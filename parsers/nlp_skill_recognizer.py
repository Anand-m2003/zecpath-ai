import spacy


nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Extract named entities from resume text using spaCy.
    """
    doc = nlp(text)

    entities = []

    for entity in doc.ents:
        entities.append({
            "text": entity.text,
            "label": entity.label_
        })

    return entities