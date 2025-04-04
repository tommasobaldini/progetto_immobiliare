# 🏠📈 Smart Pricing: Modelli Predittivi per la Valutazione Immobiliare

## Descrizione
Questo progetto sviluppa 3 modelli di regressione XGBoost per predire il prezzo al metro quadro di immobili nella regione di Sindian, Nuova Taipei, Taiwan, utilizzando 3 diversi subsets del Real Estate Valuation Data Set.  
Successivamente, crea una web app con Streamlit che permette agli utenti di ottenere una stima del prezzo inserendo:

• __Latitudine__ e __longitudine__, oppure

• __Età dell’immobile__, __distanza dalla stazione MRT più vicina__ e __numero di minimarket nelle vicinanze__ oppure

• __Tutte le caratteristiche sopra elencate__

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
│  
├── *data*/  
│   └── Real estate valuation data set.xlsx  # Il dataset utilizzato per il training dei modelli    
│  
├── *scripts*/  
│   ├── run_pipeline.py  # Script principale per eseguire la pipeline  
│   ├── make_model.py  # Script per la creazione dei modelli  
│   ├── UI.py  # Interfaccia utente con Streamlit  
│   ├── __init__.py  # File di inizializzazione  
│   └── config.py  # Configurazione per la pipeline e i modelli  
│  
├── *MODEL*/    
│       ├── XGBoost_LatLong.pickle # Modello addestrato su Latitudine e Longitudine  
│       ├── XGBoost_Other.pickle # Modello addestrato su Età dell’immobile, distanza dalla stazione MRT più vicina, numero di minimarket nelle vicinanze     
│       └── XGBoost_All.pickle # Modello addestrato su tutte e 5 le variabili    
│      
├── *logs*/    
│   └── pipeline.log  # Log delle esecuzioni della pipeline      
│      
├── *README.md*  # Questo file  




## Addestramento del modello Gradient Boosting
La fase di preprocessing dei dati non è stata eseguita poiché, durante il controllo preliminare del dataset, si è riscontrato che non era necessaria.   
Il modello XGBoost, in quanto algoritmo di tipo ensemble basato su alberi decisionali, non richiede trasformazioni come la standardizzazione o la normalizzazione delle variabili, risultando robusto rispetto alla scala e alla distribuzione dei dati.  

Per ottimizzare le prestazioni dei 3 modelli, è stata implementata una fase di tuning degli iperparametri utilizzando Grid Search.   
Questo processo mira a identificare la combinazione di iperparametri che massimizza la performance del modello (tunato su R^2), tra cui il numero di alberi (n_estimators), il tasso di apprendimento (learning_rate) e la profondità massima degli alberi (max_depth).  
La selezione ottimale degli iperparametri è stata effettuata tramite cross-validation, garantendo una valutazione robusta della capacità predittiva del modello.  

Questa strategia ha permesso di massimizzare le prestazioni dei modelli, migliorandone la generalizzazione sui dati di test e rendendoli più efficaci nella previsione dei prezzi immobiliari.  
  

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

