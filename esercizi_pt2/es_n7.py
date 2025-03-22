



import random

CASUALE = random.randint(1,10)
while True:
    numero = input("Inserisci un intero tra 1 e 10 >>> ")
    if numero:
        if numero.isnumeric():
            numero = int(numero)
            if numero < 1 or numero > 10:
                print("Errore!")
            elif numero == CASUALE:
                print("numero è uguale a CASUALE")
                break
        else:
            print("Non hai inserito un numero")
    else:
        print("Non hai inserito un input")
