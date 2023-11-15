# Jesus Ojeda
# PragmatiCoders 12 week challenge
# Problem Set 2
# Problem 13
# 11-14-2023

#___________________________________________________________________________________________
# HTML Tag Validator: Write a function that validates a string of HTML, ensuring all tags 
# are properly opened and closed in the correct order.
#___________________________________________________________________________________________

def is_valid_html(html):
    # A stack to keep track of opening tags.
    stack = []
    
    # The index variable will be used to loop through the string.
    i = 0
    
    # Loop over the HTML string.
    while i < len(html):
        # If we find an opening angle bracket, it might be the start of a tag.
        if html[i] == '<':
            # Find the closing angle bracket of the tag.
            closing_bracket = html.find('>', i + 1)
            
            # If there is no closing bracket, the HTML is invalid.
            if closing_bracket == -1:
                return False
            
            # Extract the tag name between the angle brackets.
            tag = html[i + 1:closing_bracket]
            
            # If it's an opening tag (doesn't start with a slash), push it onto the stack.
            if not tag.startswith('/'):
                stack.append(tag)
            else:
                # If it's a closing tag, it should close the most recent open tag.
                # Remove the slash to get the tag name.
                tag = tag[1:]
                
                # If the stack is empty or the tag on top of the stack doesn't match,
                # the HTML is invalid.
                if not stack or stack.pop() != tag:
                    return False
            
            # Move the index to the character after the closing bracket.
            i = closing_bracket
        # Move to the next character.
        i += 1
    
    # If the stack is empty, all tags were properly closed. Otherwise, the HTML is invalid.
    return not stack

# Example usage:
print(is_valid_html("<html><body></body></html>"))  # Expected True
print(is_valid_html("<html><body></html>"))         # Expected False
