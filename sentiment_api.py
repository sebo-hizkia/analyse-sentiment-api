from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer
from loguru import logger

# Configuration du logger
logger.add("logs/sentiment_api.log", rotation="100 MB", level="INFO")

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
        logger.info(f"Texte reçu : {texte_object.texte}")
        sentiment = sia.polarity_scores(texte_object.texte)
        logger.info(f"Résultat : {sentiment}")

        return {
            "neg": sentiment["neg"],
            "neu": sentiment["neu"],
            "pos": sentiment["pos"],
            "compound": sentiment["compound"]
        }

    except Exception as e:
        logger.error(f"Erreur d'analyse : {e}")
        raise HTTPException(status_code=500, detail=str(e))
