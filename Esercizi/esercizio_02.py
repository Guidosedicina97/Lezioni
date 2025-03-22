#crea uno script nominandolo "esercizio_02"
#dichiara una variabile e istanziala con l'anno attuale
#richiedi all'utente di inserire in input il suo anno di nascita (nessun controllo)

anno = 2025
anno_nascita_utente = int(input("Inserisci il tuo anno di nascita: "))
eta_utente = anno - anno_nascita_utente
maggiorenne = bool(eta_utente > 18)
print(f"hai {eta_utente} anni, sei maggiorenne {maggiorenne}")