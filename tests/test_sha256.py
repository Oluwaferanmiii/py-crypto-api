import unittest
from app.modern.sha256_hash import sha256_hash
import hashlib


class TestSHA256(unittest.TestCase):
    def test_hash_output(self):
        inputs = ["HELLO WORLD", "FeranmiAkinwale"]
        for text in inputs:
            expected = hashlib.sha256(text.encode()).hexdigest()
            actual = sha256_hash(text)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
