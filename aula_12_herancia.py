class Mae(object):

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo !!!')

    def estudar(self) -> None:
        print('Estou estudando !!!')


class Filha(Mae):

    def __init__(self):
        super().__init__('Rua do Bolo')

    def brincar(self, brinquedo: str) -> None:
        print('Estou brincando com {}'.format(brinquedo))


filha = Filha()
filha.comer()