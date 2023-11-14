# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 9
# 11-09-2023

#___________________________________________________________________________________________
# Unique Elements: Write a function that returns the unique elements in a list.
#___________________________________________________________________________________________

def unique_elements(lst):
    return list(set(lst))

#example
my_list = {2,5,3,5,2,2,5,6,7,3,5}
print(unique_elements(my_list))

# Main Lesson
# .set() converts the list into a data structure called 'set'. Sets in Pythin are collections
# of unique elements , so any duplicates are removed. 
# list() converts the set into a list 