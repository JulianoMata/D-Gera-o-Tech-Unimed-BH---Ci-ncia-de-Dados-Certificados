""" 
Desafio
Dada a letra N do alfabeto, nos diga qual a sua posição.

Entrada
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

Saída
Um único inteiro, que representa a posição da letra no alfabeto.

 
Exemplo de Entrada	Exemplo de Saída
C                         3
J	                     10
Z                        26                         
A                         1                           
 
"""
import string

alfabeto = list(string.ascii_uppercase)
letra = input().upper()
posicao = alfabeto.index(letra) + 1

print(posicao)
