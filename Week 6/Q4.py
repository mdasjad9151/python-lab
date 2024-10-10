<<<<<<< HEAD
# 4. Write a program that inputs a main string and creates an encrypted string by embedding a short symbol-based string after each character. The program should also decrypt the string.
def encrypt_string(main_str, short_str):
    encrypted_str = ''
    for char in main_str:
        encrypted_str += char + short_str
    return encrypted_str

def decrypt_string(encrypted_str, short_str):
    decrypted_str = encrypted_str.replace(short_str, '')
    return decrypted_str

main_string = input("Enter the main string: ")
short_string = input("Enter the short string: ")
encrypted = encrypt_string(main_string, short_string)
print("Encrypted string:", encrypted)

decrypted = decrypt_string(encrypted, short_string)
=======
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
>>>>>>> f7f9ef7418e9cfe8a8b6ce836fef22c1c6059b2c
print("Decrypted string:", decrypted)
