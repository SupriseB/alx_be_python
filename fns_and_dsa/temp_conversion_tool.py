#temp_conversion_tool.py

# Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

# Implement conversion functions
def convert_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius_temp):
    return (celsius_temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
def main():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Enter unit (C or F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid unit")
    except ValueError as ve:
        print(f"Error: {ve}")

# Run only if this file is executed directly
if __name__ == "__main__":
    main()
