# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 11
# 11-09-2023

#___________________________________________________________________________________________
# Dictionary Merger: Write a function that merges two dictionaries. If there is a conflict 
# between dictionaries (same key), the value from the second dictionary should be kept.
#___________________________________________________________________________________________

def merge_dictionaries(dict1, dict2):
    # Create copy of dictionary 1
    merge_dict = dict1.copy()
    # Merge the two dictionaries
    merge_dict.update(dict2)

    return merge_dict


# Main Lesson 
# Copying: .copy() creates a shallowcopy of the dictionary
# Updating: .update() merges 2 dictionaries andhandles conflicts by keeping values
#           from second dictionary   