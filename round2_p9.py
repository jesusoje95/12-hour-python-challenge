# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 9
# 11-14-2023

#___________________________________________________________________________________________
# Matrix Transposer: Write a function that transposes a matrix represented as a list of 
# lists.
#___________________________________________________________________________________________

def transpose_matrix(matrix):
 
    # Use a nested list comprehension to generate the transposed matrix.
    # The outer list comprehension iterates over each index in the length of the first row (number of columns).
    # The inner list comprehension iterates over each row of the matrix to collect the ith element from each row.
    # The result is a new list of lists where the inner lists represent the columns of the original matrix (now rows).
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    # Return the transposed matrix.
    return transposed

# Example usage:
# To transpose a matrix 'm' which is a list of lists:
# transposed_m = transpose_matrix(m)
# print(transposed_m)
