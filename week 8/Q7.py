''' Write a Python program to create a list of user’s supplied distinct integers having   of elements. The program further creates two lists of equal lengths based on the original list, where first list is having all elements less than elements of second list. Display both the lists.

'''
def create_even_length_list():
    original_list = []

    # Input until the user provides an even-length list of distinct integers
    while True:
        user_input = input("Enter distinct integers separated by spaces: ")
        try:
            # Convert input to a list of integers and remove duplicates
            original_list = list(set(map(int, user_input.split())))

            if len(original_list) % 2 == 0:
                break  # Exit loop if the list has an even number of elements
            else:
                print("Please enter an even number of distinct integers.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

    # Sort the original list in ascending order
    original_list.sort()

    # Split the list into two equal halves
    mid = len(original_list) // 2
    L1 = original_list[:mid]  # First half (smaller elements)
    L2 = original_list[mid:]  # Second half (larger elements)

    # Display both lists
    print("List 1 (smaller elements):", L1)
    print("List 2 (larger elements):", L2)

# Example usage
create_even_length_list()
