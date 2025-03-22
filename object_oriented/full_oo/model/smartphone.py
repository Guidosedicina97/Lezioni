from object_oriented.full_oo.model.dispositivo import Dispositivo
from object_oriented.full_oo.model.telefono import Telefono


# definizione sottoclasse concreta Smartphone
class Smartphone(Telefono, Dispositivo):

    # metodo di inizializzazione
    def __init__(self, durata_batteria, tipo_sim):
        super().__init__(durata_batteria)
        self.tipo_sim = tipo_sim

    # override obbligatorio metodo astratto di superclasse Telefono
    def connessione(self):
        print("Inserire SIM")

    # override obbligatorio metodo astratto di superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print("Acquisisci connessioni e configura account Google")

    # override metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f"Tipo: Smartphone - Tipo SIM: {self.tipo_sim}"

    # override metodo per personalizzare il criterio di uguaglianza da classe object
    def __eq__(self, __value): # rappresenta smartphone_due
        if isinstance(__value, Smartphone):
            return self.durata_batteria == __value.durata_batteria and self.tipo_sim == __value.tipo_sim
        return False

