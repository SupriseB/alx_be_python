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
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."



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
 

"""
Command-Line Division Tool
--------------------------

This script safely divides two numbers provided as command-line arguments.

Usage:
  python main.py <numerator> <denominator>

Examples:
  Normal Division:
    python main.py 10 5
    Expected Output: The result of the division is 2.0

  Division by Zero:
    python main.py 10 0
    Expected Output: Error: Cannot divide by zero.

  Invalid Input (Non-numeric):
    python main.py ten 5
    Expected Output: Error: Please enter numeric values only.
"""


