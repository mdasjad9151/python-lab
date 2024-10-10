# Print Numbers Divisible by 5.

def print_divisible_by_5(numbers):
    for num in numbers:
        if num % 5 == 0:
            print(num)


numbers = []

print("Please enter 20 numbers:")
for _ in range(20):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Numbers divisible by 5 are:")
print_divisible_by_5(numbers)
