from database import PostgresDB
from database import MySQL
from repository import Repositorio


db_connection_postgres = PostgresDB()
db_connection_mysql = MySQL()
repository = Repositorio()

repository.select(db_connection_postgres)
repository.insert(db_connection_mysql)
