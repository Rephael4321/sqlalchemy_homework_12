import sqlalchemy
from sqlalchemy.engine.base import Engine
from utils import getInt

def fetchData(engine: Engine, query: str, title: str) -> None:
    print(title)
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(query))
        print(result.fetchone()[0])

def insertData(engine: Engine, query: str) -> None:
    name = input("Insert student's name: ")
    age = getInt("Insert student's age: ")
    email = input("Insert student's email: ")

    with engine.connect() as connection:
        result = connection.execute(
            sqlalchemy.text(query),
            {'name': name, 'age': age, 'email': email}
            )
        connection.commit()
        print(result.fetchone()[0])

def exitFunc():
    exit(0)
