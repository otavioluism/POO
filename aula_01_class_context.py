# Classes e Contexto
"""
Em termos técnicos:

Classe: É um conjunto de métodos denominados ações e de atributos denominados características, no qual obtêm
um objetivo específico.

Exemplo: Iremos criar uma classe de controle remoto (Objeto) que terá suas característacas (atributos) e seus
respectivos métodos.

Classe:
Controle Remoto

Atributos:
Televisão e cômodo

Métodos:
Avançcar Canal, Voltar Canal e Escolher Canal

"""


class ControleRemoto(object):

    def __init__(self, televisao: str, comodo: str) -> None:
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self) -> None:
        print('Avançar Canal!')

    def voltar_canal(self) -> None:
        print('Voltar Canal!')

    def escolher_canal(self, canal: int) -> None:
        print('Alterado para o canal -> {}'.format(canal))


controle_sala = ControleRemoto("Samsumg", "sala")
print(controle_sala.televisao)
print(controle_sala.comodo)
print(controle_sala.avancar_canal())
print(controle_sala.voltar_canal())
print(controle_sala.escolher_canal(15))

controle_quarto = ControleRemoto("LG", "quarto")
print(controle_quarto.televisao)
print(controle_quarto.comodo)
print(controle_quarto.avancar_canal())
print(controle_quarto.voltar_canal())
print(controle_quarto.escolher_canal(12))