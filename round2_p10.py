# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 10
# 11-14-2023

#___________________________________________________________________________________________
# Custom String Formatter: Create a function that takes a string and capitalizes every other 
# letter in the string.
#___________________________________________________________________________________________

def capitalize_every_other(input_string):
 
    # Initialize an empty list to hold the new characters.
    new_chars = []
    
    # Loop over the string with both the index and character.
    for i, char in enumerate(input_string):
        # If the index is even, capitalize the character.
        # If the index is odd, keep the character as it is (lowercase).
        # Use the modulo operator to determine if the index is even (i % 2 == 0).
        # Append the appropriately cased character to the new_chars list.
        new_chars.append(char.upper() if i % 2 == 0 else char.lower())
    
    # Join all the characters in the list into a new string.
    # The ''.join() method concatenates the elements of the list into a single string.
    new_string = ''.join(new_chars)
    
    # Return the newly formatted string.
    return new_string

# Example usage:
# To capitalize every other letter of the string 'hello world':
# formatted_string = capitalize_every_other('hello world')
# print(formatted_string)  # This would return 'HeLlO WoRlD'
