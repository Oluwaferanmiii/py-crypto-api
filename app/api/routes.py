from fastapi import APIRouter
from pydantic import BaseModel
from app.classical.caesar import encrypt_caesar, decrypt_caesar
from app.classical.vigenere import encrypt_vigenere, decrypt_vigenere
from app.modern.sha256_hash import sha256_hash
from app.modern.rsa_crypto import generate_keys, encrypt_rsa, decrypt_rsa

router = APIRouter()


class CipherRequest(BaseModel):
    text: str
    key: str | None = None
    shift: int | None = 3


@router.post("/encrypt/caesar")
def caesar_encrypt(req: CipherRequest):
    return {"ciphertext": encrypt_caesar(req.text, req.shift)}


@router.post("/decrypt/caesar")
def caesar_decrypt(req: CipherRequest):
    return {"plaintext": decrypt_caesar(req.text, req.shift)}


@router.post("/encrypt/vigenere")
def vigenere_encrypt(req: CipherRequest):
    return {"ciphertext": encrypt_vigenere(req.text, req.key or "cryptolab")}


@router.post("/decrypt/vigenere")
def vigenere_decrypt(req: CipherRequest):
    return {"plaintext": decrypt_vigenere(req.text, req.key or "cryptolab")}


@router.post("/hash/sha256")
def hash_text(req: CipherRequest):
    return {"hash": sha256_hash(req.text)}


class RSARequest(BaseModel):
    text: str
    key: str


@router.get("/rsa/keys")
def get_rsa_keys():
    private_key, public_key = generate_keys()
    return {"private_key": private_key, "public_key": public_key}


@router.post("/encrypt/rsa")
def rsa_encrypt(req: RSARequest):
    return {"ciphertext": encrypt_rsa(req.text, req.key)}


@router.post("/decrypt/rsa")
def rsa_decrypt(req: RSARequest):
    return {"plaintext": decrypt_rsa(req.text, req.key)}
