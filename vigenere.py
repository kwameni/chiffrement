def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypt_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
          encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypt_text.append(encrypted_char)
    return "".join(encrypt_text)
        


def decrypt_vigenere(encrypted_text, key):
    decrypted_text = []
    key = generate_key(encrypted_text, key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isupper():
            decrypted_char= chr((ord(char)- ord(key[i]) + 2 * ord('A'))%26 + ord('A'))
        elif char.islower():
            decrypted_char= chr((ord(char)- ord(key[i]) + 2 * ord('a'))%26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)





text_to_encrypt = "bonjour"
key = "KEY"

encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")