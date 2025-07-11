import hashlib


def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()
