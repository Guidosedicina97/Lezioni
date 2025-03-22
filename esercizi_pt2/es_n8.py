

giocatore_uno = input(f"Inserisci il tuo nome ")
giocatore_due = input(f"inserisci il tuo nome ")
scelta_uno = input(f"{giocatore_uno} inserisci tra S-sasso, C-carta, F-forbice >>> ").upper()
scelta_due = input(f"{giocatore_due} inserisci tra S-sasso, C-carta, F-forbice >>> ").upper()
if scelta_uno == scelta_due:
    print("pareggio")
elif (scelta_uno == "S" and scelta_due == "F") or ( scelta_uno == "C" and scelta_due == "s" or scelta_uno == "F" and scelta_due == "C"):
    print(f"{giocatore_uno} ha vinto")
else:
    print(f"{giocatore_due} ha vinto")


