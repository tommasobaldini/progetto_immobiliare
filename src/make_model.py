from src import config
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import os
import sys
import pickle
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from config import DATASET_PATH
import logging


def load_data():
    """Carica il dataset e crea i sottoinsiemi di variabili."""
    df = pd.read_excel(DATASET_PATH, engine="openpyxl")

    # Rinomina delle colonne
    df.columns = [
        "ID", "Data_Transazione", "Età_Casa", "Distanza_MRT", "Negozi_Vicinato",
        "Latitudine", "Longitudine", "Prezzo_Casa_per_Unità_Area"
    ]

    # Creazione dei 3 sottoinsiemi di variabili
    X_lat_long = df[["Latitudine", "Longitudine"]]
    X_other = df[["Età_Casa", "Distanza_MRT", "Negozi_Vicinato"]]
    X_all = df[["Latitudine", "Longitudine", "Età_Casa", "Distanza_MRT", "Negozi_Vicinato"]]
    y = df["Prezzo_Casa_per_Unità_Area"]
    
    return df, X_lat_long, X_other, X_all, y


def train_model_lat_long(grid_search=False):
    """Allena il modello XGBoost per il sottoinsieme 'Latitudine e Longitudine'."""
    df, X_lat_long, _, _, y = load_data()

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_lat_long, y, test_size=0.2, random_state=42)

    if grid_search:
        param_grid_xgb = {
            "n_estimators": [50, 100],
            "learning_rate": [0.01, 0.1, 0.3],
            "max_depth": [3, 6, 10]
        }
        
        grid_search_xgb = GridSearchCV(XGBRegressor(random_state=42), param_grid_xgb, cv=3, scoring='r2', n_jobs=-1, verbose=1)
        grid_search_xgb.fit(X_train, y_train)
        best_model = grid_search_xgb.best_estimator_
    else:
        best_model = XGBRegressor(random_state=42)
        best_model.fit(X_train, y_train)

    # Salvataggio del modello
    with open(os.path.join(config.MODELS_PATH, "XGBoost_LatLong.pickle"), "wb") as file:
        pickle.dump(best_model, file)

    logging.info("Modello XGBoost per Latitudine e Longitudine addestrato e salvato con successo.")


def train_model_other(grid_search=False):
    """Allena il modello XGBoost per il sottoinsieme 'Altre Variabili'."""
    df, _, X_other, _, y = load_data()

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_other, y, test_size=0.2, random_state=42)

    if grid_search:
        param_grid_xgb = {
            "n_estimators": [50, 100],
            "learning_rate": [0.01, 0.1, 0.3],
            "max_depth": [3, 6, 10]
        }
        
        grid_search_xgb = GridSearchCV(XGBRegressor(random_state=42), param_grid_xgb, cv=3, scoring='r2', n_jobs=-1, verbose=1)
        grid_search_xgb.fit(X_train, y_train)
        best_model = grid_search_xgb.best_estimator_
    else:
        best_model = XGBRegressor(random_state=42)
        best_model.fit(X_train, y_train)

    # Salvataggio del modello
    with open(os.path.join(config.MODELS_PATH, "XGBoost_Other.pickle"), "wb") as file:
        pickle.dump(best_model, file)

    logging.info("Modello XGBoost per Altre Variabili addestrato e salvato con successo.")


def train_model_all(grid_search=False):
    """Allena il modello XGBoost per il sottoinsieme 'Tutte le Variabili'."""
    df, _, _, X_all, y = load_data()

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_all, y, test_size=0.2, random_state=42)

    if grid_search:
        param_grid_xgb = {
            "n_estimators": [50, 100],
            "learning_rate": [0.01, 0.1, 0.3],
            "max_depth": [3, 6, 10]
        }
        
        grid_search_xgb = GridSearchCV(XGBRegressor(random_state=42), param_grid_xgb, cv=3, scoring='r2', n_jobs=-1, verbose=1)
        grid_search_xgb.fit(X_train, y_train)
        best_model = grid_search_xgb.best_estimator_
    else:
        best_model = XGBRegressor(random_state=42)
        best_model.fit(X_train, y_train)

    # Salvataggio del modello
    with open(os.path.join(config.MODELS_PATH, "XGBoost_All.pickle"), "wb") as file:
        pickle.dump(best_model, file)

    logging.info("Modello XGBoost per Tutte le Variabili addestrato e salvato con successo.")
