import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Encrypt/Decrypt App", page_icon="🔐")

st.title("🔐 Encrypt & Decrypt UI")
st.subheader("A simple frontend for FastAPI crypto backend")

cipher = st.selectbox("Choose a Cipher", [
                      "Caesar", "Vigenère", "SHA-256", "RSA"])
action = st.radio("Action", ["Encrypt", "Decrypt", "Hash (SHA-256 Only)"])

text = st.text_area("Enter your text")

if cipher == "Caesar":
    shift = st.number_input("Shift (Caesar only)",
                            min_value=1, max_value=25, value=3)
    if st.button("Submit"):
        route = "/encrypt/caesar" if action == "Encrypt" else "/decrypt/caesar"
        response = requests.post(
            API_URL + route, json={"text": text, "shift": shift}, timeout=5)
        st.code(response.json().get("ciphertext" if action ==
                "Encrypt" else "plaintext", "Error"))

elif cipher == "Vigenère":
    key = st.text_input("Key (default: cryptolab)", value="cryptolab")
    if st.button("Submit"):
        route = "/encrypt/vigenere" if action == "Encrypt" else "/decrypt/vigenere"
        response = requests.post(
            API_URL + route, json={"text": text, "key": key}, timeout=5)
        st.code(response.json().get("ciphertext" if action ==
                "Encrypt" else "plaintext", "Error"))

elif cipher == "SHA-256":
    if action != "Hash (SHA-256 Only)":
        st.warning("SHA-256 only supports hashing")
    if st.button("Hash Text"):
        response = requests.post(
            API_URL + "/hash/sha256", json={"text": text}, timeout=5)
        st.code(response.json().get("hash", "Error"))

elif cipher == "RSA":
    st.markdown(
        "⚠️ Generate keys using the backend first at `/rsa/keys` or use your own keys.")
    key_input = st.text_area("Paste your Public or Private Key")
    if st.button("Submit"):
        route = "/encrypt/rsa" if action == "Encrypt" else "/decrypt/rsa"
        response = requests.post(
            API_URL + route, json={"text": text, "key": key_input}, timeout=5)
        st.code(response.json().get("ciphertext" if action ==
                "Encrypt" else "plaintext", "Error"))
