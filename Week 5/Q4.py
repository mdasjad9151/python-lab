# 4. Given two lists of numbers, write a program to create a new list containing odd numbers from the first list and even numbers from the second list.
def merge_odd_even(lst1, lst2):
    odd_numbers = [x for x in lst1 if x % 2 != 0]
    even_numbers = [x for x in lst2 if x % 2 == 0]
    return odd_numbers + even_numbers

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = merge_odd_even(list1, list2)
print("Merged list:", result)
