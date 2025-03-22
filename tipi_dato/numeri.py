import math

# dichiarazione e istanziazione di variabili per numeri interi
intero_uno = 10 # literal
print(intero_uno, type(intero_uno))
intero_due = int(12) #con costruttore di classe int
print(intero_due, type(intero_due))
intero_tre = int("20") #trasformazione di stringa in intero
print(intero_tre,type(intero_tre))
intero_quattro = int() #creazione di un valore intero pari a 0
print(intero_quattro, type(intero_quattro))

#dichiarazione e istanziazione di variabili per numeri decimali
decimale_uno = 10.25 #literal
print(decimale_uno, type(decimale_uno))
decimale_due = float(13.67) #con costruttore di classe float
print(decimale_due, type(decimale_due))
decimale_tre = float ("67.88")
print(decimale_tre, type(decimale_tre))
decimale_quattro = float()
print(decimale_quattro, type(decimale_quattro))


#utilizzo operatori + - * tra interi e decimali
risultato_somma = intero_uno + decimale_uno
print (risultato_somma,type(risultato_somma)) # tipo float in quanto parte decimale

# utilizzo operatore / (divisione naturale tra interi
risultato_divisione = intero_due / intero_tre
print (risultato_divisione, type(risultato_divisione))

# utilizzo operatore // (divisione intera) tra interi
risultato_divisioneintera = intero_due // intero_tre
print(risultato_divisioneintera, type(risultato_divisioneintera)) # o (parte decimale troncata) tipo int

# utilizzo operatore // (divisione intera) tra decimali
risultato_divisioneintera_decimali = decimale_due // decimale_uno
print (risultato_divisioneintera_decimali,type (risultato_divisioneintera_decimali)) # 1.0 (parte decimale troncata) ma tipo float

#utilizzo operatore % (resto modulo)
print(5 % 2)

#utilizzo operatore ** (elevazione a potenza)
print(5 **2 )

#ordine di precedenza operatori aritmetici
print (5 + 2 * 2) # se leggo mi aspetto 14 e invece ottengo 9
print((5 + 2) * 2) # ottengo 14

#arrotondamento valori decimali
print(round(5.5)) #arrotondamento a intero (per difetto se intero pari / per eccesso se intero dispari
print(round(10.51)) #arrotondamento a intero
print(round(9.125, 2)) #arrotondamento su cifra decimale successiva a quella indicata
print(math.ceil(5.123456)) #arrotondamento a intero sempre per eccesso
print (math.floor(10.678934)) #arrotondamento a intero sempre per difetto

# i numeri sono oggetti immutabili
numero = 10
print(numero, id(numero))
numero = numero + 12
print(numero, id(numero))

