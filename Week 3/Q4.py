# 4. Write a program to accept a string from the user and display characters that are
# present at an even index number.

def print_even_index_characters_from_user_input():
    string = input("Enter a string: ")
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    print("Characters at even index positions:", result)


print_even_index_characters_from_user_input()
