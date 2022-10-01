# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
# valores = input().split() 

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.

cachorros_quente, participante = list(map(int, input().split(" ")))

def media_consumo():
    return cachorros_quente / participante

print(f"{media_consumo():.2f}")

# Segue mesmo raciocínio Desafio 1, 

"""
Estrutura map no Python
Utilizar o map com a função desejada e a lista em que vai aplicar.

O map vai pegar cada elemento dessa lista e vai aplicar a função.

IMPORTANTE: Isso só vai funcionar para elementos que o map pode percorrer, pois ele pega os elementos e joga eles como argumento da função, então sua função também precisa ter um valor de entrada.

O resultado não sai exatamente como esperado(recebemos um map object). 

Isso acontece porque ele não vem com um formato de lista.

Então para resolver esse problema basta utilizar o list para transformar isso em uma lista.

"""

# Esse código é p rodar na plataforma DIO