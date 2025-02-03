from options import Options
from functions import fetchData, insertData, exitFunc
from utils import getInt
from queries import count_students_query, average_ages_query, insert_student_query

def printMenu():
    print()
    print('What do you want to do?')
    for option in Options:
        print(f'{option.value}. {option.name.replace('_', ' ').capitalize()}')
    choice = Options(getInt('Enter your choice: '))

    if choice == Options.PRINT_STUDENTS_COUNT:
        fetchData(count_students_query, 'Students count: ')
    elif choice == Options.PRINT_AVERAGE_AGES:
        fetchData(average_ages_query, 'Students ages average: ')
    elif choice == Options.INSERT_NEW_STUDENT:
        insertData(insert_student_query)
    elif choice == Options.EXIT:
        exitFunc()

while True:
    printMenu()
