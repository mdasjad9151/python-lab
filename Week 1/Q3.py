# Print Numbers Divisible by 5.

def numbers_divisible_by_5(numbers):
    return [num for num in numbers if num % 5 == 0]


numbers = [int(input(f"Enter number {i+1}: ")) for i in range(20)]
print("Numbers divisible by 5:", numbers_divisible_by_5(numbers))
