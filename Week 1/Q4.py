# Check if a Number is a Palindrome

def is_palindrome(number):
    return str(number) == str(number)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
