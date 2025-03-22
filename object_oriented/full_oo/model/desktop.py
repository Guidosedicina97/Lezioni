from object_oriented.full_oo.model.computer import Computer
from object_oriented.full_oo.model.dispositivo import Dispositivo


# definizione sottoclasse concreta Desktop
class Desktop(Computer, Dispositivo):

    # metodo di inizializzazione
    def __init__(self, sistema_operativo, monitor_incluso):
        super().__init__(sistema_operativo)
        self.monitor_incluso = monitor_incluso

    # override obbligatorio metodo astratto di superclasse Computer
    def sospensione_sistema(self):
        print("Seleziona SOSPENSIONE dal menu Start")

    # override obbligatorio metodo astratto di superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print("Collega alla presa di corrente e configura account")

    # override metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f"Tipo: Desktop - Monitor Incluso: {self.monitor_incluso}"


