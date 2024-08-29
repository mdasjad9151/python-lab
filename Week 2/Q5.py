# 5. Write a program to find the sum of digits of a supplied integer.

def sum_of_digits(num):
    sum =0
    while num > 0:
        digit = num % 10
        sum = sum +digit
        num  = num// 10
    return sum
num = int(input("Enter an integer: "))
print("Sum of digits: ", sum_of_digits(num))
