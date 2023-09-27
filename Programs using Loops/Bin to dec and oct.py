#Binary to decimal and octal numbers
binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)
octal_number = oct(decimal_number)
print(f"The decimal representation is: {decimal_number}")
print(f"The octal representation is: {octal_number}")
