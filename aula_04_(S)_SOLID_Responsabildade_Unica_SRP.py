# Conceito SOLID (S) - Princípio de Designer Clear Code
"""
S - Single Responsability Principle (SRP) - Responsabilidade Única

Este conceito tem como objetivo fazer com que todos os métodos tenha epenas uma responsabilidade, para que caso haja
algum problema, ou adição de regra, seja mexido apenas em um método específico. Isto também transparecerá
um código mais limpo para acelerar o desenvolvimento;

Lembrando que o conceito não esta atrelado somente para a mesma classe, pode ser criado outras classes por exemplo
de validar dados, e ser acessado pelo contexto do sistema cadastral em exemplo. Com isto, conseguimos também ir
colocando responsabilidade para cada classe;

"""


# Código sem o conceito de responsabilidade única
class SistemaCadastral(object):

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados...')
            print('Cadastrar o usuário {}, idade {}'.format(nome, idade))
        else:
            print('dados inválidos!')


# Código utilizando o conceito de responsabilidade única

class SistemaCadastralResponsabilidade(object):

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __validar_dados(self, nome: str, idade: int) -> bool:
        return True if isinstance(nome, str) and isinstance(idade, int) else False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o usuário {}, idade {}'.format(nome, idade))

    def __indicar_erro(self):
        print('dados inválidos!')
