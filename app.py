import streamlit as st
import pandas as pd
import sqlite3

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

    st.subheader("Analyse des livres")

    st.write("Répartition des livres selon leur note")

    graphique = books["rating"].value_counts().sort_index()

    st.bar_chart(graphique)

elif choix == "Voitures":
    st.dataframe(gaaraas)

    st.subheader("Analyse des voitures")

    st.write("Prix moyen des voitures par marque")

    graphique = gaaraas.groupby("marque")["prix"].mean().sort_values(ascending=False).head(10)

    st.bar_chart(graphique)

elif choix == "Motos et scooters":
    st.dataframe(motos)

    st.subheader("Analyse des motos et scooters")

    st.write("Nombre d'annonces par catégorie")

    graphique = motos["categorie"].value_counts()

    st.bar_chart(graphique)

# Données brutes collectées avec Web Scraper
st.header("Données collectées avec Web Scraper")

books_raw = pd.read_csv("data/books_webscraper_raw.csv")
gaaraas_raw = pd.read_csv("data/gaaraas_webscraper_raw.csv")
motos_raw = pd.read_csv("data/motos_scooters_webscraper_raw.csv")

choix_raw = st.selectbox(
    "Choisir une source Web Scraper",
    ["Livres", "Voitures", "Motos et scooters"],
    key="raw"
)

if choix_raw == "Livres":
    st.dataframe(books_raw)
    st.download_button(
        "Télécharger les données brutes",
        books_raw.to_csv(index=False),
        file_name="books_webscraper_raw.csv"
    )

elif choix_raw == "Voitures":
    st.dataframe(gaaraas_raw)
    st.download_button(
        "Télécharger les données brutes",
        gaaraas_raw.to_csv(index=False),
        file_name="gaaraas_webscraper_raw.csv"
    )

elif choix_raw == "Motos et scooters":
    st.dataframe(motos_raw)
    st.download_button(
        "Télécharger les données brutes",
        motos_raw.to_csv(index=False),
        file_name="motos_scooters_webscraper_raw.csv"
    )

# Tableau de bord des bulletins climatiques
st.header("Bulletins climatiques")

st.write("Analyse des températures par mois et par année")

# Choix de l'année
annee = st.selectbox(
    "Choisir une année",
    sorted(bulletins["annee"].unique())
)

# Filtrer les données
bulletins_annee = bulletins[bulletins["annee"] == annee]

# Affichage du tableau
st.dataframe(bulletins_annee)

# Graphique des températures maximales
st.subheader("Températures maximales par mois")

ordre_mois = [
    "janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"
]

graphique = bulletins_annee.groupby("mois")["tmax_maxmax"].mean()
graphique = graphique.reindex(ordre_mois).dropna()

st.bar_chart(graphique)
