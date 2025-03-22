
import math
numero= int(input(f"inserisci un numero intero positivo "))
while numero < 0:
    numero = int(input("Errore. inserisci un intero positivo"))
fattoriale = math.factorial(numero)
print (f"il fattoriale di {numero} è {fattoriale}")
