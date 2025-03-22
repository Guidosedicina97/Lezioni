# dichiarazione e istanziazione di una variabile globale
variabile_globale = 10

# funzione che dichiara una variabile locale e legge la variabile globale
def funzione_uno():
    variabile_locale = 12
    print(variabile_globale + variabile_locale)

# funzione che modifica la variabile globale
def funzione_due():
    global variabile_globale
    variabile_globale += 13
    print(variabile_globale)


# proviamo a leggere le variabili
#print(variabile_globale) # possibile
# print(variabile_locale) # commentato perchè impossibile

# invocazione funzione di lettura
# funzione_uno()
# funzione_due()

# definizione di una funzione anonima
anonima = lambda x, y: x + y
print(type(anonima)) # tipo function

# utilizzo di una funzione anonima
print(anonima(2, 5))
print(anonima("ciao", "mondo"))