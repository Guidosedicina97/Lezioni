from object_oriented.full_oo.model.cordless import Cordless
from object_oriented.full_oo.model.desktop import Desktop
from object_oriented.full_oo.model.laptop import Laptop
from object_oriented.full_oo.model.smartphone import Smartphone

# dichiarazione e istanziazione oggetti concreti
desktop = Desktop("Windows", True)
laptop = Laptop("MAC-OS", False)
smartphone = Smartphone(12, "Nano-SIM")
cordless = Cordless(24, 7)
print(desktop)
print(laptop)
print(smartphone)
print(cordless)

# invocazioni possibili da superclassi base
desktop.installazione_software("Pycharm")
laptop.installazione_software("Eclipse")
desktop.sospensione_sistema()
laptop.sospensione_sistema()
smartphone.invio_chiamata("+39 1234")
cordless.invio_chiamata("+39 4567")
smartphone.connessione()
cordless.connessione()

# invocazioni possibili da superclasse Dispositivo
desktop.inizializzazione_dispositivo()
cordless.ricarica_batteria()
laptop.inizializzazione_dispositivo()
smartphone.ricarica_batteria()

# uguaglianza oggetti
smartphone_due = Smartphone(12, "Nano-SIM")
print(smartphone == smartphone_due)