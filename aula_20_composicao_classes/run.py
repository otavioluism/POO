"""
Composição de classes é utilizado para não ficar usando herança, um exemplo é criar um selecionador e inserçor de dado
onde o repositorio é composto pelos dois

"""

from repositorio import Repositorio

repository = Repositorio()
repository.insert_one()
repository.select_by_id()