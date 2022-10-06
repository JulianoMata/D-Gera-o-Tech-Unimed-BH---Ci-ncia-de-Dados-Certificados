""" 
Escopo local e global

Python trabalha com escopo global e local.
Dentro do bloco da função o escopo é local, portando alterações ali feitas em objetos imutáveis serão perdidas quando método terminar de ser executado. 
Para objetos globais utilizamos a palavra-chave 'global', que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
*Essa NÂO é uma boa prática e deve ser evitada


"""

salario = 2000


def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    salario += bonus
    return salario
lista = [1]

salario_bonus = salario_bonus(500, lista)  # 2500
print(f"\033[095m{salario_bonus}\033[m")
print(f"\033[032m{lista}\033[m")
