import art
print(art.logo)

# Option 1

def calculator(first_num, next_num, operation):
    """a calculator funtion without using dictionary"""
    if operation=="+":
        return first_num + next_num
    elif operation=="-":
        return first_num - next_num
    elif operation=="*":
        return first_num * next_num
    else:
        return first_num / next_num

first_num = float(input("Type your first number: "))
loop = True
while loop:
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_num = float(input("Type your next number: "))
    result = calculator(first_num, next_num, operation)
    print(result)
    choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
    if choice=="n":
        loop = False
    else:
        first_num = result




# Option 2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    """a calculator function using dictionary to store operations"""
    loop = True
    first_num = float(input("Type your first number: "))

    while loop:
        for symbol in operations:
            print(symbol)
        operation_sym = input("Pick an operation: ")
        next_num = float(input("Type your next number: "))
        result = operations[operation_sym](first_num, next_num)
        print(result)
        choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
        if choice=="n":
            loop = False
            calculator()
        else:
            first_num = result
calculator()
