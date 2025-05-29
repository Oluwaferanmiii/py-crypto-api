import unittest
from app.modern.rsa_crypto import generate_keys, encrypt_rsa, decrypt_rsa


class TestRSA(unittest.TestCase):
    def test_encrypt_decrypt(self):
        private_key, public_key = generate_keys()
        inputs = ["HELLO WORLD", "FeranmiAkinwale"]
        for text in inputs:
            encrypted = encrypt_rsa(text, public_key)
            decrypted = decrypt_rsa(encrypted, private_key)
            self.assertEqual(decrypted, text)


if __name__ == '__main__':
    unittest.main()
