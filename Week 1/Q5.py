# Calculate Cube of Numbers from 1 to a Given Number
def cubes_up_to_n(n):
    return {i: i**3 for i in range(1, n+1)}


n = int(input("Enter a number: "))
print("Cubes from 1 to", n, ":", cubes_up_to_n(n))
