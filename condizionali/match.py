# codice del linguaggio predefinito nel dispositivo
linguaggio = "IT"

# analisi_dataset del valore acquisito per inpostazione GUI (Graphic User Interface)
match linguaggio:
    case "fr":
        print("Impostiamo interfaccia in francese")
    case "it" | "IT":
        print("Impostiamo interfaccia in italiano")
    case "de":
        print("Impostiamo interfaccia in tedesco")
    case _:
        print("Impostiamo interfaccia in inglese")

