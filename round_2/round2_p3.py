# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 3
# 11-14-2023

#___________________________________________________________________________________________
# Recursive Factorial: Write a recursive function that returns the factorial of a given number.
#___________________________________________________________________________________________

# Define a function named 'recursive_factorial' that takes a single argument, 'n'.
# This function will calculate the factorial of 'n' using recursion.
def recursive_factorial(n):
    # The base case: if 'n' is 0, the factorial is 1 by definition.
    # This condition also prevents the function from calling itself indefinitely.
    if n == 0:
        return 1
    
    # The recursive case: if 'n' is greater than 0, the function calls itself.
    # It multiplies 'n' by the factorial of 'n-1'.
    # This step breaks down the problem into smaller, similar problems.
    else:
        return n * recursive_factorial(n - 1)

# Example usage:
# Find the factorial of 5:
print(recursive_factorial(5))
