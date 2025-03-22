# acquisizione età utente in input
eta = input("Digita la tua età >>> ")

# controllo del dato in input
if eta.isnumeric():
    eta = int(eta)
    print("Sei maggiorenne") if eta >= 18 else print("Sei minorenne") # solo python
    messaggio = "Sei maggiorenne" if eta >= 18 else "Sei minorenne" # uso generico
    print (messaggio)
