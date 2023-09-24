# Function to print the multiplication table for a given number up to a specified limit
def print_multiplication_table(number, limit):
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Input from the user
try:
    number = int(input("Enter a number: "))  # Use int to ensure an integer input
    limit = int(input("Enter the limit: "))   # Use int to ensure an integer input
    print_multiplication_table(number, limit)
except ValueError:
    print("Invalid input. Please enter valid integers.")
