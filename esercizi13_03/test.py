from esercizi13_03.model.autovettura import Autovettura
from esercizi13_03.model.clienti import Cliente
from esercizi13_03.model.furgone import Furgone
from esercizi13_03.model.noleggi import Noleggio

veicoli = []
clienti = []
noleggi = []

def registra_autovettura(marca,modello,numero_targa,tariffa_giornaliera,numero_porte,tipologia_cambio):
    veicoli.append(Autovettura(marca,modello,numero_targa,tariffa_giornaliera,numero_porte,tipologia_cambio))
    return Autovettura(marca,modello,numero_targa,tariffa_giornaliera,numero_porte,tipologia_cambio)

def registra_furgone(marca,modello,numero_targa,tariffa_giornaliera,portata,dimensioni):
    veicoli.append(Furgone(marca,modello,numero_targa,tariffa_giornaliera,portata,dimensioni))
    return Furgone(marca,modello,numero_targa,tariffa_giornaliera,portata,dimensioni)

def registra_cliente(nome,cognome,numero_patente):
    clienti.append(Cliente(nome,cognome,numero_patente))
    return Cliente(nome,cognome,numero_patente)

def registrazione_noleggio():
    scelta= input("\nDigita A per registrare un auto:\nDigita F per rigistrare un furgone:\nDigita N per effettuare un noleggio:\nDigita L per visualizzare le liste:\nDigita C per registrare un cliente: \n")
    match scelta:
        case "A" | "a":
            marca = input("Inserisci la marca dell'auto: ")
            modello = input("Inserisci il modello dell'auto: ")
            numero_targa = input("Inserisci il numero di targa: ")
            tariffa_giornaliera = int(input("Inserisci la tariffa giornaliera: "))
            numero_porte = input("Inserisci il numero di porte: ")
            tipologia_cambio = input("Inserisci il tipo di cambio: ")

            registra_autovettura(marca,modello,numero_targa,tariffa_giornaliera,numero_porte,tipologia_cambio)
        case "F" | "f":
            marca = input("Inserisci la marca del furgone: ")
            modello = input("Inserisci il modello del furgone: ")
            numero_targa = input("Inserisci il numero di targa: ")
            tariffa_giornaliera = int(input("Inserisci la tariffa giornaliera: "))
            portata = input("Inserisci la portata in KG: ")
            dimensioni = input("Inserisci le dimensioni in cm: ")
            registra_furgone(marca, modello, numero_targa, tariffa_giornaliera, portata, dimensioni)
        case "C" | "c":
            nome = input("Inserisci il nome del cliente: ")
            cognome = input ("Inserisci il cognome del cliente: ")
            numero_patente = input("Inserisci il numero della patente del cliente: ")
            registra_cliente(nome,cognome,numero_patente)
        case "N" | "n":
            data_noleggio =input("Inserisci data di inizio del noleggio in formato gg-mm-aaaa: ")
            data_fine = input("Inserisci la data di fine del noleggio in formato gg-mm-aaaa: ")
            nuovo_noleggio = Noleggio(data_noleggio,data_fine,clienti[0],veicoli[0])
            noleggi.append(nuovo_noleggio)
        case "L" | "l":
            print(veicoli)
            print("")
            print(clienti)
            print("")
            print(noleggi)
        case _:
            print("ERRORE")
            exit(0)

while True:
    registrazione_noleggio()

