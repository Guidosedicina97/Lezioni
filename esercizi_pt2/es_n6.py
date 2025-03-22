


righe = 10
colonne = 10
for ciao in range(righe):
    riga = ""
    for mondo in range(colonne):
        if mondo % 2 == 0:
            riga += "X"
        else:
            riga += "O"
    print(riga.strip())