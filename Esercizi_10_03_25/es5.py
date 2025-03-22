import string
import random
class Utente:
    contatti= []
    def __init__(self,nome,cognome,eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.password = self.nome [-3:] + self.cognome[:3]
        if len(self.password) < 6:
            lettere = string.ascii_letters
            self.password = "".join(random.choice(lettere)for _ in range (6))

    def __repr__(self):
        return f"Nome = {self.nome}\nCognome = {self.cognome}\nEtà = {self.eta}\nPassword ={self.password}"
while True:
    primo_nome= input ("Inserisci il tuo nome >>> ").strip()
    if primo_nome.isnumeric():
        print("Hai inserito dei caratteri non idonei")
        continue

    primo_cognome= input("Inserisci il cognome >>> ").strip()
    if primo_cognome.isnumeric():
        print("Hai inserito dei caratteri non idonei")
        primo_cognome = input("Inserisci il tuo cognome >>> ")

    prima_eta = input("Inserisci la tua età >>> ").strip()
    if not prima_eta.isnumeric():
        print("Inserisci l'età a numero")
        prima_eta = input("Inserisci la tua età >>> ").strip()

    utente_uno = Utente(primo_nome,primo_cognome,prima_eta)
    print(utente_uno)
    break