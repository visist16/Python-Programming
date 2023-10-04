# Function to generate and print Pascal's Triangle
# Print Pascal's Triangle in Python

# input n
n = 5

for i in range(1, n+1):
	for j in range(0, n-i+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for j in range(1, i+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		# using Binomial Coefficient
		C = C * (i - j) // j
	print()

#Other Method
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
