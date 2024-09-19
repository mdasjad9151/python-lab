'''
6. Write a program to create a numpy array and sort it as per the following cases:
a. Case 1: Sort the array by the second row.
b. Case 2: Sort the array by the second column.
'''

import numpy as np

# a) Sort array by second row
def sort_by_second_row(arr):
    return arr[:, arr[1, :].argsort()]

# b) Sort array by second column
def sort_by_second_column(arr):
    return arr[arr[:, 1].argsort()]


arr = np.array([[4, 2, 3], [9, 1, 7], [8, 5, 6]])

# Case 1
sorted_by_row = sort_by_second_row(arr)
print("Array sorted by second row:\n", sorted_by_row)

# Case 2
sorted_by_column = sort_by_second_column(arr)
print("Array sorted by second column:\n", sorted_by_column)
