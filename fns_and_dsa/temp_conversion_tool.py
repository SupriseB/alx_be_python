#temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

# Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32

# Implement user interaction
def main():
    try:
        temperature = float(input("Enter temperature: "))
        unit = input("Enter unit (C or F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid temperature unit")
    except ValueError as e:
        print(f"Error: {e}")

# Execute only if run as a script
if __name__ == "__main__":
    main()
