# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 11
# 11-14-2023

#___________________________________________________________________________________________
# Max Heap Checker: Write a function that checks if a given list of numbers represents a 
# valid max heap.
#___________________________________________________________________________________________

def is_max_heap(heap):
    # Calculate the size of the list.
    heap_size = len(heap)
    
    # Loop over each element in the list. Since a heap is a complete binary tree, we only need to
    # check elements until the last parent, which is at index (heap_size // 2 - 1).
    for i in range(heap_size // 2):
        # Calculate the indices of the left and right children.
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if the left child exists and if the current element is less than the left child.
        # If so, it's not a max heap, so return False.
        if left < heap_size and heap[i] < heap[left]:
            return False
        
        # Check if the right child exists and if the current element is less than the right child.
        # If so, it's not a max heap, so return False.
        if right < heap_size and heap[i] < heap[right]:
            return False
    
    # If all elements satisfy the max heap property, return True.
    return True

# Example usage:
# To check if the list [10, 9, 8, 7, 6, 5, 4] represents a max heap:
# print(is_max_heap([10, 9, 8, 7, 6, 5, 4]))  # This would return True
