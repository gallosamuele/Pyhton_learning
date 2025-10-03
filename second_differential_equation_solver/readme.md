# Risolutore ODE di Secondo Ordine

Questo programma risolve equazioni differenziali lineari omogenee del secondo ordine con coefficienti costanti della forma:

\[
x''(t) + b \, x'(t) + c \, x(t) = 0
\]

---

## Funzionalità

- Input interattivo dei coefficienti \(b\) e \(c\).  
- Gestione dei tre casi principali:
  - **Radici reali distinte**  
  - **Radice reale doppia**  
  - **Radici complesse**  
- Calcolo della soluzione simbolica tramite **Sympy**.  
- Conversione della soluzione simbolica in funzione numerica per il **plot della soluzione** con Matplotlib.  
- Possibilità di scegliere le costanti arbitrarie \(A\) e \(B\) della soluzione generale.  

---

## Esempio di utilizzo

```bash
$ python3 second_order_ode.py
Inserisci b: 2
Inserisci c: 1
Costante A (default=1): 1
Costante B (default=1): 1
