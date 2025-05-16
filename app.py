import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(page_title="SentimentRadar - Lamine Niang", layout="centered")
st.title("SentimentRadar : Opinion sur Lamine Niang")
st.markdown("""
Ce tableau de bord analyse les sentiments dans les tweets publics mentionnant **Lamine Niang**, Directeur Général du journal *Le Soleil*.

Source : Twitter (via `snscrape`) - données sur les 30 derniers jours.
""")

@st.cache_data
def collect_tweets(max_tweets=300):
    query = "\"Lamine Niang\" OR \"DG Soleil\" since:2024-12-01 until:2025-05-15"
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > max_tweets:
            break
        tweets.append([tweet.date, tweet.content])
    df = pd.DataFrame(tweets, columns=["Date", "Contenu"])
    return df

@st.cache_data
def analyse_sentiment(df):
    def get_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0.1:
            return 'Positif'
        elif analysis.sentiment.polarity < -0.1:
            return 'Négatif'
        else:
            return 'Neutre'
    df["Sentiment"] = df["Contenu"].apply(get_sentiment)
    return df

with st.spinner("Analyse en cours..."):
    df = collect_tweets()
    df = analyse_sentiment(df)

sentiment_count = df['Sentiment'].value_counts().reset_index()
sentiment_count.columns = ['Sentiment', 'Total']

st.subheader("Répartition des sentiments")
st.altair_chart(
    alt.Chart(sentiment_count).mark_arc(innerRadius=50).encode(
        theta="Total", color="Sentiment", tooltip=['Sentiment', 'Total']
    ), use_container_width=True
)

st.subheader("Exemples de tweets")
show_df = df[['Date', 'Contenu', 'Sentiment']].sort_values("Date", ascending=False).head(10)
st.dataframe(show_df, use_container_width=True)

st.markdown("""
*Basé sur une analyse automatique. Peut contenir des biais selon les mots utilisés.*
""")
