# 3. Write a program to display all prime numbers within a range.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for num in range(lower, upper + 1):
    if is_prime(num):
        print(num)
