# Associação de classes

"""

Classe Pessoa ----> Classe Interruptor

Classe pessoa associada a classe interruptor

Associação de classe é muito utilizado para uma questão de compartilhamento de algo que precisa ser criado só uma vez
e depois é associado por quem utiliza. Como banco de dados, conexão com rest api;
Podendo ser criado uma classe para o banco de dados fazendo toda conexão e desconexão, sendo passado para modulo de regra
de negocio (os controllers) afim de chamar o banco quando for preciso;

"""


class Interruptor(object):

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print('Acendendo {}'.format(self.__comodo))

    def apagar(self) -> None:
        print('Apagando {}'.format(self.__comodo))


class Pessoa(object):

    def acender_luz(self, interruptor: Interruptor) -> None:
        print(interruptor.acender())

    def apagar_luz(self, interruptor: Interruptor) -> None:
        print(interruptor.apagar())

    def dormir(self) -> None:
        print('Fui dormir!')

pessoa_1 = Pessoa().acender_luz(Interruptor('Quarto'))
pessoa_2 = Pessoa().acender_luz(Interruptor('Sala'))
pessoa_2 = Pessoa().apagar_luz(Interruptor('Sala'))
pessoa_1 = Pessoa().apagar_luz(Interruptor('Quarto'))