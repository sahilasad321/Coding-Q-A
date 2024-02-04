# Count Duplicates

# Write a Python program to count the repeated word given by user in that string.

input_string = input("Enter the string : ")
input_word = input("Enter the word : ")

lower_case_input_string = input_string.lower()
lower_case_input_word = input_word.lower()

count_repeated_word = lower_case_input_string.count(lower_case_input_word)

print(f"The word {input_word} appears {count_repeated_word} times in '{input_string}' ")



