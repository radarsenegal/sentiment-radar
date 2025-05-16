import streamlit as st
import pandas as pd
from textblob import TextBlob
import altair as alt

st.set_page_config(page_title="SentimentRadar - Lamine Niang", layout="centered")
st.title("SentimentRadar : Opinion sur Lamine Niang")
st.markdown("""
Ce tableau de bord analyse les sentiments d’un échantillon de tweets simulés sur **Lamine Niang**, Directeur Général du journal *Le Soleil*.
""")

# Tweets simulés
data = {
    "Date": [
        "2025-05-10", "2025-05-11", "2025-05-12", "2025-05-13",
        "2025-05-14", "2025-05-15", "2025-05-16", "2025-05-17"
    ],
    "Contenu": [
        "Lamine Niang fait du bon travail à la tête du journal.",
        "Le DG du Soleil semble absent sur les vrais enjeux.",
        "Bravo pour la couverture de la Tabaski, excellent travail !",
        "Encore une Une inutile aujourd'hui, décevant.",
        "Ce monsieur gère bien la rédaction, soyons honnêtes.",
        "Ligne éditoriale trop proche du pouvoir, ça dérange.",
        "Il innove sur la maquette, c’est à saluer.",
        "Aucune transparence sur les recrutements, dommage."
    ]
}

df = pd.DataFrame(data)

# Analyse de sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return 'Positif'
    elif analysis.sentiment.polarity < -0.1:
        return 'Négatif'
    else:
        return 'Neutre'

df["Sentiment"] = df["Contenu"].apply(get_sentiment)

# Répartition des sentiments
sentiment_count = df["Sentiment"].value_counts().reset_index()
sentiment_count.columns = ["Sentiment", "Total"]

# Affichage
st.subheader("Répartition des sentiments")
st.altair_chart(
    alt.Chart(sentiment_count).mark_arc(innerRadius=50).encode(
        theta="Total", color="Sentiment", tooltip=['Sentiment', 'Total']
    ), use_container_width=True
)

st.subheader("Exemples de tweets analysés")
st.dataframe(df, use_container_width=True)

st.markdown("""
*Ces tweets sont simulés à
