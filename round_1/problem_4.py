# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 4
# 11-08-2023


def frequency_counter(numbers):
    #create empty dictionary 
    frequency = {}                                        
    # loop through numbers 
    for number in numbers: 
        # here we try and find if number is already in the dictionary, if it isn't 
        # then add it to the dictionary, if it is then add one to the key                                 
        frequency[number] = frequency.get(number, 0) +1    
  
    return frequency                                       


    # Main Lesson
    # .get() helps retrieve the current value of the key 'number'. If number does't exist in the dictionary
    # it returns 0. If the number is in the dictionary get its count, add one and store it back. If not there then 
    # treat that count as zero and add one