# Leap year checking
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "The given year is a leap year."
    else:
        return "The given year is not a leap year."

# Test cases

# Basic Test Cases
print(is_leap_year(2024))  # Expected Output: "The given year is a leap year."
print(is_leap_year(2022))  # Expected Output: "The given year is not a leap year."

# Common Leap Years and Non-Leap Years
print(is_leap_year(2000))  # Expected Output: "The given year is a leap year."
print(is_leap_year(1900))  # Expected Output: "The given year is not a leap year."
print(is_leap_year(2028))  # Expected Output: "The given year is a leap year."
print(is_leap_year(2100))  # Expected Output: "The given year is not a leap year."
