# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 15
# 11-09-2023

#___________________________________________________________________________________________
# Fibonacci Sequence Generator: Write a function that returns the Fibonacci sequence up to a 
# given number of elements.
#___________________________________________________________________________________________

def fibonacci(n):
    # Starting with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # If the number of elements requested is 1, return [0]
    if n == 1:
        return [0]
    
    # If the number of elements requested is 0 or negative, return an empty list
    if n <= 0:
        return []
    
    # Generate the sequence up to 'n' elements
    # Start at 2 because we already have two numbers in the sequence
    for i in range(2, n):  
        # Calculate the next number in the sequence
        next_fib = fib_sequence[-1] + fib_sequence[-2]  
        # Append it to the sequence
        fib_sequence.append(next_fib)  
        
    return fib_sequence

print(fibonacci(8))