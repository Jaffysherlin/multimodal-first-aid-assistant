from transformers import pipeline

# NER pipeline to extract symptoms
ner = pipeline("ner", model="dslim/bert-base-NER")

def extract_symptoms(text):
    entities = ner(text)
    symptoms = [e['word'] for e in entities if e['entity'].lower() in ['symptom','injury','pain']]
    return symptoms
