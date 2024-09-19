'''
6. Write a program to accept a string and display:
    a. Number of uppercase characters
    b. Number of lowercase characters
    c. Total number of alphabets
    d. Number of digits
    
'''
def analyze_string(input_str):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    alphabet_count = 0
    
    for char in input_str:
        if char.isupper():
            uppercase_count += 1
            alphabet_count += 1
        elif char.islower():
            lowercase_count += 1
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
    
    print("Number of uppercase characters:", uppercase_count)
    print("Number of lowercase characters:", lowercase_count)
    print("Total number of alphabets:", alphabet_count)
    print("Number of digits:", digit_count)

# Example usage
user_string = input("Enter a string: ")
analyze_string(user_string)
