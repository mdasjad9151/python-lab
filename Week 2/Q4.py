# 4. Write a program to use the loop to find the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} = {factorial(num)}")
