#crea uno script nominandolo esercioz_04
#dichiara una variabile e istanziala con l'anno attuale
#richiedi all'utente di inserire in input il suo anno di nascita (nessun controllo)
#output stampa in console il risultato booleano (True o False) del seguente controllo: l'età dell'utente corrisponde a un numero pari?


anno_corrente= 2025
anno_di_nascita = int(input("Inserisci il tuo anno di nascita:"))

eta_utente = anno_corrente - anno_di_nascita

numero_pari = bool(eta_utente % 2 == 0)

print(f"Hai {eta_utente} anni. La tua età è pari {numero_pari}")