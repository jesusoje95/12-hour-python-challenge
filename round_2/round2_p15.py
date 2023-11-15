# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 15
# 11-14-2023

#___________________________________________________________________________________________
# Regular Expression Matcher: Write a function that uses regular expressions to check if 
# a given string matches a given pattern.
#___________________________________________________________________________________________

import re

def regex_matcher(pattern, string):
    
    # The re.fullmatch function checks if the whole string matches the pattern.
    # If a match is found, re.fullmatch returns a Match object. Otherwise, it returns None.
    # The 'bool()' function converts the result to True if a match is found, or False if not.
    return bool(re.fullmatch(pattern, string))

# Example usage:
# To check if the string 'abc123' matches the pattern 'abc\d+':
print(regex_matcher(r'abc\d+', 'abc123'))  # Expected output is True
