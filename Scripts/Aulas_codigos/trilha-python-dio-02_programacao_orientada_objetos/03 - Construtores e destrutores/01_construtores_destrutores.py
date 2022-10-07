""" 
O MÉTODO CONSTRUTOR SEMPRE É EXECUTADO QUANDO UMA NOVA INSTÂNCIA DA CLASSE É CRIADA. NESSE MÉTODO INICIALIZAMOS O ESTADO DO NOSSO OBJETO. PARA DECLARAR O MÉTODO CONSTRUTOR DA CLASSE, CRIAMOS UM MÉTODO COM O NOME __init__.

"""
""" 
O MÉTODO DESTRUTOR SEMPRE É EXECUTADO QUANDO UMA INSTÂNCIA (OBJETO) É DESTRUÍDA. DESTRUTORES EM PYTHON NÃO SÃO TÃO NECESSÁRIOS QUANTO EM C++ PORQUE O PYTHON TEM UM COLETOR DE LIXO QUE LIDA COM O GERENCIAMENTO DE MEMÓRIA AUTOMATICAMENTE. PARA DECLARAR O MÉTODO DESTRUTOR DA CLASSE, CRIAMOS UM MÉTODO COM O NOME __del__.

"""

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
