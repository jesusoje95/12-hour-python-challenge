# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 7
# 11-09-2023

#___________________________________________________________________________________________
# Data Filter: Write a function that takes a list of dictionaries (representing people, 
# with keys for name, age, and profession) and a profession string, and returns a new 
# list with dictionaries where the profession matches the given string.
#___________________________________________________________________________________________

def find_primes(n):
    #Initialize empty list 
    primes = []

    # Iterate through the values, we start at 2 and go all the way to the last number
    # hence why we use n+1 so that we can access the last number
    for i in range(2, n+1):
        #Assume it is prime
        is_prime = True
        
        # Loop through all numbers between 2 and the numbers sqrt. 
        for j in range(2, int(i**0.5)+1):
          #If i canbe divided by j wihout residue it is not a prime number
           if i % j == 0: 
                is_prime = False
                break
    
        # If it is not divisible without residue it is prime and we append it
        if is_prime:
            primes.append(i)
    return primes

#example
print(find_primes(80))

# Why so we loop up to the number's sqrt? This is due to 
# the nature of prime numbers. If i has a factor largee than its sqrt, the corresponding factor
# that multiplies with it has already been calculated   
# ie i = 36 -> (1,36), (2,18), (4,9), (6,6)
# for a number larger than the srt, in this case 6. We alreasy have the numbers (36,1), (18,2)...


# Main Lesson
# Understand nested loops and the concept of primer numbers
