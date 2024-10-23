# Write a python program that reads a string which contains English alphabets and numbers. The program should create two lists L1 and L2, where L1 includes all the numbers present in the string while L2 includes all the alphabets of the string.

def separate_alphabets_and_numbers(input_string):
    L1 = []  # List to store numbers
    L2 = []  # List to store alphabets

    for char in input_string:
        if char.isdigit():  # Check if the character is a digit
            L1.append(int(char))  # Convert digit to integer and add to L1
        elif char.isalpha():  # Check if the character is an alphabet
            L2.append(char)  # Add alphabet to L2

    return L1, L2

# Input from the user
input_string = input("Enter a string containing alphabets and numbers: ")

# Separate into lists
L1, L2 = separate_alphabets_and_numbers(input_string)

# Output the lists
print("List of numbers (L1):", L1)
print("List of alphabets (L2):", L2)
