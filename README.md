# 🔐 Encrypt Decrypt API

A Python-based application that provides encryption, decryption, and hashing services via a RESTful API built with FastAPI.

## ✨ Features

- 🔁 **Classic Ciphers**
  - Caesar Cipher (Custom shift)
  - Vigenère Cipher (Custom key)

- 🔒 **Modern Cryptography**
  - SHA-256 Hashing
  - RSA Key Generation
  - RSA Encryption & Decryption

- ⚡ REST API via FastAPI
- 🖥️ Streamlit Frontend UI
- ✅ Unit tested with `unittest`

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Oluwaferanmiii/py-crypto-api
cd encrypt_decrypt_api
```

### 2. Install Dependencies (via Pipenv)
```bash
pipenv install
pipenv shell
```

### 3. Start the API Server
```bash
uvicorn main:app --reload
```

### 4. Run the Streamlit Frontend 
```bash
streamlit run streamlit_app.py
```

---

## Running Tests
```bash
python -m unittest discover -s tests
```

---

## Project Structure
```bash
crypto_project/
├── app/
│   ├── classical/         # Caesar and Vigenère ciphers
│   ├── modern/            # SHA-256 and RSA
│   ├── api/               # FastAPI route definitions
│   └── utils/             # File I/O or key formatting helpers
├── tests/                 # Unit tests
├── main.py                # App entrypoint
├── Pipfile                # Pipenv dependency file
```

---

## 👨‍💻 Author
Feranmi Akinwale

Built for educational purposes — Cryptography & Security Lab Final Project