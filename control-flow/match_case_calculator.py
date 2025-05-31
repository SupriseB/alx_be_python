#match_case_calculator.py

num1 = float(input ("Enter_the_first_number: "))
num2 = float(input("Enter_the_second_number: "))
Operation = input("Choose the operation (+, -, *, /):")


match Operation:
    case '+':
        result = num1 + num2
        print(f"The result is [result]")
    case '-':
        result = num1 - num2
        print(f"The result is [result]")
    case '*':
        result = num1 * num2
        print(f"The result is [result]")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is [result]")
        else:
            print("Cannot divide by zero")
    
