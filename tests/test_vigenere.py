import unittest
from app.classical.vigenere import encrypt_vigenere, decrypt_vigenere


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        inputs = ["HELLO WORLD", "FeranmiAkinwale"]
        key = "cryptolab"
        for text in inputs:
            encrypted = encrypt_vigenere(text, key)
            decrypted = decrypt_vigenere(encrypted, key)
            self.assertEqual(decrypted, text.upper())


if __name__ == '__main__':
    unittest.main()
