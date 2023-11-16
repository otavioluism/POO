# Variáveis e métodos de classe
"""
Váriavel de classe é uma varíável global, onde todos os objetos que se instanciarem da classe terão o valor desta variável igual,
pois o valor será global para todos, caso for alterada ela pelo contexto self, só será alterado o valor para o
determinado objeto intansciado que esta realizando a alteração;

Método de Classe é o metodo com objetivo de modificar o valor da variável de classe, sendo que quando ocorrer a modificação
todos os valores da variável de classe dos objetos intasciados serão modificados junto com valor passado
para o método de classe;

Exemplo: Vamos criar uma classe chamada Governo, depois intansciaremos vários objetos que serão os governos do estado como
SC, DF, PR e etc. Ai sabemos que o governo federal pode aplicar uma regra e alterar o imposto para todos os estados. Com isto,
podemos utilizar o método de classe (cls) decorador @classmethod para um método e alterarmos o imposto para todos os objetos
que são os governos que devem obedecer o novo imposto federal;

"""


class Governo(object):

    imposto = 1.0

    def __init__(self, instituicao: str) -> None:
        self.instituicao = instituicao

    def apresentar_instituicao(self) -> None:
        print(self.instituicao)

    @classmethod
    def arrecadar(cls) -> int:
        return 40 * cls.imposto

    @classmethod
    def alterar_imposto(cls, nova_taxa: int) -> None:
        print('Mudança de imposto para todos os governos!')
        cls.imposto = nova_taxa


governo_federal = Governo('FEDERAL')
governo_sc = Governo('SC')
governo_federal.apresentar_instituicao()
governo_sc.apresentar_instituicao()

print(governo_federal.arrecadar())
print(governo_sc.arrecadar())

governo_federal.alterar_imposto(1.5)

print(governo_federal.arrecadar())
print(governo_sc.arrecadar())
