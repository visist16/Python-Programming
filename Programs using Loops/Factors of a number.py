#factors of a number
num = int(input("Enter a positive integer: "))

factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
        
print(f"The factors of {num} are:", factors)        
