"""
 I.
 Crea uno script nominandolo “esercizio_03”
 II. Utilizzando dei costrutti iterativi a tua scelta, crea una lista bidimensionale che
 rappresenti una tabella composta da 2 righe e 3 colonne, popolata con valori
 numerici interi casuali in range 50-100 (compresi)
 OUTPUT
 Utilizzando dei costrutti iterativi a tua scelta, stampa in console tutti gli elementi contenuti
 nella struttura in formato tabellare
"""

import random
riga = 2
colonne = 3
matrice = [[random.randint(50,100) for _ in range(colonne)] for _ in range(riga)]
for riga in matrice:
    print(*riga)