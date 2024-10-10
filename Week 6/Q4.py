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
print("Decrypted string:", decrypted)
