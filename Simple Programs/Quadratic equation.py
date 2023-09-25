import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Initialize variables for real and imaginary parts
    real_part = None
    imaginary_part = None
    
    # Check for real solutions
    if discriminant > 0:
        # Two real solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots are real and different: {root1} and {root2}")
    elif discriminant == 0:
        # One real solution (repeated root)
        root1 = -b / (2*a)
        print(f"Roots are real and equal: {root1}")
    else:
        # Complex Roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)

    # Check if complex roots were calculated
    if real_part is not None and imaginary_part is not None:
        # Round the real and imaginary parts
        rounded_real_part = round(real_part, 4)
        rounded_imaginary_part = round(imaginary_part, 4)
        
        # Print complex roots
        print(f"Roots are complex: {rounded_real_part} + {rounded_imaginary_part}i and {rounded_real_part} - {rounded_imaginary_part}i")

# Call the quadratic_solver function
quadratic_solver(a, b, c)


# Test Cases

# Basic Test Cases
print(quadratic_solver(1, -3, 2))  # Expected Output: "Roots are real and different: 2.0 and 1.0"
print(quadratic_solver(1, 0, -1))  # Expected Output: "Roots are real and different: 1.0 and -1.0"
print(quadratic_solver(1, 0, 0))   # Expected Output: "Roots are real and equal: 0.0"

# Common Complex Roots
print(quadratic_solver(1, 1, 1))   # Expected Output: "Roots are complex: -0.5 + 0.866i and -0.5 - 0.866i"
print(quadratic_solver(2, 4, 5))   # Expected Output: "Roots are complex: -1.0 + 1.0i and -1.0 - 1.0i"

# Zero Discriminant (Repeated Root)
print(quadratic_solver(4, -4, 1))  # Expected Output: "Roots are real and equal: 0.5"
