# 2. Write a program to pick a random character from a user-supplied string.
import random

def pick_random_char(user_string):
    return random.choice(user_string)


user_string = input("Enter a string: ")
print("Random character:", pick_random_char(user_string))
