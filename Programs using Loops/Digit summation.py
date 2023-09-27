#sum of the digits
number = int(input("Enter an integer: "))
digit_sum = 0
while number > 0:
    digit = number%10
    digit_sum +=digit
    number //=10
print(f"The sum of the digits is: {digit_sum}")    
