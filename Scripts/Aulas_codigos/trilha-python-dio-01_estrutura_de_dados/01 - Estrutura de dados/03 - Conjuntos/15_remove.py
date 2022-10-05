numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0  - Se o valor existir então é removido senao dá 'erro'. Já o 'discard', não!
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
