def divisione(a, b):
    try:
        print(int(a) / int(b))
    except ValueError as v:
        print(v)
    except ZeroDivisionError as z:
        print(z)

def divisione_due(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("valori non corretti") if isinstance(e, ValueError) else print("Divisione per 0 impossibile")

def divisione_tre(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("valori non corretti") if isinstance(e, ValueError) else print("Divisione per 0 impossibile")
    finally:
        print("questa istruzione viene eseguita comunque")

def divisione_quattro(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("valori non corretti") if isinstance(e, ValueError) else print("Divisione per 0 impossibile")
    else:
        print("tutto è andato per il meglio")
    finally:
        print("questa istruzione viene eseguita comunque")



#invocazioni funzioni
print("Avvio Programma")

divisione("5", "0")

divisione_tre("5", "0")

divisione_quattro("5", "ciao")

print("Fine Programma")