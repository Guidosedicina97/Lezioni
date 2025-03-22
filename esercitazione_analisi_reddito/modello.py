import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

class Modello1:
    def __init__(self,percorso_data):
        self.dataframe = pd.read_csv(percorso_data)

    def analisi_generali(self):
        print("********** ANALISI GENERALI DATAFRAME **********")
        print("Prime cinque osservazioni:", self.dataframe.head().to_string(), sep="\n")
        print("Ultime cinque osservazioni:", self.dataframe.tail().to_string(), sep="\n")
        print("Informazioni generali dataframe:")
        self.dataframe.info()


    def analisi_valori_univoci(self,colonne_da_visualizzare=[]):
        print("********** VALORI UNIVOCI DATAFRAME **********")
        for col in self.dataframe.columns:
            print(f"In colonna {col} abbiamo {self.dataframe[col].nunique()} valori univoci")
            if col in colonne_da_visualizzare:
                for value in self.dataframe[col].unique():
                    print(value)
        print("\n****************************\n")


    def tabella_contingenza(self, colonna, target):
        tabella = pd.crosstab(self.dataframe[colonna], self.dataframe[target])
        print(f"\nTABELLA DI CONTINGENZA {colonna}--{target}:", tabella, sep="\n")
        #chi2, p, dof, expected = chi2_contingency(tabella)
        p = chi2_contingency(tabella)[1]
        print(f"\n- Il p-value risultante del test del chi quadro sulla"
              f" tabella di contingenza {colonna}--{target} è: {p}")
        print(f"  (Notazione non scientifica del p-value -> {format(p, ".53f")})")
        cramer = contingency.association(tabella, method="cramer")
        print(f"- L'indice di Cramer calcolato sulla tabella di contingenza {colonna}--{target} è pari a -> {cramer}")
        print("\n*************************")
        return tabella

    def correlazione_spearman(self, colonna, target):
        sperarman_corr, p = spearmanr(self.dataframe[colonna], self.dataframe[target])
        print(f"\n- La correlazione di Spearman risultante tra {colonna} e {target} risulta pari a {sperarman_corr}")
        print(f"- Il p-value risultante sulla correlazione di Spearman tra {colonna} e {target} è: {p}")
        print("\n*************************")










