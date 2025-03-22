

class Telecomando:
    def __init__(self):
        self.numeri = list(range(1, 10))

    def selezione_numero(self, numero):

        if numero in self.numeri:
            sostituto = self.numeri.index(numero)
            self.numeri[sostituto] = "P"
            return f"Hai selezionato il numero {numero}"
        else:
            return "Numero non valido! Scegli un numero da 1 a 9"

    def visualizza_tastierino(self):

        for riga in range(3):
            numeri_visualizzati = [str(numero) for numero in self.numeri[riga*3:(riga+1)*3]]
            print(" ".join(numeri_visualizzati))

telecomando = Telecomando()

while True:
    telecomando.visualizza_tastierino()
    try:
        scelta = int(input("Premi un numero da 1 a 9, (oppure 0 per uscire): "))
        if scelta == 0:
            print("Uscita dal telecomando, Arrivederci!")
            break
        print(telecomando.selezione_numero(scelta))
    except ValueError:
        print("Inserisci un numero valido.")


