from abc import ABC, abstractmethod


class AvesQueVoam(ABC):

    def comer(self):
        raise 'Aves que comem'

    def gritar(self):
        raise 'Aves que cantam'

    def voar(self):
        raise 'Aves que voam'


class AvesQueNaoVoam(ABC):

    def comer(self):
        raise 'Aves que comem'

    def gritar(self):
        raise 'Aves que cantam'
