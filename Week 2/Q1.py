# 1. Write a Program to extract each digit from an integer in the reverse order

def extract_digits_reverse(num):
    while num > 0:
        digit = num % 10
        print(digit, end="")
        num //= 10

num = int(input("Enter a number with multiple digits: "))
extract_digits_reverse(num)
