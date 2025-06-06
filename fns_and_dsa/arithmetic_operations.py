#arithmetic_operations.py
def perform_operation():
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))
    operation = input("Choose operation ('add', 'subtract', 'multiply', or 'divide'): ")

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."
