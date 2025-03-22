import time

class Orologio:
    def __init__(self,ore= 0, minuti =0, secondi = 0):
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi


    def incrementa(self):

        self.secondi += 1
        if self.secondi == 60:
            self.secondi = 0
            self.minuti += 1

        if self.minuti == 60:
            self.minuti = 0
            self.ore += 1
        if self.ore == 24:
            self.ore = 0
    def avvia(self):
            while True :
                print(f"{self.ore:02}: {self.minuti:02}: {self.secondi:02}")
                time.sleep(1)
                self.incrementa()
orologio= Orologio()
orologio.avvia()





