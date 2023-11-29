# Princípio aberto e fechado

"""

Módulo fechado é quando um método que gerencia as ações tem estipulado um conjunto finito de funcionalidades para se realizar,
ele acaba sendo aberto quando o conjunto acaba sendo infinito a partir da sua entrada.

"""
import abc


# Principio fechado, onde a classe que gerencia as acoes tem um numero finitos de entradas para gerar acoes de saidas
class Circo(object):

    def apresentar(self, tipo: int) -> None:
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhacao()

    def apresentar_malabarista(self) -> None:
        print('Malabarista apresentando seu show')

    def apresentar_palhacao(self) -> None:
        print('Palhaco apresentando seu show')


circo = Circo()
circo.apresentar(3)


# Principio Aberto, quando o numero de entradas passadas pode ser infinitas que tera saidas diferentes

class Circo(object):

    @staticmethod
    def apresentar(apresentador) -> None:
        apresentador.apresentar_show()


class Malabarista(object):

    @staticmethod
    def apresentar_show() -> None:
        print('Malabarista apresentando seu show')


class Palhaco(object):

    @staticmethod
    def apresentar_show() -> None:
        print('Palhaco apresentando seu show')

circo = Circo()
circo.apresentar(Palhaco)