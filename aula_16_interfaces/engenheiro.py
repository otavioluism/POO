from interfaces import IFormas


class Engenheiro(object):

    def __init__(self, nome: str):
        self.nome = nome

    def medir_perimetro(self, terreno: IFormas) -> int:
        perimetro = terreno.get_perimetro()
        return perimetro

    def medir_area(self, terreno: IFormas) -> int:
        area = terreno.get_area()
        return area
