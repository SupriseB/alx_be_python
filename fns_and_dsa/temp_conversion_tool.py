#temp_conversion_tool.py

# Global conversion factors (as constants with exact names expected)
FAHRENHEIT_TO_CELSIUS = 0.5556  # 5/9
CELSIUS_TO_FAHRENHEIT = 1.8     # 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32

def main():
    try:
        temp = float(input("Enter the temperature value (e.g., 37.5): "))
        unit = input("Enter the unit ('C' for Celsius, 'F' for Fahrenheit): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp:.2f}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
