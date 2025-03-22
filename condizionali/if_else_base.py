# acquisizione input utente (genere)
genere = input("digita F per femmina o M per maschio >>> ")

# output utente in base a valutazione input
if genere.upper() == "F": # caso Femmina
    print("Benvenuta")
elif genere.upper() == "M": # caso maschio
    print("Benvenuto")
elif not genere: # caso senza input
    print ("non hai digitato nulla")
else:
    print("Hai digitato qualcosa che non capisco")
