# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Write a python program to increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    # Calculate the length of the input list
    n = len(digits)

    # Iterate over the digits in reverse
    for i in range(n):
        idx = n - 1 - i
        # Check and modify the digit
        if digits[idx] != 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
    
    # Handle the case where all digits are nines
    return [1] + digits

# Prompt for user input
digits = eval(input())

# Display the result after adding one
print(plusOne(digits))
