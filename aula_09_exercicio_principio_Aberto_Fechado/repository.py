from database import PostgresDB, MySQL


class Repositorio(object):

    def select(self, conexao: MySQL) -> None:
        conexao.conectar()
        print('QUERY SELECT * FROM ....')
        conexao.desconectar()

    def insert(self, conexao: MySQL) -> None:
        conexao.conectar()
        print('QUERY INSERT INTO * VALUES ....')
        conexao.desconectar()
