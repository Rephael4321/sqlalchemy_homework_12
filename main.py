from options import Options
from functions import fetchData, insertData, exitFunc
from utils import getInt
from queries import count_students_query, average_ages_query, insert_student_query
from dotenv import dotenv_values
import sqlalchemy

env_vars = dotenv_values(".env.example")

USERNAME = env_vars.get("USERNAME")
PASSWORD = env_vars.get("PASSWORD")
DB_HOSTNAME = env_vars.get("DB_HOSTNAME")
DB_NAME = env_vars.get("DB_NAME")

DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"
engine = sqlalchemy.create_engine(DATABASE_URI)

def printMenu():
    print()
    print('What do you want to do?')
    for option in Options:
        print(f'{option.value}. {option.name.replace('_', ' ').capitalize()}')
    choice = Options(getInt('Enter your choice: '))

    if choice == Options.PRINT_STUDENTS_COUNT:
        fetchData(engine, count_students_query, 'Students count: ')
    elif choice == Options.PRINT_AVERAGE_AGES:
        fetchData(engine, average_ages_query, 'Students ages average: ')
    elif choice == Options.INSERT_NEW_STUDENT:
        insertData(engine, insert_student_query)
    elif choice == Options.EXIT:
        exitFunc()

while True:
    printMenu()
