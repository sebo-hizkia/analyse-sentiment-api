from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer

# Création de l'application FastAPI
app = FastAPI(title="API d'analyse de sentiment")

# Initialisation du modèle d'analyse de sentiment
sia = SentimentIntensityAnalyzer()

# Modèle Pydantic pour la validation des données reçues
class Texte(BaseModel):
    texte: str

# Point de terminaison pour recevoir le texte via une requête POST
@app.post("/analyse_sentiment/")
async def analyse_sentiment(texte_object: Texte):
    """
    Analyse le sentiment du texte fourni en entrée.
    Retourne un dictionnaire JSON avec les scores VADER.
    """
    try:
        sentiment = sia.polarity_scores(texte_object.texte)

        return {
            "neg": sentiment["neg"],
            "neu": sentiment["neu"],
            "pos": sentiment["pos"],
            "compound": sentiment["compound"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
