#temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature value (e.g., 37.5): "))
        unit = input("Enter the unit ('C' for Celsius, 'F' for Fahrenheit): ").strip().upper()

        if unit == 'C':
            print(f"{temp}°C is {convert_to_fahrenheit(temp):.2f}°F")
        elif unit == 'F':
            print(f"{temp}°F is {convert_to_celsius(temp):.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

