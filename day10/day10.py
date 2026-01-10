import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
opeartions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What's the first number: "))
    while should_continue:
        for symbol in opeartions:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the second number: "))
        answer = opeartions[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()