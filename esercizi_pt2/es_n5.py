

while True:
    numero = input("Inserisci un intero positivo >>> ")
    if numero:
        if numero.isnumeric():
            numero = int(numero)
            if numero < 2:
                primo = False
                break
            else:
                primo = True
                for intero in range(2, int(numero ** 0.5) + 1):
                    if numero % intero == 0:
                        primo = False
                        break
                break
        else:
            print("Non hai inserito un numero")
    else:
        print("Non hai inserito un input")
print(f"{numero} è primo") if primo else print(f"{numero} non è primo ")







