from esercizio_fatture.gestore_fatture import GestoreFatture
from esercizio_fatture.cliente import Cliente


gestore = GestoreFatture()
while True:
    print("\n--- Menu ---")
    print("1. Registra nuova fattura")
    print("2. Visualizza fatture")
    print("3. Stampa riepilogo")
    print("4. Esci")
    scelta = input("Scegli un'opzione: ")
    if scelta == "1":
        nome = input("Nome cliente: ")
        cognome = input("Cognome cliente: ")
        imponibile = float(input("Importo imponibile: "))
        aliquota_iva = float(input("Aliquota IVA (%): "))
        cliente = Cliente(nome, cognome)
        gestore.registra_fattura(cliente, imponibile, aliquota_iva)
    elif scelta == "2":
        gestore.stampa_fatture()
    elif scelta == "3":
        gestore.stampa_riepilogo()
    elif scelta == "4":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida, riprova.")