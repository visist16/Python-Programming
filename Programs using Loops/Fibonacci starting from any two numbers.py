#Fibonacci starting from any two numbers

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Input the number of terms in the sequence
n = int(input("Enter the number of terms in the sequence: "))

# Initialize variables for the current and next numbers
current_number = first_number
next_number = second_number

fibonacci_sequence = [current_number, next_number]

# Check if the number of terms is greater than 2
if n <= 2:
    print("The Fibonacci sequence is:", fibonacci_sequence[:n])
else:
    for _ in range(2, n):
        new_number = current_number + next_number
        fibonacci_sequence.append(new_number)
        current_number, next_number = next_number, new_number

    # Print the Fibonacci sequence
    print("The Fibonacci sequence is:", fibonacci_sequence)
