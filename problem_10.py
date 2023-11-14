# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 10
# 11-09-2023

#___________________________________________________________________________________________
# String Reverser: Create a function that takes a string and returns the string in reversed 
# order without using the [::-1] syntax.
#___________________________________________________________________________________________

def reverse_string(s):
    # Create empty string 
    reversed_str = ''

    for char_ in s:
        # Add characters before the last one 
        reversed_str = char_ + reversed_str
    return reversed_str

# Example
my_str = 'Hello World'
print(reverse_string(my_str))

# Main Lesson
# String Concatenation: Strings can be joined using the '+' sign