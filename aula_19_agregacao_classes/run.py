from produto import Produto
from carrinho_compra import CarrinhoCompra

carrinho = CarrinhoCompra()
carrinho.adicionar_produto(Produto('TV', 2000))
carrinho.finalizar_compra()
