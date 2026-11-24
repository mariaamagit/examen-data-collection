import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Data Collection",
    page_icon="📊",
    layout="wide"
)

# Titre de l'application
st.title("📊 Projet Data Collection")

st.write("""
Bienvenue sur notre plateforme de collecte et d'analyse de données.

Cette application présente les données collectées à partir de différentes sources.
""")

# Chargement des données nettoyées
books = pd.read_csv("data/books_clean.csv")
gaaraas = pd.read_csv("data/gaaraas_clean.csv")
motos = pd.read_csv("data/motos_scooters_clean.csv")
bulletins = pd.read_csv("data/bulletins_climatiques_clean.csv")

# Affichage des données
st.header("Données collectées avec Python")

choix = st.selectbox(
    "Choisir une source de données",
    ["Livres", "Voitures", "Motos et scooters"]
)

if choix == "Livres":
    st.dataframe(books)

elif choix == "Voitures":
    st.dataframe(gaaraas)

elif choix == "Motos et scooters":
    st.dataframe(motos)
