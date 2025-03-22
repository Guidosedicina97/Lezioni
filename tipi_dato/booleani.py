#dichiarazione e istanziazione di variabili per booleani
booleano_uno =True
booleano_due =False
print(booleano_uno,type(booleano_uno))
print(booleano_due,type(booleano_due))

# analisi_dataset logiche di verità
print(bool(12), bool(0)) # True ( tutti i numeri tranne lo 0) / False (numeri 0)
print(bool(" "), bool("")) # True (ogni stringa con almeno un carattere) / False (stringhe vuote)
print (bool([]), bool([1,2])) # False (strutture vuote) / True (strutture con almeno un elemento)
print(bool(None)) # False valore booleano implicito di tutto che è nullo

# operatori logici and e or
print(True and True) # True (tutte le sotto-espressioni devono essere vere)
print(True and False) # False (se una delle sotto-espressioni è falsa)
print(True or False) # True (basta che una sotto-espressione sia vera)
print(False or False) # False (se tutte le sotto-espressioni sono false)

# espressioni con operatori di confronto
espressione_uno = 12 <= 10
print(espressione_uno,(type(espressione_uno)))
espressione_due = "ciao" == "ciao"
print (espressione_due, type(espressione_due))
espressione_tre = 10 != 10 and 1 < 3
print(espressione_tre,type(espressione_tre))
espressione_quattro = 10 != 10 or 1 < 3
print (espressione_quattro,type(espressione_quattro))

# operatore not (negazione)
espressione_cinque = not (10 == 10)
print (espressione_cinque)

# operatori di identità is per numeri
potenza_uno = 2 ** 1000
potenza_due = 2 ** 1000
print(potenza_uno == potenza_due) # operatore == controlla il valore (True)
print(potenza_uno is potenza_due) # operatore is controlla la locazione di memoria
potenza_due = potenza_uno
print(potenza_uno is potenza_due)

# operatori di identita is per stringhe
stringa_uno = "a" * 2
stringa_due = "a" * 2
print(id(stringa_uno), id(stringa_due))
print(stringa_uno == stringa_due) # operatore == controlla il contenuto (True)
print (stringa_uno is stringa_due) # operatore is controlla la locazione di memoria
