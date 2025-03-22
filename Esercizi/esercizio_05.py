#crea uno script nominandolo "esercizio_05"
#richiedi all'utente di inserire in input una parola (nessun controllo)
#output stampa in console il risultato booleano (True o False) del seguente controllo: la parola interita è palindroma?

parola = input("Inserisci una parola")
palindroma = bool(parola == parola[::-1])
print (f"La parola è: {parola}, è palindroma? {palindroma}")
