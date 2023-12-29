from abc import ABC, abstractmethod


class IItens(ABC):

    @abstractmethod
    def informacoes_produto(self) -> None:
        pass
