def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():  # Uppercase letters
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():  # Lowercase letters
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isdigit():  # Numbers
            encrypted_text += chr((ord(char) - 48 + shift) % 10 + 48)
        else:  # Other characters remain the same
            encrypted_text += char

    return encrypted_text


# Ask the user for input
user_text = input("Enter a sentence to encrypt: ")
user_shift = int(input("Enter the shift value (number): "))

# Encrypt the text
encrypted = caesar_encrypt(user_text, user_shift)

print(f"Encrypted text: {encrypted}")
