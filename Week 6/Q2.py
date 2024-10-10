# Create a dictionary with names as keys and phone numbers as values
phone_book = {
    "asjad": "12345678",
    "faraz": "654983787",
    "anas": "345-678-9012"
}

# Ask the user for a name
name = input("Enter a name: ")

# Print the corresponding phone number
if name in phone_book:
    print(f"{name}'s phone number is {phone_book[name]}")
else:
    print(f"Sorry, {name} is not in the phone book.")
