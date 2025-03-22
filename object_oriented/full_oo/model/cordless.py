from object_oriented.full_oo.model.dispositivo import Dispositivo
from object_oriented.full_oo.model.telefono import Telefono


# definizione sottoclasse concreta Cordless
class Cordless(Telefono, Dispositivo):

    # metodo di inizializzazione
    def __init__(self, durata_batteria, raggio_azione):
        super().__init__(durata_batteria)
        self.raggio_azione = raggio_azione

    # override obbligatorio metodo astratto di superclasse Telefono
    def connessione(self):
        print("Collega alla presa telefonica")

    # override obbligatorio metodo astratto di superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print("Imposta il tuo numero personale")

    # override metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f"Tipo: Cordless - Raggio Azione: {self.raggio_azione}"