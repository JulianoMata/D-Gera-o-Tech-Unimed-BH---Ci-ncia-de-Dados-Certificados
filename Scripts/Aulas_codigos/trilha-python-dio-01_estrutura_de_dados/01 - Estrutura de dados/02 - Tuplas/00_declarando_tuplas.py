# Criação de 'Tuplas' utiliza-se 'Parênteses'(com vírgula após o ultimo valor) ou 'Tuple'
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# Exercicio
carros = ("gol")
print(isinstance(carros, tuple)) # False
