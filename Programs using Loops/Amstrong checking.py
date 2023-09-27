# Input an integer
number = int(input("Enter an integer: "))

# Convert the integer to a string to count its digits
number_str = str(number)

# Calculate the number of digits
num_digits = len(number_str)

# Initialize a variable to store the sum of digits raised to the power of num_digits
armstrong_sum = 0

# Calculate the sum of digits raised to the power of num_digits
temp = number
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

# Check if the original number is equal to the sum
if number == armstrong_sum:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
