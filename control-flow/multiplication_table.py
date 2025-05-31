#Prompting the user to input number
number = int(input("Enter a number between 1-10 for which you want to see the multiplication table: "))
# Generating and printing the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
