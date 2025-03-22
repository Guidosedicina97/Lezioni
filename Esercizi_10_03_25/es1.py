

class Cerchio:

    pigreco = 3.14
    def __init__(self,raggio):
         self.raggio = raggio
    def calcolo_area(self):
        return self.pigreco * (self.raggio**2)

    def calcolo_circonferenza(self):
        return 2 * self.pigreco * self.raggio

scelta_raggio= float(input("Inserisci il tuo raggio >>> "))
mio_cerchio = Cerchio(scelta_raggio)
print("area:",mio_cerchio.calcolo_area())
print("circonferenza", mio_cerchio.calcolo_circonferenza())







