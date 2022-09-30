opcao = -1

while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break
    
    print(numero)

#------------------------------------------------------------------------------------------------------------    
    
for numero in range(100):
    
    if numero == 10:
        break       # corta a execução
    
    print(numero, end = " ")
    
#------------------------------------------------------------------------------------------------------------

for numero in range(100):
    
    if numero % 2 == 0:  # numeros pares de o a 100
        continue
    
    print(numero, end = " ")