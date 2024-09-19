'''
3. Write a program to generate a random password that meets the following conditions:
a. Password length must be 10 characters long.
b. It must contain at least 2 uppercase letters, 1 digit, and 1 special symbol.
'''
import random
import string

def generate_password():
    upper_case = random.choices(string.ascii_uppercase, k=2)
    digit = random.choice(string.digits)
    remaining_chars = random.choices(string.ascii_letters + string.digits + string.punctuation, k=6)
    
    password_list = upper_case + [digit] + remaining_chars
    random.shuffle(password_list)
    
    return ''.join(password_list)


print("Generated password:", generate_password())
print(len(generate_password()))
