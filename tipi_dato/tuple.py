# dichiarazione e istanziazione tuple
tupla_uno = 1, 2, ["ciao mondo"], True, "bello" # literal (parentesi tonde opzionali
print(tupla_uno,type(tupla_uno))
tupla_due = tuple([1,2,3,4]) #con costruttore (vuole un iterabile)
print(tupla_due,type(tupla_due))
# tupla_tre = tuple(1) # commentato per errore (non possibile passare non iterabili)
tupla_quattro = tuple("ciao") # ritorna tupla con tutti i caratteri che compongono una stringa
print (tupla_quattro,type(tupla_quattro))
tupla_cinque = 1, # crea tupla con singolo elemento
print(tupla_cinque,type(tupla_cinque))
tupla_vuota_uno = () # vuota literal
print(tupla_vuota_uno,type(tupla_vuota_uno))
tupla_vuota_due = tuple () # vuota mediante costruttore


# accesso elementi
print(tupla_uno[2])
print(len(tupla_uno), len(tupla_vuota_uno))

# slicing su tuple
tupla_sei = tupla_uno[1:4]
print(tupla_sei)

# unpackaging
a, b, c = tupla_sei
print(a, b, c)