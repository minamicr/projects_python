

def add(first_number: int, second_number: int) -> int:
    return first_number + second_number

def subtract(first_number: int, second_number: int) -> int:
    return first_number - second_number

def multiply(first_number: int, second_number: int) -> int:
    return first_number * second_number

def divide(first_number: int, second_number: int) -> int:
    return first_number / second_number

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def make_operations():
    first_number = int(input("What's the first number ? "))
    for operation in operations:
        print(operation)

    answer = ''

    while answer == 'y' or answer == '':
        operation = input("Pick an operation: ")

        second_number = int(input("What's the next number ? "))

        calculation = operations[operation]
        result = calculation(first_number, second_number)

        print(f"{first_number} operation {second_number} = {result}")

        first_number = result

        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")

if __name__ == '__main__':
    make_operations()
