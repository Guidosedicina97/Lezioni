"""  I.
 Crea uno script nominandolo “esercizio_02”
 II. Richiedi in input all'utente due numeri interi positivi
 III. Controlla che il secondo numero inserito sia maggiore del primo e, sino a quando
 tale condizione non si verifica, continua a richiedere all'utente l'inserimento del
 secondo numero
 OUTPUT
 Stampa in console i soli numeri pari compresi nell'intervallo tra il 1° ed il 2° numero
 ricevuti in input (compresi """

numero_uno = int(input("Inserisci il primo numero intero positivo: "))
while numero_uno <= 0:
    print("Per favore, inserisci un numero intero positivo.")
    numero_uno = int(input("Inserisci il primo numero intero positivo: "))

numero_due = int(input("Inserisci il secondo numero intero positivo: "))
while numero_due <= 0 or numero_due <= numero_uno:
    print("Per favore, inserisci un numero intero positivo.")
    numero_due = int(input("Inserisci il secondo numero intero positivo: "))
for numero_uno in range(numero_uno, numero_due + 1):
    if numero_uno % 2 == 0:
        print(numero_uno)




