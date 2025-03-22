from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

class ModelloTitanic(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
      # self.dataframe_sistemato = self.sistemazione_dataframe()
        self.coningenza_classe = self.tabella_contingenza("Classe Passeggero", "Sopravvissuto")
        self.contingenza_genere = self.tabella_contingenza("Genere", "Sopravvissuto")
        self.correlazione_spearman("Età", "Sopravvissuto")
        self.grafici_contingenza()
        self.grafico_spearman()
        self.grafico_ripartizione()

    # metodo di istanza per sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. drop delle colonne inutili ai fini del modello
        variabili_da_droppare = ["name","ticket", "fare", "cabin","embarked","home.dest", "boat","body"]
        df_sistemato = self.dataframe.drop(variabili_da_droppare,axis=1)
        # 2. drop osservazione con tutti i valori nan
        df_sistemato = df_sistemato.drop(index=1309, axis=0)
        # 3. sostituzione valori nan colonna age con mediana
        # df_sistemato["age"] = df_sistemato["age"].fillna(df_sistemato["age"].median())
        df_sistemato["age"] = (df_sistemato.groupby(["pclass", "sex"]) ["age"]
                               .apply(lambda x: x.fillna(x.median())).reset_index(level=[0,1], drop=True))

        # 4. rimappatura valori colonna sex (0:female - 1:male)
        df_sistemato["sex"] = df_sistemato["sex"].map({"female":0, "male":1})
        # 5. modifica nomi colonne
        df_sistemato = df_sistemato.rename(columns={
            "pclass": "Classe Passeggero",
            "survived": "Sopravvissuto",
            "sex": "Genere",
            "age": "Età",
            "sibsp": "Fratelli/Coniugi",
            "parch": "Genitori/Figli"
        })
        # 6. conversione tipo float in tipo int
        for col in df_sistemato:
            df_sistemato[col] = df_sistemato[col].astype(int)
        return df_sistemato

    # metodo per ottenere tabelle di contingenza - test chi quadro e Cramer (correlazione tra variabili categoriali)
    def tabella_contingenza(self, column, target):
        # generazione e stampa tabella di contingenza
        tabella_contingenza = pd.crosstab(self.dataframe[column], self.dataframe[target])
        # sostituzione label
        tabella_contingenza.columns = tabella_contingenza.columns.map({0:"Deceduti", 1:"Sopravvissuti"})
        if column == "Classe Passeggero":
            tabella_contingenza.index = tabella_contingenza.index.map({1:"1^ classe", 2: "2^ classe", 3: "3^ classe"})
        else:tabella_contingenza.index = tabella_contingenza.index.map({0:"Femmine", 1: "Maschi"})
        print(f"TABELLA DI CONTINGENZA {column}-{target}:", tabella_contingenza, sep="\n")

        # test chi quadro e stampa esito
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f"Il p-value risultante dal test del chi quadro sulla tabella di contingenza {column}-{target} è: {p}")
        print(f"Notazione non scientifica del p-value --> {format(p, ".53f")}") # limite massimo decimali
        # calcolo indice di Cramer e stampa del valore
        cramer = contingency.association(tabella_contingenza, method="cramer")
        print(f"L'indice di Cramer calcolato sulla tabella di contingenza{column}-{target} è pari a {cramer}")
        return tabella_contingenza

    # metodo per ottenere correlazione di Spearman (correlazione tra variabile quantitativa e categoriale)
    def correlazione_spearman(self, column, target):
        spearman_corr,p = spearmanr(self.dataframe[column], self.dataframe[target])
        print(f"La correlazione di Spearman risultante tra {column} e {target} risulta pari a {spearman_corr}")
        print(f"Il p-value sulla correlazione di Spearman tra {column} e {target} risulta pari a {p}")

    # metodo per generare grafici a barre partendo da tabelle contingenza
    def grafici_contingenza(self):
        # generazione figura
        figura, cella = plt.subplots(1, 2, figsize=(12, 5))
        # 1. primo grafico - sopravvivenza per classe
        self.coningenza_classe.plot(kind="bar", ax=cella[0], color=["red", "green"])
        cella[0].set_title("Frequenza di Sopravvivenza per Classe Passeggero")
        cella[0].set_xlabel("Classe Passeggero")
        cella[0].set_ylabel("Frequenza")
        cella[0].legend(title="Legenda")
        cella[0].tick_params(axis="x", rotation=0) # disposizione etichette asse x in orizzontale
        # 2. secondo grafico - sopravvivenza per genere
        self.contingenza_genere.plot(kind="bar", ax=cella[1], color=["red", "green"])
        cella[1].set_title("Frequenza di Sopravvivenza per Genere Passeggero")
        cella[1].set_xlabel("Genere Passeggero")
        cella[1].set_ylabel("Frequenza")
        cella[1].legend(title="Legenda")
        cella[1].tick_params(axis="x", rotation=0) # disposizione etichette asse x in orizzontale
        # show della figura
        plt.tight_layout() # aggiustamento spazi per evitare sovrapposizioni
        plt.show()


    # metodo per generare grafico a dispersione per dimostrare correlazione di Spearman
    def grafico_spearman(self):
        # generazione figura
        plt.figure(figsize=(8, 5))
        # grafico unico (asse x = età, asse y = sopravvivenza)
        plt.scatter(self.dataframe["Età"], self.dataframe["Sopravvissuto"], alpha=0.5, color="blue")
        plt.title("Distribuzione Età vs Sopravvivenza")
        plt.xlabel("Età del passeggero")
        plt.ylabel("Sopravvissuto (0 = No, 1 = Si")
        # show della figura
        plt.show()

    # metodo per generare grafico a torta per ripartizione sopravvissuti-deceduti
    def grafico_ripartizione(self):
        # conteggio generale osservazioni
        sopravvissuti_deceduti = self.dataframe["Sopravvissuto"].value_counts()
        sopravvissuti_deceduti.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["red","green"],
                                    labels=sopravvissuti_deceduti.index.map({0:"Deceduti", 1: "Sopravvissuti"}))
        plt.title("Distribuzione Sopravvissuti-Deceduti")
        plt.ylabel("")
        # show del grafico
        plt.show()





# utilizzo del modello
modello = ModelloTitanic("../dataset_sistemati/data_4.csv")
# modello.analisi_generali(modello.dataframe)
# modello.analisi_valori_univoci(modello.dataframe_sistemato,[ "Età", "Fratelli/Coniugi", "Genitori/Figli"])
# modello.individuazione_outliers(modello.dataframe_sistemato, ["Genere"])
# modello.dataframe_sistemato.to_csv("../dataset_sistemati/data_4.csv", index= False)