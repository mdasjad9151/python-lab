'''
4. Write a program that inputs a main string and then creates an encrypted string
by embedding a short symbol-based string after each character. The program
should also be able to produce the decrypted string from encrypted string.
'''
def encrypt(main_string, symbol_string):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol_string
    return encrypted_string

def decrypt(encrypted_string, symbol_string):
    symbol_length = len(symbol_string)
    decrypted_string = ""
    i = 0
    while i < len(encrypted_string):
        decrypted_string += encrypted_string[i]
        i += symbol_length + 1
    return decrypted_string


main_string = input("Enter the main string: ")
symbol_string = input("Enter the symbol-based string: ")

encrypted = encrypt(main_string, symbol_string)
print("Encrypted string:", encrypted)

decrypted = decrypt(encrypted, symbol_string)
print("Decrypted string:", decrypted)
