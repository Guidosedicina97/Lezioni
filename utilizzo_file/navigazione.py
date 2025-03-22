import os

# capire dove lavora lo script in esecuzione
print(os.getcwd()) # ritorna il percorso assoluto della directory di lavoro script
print(os.listdir()) # ritorna una lista con nomi di file e di directory nella directory di lavoro

# risalita di 3 livelli
os.chdir("../../../")
print(os.getcwd())
print(os.listdir())

# ingresso in una cartella directory specifica
os.chdir("Generation")
print(os.getcwd())
print(os.listdir())

# ispezionamento contenuto completo directory di lavoro
for cartella, sottocartelle, files in os.walk(os.getcwd()):
    print(f"Analizzando la cartella {cartella}, troviamo le sottocartelle {sottocartelle}, e i files {files}")