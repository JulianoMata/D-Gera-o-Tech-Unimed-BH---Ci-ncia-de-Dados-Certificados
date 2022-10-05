lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(lista2), id(lista))  # Comprovando que são listas diferentes

lista2[0] = 2

print(lista2)
print(lista)