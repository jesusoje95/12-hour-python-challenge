# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 6
# 11-14-2023

#___________________________________________________________________________________________
# Leap Year Verifier: Create a function that checks if a given year is a leap year.
# Hint: Use the rules that define leap years (divisible by 4, not by 100 unless also by 400).
#___________________________________________________________________________________________

def is_leap_year(year):
    # First, check if the year is divisible by 4 because all leap years must be.
    if year % 4 == 0:
        # If the year is divisible by 100, it is a leap year only if it's also divisible by 400.
        if year % 100 == 0:
            # Check divisibility by 400. If true, it is a leap year. If not, it's not a leap year.
            return year % 400 == 0
        else:
            # If the year is divisible by 4 but not by 100, it is a leap year.
            return True
    else:
        # If the year is not divisible by 4, it's not a leap year.
        return False

# Example usage:
# To check if the year 2000 is a leap year:
print(is_leap_year(2000))  # This would return True because 2000 is a leap year.
