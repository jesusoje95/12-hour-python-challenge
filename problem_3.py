# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 3
# 11-08-2023


def calculator(num1, num2, operation):
    
    #add
    if operation == 'add':
        return num1 + num2
    #subtract
    elif operation =='subtract':
        return num1 - num2
    #multiply
    elif operation == 'multiply':
        return num1 * num2 
   #divide
    elif operation == 'divide':
        #check to see if user is trying to divide bt 0
        if num2 != 0:
            return num1 / num2   
        else: 
            return 'Error, you cannot divide by zero'    
    #if none of the 4 operators is used output an error message
    else: 
        return ' Error, operator not recognized'


#testing 
print(calculator(5.234,5,'divide'))
print(calculator(5.989898777,5,'add')) 