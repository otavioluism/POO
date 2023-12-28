"""
Classe Abstrata -> uma classe que não pode ser instanciada e ser chamada seus métodos, ela somente pode ser
passada como herança ou seja, somente se uma classe herde dela. Sendo que classe abstrata os seus métodos marcados
como abstrato devem obrigatoriamente estar declarados também na classe que herdou a classe abstrata.

"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def __init__(self):
        self.atributo = 'Ola Mundo'

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass


class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Metodo abstrato')


filha = Filha()
filha.apresentar_metodo()
filha.metodo('Oi')
filha.metodo_abstrato()
