# dichiarazione e istanziazione dizionario
# diz_uno = {1:2, 2:"ciao", "ciao": [1,2,3,4], (1,2,3):True, [1,2]:",mondo"} #commentato (le chiavi devono essere immutabili)
diz_due = {1:2, 2:"ciao", "ciao": [1,2,3,4], (1,2,3):True, 1:",mondo"} # mantenuta unica chiave con ultimo valore
print(diz_due,type(diz_due))
diz_tre = dict(nome="mario", cognome = "Rossi")
print(diz_tre,type(diz_tre))
diz_quattro = {}
diz_cinque = dict()
print(type(diz_quattro),type(diz_cinque))

# accesso ai singoli elementi
print(diz_due["ciao"])

# unpackiging sui dizionari
a, b, c, d = diz_due
print(a, b, c, d)

# manipolazione dizionari
diz_due[4] = " nuovo elemento " # AGGIUNTA tra quadre no indice ma chiave associativa
print(diz_due)
diz_due[4] = " nuovo elemento modificato" # MODIFICA
print(diz_due)
print(diz_due.pop(4))
print(diz_due)
print(diz_due.pop(4, "elemento non trovato"))

# ispezione dizionari
print(len(diz_due))
print(diz_due.items()) # lista di tuple contenenti le coppie chiave-valore
print(diz_due.keys()) # una lista con tutte le chiavi del dizionario
print(diz_due.values()) # lista con tutti i valori del dizionario

