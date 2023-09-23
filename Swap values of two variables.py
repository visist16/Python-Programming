# Input two values from the user
a = input("Enter the value of variable 'a': ")
b = input("Enter the value of variable 'b': ")

# Print the original values
print("Original values:")
print("a =", a)
print("b =", b)

# Swap the values using a temporary variable
temp = a
a = b
b = temp

# Print the swapped values
print("\nSwapped values:")
print("a =", a)
print("b =", b)
