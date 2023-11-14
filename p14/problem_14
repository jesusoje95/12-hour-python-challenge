# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 14
# 11-09-2023

#___________________________________________________________________________________________
# Multiplication Table Printer: Develop a function that prints out a multiplication table 
# for numbers up to a given number.
#___________________________________________________________________________________________

import string

def word_occurrence(sentence, word):
    # Clean upthe string so that we are only left with words
     clean_str = sentence
     clean_str = ''.join(char_ for char_ in clean_str if char_ not in string.punctuation)
    #Split the string into words
     return clean_str.lower().split().count(word.lower())

print(word_occurrence('The name of the planet we live is earth. Earth is a planet','earth'))

# Main Lesson
# String manipulation

# clean_str.lower() converts the entire cleaned sentence to lowercase. This ensures that the word counting is case-insensitive. For example, "Word" and "word" will be considered the same word.
# .split() splits the lowercase sentence into a list of words. By default, split() uses any whitespace (like spaces, tabs, or newlines) to separate the string into words.
# word.lower() ensures that the word we are looking for is also in lowercase to match the case-insensitivity of the sentence.
# .count(word.lower()) counts how many times the lowercase word appears in the list of lowercase words we obtained from clean_str.
