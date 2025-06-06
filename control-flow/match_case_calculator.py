# Prompting for user input
num1 = float(input ("Enter the first number: "))
num2 = float(input("Enter the second number: "))
Operator = input("Choose the operation (+, -, *, /):")

# Performing the calculation using match case
match Operator:
    case '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    case '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    case '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, or /.")
        

