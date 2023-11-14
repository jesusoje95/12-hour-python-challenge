# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 6
# 11-09-2023

#___________________________________________________________________________________________
# Temperature Converter: Create a function that converts a temperature from Fahrenheit to 
# Celsius and vice versa, based on a second argument indicating the direction of conversion 
# ('F_to_C' or 'C_to_F').
#___________________________________________________________________________________________


def convert_temperature(temp,direction):
    #F_to_C direction
    if direction == 'F_to_C':
        return (temp-32) * 5/9
    elif direction == 'C_to_F':
        return (temp * 9/5) + 32
    else:
        return 'Invalid Direction'


print(convert_temperature(73,'F_to_C'))



# Main Lesson
#Learning how to use conditionals in python 