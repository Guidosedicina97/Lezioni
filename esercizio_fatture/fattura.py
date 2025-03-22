import csv
from datetime import datetime

class Fattura :

    def __init__(self, cliente, imponibile, aliquota_iva):
        self.numero = 0
        self.data = datetime.now().strftime("%d-%m-%Y")
        self.cliente = cliente
        self.imponibile = imponibile
        self.aliquota_iva = aliquota_iva
        self.totale = imponibile * (1 + aliquota_iva / 100)
        #Fattura.numero_progressivo += 1

    def __str__(self):
        return f"Fattura {self.numero} - {self.data} - {self.cliente} - Imponibile: {self.imponibile}€, IVA: {self.aliquota_iva}%, Totale: {self.totale}€"