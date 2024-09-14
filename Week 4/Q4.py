# 4. Given two Python lists, write a program to iterate both lists simultaneously and display items from list 1 in original order and items from list 2 in reverse order.

def iterate_lists(lst1, lst2):
    for x, y in zip(lst1, lst2[::-1]):
        print(f"List 1 item: {x}, List 2 item: {y}")

def input_fun(a):
    l =[]
    a =  input(f"Enter value {a} for list (for quit enter 'q'): ")
    while a != 'q':
        try:
            l.append(int(a))
        except:
            pass
        

        a =  input("Enter number (for quitenter 'q'): ")
    return l;
    


list1 = input_fun(1)
print("Enter value for 2nd list")
list2  =input_fun(2)
iterate_lists(list1, list2)
