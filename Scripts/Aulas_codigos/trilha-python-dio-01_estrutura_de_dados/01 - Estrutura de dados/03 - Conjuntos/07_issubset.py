conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado) # True  - Todos elentos de 'a' estão em 'b'

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado) # False - Não são todos elementos de 'b' que estão em 'a'
