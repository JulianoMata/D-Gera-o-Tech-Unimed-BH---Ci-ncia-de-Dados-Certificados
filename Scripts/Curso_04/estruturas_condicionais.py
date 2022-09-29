# Exemplos:

import sys


saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizadndo saque!")
    
if saldo < saque:
    print("Saldo insuficiente!")
    
#------------------------------------------------------------------------------------------------------------
    
saldo_2 = 2000
saque_2 = float(input("Informe o valor do saque: "))

if saldo_2 >= saque_2:
    print("Realizadndo saque!")
    
else:
    print("Saldo insuficiente!")
    
#------------------------------------------------------------------------------------------------------------

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a o valor para o saque: "))
    
elif opcao == 2:
    print("Exibindo extrato ...")
    
else:
    sys.exit("Opção inválida.")
     
#------------------------------------------------------------------------------------------------------------

MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")
   
#------------------------------------------------------------------------------------------------------------ 
    
MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

else:
    print("Ainda não pode tirar CNH.")

#------------------------------------------------------------------------------------------------------------

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
    
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode tirar CNH.")

else:
    print("Ainda não pode tirar CNH.")
