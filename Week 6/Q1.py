# Write a Python program that inputs two tuples and creates a third that contains all elements of the first followed by all elements of the second.
def merge_tuples(tup1, tup2):
    return tup1 + tup2


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = merge_tuples(tuple1, tuple2)
print("Merged tuple:", result)
