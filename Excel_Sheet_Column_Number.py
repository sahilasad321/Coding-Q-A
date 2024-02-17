# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# John, a data analyst, was tasked with analyzing sales data and representing it in an Excel sheet. He decided to use alphabets as column titles. While assigning column numbers, he got stuck after column 26 and named it "Z". He then named the 27th column "AB" as the combination of alphabets.

# Can you help John write a function to return the corresponding column number when a columnTitle is given?


def titleToNumber(s):
    # Initialize the result
    result = 0
    
    # Create a dictionary to map alphabets to numbers
    alphabet_map = {chr(i + 65): i + 1 for i in range(26)}
    
    # Calculate the length of the string
    n = len(s)
    
    # Iterate over each character and update the result
    for i in range(n):
        result += alphabet_map[s[i]] * (26 ** (n - i - 1))
    
    # Return the final result
    return result

# Prompt for user input
st = input()

# Call the function and display the result
print(titleToNumber(st))