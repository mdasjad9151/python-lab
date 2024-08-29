# 3. Write a program to print characters from a string which are present at an even
# index numbers.

def print_even_index_characters(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    print(result)


input_string = input("Enter a string: ")
print_even_index_characters(input_string)
