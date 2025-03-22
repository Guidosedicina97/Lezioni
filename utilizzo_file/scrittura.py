# funzione per scrivere testo su un file che verrà creato
def scrivi_su_file(testo):
    file = None
    try:
        file = open("file.txt", "w") # apertura stream (in modalità sovrascrittura)
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()

# funzione per scrivere testo su un file che verrà creato
def scrivi_a_file(testo):
    file = None
    try:
        file = open("file2.txt", "a") # apertura stream (in modalità append)
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()

# funzione per scrivere testo su un file con gestione automatica della chiusura
def scrivi_e_chiudi(testo):
    try:
        with open("file3.txt", "x") as file: # apertura stream (modalità protetta)
            file.write(testo)
    except Exception as e:
        print(e)

# invocazione funzioni
# scrivi_su_file("2^ riga di testo")
# scrivi_a_file("2^ riga di testo")
scrivi_e_chiudi("1^ riga di testo")