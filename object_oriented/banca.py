"""
SIMULAZIONE SOFTWARE BANCA
- Possibilità di aprire un conto corrente ricevendo IBAN (saldo 0)
- Possibilità di registrare versamenti e prelevamenti (quanti ne vuole)
- Possibilità di terminare il programma in qualsiasi momento

SVILUPPO OBJECT ORIENTED --> Oggetto logico da gestire è ContoCorrente
                             . Intestatario (nome e cognome del cliente)
                             . Saldo
                             . Numero conto (casuale)
                             . IBAN (parte fissa + numero conto)
                             . Costruzione oggetto ContoCorrente ad apertura(__init()__)
                             . Aggiornamento dinamico saldo conto corrente
                             . Rappresentazione testuale oggetti
"""
import random

# definizione classe di modellazione oggetto ContoCorrente
class ContoCorrente:

    # attributo di classe con valore comune e tutti gli oggetti
    iban_fisso = "IT 07 K 02008 13000 "

    # metodo di inizializzazione
    def __init__(self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0
        self.numero_conto = "".join(str(random.randint(0, 9)) for _ in range(7))
        self.iban = ContoCorrente.iban_fisso + self.numero_conto

    # metodo di istanza per aggiornamento saldo (invocato ad ogni operazione)
    def set_saldo(self, importo_operazione):
        try:
            importo_operazione = float(importo_operazione.strip().replace(",",".")) # se 100.78 ok sw ciao no
            self.saldo += importo_operazione
            return f"Hai registrato un'operazione di {importo_operazione:.2f} ed ora hai un saldo pari a {self.saldo:.2f}"

        except Exception as e:
            return "L'importo che hai inserito non è corretto"

    # metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return (f"Benvenuto/a {self.intestatario}\n L'IBAN del tuo nuovo conto è {self.iban}\n"
                f"Attualmente il tuo saldo è pari a {self.saldo} Euro")

# SEZIONE OPERATIVA DEL PROGRAMMA

# funzione di avvio programma e di menù
def pannello_comandi():
    scelta_utente = input(
        "***** La Tua Banca *****\n"
        "Digita 1 per aprire un nuovo conto\n"
        "Digita 0 per terminare >>>> ")
    match scelta_utente:
        case "1":
            apertura_conto()
        case _:
            print("Arrivederci... alla prossima")
            exit(0)

# funzione per gestire l'apertura del conto corrente
def apertura_conto():
    nome_cognome = input("Grazie di aver scelto di aprire un conto\nDigita il tuo nome e cognome >>>")
    conto = ContoCorrente(nome_cognome)
    print(conto)
    scelta_utente = input ("Desideri effetturare delle operazioni (SI o NO) >>> ")
    if scelta_utente.upper() == "SI":
        registrazione_operazione(conto)
    else:
        print(f"Arrivederci {conto.intestatario}...alla prossima")
        exit(0)

# funzione per gestire registrazione operazioni
def registrazione_operazione(conto):
    while True:
        importo = input("Digita importo operazione (oppure 0 per terminare) >>> ")
        if importo != "0":
            print(conto.set_saldo(importo))
        else:
            print(f"Arrivederci {conto.intestatario}... alla prossima")
            exit(0)


# invocazione funzione di avvio programma
pannello_comandi()