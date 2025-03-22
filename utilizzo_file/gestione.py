import os
import shutil

# creazione di una directory nella directory di lavoro corrente
os.makedirs("cartella", exist_ok=True)

# creazione di una struttura di directory annidate
os.makedirs("cartella2/sottocartella", exist_ok=True)

# creazione di un file in sottodirectory "sottocartella"
open("cartella2/sottocartella/file.txt", "w")

# rinomina directory
#os.rename("cartella", "nuova_cartella")

# copia di singoli elementi o intere strutture
#shutil.copytree("cartella2", "copia")

# metodi di interrogazione
print(os.path.exists("copia"))
print(os.path.isdir("nuova_cartella"))
print(os.path.isfile("cartella2/sottocartella/file.txt"))

# cancellazione di file, directory e strutture
# os.remove("copia/sottocartella/file.txt") # rimozione file sempre possibile se esiste
# os.rmdir("nuova_cartella") # rimozione directory vuota sempre possibile
# os.rmdir("copia") # rimozione di directory non vuota non possibile con questa funzione
# os.removedirs("copia/sottocartella") # rimozione struttura directory senza file
shutil.rmtree("cartella2")