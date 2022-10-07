""" 
01 - João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. adicione esses comportamentos!

"""

""" 
UMA CLASSE DEFINE AS CARACTERÍSTICAS E COMPORTAMENTOS DE UM OBJETO, PORÉM NÃO CONSEGUIMOS USÁ-LAS DIRETAMENTE. JÁ OS OBJETOS PODEMOS USÁ-LOS E ELES POSSUEM AS CARACTERÍSTICAS E COMPORTAMENTOS QUE FORMA DEFINIDOS NAS CLASSES.


"""

linha = ("=" * 50)
titulo = (" Desafio Bicicletaria ")

print(f"\033[33m{linha.center(50)}\033[m")
print(f"\033[32m{titulo.center(50, '*')}\033[m")
print(f"\033[33m{linha.center(50)}\033[m\n")

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")
        
    
    
    # esse código pode ser ÚTIL qdo vc for adicionar algum outro item em sua classe!!!
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bicicleta_1 = Bicicleta("vermelha", "caloi", 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.correr()
bicicleta_1.parar()
print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)

bicicleta_2 = Bicicleta("verde", "monark", 2000, 189)
print(bicicleta_2)
bicicleta_2.correr()
