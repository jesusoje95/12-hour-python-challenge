# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 4
# 11-14-2023

#___________________________________________________________________________________________
# Nested Dictionary Updater: Develop a function that takes a nested dictionary and updates a 
# value given its key path as a list.
#___________________________________________________________________________________________


def update_nested_dict(d, key_path, value):
    # Start with the first key in the key path.
    key = key_path[0]

    # Base case for recursion:
    # If the key path has only one key left, update the value.
    if len(key_path) == 1:
        if key in d:
            d[key] = value
            return True
        else:
            return False

    # Recursive case:
    # If the current key is found in the dictionary,
    # proceed to the next level of the nested dictionary.
    if key in d and isinstance(d[key], dict):
        # The 'key_path[1:]' is the remaining key path beyond the current key.
        # We call 'update_nested_dict' with the next level of the dictionary and the remaining key path.
        return update_nested_dict(d[key], key_path[1:], value)
    else:
        # If the current key is not found, or it's not a dictionary, we cannot proceed.
        return False

# Example usage:
# To update the value '42' in a nested dictionary 'd' at the key path ['key1', 'key2', 'key3']:
# update_nested_dict(d, ['key1', 'key2', 'key3'], 42)
