numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - Elimina valores duplicados

numeros.discard(1)  # Descarta o valor
numeros.discard(45) # Não existindo o comando é ignorado

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
