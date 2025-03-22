# dichiarazione e istanziazione variabili per stringhe (sequenze di caratteri)
stringa_uno = "Ciao Mondo" #literal
print(stringa_uno, type(stringa_uno))
stringa_due = str("Ciao Mondo") # mediante costruttore di classe str (string)
print(stringa_due,type(stringa_due))
stringa_tre = str(100.56)
print (stringa_tre,type(stringa_tre))
stringa_quattro = 'ciao' # apici singoli o doppi non cambia nulla
print (stringa_quattro,type(stringa_quattro))
stringa_cinque = """
Sono una stringa
    su più linee
e supporto indentazione
"""
print (stringa_cinque)

# stringa formattata
numero = 20
# stringa_sei = "il valore della variabile numero è " + numero commentato perchè da errore
stringa_sei = f"il valore della variabile numero è {numero}"
print (stringa_sei)

# stringa con valutazione di espressioni matematiche
print(eval("15 * (4-2) ** 2 + 1"))

#operatori utilizzati sulle stringhe
stringa_sette = "Ciao"
stringa_otto = "Mondo"
print(stringa_sette + stringa_otto)
print(stringa_sette * 3)

#alcuni metodi e funzioni utilizzabili sulle stringhe
print(len(stringa_uno)) # ritorna lunghezza stringa (n° caratteri che la compongono)
print(stringa_uno.find("i")) # ritorna indice 1° occorrenza (indici in base 0)
print(f"L'indice della prima i nella stringa è {stringa_uno.find("i")}")
stringa_uno.replace("o", "*")
print(stringa_uno)
stringa_uno = stringa_uno.replace("o", "*")
print(stringa_uno)

# slicing su stringhe
stringa_lunga = "supercalifragilistichespiralidoso"
print(stringa_lunga[2:9]) #stampa una parte della stringa tra indice 2 e indice 9 (escluso)
print(stringa_lunga[3:])  #stampa una parte della stringa tra indice 3 (compreso) e fine naturale
print(stringa_lunga[:10]) #stampa una parte della stringa tra inizio naturale e indice 10 (escluso)
print(stringa_lunga[3]) #stampa carattere ad un determinato indice della stringa
print(stringa_lunga[-4:]) #stampa ultimi 4 caratteri con indice negativo (-1 è sempre l'ultimo)
print(stringa_lunga[::2]) #stampa da inizio a fine naturale della stringa con passo 2 (caratteri indici pari)
print(stringa_lunga[::-1]) #stampa la stringa rovesciata (passo negativo)
