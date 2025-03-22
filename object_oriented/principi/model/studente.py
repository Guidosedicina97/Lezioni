from object_oriented.principi.model.persona import Persona


# definizione classe studente
class Studente(Persona):

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta, media_voti):
        super().__init__(nome, cognome, eta)
        self.media_voti = media_voti

    # metodo di istanza per funzionalità specifica
    def annotazione_appunti(self):
        print(f"{self.nome} prende appunti")

    # override metodo di superclasse per riscrittura completa logica
    def fare_qualcosa(self):
        print(f"{self.cognome} studia")

    # override metodo di superclasse per integrazione logica di base
    def __repr__(self):
        return super().__repr__() + f" (Studente) Media Voti: {self.media_voti}"



