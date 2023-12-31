# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 1
# Problem 1
# 11-07-2023

# Function to Summarize a Text File: Write a function that accepts a filename as a parameter, 
# reads the file, and returns the number of lines, words, and characters in the file.



def summarize_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

        lines = content.splitlines()
        word_count = sum(len(line.split()) for line in lines)
        char_count = len(content)

        return len(lines), word_count, char_count
    
lines, words, chars = summarize_text_file('testing_text')
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
