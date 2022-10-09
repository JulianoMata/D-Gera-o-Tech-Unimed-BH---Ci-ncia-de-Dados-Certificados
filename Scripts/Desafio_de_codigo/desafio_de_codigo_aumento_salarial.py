""" 
Desafios Intermediários Py - Unimed-BH
3 / 3 - Aumento Salarial





 Básico
 Porcentagem
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

Salário	            Percentual de Reajuste

0 - 600.00                  17%
600.01 - 900.00             13%
900.01 - 1500.00            12%
1500.01 - 2000.00           10%
Acima de 2000.00             5%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

Exemplo 1

Entrada	        Saída

1000	        Novo salario: 1120,00 
                Reajuste ganho:120,00                                                                                     
                Em percentual: 12 %
 

Exemplo 2

Entrada	        Saída

2000	        Novo salario: 2200,00                                                                                                   
                Reajuste ganho: 200,00                                                                                                  
                Em percentual: 10 %

"""
salario = float(input(f"Valor salário: "))

if (salario <= 600):
    percentual = 17
elif (salario <= 900):
    percentual = 13
elif (salario <= 1500):
    percentual = 12
elif (salario <= 2000):
    percentual = 10
else:
    percentual = 5

reajuste_ganho = (percentual * salario) / 100
novo_salario = (salario + reajuste_ganho)

print(f"Novo salario: {(novo_salario):.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %".replace(".",","))    


# Outro modo
# salario = int(input())

# def calcular_reajuste(salario):
#     reajuste = 0
#     if salario <= 600:
#         reajuste = 17
#     elif salario <= 900:
#         reajuste = 13
#     elif salario <= 1500:
#         reajuste = 12
#     elif salario <= 2000:
#         reajuste = 10
#     else:
#         reajuste = 5

#     return reajuste


# reajuste = calcular_reajuste(salario)
# parcial = (salario*reajuste) / 100
# print(f"Novo salario: {(salario + parcial):.2f}\nReajuste ganho: {parcial:.2f}\nEm percentual: {reajuste} %".replace(".","."))

