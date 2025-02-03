def getInt(msg: str) -> int:
    value = input(msg)
    while not value.isnumeric():
        value = input('Please enter a valid number: ')
    return int(value)
