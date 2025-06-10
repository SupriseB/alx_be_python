# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        try:
            result = num / denom
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


# main.py

"""
Command-Line Division Tool

Usage:
  python main.py <numerator> <denominator>

Examples:
  Normal Division:
    python main.py 10 5
    Output: The result of the division is 2.0

  Division by Zero:
    python main.py 10 0
    Output: Error: Cannot divide by zero.

  Invalid Input (Non-numeric):
    python main.py ten 5
    Output: Error: Please enter numeric values only.
"""

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
#Examples
python main.py 10 5
# The result of the division is 2.0

python main.py 10 0
# Error: Cannot divide by zero.

python main.py ten 5
# Error: Please enter numeric values only.





