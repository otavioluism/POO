
class PostgresDB(object):

    def __init__(self):
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print('Conectando ao banco Postgres...')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do banco Postgress...')


