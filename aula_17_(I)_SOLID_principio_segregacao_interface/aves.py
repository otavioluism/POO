from interface import AvesQueNaoVoam, AvesQueVoam


class Pinguin(AvesQueNaoVoam):

    def gritar(self):
        print('Estou catando!')

    def comer(self):
        print('Estou comendo!')


class Canario(AvesQueVoam):

    def gritar(self):
        print('Estou cantando!')

    def comer(self):
        print('Estou comendo!')

    def voar(self):
        print('Estou voando!')
