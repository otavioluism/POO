# Métodos estáticos

"""

Os métodos estáticos são muito utilizados nas classes, mas devemos lembrar que quando criado eles não tem acesso
a nenhum atributo da classe ou método e até variável de classe;

"""


class Error(object):

    @staticmethod
    def error_500():
        print('Internal Server Error!')

    @staticmethod
    def error_404():
        print('Not found!')


Error.error_404()
Error.error_500()
