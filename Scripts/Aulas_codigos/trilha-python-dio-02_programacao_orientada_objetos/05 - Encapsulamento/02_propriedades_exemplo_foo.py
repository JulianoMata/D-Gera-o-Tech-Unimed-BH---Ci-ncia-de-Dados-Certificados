""" 
Para que servem as propriedades?

Com o 'property()' do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, tb conhecidos como 'propriedades', qdo precisa modificar sua implementação interna sem alterar a API pública da classe.

"""


class Foo:
    def __init__(self, x = None):
        self._x = x

    @property  # Para retornar um valor
    def x(self):
        return self._x or 0

    @x.setter    # Para alterar um valor
    def x(self, value):
        self._x += value

    @x.deleter   # Para deletar um valor - usado em casos específicos
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
