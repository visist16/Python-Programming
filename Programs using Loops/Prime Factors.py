#Prime Factors
def prime_factors(num):
    factors = []
    divisor = 2
    
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //=divisor
        divisor += 1
        
    return factors
    
num = int(input("Enter a positive integer: "))    

factors = prime_factors(num)
print(f"The prime factors of {num} are:", factors)
