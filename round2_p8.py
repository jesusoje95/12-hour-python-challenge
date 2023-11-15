# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 8
# 11-14-2023

#___________________________________________________________________________________________
# Two-Sum Problem: Develop a function that takes a list of numbers and a target sum, returning 
# the indices of the two numbers that add up to the target sum.
#___________________________________________________________________________________________

def find_two_sum(nums, target):

    # Initialize a dictionary to store the number and its index.
    num_indices = {}
    
    # Loop over the list of numbers, with 'i' being the index and 'num' being the number.
    for i, num in enumerate(nums):
        # Calculate the complement number that would add up to the target sum.
        complement = target - num
        
        # Check if the complement number is already in the dictionary.
        if complement in num_indices:
            # If it is, return a list with the current index 'i' and the index of the complement.
            return [num_indices[complement], i]
        
        # If the complement is not found, store the index of 'num' in the dictionary.
        num_indices[num] = i
    
    # If no pair is found that adds up to the target sum, return an empty list.
    return []

# Example usage:
# To find two numbers that add up to 9 in the list [2, 7, 11, 15]:
# print(find_two_sum([2, 7, 11, 15], 9))  # This would return [0, 1] because nums[0] + nums[1] == 9
