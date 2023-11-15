# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 2
# 11-14-2023

#___________________________________________________________________________________________
# Anagram Checker: Create a function that checks whether two strings are anagrams of each other.
#___________________________________________________________________________________________

# Define a function named 'are_anagrams' that takes two strings as arguments.
def are_anagrams(str1, str2):
    # First, remove any spaces from the strings and convert all letters to lowercase.
    # This standardizes the strings so that 'Race car' and 'racecar' or 'Racecar' are considered anagrams.
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If the lengths of the processed strings are different,
    # they can't be anagrams, so return False immediately.
    if len(str1) != len(str2):
        return False
    
    # Initialize two dictionaries to keep track of the character counts for each string.
    # Dictionaries are chosen because they allow fast lookups and can be directly compared for equality.
    char_count1 = {}
    char_count2 = {}
    
    # Loop over each character in the first string.
    for char in str1:
        # If the character is already in the dictionary, increment its count.
        if char in char_count1:
            char_count1[char] += 1
        # If it's not in the dictionary, add it with a count of 1.
        else:
            char_count1[char] = 1
    
    # Repeat the same counting process for the second string.
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    # After counting all characters, compare the two dictionaries.
    # If they are the same, it means both strings have the exact same characters
    # with the exact same number of occurrences, thus are anagrams of each other.
    return char_count1 == char_count2
