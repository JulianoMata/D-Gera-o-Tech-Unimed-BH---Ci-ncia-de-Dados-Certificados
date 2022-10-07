class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw): # conceito chave:valor
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)
        # print(Ornitorrinco.mro())

gato = Gato(nro_patas = 4, cor_pelo = "Preto")  # conceito chave:valor
print(gato)

ornitorrinco = Ornitorrinco(nro_patas = 2, cor_pelo = "vermelho", cor_bico = "laranja") # conceito chave:valor
print(ornitorrinco)
print()
# print(Ornitorrinco.mro()) - exibe a ordem da resolução python para encontrar atributos

linha = ("-=-" * 16)
titulo = (" Qual retorno código abaixo ? ")

print(f"\033[31m{linha.center(50)}\033[m")
print(f"\033[32m{titulo.center(50, '*')}\033[m")
print(f"\033[31m{linha.center(50)}\033[m")

class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()