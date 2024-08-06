#Caesar_Shift_Cipher#
def c_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start +(ord(char) - start +shift) % 26)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)
plain_text = input("Enter message to encrypt here")
shift = 5
encrypted_text = c_cipher(plain_text, shift)
print("Encrypted text:", encrypted_text)