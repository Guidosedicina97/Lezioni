from object_oriented.principi.model.persona import Persona


# definizione classe Lavoratore
class Lavoratore(Persona):

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta, reddito):
        super().__init__(nome, cognome, eta)
        self.reddito = reddito

    # metodo di istanza per funzionalità specifica di un lavoratore
    def richiesta_permesso(self):
        print(f"{self.cognome} chiede un permesso")

    # override metodo di superclasse per riscrittura completa logica
    def fare_qualcosa(self):
        print(f"{self.cognome} lavora")

    # override metodo di superclasse per integrazione logica di base
    def __repr__(self):
            return super().__repr__() + f" (Lavoratore) Reddito: {self.reddito}"