# definizione di una funzione di pura esecuzione (non restituisce nulla)
def stampa_saluto():
    print("Ciao a tutti")

# definizione di una funzione che restituisce un valore (un oggetto)
def torna_saluto():
    return "Ciao a tutti"

# definizione di una funzione che accetta un parametro ed esegue un istruzione
def salutami(nome):
    print(f"Ciao {nome}")

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena(a, b):
    return a + b

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena_due(a, b):
    return str(a) + str(b)

# definzione di una funzione che accetta 3 parametri (di cui uno facoltativo) e ritorna un valore
def somma(a, b, c=0):
    return a + b + c

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena_tre(a, b):
    return a + str(b)

# definzione di una funzione che accetta 3 parametri (di cui uno facoltativo) e ritorna un valore
def somma_due(a=0, b=0, c=0):
    return a + b + c

# definizione di una funzione che accetta n parametri e esegue un istruzione
def itera(*args):
    print(args, type(args))
    for elemento in args:
        print(elemento)

# definizione di una funzione che accetta n parametri nominali
def stampa(**kwargs):
    print(kwargs,type(kwargs))


# INVOCAZIONE DELLE FUNZIONI
# stampa_saluto()
# saluto = torna_saluto()
# print(saluto)
# print(torna_saluto())
# salutami("Guido")
# print(concatena("Ciao" , "mondo"))
# print(concatena(2, 5))
# print(concatena("ciao", 5)) commentata per errore
# print(concatena_due( "ciao" , 5))
# print(somma(2, 6, 7))
# print(somma(2, 6))
# print(concatena_tre("ciao", 10))
# print(concatena_tre(10, "ciao")) # commentata per errore
# print(concatena_tre(b=10, a="ciao"))
# print(somma_due())
# print(somma_due(1, 4, 5))
# print(somma_due(b=67, c=56))
# itera(1, 4, 6, 7)
# itera("ciao", "mondo")
stampa(nome="Mario", cognome="Rossi")
stampa(nome="Laura", cognome="Gialli", eta=34)