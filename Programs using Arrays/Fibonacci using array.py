def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)

    return fibonacci

# Example usage:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)

