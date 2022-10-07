""" 
Objetos de primeira classe

Em python tudo é objeto, dessa forma funções também são objetos o que tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).

"""


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é:  \033[1;32m{resultado}\033[m")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 - 10 = 0

# testes com variavel

operacao = somar
print(f"\033[1;31mOperação usando cores\033[m \033[1;32m{operacao(15, 12)}\033[m")