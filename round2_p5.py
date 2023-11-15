


# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 5
# 11-14-2023

#___________________________________________________________________________________________
# Custom Sorter: Write a function that sorts a list of tuples based on the second value in each 
# tuple.
#___________________________________________________________________________________________

def sort_by_second(tuples_list):
    
    # The 'sorted()' function returns a new sorted list from the items in 'tuples_list'.
    # The 'key' parameter specifies a custom function to be used for sorting (in this case, a lambda function).
    # 'lambda tuple: tuple[1]' is an anonymous function that takes a tuple and returns its second element.
    # This tells 'sorted()' to sort the tuples based on the second element.
    sorted_list = sorted(tuples_list, key=lambda tuple: tuple[1])
    
    # Return the newly sorted list.
    return sorted_list

# Example usage:
# To sort a list of tuples named 'my_tuples' by the second value of each tuple:
# sorted_tuples = sort_by_second(my_tuples)
# print(sorted_tuples)
