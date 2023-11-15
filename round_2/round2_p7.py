# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 7
# 11-14-2023

#___________________________________________________________________________________________
# Palindromic Substrings: Write a function that finds and returns all the palindromic substrings 
# of a given string.
#___________________________________________________________________________________________

def find_palindromic_substrings(input_string):

    # Define a nested function that checks if a given substring is a palindrome.
    def is_palindrome(s):
        return s == s[::-1]  # A string is a palindrome if it is equal to its reverse.

    # Initialize an empty list to hold all palindromic substrings.
    palindromes = []
    
    # Get the length of the input string.
    n = len(input_string)
    
    # Generate all possible substrings using a sliding window.
    # The outer loop sets the starting point of the substring.
    for i in range(n):
        # The inner loop sets the endpoint of the substring.
        for j in range(i+1, n+1):
            # Extract the substring from index 'i' to index 'j'.
            substring = input_string[i:j]
            # Check if the substring is a palindrome.
            if is_palindrome(substring):
                # If it is, append it to the list of palindromes.
                palindromes.append(substring)
    
    # Return the list of palindromic substrings.
    return palindromes

# Example usage:
# To find all palindromic substrings of the string 'abba':
# print(find_palindromic_substrings('abba'))  # This would return ['a', 'b', 'bb', 'abba', 'b', 'a']
