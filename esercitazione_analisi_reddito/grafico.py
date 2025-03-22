import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

from esercitazione_analisi_reddito.modello import Modello1


def grafico_spearman(modello):
    plt.figure(figsize=(8, 5))
    plt.scatter(modello.dataframe["Età"], modello.dataframe["target"], alpha=0.5, color="blue")
    plt.title("Distribuzione Età vs Guadagno")
    plt.xlabel("Età del soggetto")
    plt.show()









modello_grafico=Modello1("analisi_dataset/people_nuovo.csv")
grafico_spearman(modello_grafico)



