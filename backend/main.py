from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()

# load NLP model
nlp = spacy.load("en_core_web_sm")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Resume AI API running"}

@app.post("/extract")
def extract(data: TextInput):
    doc = nlp(data.text)

    skills = []

    # simple skill extraction (nouns/proper nouns)
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            skills.append(token.text.lower())

    return {
        "skills": list(set(skills))[:15]
    }

