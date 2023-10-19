def find_smallest_number(arr):
    if not arr:
        return None  # Handle the case of an empty array

    smallest = arr[0]  # Initialize the smallest number with the first element
    for number in arr:
        if number < smallest:
            smallest = number  # Update the smallest number if a smaller one is found

    return smallest

# Example usage:
numbers = [34, 56, 12, 78, 90, 45]
smallest_number = find_smallest_number(numbers)
print("The smallest number is:", smallest_number)

