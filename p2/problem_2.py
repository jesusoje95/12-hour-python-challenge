# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 2
# 11-07-2023


import string

def is_palindrome(s):
    
    #Step 1 Clean up from spaces and convert all letters to lowercase
    clean_str = s.replace(' ','').lower()

    #Step 2 Remove all characters that are not letters
    #'' is an empty string
    #.join appends to the empty string
    cleant_str = ''.join(char_ for char_ in clean_str if char_ not in string.punctuation)

    #Step 3 Check if the cleaned string is the same forwards as backwards
    #Return a boolean to check if the string is a palindrome 
    return clean_str == clean_str[::-1]
#testing 
print(is_palindrome("Anita lava la tina"))
