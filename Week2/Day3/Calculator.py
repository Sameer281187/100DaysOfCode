def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = float(input("What is the first number?: "))
continue_execution = True

while continue_execution:
    for symbol in operation:
        print(symbol)
    operator = input("Pick an operation: ")
    num2 = float(input("what is the next number: "))
    result = operation[operator](num1, num2)

    print(f"{num1} {operator} {num2} = {result}")
    calculate_more = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    continue_execution = True if calculate_more == 'y' else False
    num1 = result