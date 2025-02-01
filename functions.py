import sqlalchemy
from db_connection import engine
from utils import getInt

def fetchData(query: str, title: str) -> None:
    print(title)
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(query))
        print(result.fetchone()[0])

def insertData(query: str) -> None:
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
