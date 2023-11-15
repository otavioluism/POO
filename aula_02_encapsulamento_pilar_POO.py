# Encapsulamento
"""
Entraremos agora em um dos pilares do POO

POO - Pilares

- Encapsulamento
- Polimorfismo
- Herança
- Abstração (Alguns colocam, outros não)

O encapsulamento tem como objetivo de privar ou deixar público os atributos/métodos da classe em contexto;

Quando a classe estiver algum atributo ou método privado não poderá ser acessado fora do contexto de classe
a não ser o contexto autal. Somente conseguirá ser acessado por outro contexto se o método ou atributo ser público.

Exemplo: Ao intanciarmos uma classe que dentro dela tem seus métodos privados e publicos, somente conseguiremos chamar
e pegar valores de metodos ou atributos publicos.

"""

class Pessoa(object):

    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def __apresentar_documento(self):
        print('Meu cpf é: {}'.format(self.__cpf))

    def correr(self) -> None:
        print('Estou correndo!')

    def beber(self, bebida: str) -> None:
        if bebida.upper() in ['CERVEJA']:
            self.__apresentar_documento()
        print('Bebendo {}'.format(bebida))
        print('-----------------------------')

ronaldo = Pessoa('Ronaldo', 34, '323233234423')
ronaldo.beber('cerveja')
ronaldo.beber('coca cola')


class Calculadora(object):

    def calcular(self, operacao: str, num_1: float, num_2: float) -> int:
        if operacao == '+':
            return self.__adicionar(num_1, num_2)
        elif operacao == '-':
            return self.__subtrair(num_1, num_2)
        else:
            print('Operacao nao encontrada!')

    @staticmethod
    def __adicionar(num_1: float, num_2: float) -> int:
        return num_1 + num_2

    @staticmethod
    def __subtrair(num_1: float, num_2: float) -> int:
        return num_1 - num_2


calcule = Calculadora()
print(calcule.calcular('-', 1.5, 2))