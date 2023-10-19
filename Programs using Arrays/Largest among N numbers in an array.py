def find_largest_number(arr):
    if not arr:
        return None  # Handle the case of an empty array

    largest = arr[0]  # Initialize the largest number with the first element
    for number in arr:
        if number > largest:
            largest = number  # Update the largest number if a larger one is found

    return largest

# Example usage:
numbers = [34, 56, 12, 78, 90, 45]
largest_number = find_largest_number(numbers)
print("The largest number is:", largest_number)

