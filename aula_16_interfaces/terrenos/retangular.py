from interfaces import IFormas


class TerrenoRetangular(IFormas):

    def __init__(self, largura: int, comprimento: int) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self) -> int:
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro

    def get_area(self) -> int:
        area = self.comprimento * self.largura
        return area