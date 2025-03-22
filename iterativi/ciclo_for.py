# dobbiamo stampare 10 volte la frase "Hello world" tenendo il conteggio delle interazioni (0-9)
for contatore in range(10): # 0-9
    print(f"Hello World --> a questo giro, contatore vale {contatore}")

print("*****************************************************************")

# dobbiamo stampare 10 volte la frase "Hello world" tenendo il conteggio delle interazioni (1-10)
for contatore in range(1, 11): # 1-10
    print(f"Hello World --> a questo giro, contatore vale {contatore}")

print("*****************************************************************")

# iteriamo gli elemendi di una lista per stamparli
lista = ["uno","due", "tre", "quattro"]

for elemento in lista:
    print(elemento)

print("*****************************************************************")

#iteriamo gli elementi di una lista per stampare solo quelli con indice pari
for indice in range(0,len(lista), 2):
    print(lista[indice])

print("*****************************************************************")

#iteriamo gli elementi di una lista dall'ultimo al primo (iterazione inversa)
for indice in range(len(lista) - 1, -1, -1 ):
    print (lista[indice])

print("*****************************************************************")

#iteriamo gli elementi di una lista dall'ultimo al primo (iterazione inversa) con slicing lista
for elemento in lista[::-1]:
    print(elemento)
print(lista) #no alterazione struttura lista


print("*****************************************************************")

#abbiamo una lista di numeri e li vogliamo stampare ma se nella lista troviamo il numero 5 fermiamo il ciclo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeri:
    if numero == 5:
        break
    print(numero)
else:
    print("Il ciclo ha terminato il suo lavoro")
print("Fine programma")

print("*****************************************************************")

# abbiamo una lista di numeri e li vogliamo stampare tutti tranne il numero 5
for numero in numeri:
    if numero == 5:
        continue
    print(numero)