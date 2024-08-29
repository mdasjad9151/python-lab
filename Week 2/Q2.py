# 2. Write a program to count the total number of digits in a number using a while
# loop.
def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))

