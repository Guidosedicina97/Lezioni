"""
CONTROLLARE UNA DATA RICEVUTA IN INPUT DA UN UTENTE
- Chiederemo ad utente di inserire una data in formato gg-mm-aaaa (recupero input come stringa)
- Output: Dire all'utente se la data è corretta oppure cosa è sbagliato
- Controlli di validazione:
 . mese in range 1-12
 . giorno in range 1-30 o 1-31 o 1-28 o 1-29

PRE-CONTROLLI DA EFFETTUARE:
1. Verifichiamo che ci sia un input
2. Verifica che il separatore dei 3 rami sia il - e che i 3 rami siano corretti (04-03-20-2025)
3. Verificare che i 3 rami della stringa siano numeri
"""

# acquisizione input utente (stringa data)
data = input("Inserisci una data in formato gg-mm-aaaa >>> ")

# controllo #1: presenza di un input
if data:
    # controllo #2: validità del formato
    if len(data) == 10 and data[2] == "-" and data[5] == "-":
        lista_elementi = data.split("-")
        #controllo #3: elementi nella lista (devono essere 3)
        if len(lista_elementi) == 3:
            giorno, mese, anno = lista_elementi # unpackaging della lista elementi
            # controllo #4: validità numerica elementi della data
            if giorno.isnumeric() and mese.isnumeric() and anno.isnumeric():
                # conversione elementi data in valori numerici
                giorno = int(giorno)
                mese = int(mese)
                anno = int(anno)
                # controllo #5: validità del range numerico mese (1-12)
                if 1 <= mese <= 12: # if mese >=1 and mese <= 12
                    # verifica anno bisestile
                    bisestile = anno % 400 == 0 or (anno % 4 == 0 and anno % 100 != 0)
                    # controllo #6: il giorno deve essere maggiore o uguale a 1
                    if giorno >= 1:
                        match mese:
                            case 2:
                                if bisestile:
                                    print("Data corretta") if giorno <= 29 else print("Range giorno non corretto")
                                else:
                                    print("Data corretta") if giorno <= 28 else print("Range giorno non corretto")
                            case 4 | 6 | 9 | 11:
                                    print("Data corretta") if giorno <= 30 else print("Range giorno non corretto")
                            case _:
                                    print("Data corretta") if giorno <= 31 else print("Range giorno non corretto")
                    else: # gestiamo errore #6
                        print("Il giorno non risulta nel range corretto")
                else: # gestione errore #5
                    print("Il mese non risulta nel range corretto")
            else: # gestione errore #4
                print("Questa non è una data")
        else: # gestione errore #3
            print("Il formato non è corretto")
    else: # gestione errore 2
        print("Il formato non è corretto")
else: # gestione errore#1
    print("Non hai inserito nulla")
