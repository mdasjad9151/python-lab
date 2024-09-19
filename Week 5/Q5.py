# 5. Write a program to create a numpy array and return an array of odd rows and even columns from the numpy array.

import numpy as np


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
result = arr[1::2, ::2]
print("Array of odd rows and even columns:\n", result)
