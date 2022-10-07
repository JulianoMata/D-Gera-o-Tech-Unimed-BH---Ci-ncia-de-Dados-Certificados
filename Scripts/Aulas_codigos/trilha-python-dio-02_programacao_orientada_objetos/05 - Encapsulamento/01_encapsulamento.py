""" 
                                        Proteção de Acesso
                                        
O encapsulamento é um dos conceitos fundamentais em 'POO'. Ele descreve a idéia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acessso direto a variáveis e métodos epode evitar a modificação acidental de dados. Para evitar alterações acidentais,  a variável de um objeto só pode ser alterada pelo método desse objeto.

"""

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
