# acquisizione input utente e stoccaggio in variabili
nome = input("Digita il tuo nome >>> ")
cognome = input( "Digita il tuo cognome >>>")
eta = input ("Digita la tua età >>> ") # ritorna sempre una stringa

# analisi_dataset dei dati ricevuti
print (nome, type(nome))
print (cognome, type (cognome))
print (eta, type ( eta))

# conoversione input età in valore numerico
eta = int(eta)
print (eta, type( eta))

# output utente
print (f"Ti chiami {nome} {cognome} ed hai {eta} anni")
# print ("Ti chiami " + nome + " " + cognome " ed hai " + eta + " anni") commentato (brutto e da errore)
