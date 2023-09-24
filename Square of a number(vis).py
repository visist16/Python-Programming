# Function to calculate the square of a number
def square(number):
    return number ** 2

# Input from the user
try:
    number = float(input("Enter a number: "))  # Use float to allow decimal input
    result = square(number)
    print(f"The square of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
