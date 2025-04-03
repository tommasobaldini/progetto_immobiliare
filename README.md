# Progetto Immobiliare: Previsione del Prezzo delle Case

## Descrizione
Questo progetto sviluppa 3 modelli di regressione XGBoost per predire il prezzo al metro quadro di immobili nella regione di Sindian, Nuova Taipei, Taiwan, utilizzando 3 diversi subsets del Real Estate Valuation Data Set.  
Successivamente, crea una web app con Streamlit che permette agli utenti di ottenere una stima del prezzo inserendo:

• Latitudine e longitudine, oppure

• Età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket nelle vicinanze oppure

• Tutte queste caratteristiche

## Il Dataset
Il dataset utilizzato per questo progetto è composto da 414 righe e 8 colonne. Di seguito è riportata una breve descrizione delle colonne:

• *No*:  
    Tipo: int64  
    Descrizione: Identificativo univoco per ogni riga.  

• *X1 transaction date*:  
    Tipo: float64  
    Descrizione: Data della transazione immobiliare (necessario preprocessing se utilizzata per addestramento).
  
• *X2 house age*:  
    Tipo: float64  
    Descrizione: Età dell'immobile in anni.  

• *X3 distance to the nearest MRT station*:  
    Tipo: float64  
    Descrizione: Distanza dalla stazione MRT più vicina.  

• *X4 number of convenience stores*:  
    Tipo: int64  
    Descrizione: Numero di minimarket o negozi di convenienza nelle vicinanze.  

• *X5 latitude*:  
    Tipo: float64  
    Descrizione: Latitudine della posizione dell'immobile.  

• *X6 longitude*:  
    Tipo: float64  
    Descrizione: Longitudine della posizione dell'immobile.  
  
• *Y house price of unit area* (variabile dipendente):  
    Tipo: float64  
    Descrizione: Prezzo per unità di superficie dell'immobile (ad esempio, il prezzo al metro quadrato).  
  
•  **Sommario**:  
Totale righe: 414.  
Totale colonne: 8.  
Tipo di Dati: 6 colonne di tipo float64 e 2 colonne di tipo int64.  
Valori Mancanti: Non ci sono valori mancanti nel dataset.  

## Struttura del Progetto
Il progetto è organizzato come segue:

progetto_immobiliare/  
├── data/             # Contiene il dataset utilizzato per l'analisi  
├── scripts/          # Script per l'esecuzione della pipeline  
├── src/              # Contiene i codici per l'addestramento dei modelli e lo sviluppo della web app  
├── logs/             # Log delle operazioni e pipeline  
├── MODEL/            # Contiene i modelli pre-allenati  
├── README.md         # Questo file  


## Tuning del modello XGBoost
Il codice implementa una fase di tuning degli iperparametri utilizzando Grid Search per ottimizzare le prestazioni del modello XGBoost. La ricerca esaustiva esplora una griglia di possibili valori per i parametri chiave del modello, come il numero di alberi (n_estimators), il tasso di apprendimento (learning_rate) e la profondità massima degli alberi (max_depth). Questo processo mira a identificare la combinazione di iperparametri che massimizza la performance del modello, utilizzando la tecnica della cross-validation per garantire una stima robusta delle sue capacità predittive.


## Istruzioni per eseguire l'applicazione
Per eseguire l'applicazione, segui i passaggi descritti di seguito.

1. **Esegui il file `UI.py`**:
    Dopo aver configurato il tuo ambiente e installato le dipendenze, il file principale da eseguire è `UI.py`. Per avviare l'applicazione, apri il terminale e naviga nella cartella contenente il file, quindi esegui il comando:

    ```bash
    streamlit run UI.py
    ```

2. **Interagisci con l'applicazione**:
    Una volta aperto il browser, inserisci i dati richiesti (ad esempio, latitudine, longitudine, ecc.) per ottenere le previsioni dei modelli XGBoost.  

 **Verifica dei valori inseriti**:
    - L'applicazione esegue una validazione dei dati inseriti dall'utente.   I valori immessi (come latitudine, longitudine, età dell’immobile, distanza dalla stazione MRT, ecc.) devono rientrare nei limiti minimi e massimi che ciascuna variabile assume nel dataset di addestramento.  
    - Se i valori inseriti sono fuori da questi intervalli, l'applicazione mostrerà un messaggio di errore, avvisando l'utente di correggere i dati in modo che siano compatibili con il dataset originale.

