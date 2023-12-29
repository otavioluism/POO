from terrenos import TerrenoQuadrado, TerrenoRetangular
from engenheiro import Engenheiro


terreno_quadrado = TerrenoQuadrado(4)
terreno_retangular = TerrenoRetangular(2, 3)
engenheiro = Engenheiro('Oswaldo')

engenheiro.medir_perimetro(terreno_quadrado)
engenheiro.medir_perimetro(terreno_retangular)

engenheiro.medir_area(terreno_retangular)
engenheiro.medir_area(terreno_quadrado)
