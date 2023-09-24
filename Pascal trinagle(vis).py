# Function to generate and print Pascal's Triangle
def print_pascals_triangle(num_rows):
    for i in range(num_rows):
        # Calculate the value of the current row
        current = 1
        for j in range(1, i + 2):
            print(current, end=" ")
            current = current * (i + 1 - j) // j
        print()

# Input from the user
try:
    num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
    if num_rows <= 0:
        print("Please enter a positive integer.")
    else:
        print_pascals_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
