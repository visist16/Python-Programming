#LCM & GCD
import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = math.gcd(num1, num2)

lcm = (num1 * num2) // gcd #LCM = (num1*num2) / GCD

print(f"The GCD of {num1} and {num2} is {gcd}")
print(f"The LCM of {num1} and {num2} is {lcm}")
