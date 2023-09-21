# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Input from the user
try:
    input_str = input("Enter a string or number to check for palindrome: ")
    
    if is_palindrome(input_str):
        print(f"'{input_str}' is a palindrome.")
    else:
        print(f"'{input_str}' is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid string or number.")
