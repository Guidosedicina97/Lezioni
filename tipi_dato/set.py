# dichiarazione e istanziazione di un set
#set_uno = {1, "ciao", True, (1,2,3), [1,2,3]} commentato --> i seti non possono contenere elementi mutabili (come liste)
set_due = {1, "ciao", True, (1,2,3)}
print(set_due,type(set_due))
set_tre = set([1, 3, 3, 4, 4, 2])
print(set_tre, type(set_tre))
set_vuoto_uno = set() # con costruttore crea un set vuoto
print(set_vuoto_uno,type(set_vuoto_uno))
set_vuoto_due = {} # lo literal per set vuoto (si crea un oggetto dict)
print(set_vuoto_due,type(set_vuoto_due))

# aggiunte e rimozioni elementi set
set_vuoto_uno.add(34)
print(set_vuoto_uno)
set_due.add("ciao")
print(set_due)
set_due.remove(1)
print(set_due)
# set_due.remove(1) # commentato in quanto causa errore (elemento non presente)

