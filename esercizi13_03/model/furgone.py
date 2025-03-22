from esercizi13_03.model.veicoli import Veicolo


class Furgone(Veicolo):

    def __init__(self,marca, modello, numero_targa, tariffa_giornaliera,portata, dimensioni):
        super().__init__(marca, modello, numero_targa, tariffa_giornaliera)
        self.portata = portata
        self.dimensioni = dimensioni

    def __repr__(self):
        return f"Autovettura - Marca: {self.marca} - Modello: {self.modello} - Numero targa: {self.numero_targa} - Tariffa: {self.tariffa_giornaliera} € Portata: {self.portata} - Dimensioni: {self.dimensioni}"