# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 12
# 11-14-2023

#___________________________________________________________________________________________
# Circular Prime Checker: Develop a function that checks if all rotations of a number's 
# digits are prime.
#___________________________________________________________________________________________

def is_circular_prime(n):
    # Check to filter out non-prime numbers and single-digit primes.
    if n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    if n < 10:
        return True

    # Convert the number to a string to facilitate rotation.
    s = str(n)
    
    # Generate and check all rotations for primality.
    # Rotate by moving the first digit to the end of the string.
    for i in range(len(s)):
        if not is_prime(int(s[i:] + s[:i])):
            return False
            
    return True

# The primality check is still needed; using a simpler version here for brevity.
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

# Example usage:
print(is_circular_prime(197))  # Expected True, 197 is a circular prime.
