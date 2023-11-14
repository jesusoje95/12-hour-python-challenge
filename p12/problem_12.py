# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 12
# 11-09-2023

#___________________________________________________________________________________________
# Multiplication Table Printer: Develop a function that prints out a multiplication table 
# for numbers up to a given number.
#___________________________________________________________________________________________

def print_multiplication_table(n):
    # Outer loop to create the rows
    for i in range(1,n+1):
        # Inner loop to create columns
        for j in range(1,n+1):
            #Print formated poduct 
            print(f"{i * j:4}",end='')
        # Print new line
        print()

#Example

print_multiplication_table(5)
