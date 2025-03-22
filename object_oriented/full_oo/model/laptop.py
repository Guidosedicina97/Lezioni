from object_oriented.full_oo.model.computer import Computer
from object_oriented.full_oo.model.dispositivo import Dispositivo


# definizione sottoclasse concreta laptop
class Laptop(Computer, Dispositivo):

    # metodo inizializzazione
    def __init__(self, sistema_operativo, schermo_touch):
        super().__init__(sistema_operativo)
        self.schermo_touch = schermo_touch

    # override obbligatorio metodo astratto di superclasse computer
    def sospensione_sistema(self):
        print("Chiudi lo schermo")

    def inizializzazione_dispositivo(self):
        print("Controlla carica batteria e configura account")

    # override metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f"Tipo: Laptop - Schermo Touch: {self.schermo_touch}"