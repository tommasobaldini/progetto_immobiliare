import streamlit as st
import pickle
import pandas as pd
import os
from config import DATASET_PATH

# Percorso della cartella modelli
MODEL_PATH = "../MODEL/"

df = pd.read_excel(DATASET_PATH, engine="openpyxl")

# Rinomina delle colonne
df.columns = [
    "ID", "Data_Transazione", "Età_Casa", "Distanza_MRT", "Negozi_Vicinato",
    "Latitudine", "Longitudine", "Prezzo_Casa_per_Unità_Area"
]

# Definisci i limiti per ogni variabile
limiti =  {
    "Latitudine": (float(df["Latitudine"].min()), float(df["Latitudine"].max())),
    "Longitudine": (float(df["Longitudine"].min()), float(df["Longitudine"].max())),
    "Età_Casa": (float(df["Età_Casa"].min()), float(df["Età_Casa"].max())),
    "Distanza_MRT": (float(df["Distanza_MRT"].min()), float(df["Distanza_MRT"].max())),
    "Negozi_Vicinato": (int(df["Negozi_Vicinato"].min()), int(df["Negozi_Vicinato"].max())),
}

# Funzione per validare gli input rispetto ai limiti
def valida_input(valori, nomi_variabili):
    errori = []
    for nome, valore in zip(nomi_variabili, valori):
        minimo, massimo = limiti[nome]
        if not (minimo <= valore <= massimo):
            errori.append(f"⚠️ **{nome} fuori intervallo ({valore})**. Limiti: minimo = {minimo}\nmassimo = {massimo}")
    return errori

# Titolo UI
st.title("🏡 Stima del Prezzo delle Case")

# Selezione del metodo di input
opzione = st.radio(
    "Seleziona il metodo di previsione:",
    ("Latitudine & Longitudine", "Altre Caratteristiche", "Tutte le Variabili")
)

# Gestione delle opzioni di input
if opzione == "Latitudine & Longitudine":
    latitudine = st.number_input("Latitudine", value=limiti["Latitudine"][0], step=0.01)
    longitudine = st.number_input("Longitudine", value=limiti["Longitudine"][0], step=0.01)
    nomi_variabili = ["Latitudine", "Longitudine"]
    valori_input = [latitudine, longitudine]
    model_file = "XGBoost_LatLong.pickle"

elif opzione == "Altre Caratteristiche":
    eta_casa = st.number_input("Età della Casa", value=limiti["Età_Casa"][0], step=1.0)
    distanza_mrt = st.number_input("Distanza dalla Stazione MRT", value=limiti["Distanza_MRT"][0], step=5.0)
    negozi_vicinato = st.number_input("Numero di Negozi Vicino", value=limiti["Negozi_Vicinato"][0], step=1)
    nomi_variabili = ["Età_Casa", "Distanza_MRT", "Negozi_Vicinato"]
    valori_input = [eta_casa, distanza_mrt, negozi_vicinato]
    model_file = "XGBoost_Other.pickle"

else:  # Tutte le Variabili
    latitudine = st.number_input("Latitudine", value=limiti["Latitudine"][0], step=0.001)
    longitudine = st.number_input("Longitudine", value=limiti["Longitudine"][0], step=0.001)
    eta_casa = st.number_input("Età della Casa", value=limiti["Età_Casa"][0], step=1.0)
    distanza_mrt = st.number_input("Distanza dalla Stazione MRT", value=limiti["Distanza_MRT"][0], step=5.0)
    negozi_vicinato = st.number_input("Numero di Negozi Vicino", value=limiti["Negozi_Vicinato"][0], step=1)
    nomi_variabili = ["Latitudine", "Longitudine", "Età_Casa", "Distanza_MRT", "Negozi_Vicinato"]
    valori_input = [latitudine, longitudine, eta_casa, distanza_mrt, negozi_vicinato]
    model_file = "XGBoost_All.pickle"

# Pulsante di previsione
if st.button("📈 Stima il Prezzo"):
    errori = valida_input(valori_input, nomi_variabili)
    
    if errori:
        for errore in errori:
            st.error(errore)
    else:
        # Carica il modello corretto
        model_path = os.path.join(MODEL_PATH, model_file)
        with open(model_path, "rb") as file:
            model = pickle.load(file)

        # Effettua la previsione
        valori_input = [valori_input]  # Converti in formato adatto al modello
        prediction = model.predict(valori_input)[0]

        st.success(f"🏠 **Prezzo Stimato:** {prediction:.2f} per unità di area")

