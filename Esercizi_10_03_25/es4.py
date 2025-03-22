class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€"
class Catalogo:
    def __init__(self):
        self.prodotti = []
    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
        print(f"Prodotto '{prodotto.nome}' aggiunto")

    def visualizza_catalogo(self):
        if not self.prodotti:
            print("Il catalogo è vuoto.")
        else:
            print("Catalogo Prodotti:")
            for prodotto in self.prodotti:
                print(prodotto)
class GestioneCatalogo:
    def __init__(self):
        self.catalogo = Catalogo()
    def aggiungi_nuovo_prodotto(self):
        nome = input("Inserisci il nome del prodotto >>> ").strip()
        if nome == "":
            print("Errore: Il nome del prodotto non può essere vuoto.")
            return
        prezzo_input = input("Inserisci il prezzo del prodotto: ").strip()
        try:
            prezzo = float(prezzo_input)
            if prezzo <= 0:
                print("Errore: Il prezzo deve essere un numero maggiore di zero.")
                return
        except ValueError:
            print("Errore: Il prezzo deve essere un numero valido.")
            return
        prodotto = Prodotto(nome, prezzo)
        self.catalogo.aggiungi_prodotto(prodotto)
    def visualizza_catalogo(self):
        self.catalogo.visualizza_catalogo()

    def menu(self):
        while True:
            print("\nMenu Catalogo")
            print("1. Aggiungi nuovo prodotto")
            print("2. Visualizza catalogo")
            print("3. Esci")
            scelta = input("Scegli un'opzione (1, 2, 3): ").strip()

            if scelta == "1":
                self.aggiungi_nuovo_prodotto()
            elif scelta == "2":
                self.visualizza_catalogo()
            elif scelta == "3":
                print("Uscita... Arrivederci!")
                break
            else:
                print("Opzione non valida. Riprova.")
app = GestioneCatalogo()
app.menu()
