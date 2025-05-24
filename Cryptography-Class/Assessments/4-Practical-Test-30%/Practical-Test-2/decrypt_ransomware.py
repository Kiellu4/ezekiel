from Crypto.Cipher import AES
from hashlib import sha256
import os

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Correct key derivation
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    new_path = filepath.replace(".enc", ".decrypted.txt")
    with open(new_path, "wb") as f:
        f.write(plaintext)
    print(f"Decrypted: {new_path}")

if __name__ == "__main__":
    folder = "locked_files/"
    for file in os.listdir(folder):
        if file.endswith(".enc"):
            decrypt_file(os.path.join(folder, file))
