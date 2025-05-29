def repeat_key(key: str, length: int) -> str:
    return (key * (length // len(key) + 1))[:length]


def encrypt_vigenere(plain_text: str, key: str = "cryptolab") -> str:
    plain_text = plain_text.upper()
    key = repeat_key(key.upper(), len(plain_text))
    encrypted = ""
    for p, k in zip(plain_text, key):
        if p.isalpha():
            encrypted += chr(((ord(p) - 65 + ord(k) - 65) % 26) + 65)
        else:
            encrypted += p
    return encrypted


def decrypt_vigenere(cipher_text: str, key: str = "cryptolab") -> str:
    cipher_text = cipher_text.upper()
    key = repeat_key(key.upper(), len(cipher_text))
    decrypted = ""
    for c, k in zip(cipher_text, key):
        if c.isalpha():
            decrypted += chr(((ord(c) - ord(k) + 26) % 26) + 65)
        else:
            decrypted += c
    return decrypted
