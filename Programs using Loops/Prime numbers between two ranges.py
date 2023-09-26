# Input the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Find and print prime numbers within the range
print(f"Prime numbers between {start_range} and {end_range} are:")

for num in range(start_range, end_range + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
