# Istogramma di valori casuali

Questo progetto genera **1000 numeri casuali** distribuiti uniformemente nell'intervallo [0,1) e li analizza tramite un semplice algoritmo di **bubble sort** (a scopo didattico).  

Successivamente, i valori vengono suddivisi in **10 intervalli uguali** e viene calcolata la **frequenza relativa** (percentuale) di occorrenza di ciascun intervallo.

## Grafico risultante

Il codice produce un **istogramma della distribuzione dei numeri casuali**:

- **Asse X:** intervalli [0.0–0.1), [0.1–0.2), … [0.9–1.0)  
- **Asse Y:** percentuale di valori osservati in ciascun intervallo  

Poiché i numeri sono generati secondo una distribuzione uniforme, ci si aspetta che ogni barra sia circa il **10%**, con leggere fluttuazioni dovute al numero finito di campioni.

## Obiettivo del progetto

- Verificare visivamente la bontà del generatore di numeri casuali  
- Praticare la manipolazione di array e l’ordinamento di dati  
- Creare visualizzazioni semplici e interpretabili con Python

## Tecnologie utilizzate

- Python  
- NumPy (generazione numeri casuali, array)  
- Matplotlib (grafico)  

---

> Questo progetto fa parte di una raccolta di mini-esperimenti di apprendimento Python.
