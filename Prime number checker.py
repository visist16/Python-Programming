# Function to check if a number is prime
def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

# Input from the user
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
