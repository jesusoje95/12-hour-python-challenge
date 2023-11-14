# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 8
# 11-09-2023

#___________________________________________________________________________________________
# List Flattener: Develop a function that takes a list of lists and flattens it to a single 
# list without using any built-in Python flattening function
#___________________________________________________________________________________________

def flatten_list(nested_list):
    # Initialize empty list 
    flat_list= []

    # Loop through elements in nested_list
    for element in nested_list:
        # Check to see if the element in question is itself a list
        if isinstance(element,list):
            # If the element is a list we use recursion to flatten it out
            flat_list.extend(flatten_list(element))
        else:
            # If the element is not a list we simply append it to the flat_list list
            flat_list.append(element)
    return flat_list


#Example
nested = [1,[2,[3,4]],5,6,[7],[8,9]]
print(flatten_list(nested))


# Main Lesson
# Recursion: It allows for a fucntion to call itself to handle "sub-problems" of the
# same nature as the original