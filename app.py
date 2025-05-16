import streamlit as st
import pandas as pd
from textblob import TextBlob
import altair as alt

st.set_page_config(page_title="SentimentRadar - Lamine Niang", layout="centered")
st.title("SentimentRadar : Opinion sur Lamine Niang")
st.markdown("""
Ce tableau de bord analyse les sentiments d’un échantillon de tweets simulés sur **Lamine Niang**, Directeur Général du journal *Le Soleil*.
""")

# Échantillon de tweets fictifs
data = {
    "Date": [
        "2025-05-10", "2025-05-11", "2025-05-12", "2025-05-13",
        "2025-05-14", "2025-05-15", "2025-05-16", "202
