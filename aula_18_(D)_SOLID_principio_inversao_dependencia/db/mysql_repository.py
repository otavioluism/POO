from db.repository import IRepository


class MYSQLRepository(IRepository):

    def inserir(self, dado):
        print('Inserindo dado no MYSQL!')

    def deletar(self, dado):
        print('Deletando dado no MYSQL!')