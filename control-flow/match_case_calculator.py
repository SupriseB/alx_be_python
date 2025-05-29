# Prompting for user input
num1 = float(input ("Enter_the_first_number: ")) #first input number
num2 = float(input("Enter_the_second_number: ")) #second input number
Operation = input("Choose the operation (+, -, *, /):")

# Performing the calculation using match case
match Operation:
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
