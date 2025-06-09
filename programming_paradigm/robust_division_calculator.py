#Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
#Task Description:
#Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.
#robust_division_calculator.py:
#Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:
#Division by Zero: Use a try-except block to catch ZeroDivisionError.
#Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
#Return appropriate messages for errors or the result for successful division.

 safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        try:
            result = num / denom
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input provided."



import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()