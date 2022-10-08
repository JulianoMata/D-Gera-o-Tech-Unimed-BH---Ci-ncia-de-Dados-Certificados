""" 
Importante: Interfaces definem o que uma classe deve fazer e não como.

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas par criar contratos. Classes abstratas não podem ser instanciadas.

ABC - Por padrão, o Python não oferece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é 'ABC'. Este funciona decorando métodos da classe base como abstratos e , em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato qdo descorado com '@abstractmethod'

"""

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
