import unittest
from app.classical.caesar import encrypt_caesar, decrypt_caesar


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        inputs = ["HELLO WORLD", "FeranmiAkinwale"]
        for text in inputs:
            encrypted = encrypt_caesar(text, shift=3)
            decrypted = decrypt_caesar(encrypted, shift=3)
            self.assertEqual(decrypted, text.upper())


if __name__ == '__main__':
    unittest.main()
