"""
Este metodo de injencao de dependencia tem como objetivo uma classe depender de outra injetada a ela
sendo que como cada classe tem sua funcao propria, ao juntar-se formam uma informacao completa 

"""


class Casa(object):

    def __init__(self):
        self.__endereco = 'Rua Governador Basconcelos'

    def acender_luz(self):
        print('Acendendo a luz da casa')

    def get_endereco(self) -> str:
        return self.__endereco


class Pessoa(object):

    def __init__(self, nome: str, local: Casa) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luz()

    def apresentar_local(self) -> None:
        print(self.__local.get_endereco())


casa_de_amigo = Casa()
pessoa = Pessoa('Felipe', casa_de_amigo)

pessoa.entrar_no_local()
pessoa.apresentar_local()
