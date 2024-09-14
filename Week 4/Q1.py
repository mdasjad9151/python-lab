'''
1. Write a program to create function cal_sum_sub() such that it can accept two
variables and calculate addition and subtraction. Also, it must return both
addition and subtraction in a single return call.
'''

def cal_sum_sub(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

a =  int(input("Enter 1st number: "))
b =  int(input("Enter 2nd number: "))
result = cal_sum_sub(a, b)
print("Addition:", result[0])
print("Subtraction:", result[1])
