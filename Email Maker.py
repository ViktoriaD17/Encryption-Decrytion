def encrypt_string(input_string, shift=3):
    encrypted_string = ""
    
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_string += encrypted_char
        else:
            # Keep non-alphabet characters unchanged
            encrypted_string += char

    return encrypted_string

# Example usage
input_str = "Hello, World!"
encrypted_str = encrypt_string(input_str)
print(f"Original String: {input_str}")
print(f"Encrypted String: {encrypted_str}")
