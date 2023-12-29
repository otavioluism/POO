from interface import IItens


class Produto(IItens):

    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price

    def informacoes_produto(self) -> None:
        print('{} custa R$ {},00'.format(self.__name, self.__price))
