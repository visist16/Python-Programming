#Sum of natural numbers
N = int(input("Enter a positive integer N: "))

sum_of_N = 0

if N<=0:
    print("Please enter a positive integer.")
else:
    for i in range(1,N+1):
        sum_of_N +=i
    
    print(f"The sum of natural numbers from 1 to {N} is {sum_of_N}.")    
