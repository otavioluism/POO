from sql_actions.select import Select
from sql_actions.insert import Insert


class Repositorio(object):

    def __init__(self):
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_one()

    def insert_one(self):
        self.__insert.insert_one()
