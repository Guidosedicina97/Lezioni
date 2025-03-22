"""
CALCOALRE IL PIANO DI AMMORTAMENTO DI UN FINANZIAMENTO
(metodo di calcolo italiano) --> quota capitale è costante e rata variabile
input utente (da recuperare):
- importo finanziamento
- durata del finanziamento (in anni)
- numero delle rate annuali (ad esempio 12 rate/anno)
- tasso di interesse (ad esempio 5%)

Verifica input utente
conversione input utente in nunerici
calcolo effettivo piano ammortamento
stampa tabella del piano di ammortamento (rata n. totale rata quota interessi quota capitale residuo da pagare)
"""

# funzione per le acquisizioni input utente
def acquisizione_input():
    importo_finanziamento = input("Inserisci importo del finanziamento >>> ").strip()
    durata_finanziamento = input("Inserisci la durata in anni >>> ").strip()
    rate_annuali = input("Inserisci il numero delle rate del rimborso annuali >>> ").strip()
    tasso_interesse = input("Inserisci il tasso di interesse (ad esempio 5 per 5%) >>> ").strip() .replace("%", "")
    return importo_finanziamento, durata_finanziamento, rate_annuali, tasso_interesse

"""
ESTENSIONE DELLA LIST COMPREHENSION
convertiti = []
for valore in valori:
    convertiti.append(int(valore))
"""
# funzione per il controllo e conversione sicura degli input
def conversione_input(valori): # riceve una tupla
    if all(valore.isnumeric() for valore in valori):
        convertiti = [int(valore) for valore in valori]
        return convertiti
    else:
        return None

# funzione per calcolare il piano di ammortamento (lista bidimensionale)
def calcolo_ammortamento(valori):
    # unpackiging della lista valori ricevuta
    importo, anni, rate_anno, tasso = valori
    # dati preliminari necessari per il calcolo
    totale_rate = anni * rate_anno
    tasso_effettivo = tasso / 100
    quota_capitale_rata = importo / totale_rate
    # definizione tabella piano ammortamento e riga di intestazione
    piano_ammortamento = [
        ["N° rata", "Totale Rata", "Quota Interessi", "Quota Capitale", "Capitale Residuo"]
    ]
    # popolamento tabella
    for indice in range(1, totale_rate + 1):
        interessi_rata = ((importo * tasso_effettivo) * anni) / totale_rate
        totale_rata = quota_capitale_rata + interessi_rata
        capitale_residuo = importo - quota_capitale_rata
        riga_rata = [
            f"Rata n. {indice}",
            f"{totale_rata:.2f}",
            f"{interessi_rata:.2f}",
            f"{quota_capitale_rata:.2f}",
            f"{capitale_residuo:.2f}"
        ]
        piano_ammortamento.append(riga_rata)
        importo = capitale_residuo
    return piano_ammortamento

# funzione per stampare il piano di ammortamento in formato tabellare
def stampa_ammortamento(piano_ammortamento):
    for riga in piano_ammortamento:
        for cella in riga:
            print("{:^20}".format(cella), end=" ")
        print()

# funzione di avvio programma
def start():
    valori_acquisiti = conversione_input(acquisizione_input())
    if valori_acquisiti:
        piano_ammortamento = calcolo_ammortamento(valori_acquisiti)
        #print(piano_ammortamento)
        stampa_ammortamento(piano_ammortamento)
    else:
        print("Hai sbagliato ad inserire qualche dato. Riavvia e riprova")


# invocazione funzione di avvio
start()