



numero_uno = 0
numero_due = 1
sequenza = 20
print(numero_uno, end=" ")
print(numero_due, end=" ")
for _ in range(sequenza - 2):
    numero_successivo = numero_uno + numero_due
    print(numero_successivo , end=" ")
    numero_uno, numero_due = numero_due, numero_successivo