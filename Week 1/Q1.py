# 1. Write a program to find product of two user supplied integers and if the product
# is equal to or lower than 5000 then return sum of the two numbers.

def product_and_sum(a, b):
    product = a * b
    if product <= 5000:
        return a + b
    return product


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = product_and_sum(num1, num2)
print("Result:", result)