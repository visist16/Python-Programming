#reverse number
number = int(input("Enter an integer: "))
number_str =  str(number)

reversed_str = number_str[::-1]

reversed_number = int(reversed_str)
print(f"The reversed number is: {reversed_number}")
