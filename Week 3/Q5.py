# 5. Write a program to remove characters from a string starting from n to last and
# return a new string. Example: remove_chars("aligarh", 3) so output must be
# al.

def remove_chars(string, n):
    if n > len(string):
        return ""
    return string[:n]


new_string = remove_chars("aligarh", 3)
print(new_string)  # Output: "ali"
