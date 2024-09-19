'''
2. Write a function to return True if the first and last number of a given list is
same. If numbers are different then return False.
'''
def is_first_last_same(numbers):
    return numbers[0] == numbers[-1]


numbers = []
a =  input("Enter number (for quit enter 'q'): ")
while a != 'q':
    try:
        numbers.append(int(a))
    except:
        print("enter valid input")
    
    a =  input("Enter number (for quitenter 'q'): ")
    


print(is_first_last_same(numbers))  
