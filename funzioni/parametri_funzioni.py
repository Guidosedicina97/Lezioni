# funzione che riceve un oggetto immutabile (ad esempio stringhe e/ numeri)
def modifica_immutabile(ricevuto):
    ricevuto= "buonasera"
    print(f"Nella funzione, ricevuto vale {ricevuto}")

#funzione che riceve un oggetto mutabile (ad esempio una lista)
def modifica_mutabile(ricevuto):
    ricevuto[1] = 50
    print(f"Nella funzione, la lista contiene {ricevuto}")

# INVOCAZIONE FUNZIONI
# gestione immutabile
saluto = "Buongiorno"
print(f"Dopo istanziazione, saluto vale {saluto}")
modifica_immutabile(saluto)
print(f"Dopo invocazione funzione, saluto vale {saluto}")
# gestione mutabile
lista = [12, 10, 15, 78]
print(f"Dopo istanziazione, la lista contiene {lista}") # [12, 10, 15, 78]
modifica_mutabile(lista)
print(f"Dopo invocazione funzione, la lista contiene {lista}") # [12, 50, 15, 78]

