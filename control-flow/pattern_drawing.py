
# Prompting user for a positive integer
size = int(input("Enter the size of the pattern e.g.,square: "))

if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize row counter
    row = 0

    # While loop for rows
    while row < size:
        # For loop for columns
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after each row
        row += 1
