# 3. Given a list of numbers, write a program to turn every item of the list into its square.

def square_list(lst):
    return [x**2 for x in lst]


numbers = []
a =  input("Enter number (for quit enter 'q'): ")
while a != 'q':
    try:
        numbers.append(int(a))
    except:
        print("enter valid input")
    
    a =  input("Enter number (for quitenter 'q'): ")

squared_numbers = square_list(numbers)
print(squared_numbers)  
