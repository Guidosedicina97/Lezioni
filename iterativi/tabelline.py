"""
Rappresentazione tabelline da 1 a 10
1  2  3  4  ....
2  4  6  8  ....
...
- Partire da una struttura vuota
- Popolare la struttura mediante un ciclo (2 cicli annidati)
- Stampa dei valori della struttura in formato tabellare
"""

# struttura vuota (lista bidimensionale --> lista di liste)
tabelline = []

#cicli di popolamento
for indice_riga in range (10): # gestione righe (n°10 con indici da 0 a 9)
    riga = []
    for indice_cella in range (10): #gestione celle riga (n°10 con indici da 0 a 9)
        riga.insert(indice_cella, (indice_riga + 1) * (indice_cella + 1))
    tabelline.append(riga)

# stampa tabelline
print (tabelline)

#stampa in formato tabellare
for riga in tabelline: # ciclo di acquisizione delle righe
    for cella in riga: # ciclo di acquisizione delle celle di ogni riga
        print("{:>4}".format(cella), end=" ")
    print()