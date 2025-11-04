import streamlit as st
import requests
from loguru import logger

# Configuration du logger
logger.add("logs/sentiment_streamlit.log", rotation="500 MB", level="INFO")

st.title("Analyse de sentiment (via API FastAPI)")

# Zone de texte pour la saisie
texte = st.text_area("Saisissez un texte à analyser :")

if st.button("Analyser"):
    if texte:
        logger.info(f"Texte à analyser : {texte}")
        try:
            response = requests.post(
                "http://127.0.0.1:9000/analyse_sentiment/",
                json={"texte": texte}
            )
            response.raise_for_status()
            sentiment = response.json()

            st.write("### Résultats de l'analyse :")
            st.json(sentiment)

            # Interprétation du score
            compound = sentiment['compound']
            if compound >= 0.05:
                st.write("Sentiment global : Positif 😀")
            elif compound <= -0.05:
                st.write("Sentiment global : Négatif 🙁")
            else:
                st.write("Sentiment global : Neutre 😐")

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur de connexion à l'API : {e}")
    else:
        st.warning("Veuillez entrer du texte avant d'analyser.")
