# Prompting for user input
num1 = float(input ("Enter_the_first_number: "))
num2 = float(input("Enter_the_second_number: "))
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
            print("Error: Cannot divide by zero.")
    
