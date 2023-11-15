# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 14
# 11-14-2023

#___________________________________________________________________________________________
# Longest Consecutive Sequence: Create a function that finds the length of the longest 
# consecutive elements sequence in an unsorted list.
#___________________________________________________________________________________________

def longest_consecutive(nums):
   # Create a set from the list to enable O(1) look-ups.
    num_set = set(nums)
    
    # This will store the length of the longest consecutive sequence found.
    longest_streak = 0
    
    # Loop through each number in the set.
    for num in num_set:
        # Check if 'num' is the start of a sequence.
        # It is the start of a sequence if 'num - 1' is not in the set.
        if num - 1 not in num_set:
            # Initialize the current number and the current streak length.
            current_num = num
            current_streak = 1
            
            # Increment 'current_num' and check whether the incremented number is in the set.
            # Continue until it's no longer consecutive.
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # Update the longest streak found if the current streak is longer.
            longest_streak = max(longest_streak, current_streak)
    
    # Return the length of the longest consecutive sequence.
    return longest_streak

# Example usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Expected output is 4 (because 1, 2, 3, 4 is the longest consecutive sequence)
