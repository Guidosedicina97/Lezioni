from esercitazione_analisi_reddito.modello import Modello1
from fontTools.misc.cython import returns
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt


def sistemazione_dataframe(modello01):
    # 1. drop delle colonne inutili ai fini del modello
    variabili_da_sistemare = ["capital-gain" ,"education" ,"marital-status",
                              "fnlwgt", "capital-loss" ,"hours-per-week",
                              "native-country", "relationship" ,"occupation" ,"workclass"]

    df_sistemato = modello01.dataframe.drop(variabili_da_sistemare,axis=1)
    # 5. modifica nomi colonne
    df_sistemato = df_sistemato.rename(columns={
        "age": "Età",
        "education-num": "Livello di istruzione",
        "sex": "Genere",
        "race": "razza",})
    return df_sistemato



# avvio funzioni
modello =Modello1("analisi_dataset/people.csv")
#modello.analisi_generali()
#modello.analisi_valori_univoci(["capital-gain", "fnlwgt", "capital-gain","hours-per-week", "native-country"])
sistemazione_dataframe(modello).to_csv("analisi_dataset/people_nuovo.csv", index= False)
modello2 =Modello1("analisi_dataset/people_nuovo.csv")
modello2.analisi_generali()
modello2.tabella_contingenza("Genere", "target")
