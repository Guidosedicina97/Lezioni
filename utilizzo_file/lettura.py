# funzione per leggere il contenuto di un file e ritornarlo come stringa
def leggi_file():
    try:
        with open("file2.txt", "r") as file:
            contenuto = file.read()
            print(type(contenuto))
            return contenuto
    except Exception as e:
        print(e)

# funzione per leggere il contenuto di un file e ritornarlo come stringa
def leggi_file_due():
    try:
        with open("file2.txt", "r+") as file:
            contenuto = file.readlines()
            print(type(contenuto))
            return contenuto
    except Exception as e:
        print(e)

#invocazione funzioni
print(leggi_file())
print(leggi_file_due())