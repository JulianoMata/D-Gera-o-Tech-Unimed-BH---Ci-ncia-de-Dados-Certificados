""" 
Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pela qual argumentos possam ser passados, assim um desenvovedor precisa apenas olhar para a definição da função para determinar se os itens são passados por 'posição', por 'nome e posição' ou por nome'.

"""
# OBS: Após a '/' pode passar valores por nome ou posição e antes apenas por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Atenção
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
