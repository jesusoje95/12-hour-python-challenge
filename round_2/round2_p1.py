# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 1
# 11-13-2023

#___________________________________________________________________________________________
# CSV Column Averager: Write a function that reads a CSV file and calculates the average of 
# the numbers in a given column
#___________________________________________________________________________________________


# Import the csv module, which is Python's built-in library for handling CSV files.
import csv

# Define a function named 'csv_column_averager' that takes a file path and a column index as arguments.
def csv_column_averager(file_path, column_index):
    # Initialize a variable 'total' to keep the sum of all numbers in the column.
    total = 0
    # Initialize a variable 'count' to keep track of the number of values added to 'total'.
    count = 0
    
    # Open the file at the given 'file_path' in read mode.
    # The 'with' statement ensures the file is properly closed after finishing or in case of an error.
    # 'newline='' ' ensures that newlines are processed in a way that's compatible with the csv module.
    with open(file_path, newline='') as csvfile:
        # Create a csv.reader object that will iterate over lines in the given csvfile.
        reader = csv.reader(csvfile)
        # Use 'next()' to skip the first row, which often contains the column headers.
        next(reader)
        
        # Iterate over each row in the CSV file.
        for row in reader:
            # Check if the specified column index has a value in the current row.
            if row[column_index]:
                # Convert the value at the column index to a float and add it to 'total'.
                total += float(row[column_index])
                # Increment 'count' for each value added to 'total'.
                count += 1

    # After reading all rows, calculate the average if 'count' is not 0 to avoid division by zero.
    # If 'count' is 0, meaning the column was empty or had no valid numbers, return 0.
    return total / count if count > 0 else 0

