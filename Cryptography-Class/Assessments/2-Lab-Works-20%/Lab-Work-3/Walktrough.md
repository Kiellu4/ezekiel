# Lab 3: Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures ✍️🔒

### 📌 Objective
- Learn core cryptographic operations using OpenSSL.
- Practice symmetric (AES) and asymmetric (RSA) encryption.
- Understand hashing and digital signatures.
- Verify data integrity and non-repudiation through hands-on use.

---

## 🔹 Task 1: Symmetric Encryption using AES-256-CBC (Kiel ↔ Aabas)

### 🎯 Goal
Encrypt and decrypt a file using AES with CBC mode and verify content integrity.

---

### 🛠️ Steps
### ✅ Kiel → Aabas
1. Create a plaintext file:

```bash
echo "flag{AES_256_CBC}" > kiel_aes.txt
```


2. Encrypt using AES-256-CBC:

```bash
openssl enc -aes-256-cbc -salt -in kiel_aes.txt -out kiel_aes.enc -k abc123
```


3. 