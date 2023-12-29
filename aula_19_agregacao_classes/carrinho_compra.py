from produto import Produto


class CarrinhoCompra(object):

    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self):
        print('Compra Finalizadas!')

        for produto in self.__produtos:
            produto.informacoes_produto()

        self.__produtos = []
