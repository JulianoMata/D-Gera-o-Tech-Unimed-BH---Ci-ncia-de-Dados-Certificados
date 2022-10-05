conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado) # False - Nem todos elementos de 'b' estão em 'a'

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado) # True - Todos elemntos de 'a' estão em 'b'
