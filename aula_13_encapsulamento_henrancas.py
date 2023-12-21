"""
O encapsulamento tem 3 tipos que são o público, protegido e privado

O público como todos já sabem pode ser acessado pela CLASSE, HENRECAO E OBJETO
O privado pode ser acessado exclusivamente somente pela sua CLASSE
O protegido pode ser acessado somente também pela CLASSE e HERANCA

Quando instanciamos um objeto de uma classe que tenha algum atributo protegido, nao conseguimos acessar
por ele somente pode ser acessado por sua classe ou heranca, isso em JAVA. Em python ele acaba tendo a excecao
de ser como uma variavel publica, mas o conceito foi o citado acima.

Observacao: A classe protegida tem como funcao como o nome mesmo diz proteger o metodo ou atributo para que nao seja
acessado de fora. No diagrama é represetando com o # jogo da velha.

"""


class DatabaseConnection(object):

    def __init__(self):
        self.__database = 'Postgres'
        self._con = '://connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    @staticmethod
    def _testing_connection() -> None:
        print('Connection Error!')


class Repository(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def select(self) -> None:
        self._testing_connection()
        print('Connection to {}'.format(self._con))
        print('SELECT * FROM table')
        print(self.user)


db = Repository()
db.select()