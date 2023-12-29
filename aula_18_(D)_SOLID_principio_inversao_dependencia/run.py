"""
Principio da Inversão de Dependencia é fazer com o que o nível mais alto e o nível mais baixo não estejam conectados
diretos e sim estejam conectado por meio de uma interface para que seja mais fácil de ser modificado algum banco de dados
ou algo que esteja mais no nível baixo. Porque para moficar somente precisa ser criado uma nova classe implementada
da interface para se conectar ao sistema.

"""

from db.repository import IRepository
from db.mongo_repository import MongoRepository
from db.mysql_repository import MYSQLRepository


class Usuario(object):

    def __init__(self, repository: IRepository) -> None:
        self.__repository = repository

    def armazenar_dado(self, dado) -> None:
        self.__repository.inserir(dado)

    def deletar_dado(self, dado) -> None:
        self.__repository.deletar(dado)


usuario_mongo = Usuario(MongoRepository())
usuario_mysql = Usuario(MYSQLRepository())

usuario_mysql.armazenar_dado(2)
usuario_mongo.armazenar_dado(4)

usuario_mongo.deletar_dado(5)
usuario_mysql.deletar_dado(7)
