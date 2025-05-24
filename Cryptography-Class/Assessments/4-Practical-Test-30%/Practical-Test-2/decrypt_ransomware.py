from Crypto.Cipher import AES
import os
from hashlib import sha256

KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]  # Fixing incorrect slice from original

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    unpadded = unpad(decrypted)
    new_path = filepath.replace(".enc", ".dec")
    with open(new_path, "wb") as f:
        f.write(unpadded)
    print(f"Decrypted: {filepath} -> {new_path}")

if __name__ == "__main__":
    folder = "."
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            decrypt_file(os.path.join(folder, filename))
