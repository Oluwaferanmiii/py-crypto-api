def encrypt_caesar(plain_text: str, shift: int = 3, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> str:
    plain_text = plain_text.upper()
    encrypted = ""
    for char in plain_text:
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % len(alphabet)
            encrypted += alphabet[idx]
        else:
            encrypted += char
    return encrypted


def decrypt_caesar(cipher_text: str, shift: int = 3, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> str:
    cipher_text = cipher_text.upper()
    decrypted = ""
    for char in cipher_text:
        if char in alphabet:
            idx = (alphabet.index(char) - shift) % len(alphabet)
            decrypted += alphabet[idx]
        else:
            decrypted += char
    return decrypted
