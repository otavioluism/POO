from db.repository import IRepository


class MongoRepository(IRepository):

    def inserir(self, dado):
        print('Inserindo dado no mongodb!')

    def deletar(self, dado):
        print('Deletando dado no mongodb!')
