# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 5
# 11-08-2023

def filter_by_profession(people,profession):
    return [person for person in people if person['profession'] == profession]

#example
people = [
    {'name': 'Alice', 'age': 30, 'profession':'Engineer'},
    {'name': 'Erik', 'age': 22, 'profession':'Teacher'},
    {'name': 'Angel', 'age': 40, 'profession':'Engineer'}
    
     ]
print(filter_by_profession(people, 'Engineer'))
# Result[{'name': 'Alice', 'age': 30, 'profession': 'Engineer'}, 
# {'name': 'Angel', 'age': 40, 'profession': 'Engineer'}]

# Using list cromprehension we iterate over each dictiinary (person) in the list people
# For each dictionary it checks wether the value key 'profession' matches the profession argument
# if it passed then the dictionary is added to the list 

# Main Lesson
# Understanding how list comrehension is usded to filter data. It is a powerful feature of Python 
# that allows for the user to create new lists by applying an expression to each element in a sequence 
# and optionally filtering items with a condition 