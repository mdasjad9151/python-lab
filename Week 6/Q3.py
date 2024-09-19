# 3. Write a Python program to calculate the sum of squares of the first two digits and the last two digits of a 4-digit number, e.g., for 1233, calculate 12^2 + 33^2.

def sum_of_squares_of_digits(number):
    if 1000 <= number <= 9999:  # Ensure it's a 4-digit number
        first_two_digits = number // 100
        last_two_digits = number % 100
        result = first_two_digits**2 + last_two_digits**2
        return result
    else:
        return "Please enter a 4-digit number."


num = int(input("Enter a 4-digit number: "))
result = sum_of_squares_of_digits(num)
print("Sum of squares of the first and last two digits:", result)
