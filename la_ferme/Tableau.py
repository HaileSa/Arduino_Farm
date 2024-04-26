import streamlit as st
import pandas as pd
import time

# Fonction pour charger les données à partir du fichier CSV et mettre à jour le DataFrame existant
def load_data(df):
    # Charger le fichier CSV contenant les données d'humidité
    new_data = pd.read_csv("donnees_temperature.csv")
    # Concaténer les nouvelles données avec le DataFrame existant
    df = pd.concat([df, new_data], ignore_index=True)
    return df

# Afficher le titre
st.title('Données d\'humidité en temps réel')

# Créer un DataFrame vide pour stocker les données
df = pd.DataFrame(columns=['Temperature', 'Humidity'])

# Boucle pour mettre à jour les données et les afficher en temps réel
while True:
    # Charger de nouvelles données à partir du fichier CSV et mettre à jour le DataFrame
    df = load_data(df)
    
    # Afficher la dernière valeur d'humidité
    last_temperature = df['Temperature'].iloc[-1]
    last_humidity = df['Humidity'].iloc[-1]
    st.text(f"Température (°C): {last_temperature}, Humidité (%): {last_humidity}")
    
    time.sleep(1)  # Attendre une seconde avant de charger de nouvelles données
