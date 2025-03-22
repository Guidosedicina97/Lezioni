from datetime import datetime

class Noleggio:

    def __init__(self,data_inizio,data_fine,cliente,veicolo):
        self.data_inizio = datetime.strptime(data_inizio, '%d-%m-%Y').date()
        self.data_fine = datetime.strptime(data_fine,'%d-%m-%Y').date()
        self. cliente = cliente
        self.veicolo = veicolo
        self.importo_finale = veicolo.tariffa_giornaliera * (self.data_fine-self.data_inizio).days

    def __repr__(self):
        return f"Inizio noleggio: {self.data_inizio.strftime('%d-%m-%Y')}\n - Fine noleggio: {self.data_fine.strftime('%d-%m-%Y')}\n - Cliente: {self.cliente}\n - Veicolo: {self.veicolo}\n - Importo finale: {self.importo_finale}"