# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# --------------------------------------------------------------------------
quadrado2 = []

for numero in numeros:
    quadrado2.append(numero ** 2)
print(quadrado2)

# --------------------------------------------------------------------------

# Exercicio 
numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(numeros)