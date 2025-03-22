import csv
from esercizio_fatture.cliente import Cliente
from esercizio_fatture.fattura import Fattura


class GestoreFatture:
    def __init__(self, file_archivio="registri.csv"):
        self.file_archivio = file_archivio
        self.fatture = []
        self.carica_fatture()

    def carica_fatture(self):
        try:
            with open(self.file_archivio, "r", newline="") as file:
                lettore = csv.reader(file)
                next(lettore)
                for riga in lettore:
                    numero, data, nome, cognome, imponibile, iva, totale = riga
                    cliente = Cliente(nome, cognome)
                    fattura = Fattura(cliente, float(imponibile), float(iva))
                    fattura.numero = int(numero)
                    fattura.data = data
                    fattura.totale = float(totale)
                    self.fatture.append(fattura)
        except Exception as e:
            print(e)

    def registra_fattura(self, cliente, imponibile, aliquota_iva):
        nuova_fattura = Fattura(cliente, imponibile, aliquota_iva)
        self.salva_fattura(nuova_fattura)
        print("Fattura registrata con successo!")

    def salva_fattura(self, fattura):
        with open(self.file_archivio, "a", newline="") as file:
            scrittore = csv.writer(file)
            if file == 0:
                scrittore.writerow(["Numero", "Data", "Nome", "Cognome", "Imponibile", "IVA", "Totale"])
            fattura.numero = self._generatore_numero()
            scrittore.writerow(
                [fattura.numero, fattura.data, fattura.cliente.nome, fattura.cliente.cognome, fattura.imponibile,
                 fattura.aliquota_iva, fattura.totale])
            self.fatture.append(fattura)

    def stampa_fatture(self):
        if not self.fatture:
            print("Nessuna fattura registrata.")
        else:
            for fattura in self.fatture:
                print(fattura)

    def stampa_riepilogo(self):
        totale_fatture = len(self.fatture)
        totale_imponibile = sum(f.imponibile for f in self.fatture)
        print(f"Totale Fatture: {totale_fatture}, Totale Imponibile: {totale_imponibile}€")

    def _generatore_numero(self):
        if len(self.fatture) == 0:
            return 1
        return max(list(map(lambda fattura: fattura.numero, self.fatture))) + 1
