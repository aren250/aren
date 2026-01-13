def is_leap_year(year):
    """
    Checks if a given year is a leap year according to the Gregorian calendar rules.
    """
    # Leap year conditions:
    # 1. Divisible by 4 (e.g., 2004, 2008)
    # 2. Unless it's a century year (divisible by 100), then it must also be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Prompt the user for input
user_input = input("Enter a year to check if it is a leap year: ")

try:
    # Convert the input string to an integer
    year_to_check = int(user_input)

    # Check if the year is a leap year using the function
    if is_leap_year(year_to_check):
        print(f"yes The year {year_to_check} IS a leap year.")
    else:
        print(f"no  The year {year_to_check} IS NOT a leap year.")

except ValueError:
    # Handle cases where the user does not enter a valid number
    print(" Invalid input. Please enter a valid numerical year.")
 