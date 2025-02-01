from options import Options

def getInt(msg: str) -> int:
    value = input(msg)
    while not value.isnumeric():
        value = input('Please enter a valid number: ')
    return int(value)

def choiceIs(choice: int, option: str) -> bool:
    return choice == Options[option].value
