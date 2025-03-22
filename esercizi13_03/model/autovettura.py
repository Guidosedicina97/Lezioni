from esercizi13_03.model.veicoli import Veicolo


class Autovettura(Veicolo):

    def __init__(self,marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio):
        super().__init__(marca, modello, numero_targa, tariffa_giornaliera)
        self.numero_porte = numero_porte
        self.tipologia_cambio = tipologia_cambio

    def __repr__(self):
        return f"Autovettura - Marca: {self.marca} - Modello: {self.modello} - Numero targa: {self.numero_targa} - Tariffa: {self.tariffa_giornaliera} € Porte: {self.numero_porte} - Cambio: {self.tipologia_cambio}"