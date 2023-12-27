"""
Este principio tem como objetivo fazer com que a classe pai sempre tenha métodos
que seus filhos herde metódos que também utilizam, o principio de LISKOV é quebrado no momento que a classe pai tenha
um método que seu filho também tenha com o mesmo nome e consequetemente tenha resposta diferente na chamada da classe pai
e classe filho.
"""


class ConnectionDatabase(object):

    @staticmethod
    def connect() -> None:
        print('Database connected!')

    @staticmethod
    def disconnect() -> None:
        print('Database disconnect!')


class MySQLRepository(ConnectionDatabase):

    def __init__(self):
        super().__init__()

    def select(self) -> None:
        self.connect()
        print('SELECT * FROM tabela')
        self.disconnect()


class CaseUse(object):

    @staticmethod
    def buscar_dados(db_repo: MySQLRepository) -> None:
        db_repo.select()


caso_uso = CaseUse()
caso_uso.buscar_dados(MySQLRepository())
