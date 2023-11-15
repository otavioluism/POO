# Encapsulamento
"""
Entramos em um assusnto muito importante, os métodos Getters e Setters

Estes métodos tem como objetivo auxiliar o usuário acessar os atributos(estatos) privados de uma classe, já que vimos
que quando há atributo privado fora do contexto não conseguimos ver seu valor e nem setar seu valor. Por este meio, que se
utiliza os métodos getters e setters.

"""


class Alarme(object):

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor


alarme = Alarme(False)
print(alarme.get_estado())
alarme.set_estado(True)
print(alarme.get_estado())

print('---------------------------')

alarme = Alarme(True)
print(alarme.get_estado())
alarme.set_estado('oi')
print(alarme.get_estado())
