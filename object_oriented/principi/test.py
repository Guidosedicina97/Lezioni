from model.studente import Studente
from model.lavoratore import Lavoratore

# dichiarazione e istanziazione oggetti da gestire
studente = Studente("Mario", "Rossi", 20, 6.7)
lavoratore = Lavoratore( "Gianni", "Verdi", 50, 1300.55)
print(studente)
print(lavoratore)

# invocazione metodi e attributi
print(studente.eta)
print(lavoratore.cognome)
print(studente.media_voti)
print(lavoratore.reddito)
studente.camminare()
studente.fare_qualcosa()
studente.annotazione_appunti()
lavoratore.camminare()
lavoratore.fare_qualcosa()
lavoratore.richiesta_permesso()