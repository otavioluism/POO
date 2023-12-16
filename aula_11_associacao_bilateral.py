class Casa(object):

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco
        self.__proprietario = None

    def acender_luzes(self) -> None:
        print('Estou acendendo as Luzes')

    def get_endereco(self) -> str:
        return self.__endereco

    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario

    def get_proprietario(self) -> any:
        return self.__proprietario


class Pessoa(object):

    def __init__(self, nome: str) -> None:
        self.__local = None
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

    def se_apresentar(self) -> None:
        print(f'Ola, eu sou {self.__nome}')

    def set_local(self, local: Casa) -> None:
        self.__local = local


casa = Casa('Rua dos Limoeiros')
ana = Pessoa('Ana')

ana.set_local(casa)
casa.set_proprietario(ana)

proprietario = casa.get_proprietario()
proprietario.se_apresentar()

ana.apresentar_local()
