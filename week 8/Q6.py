# Write a program in python to find vowels having maximum number of instances in a given file.
# (Note: File contains variety of data such as English alphabets, numbers etc.).
def find_max_vowel_instance(file_path):
    vowels = "aeiouAEIOU"  # Vowel characters (both lowercase and uppercase)
    vowel_count = {v: 0 for v in vowels}  # Dictionary to count vowel instances
    print(vowel_count)

    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            for line in file:
                for char in line:
                    if char in vowel_count:  # If the character is a vowel
                        vowel_count[char] += 1

        # Find the vowel with the maximum occurrence
        max_vowel = max(vowel_count, key=vowel_count.get)
        max_count = vowel_count[max_vowel]

        if max_count > 0:
            print(f"The vowel with the maximum instances is '{max_vowel}' with {max_count} occurrences.")
        else:
            print("No vowels found in the file.")

    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "week 8\simple.txt"
find_max_vowel_instance(file_path)
