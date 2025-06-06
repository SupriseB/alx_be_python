#temp_conversion_tool.py

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")    

if __name__ == "__main__":
    main()
