#dichiarazione e istanziazione di liste vuote
lista_uno = [] #literal
print(lista_uno,type(lista_uno))
lista_due = list() #mediante costruttore di classe list
print(lista_due,type(lista_due))

#popolamento delle liste
lista_uno.append(10)
lista_uno.append(20)
print(lista_uno,len(lista_uno))
lista_uno.insert(1, 34)
print(lista_uno,len(lista_uno))

#dichiarazione, istanziazione e popolamento
lista_tre = [3, 5, "ciao", False] #literal
lista_quattro = list ((4, 10, "bello", 10)) #mediante costruttore di classe list (con tupla)
print(lista_tre,len(lista_tre))
print(lista_quattro,len(lista_quattro))
lista_quattro.append(4 < 8)
print(lista_quattro, len (lista_quattro))

#accesso a elementi in una lista (in base a indice posizionale)
print(lista_tre[2]) #acceso a specifico indice (errore se inesistente)
print(lista_tre[0]) #accesso al primo elemento(errore se lista vuota)
print(lista_tre[-1]) #accesso all'ultimo elemento(errore se lista vuota)

#modifica di elementi presenti nella lista
lista_quattro[1] = True
print(lista_quattro)

# rimozione elementi presenti in lista
lista_quattro.remove(10) #rimuove il valore indicato
print(lista_quattro)

#concatenazione liste
lista_uno += lista_tre
print(lista_uno)

#raddoppio degli elementi
lista_uno *= 2
print(lista_uno)

# operazioni di slicing
print(lista_uno[3:]) #da indice inizio compreso a fine naturale
print(lista_uno[:4]) #da inizio naturale a indice fine escluso
print(lista_uno[2:5]) #da indice inizio compreso a indice fine escluso

# principali metodi di classe list
lista_uno.reverse()
print(lista_uno)
#lista_uno.sort() commentato per errore ordinamento su lista eterogenea
#print(lista_uno)

lista_cinque = [45,5,78,3]
lista_cinque.sort() #ordinamento crescente
print(lista_cinque)
lista_sei = [45,5,78,3]
lista_sei.sort(reverse=True) #ordinamento decrescente
print(lista_sei)

#rimozione di tutti gli elementi presenti
lista_sei.clear()
print(lista_sei, len(lista_sei))

# unpackaging sulle liste
lista_sette = ["ciao", True]
uno, due = lista_sette
print(uno, type(uno))
print(due,type(due))
print(lista_sette)

# scomposizione di una stringa in una lista (in base a un carattere separatore)
stringa = "uno,due,tre"
lista_otto = stringa.split(",")
print(lista_otto, len ( lista_otto))
stringa = ",".join(lista_otto)
print(stringa)
