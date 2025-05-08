# 🔒🐍 Lab 4: Implementing Cryptography with Python 

- **Author:** 👦🏾 Ezekiel Mukhriz
- **Partner:** 👦🏾 Muhammad Aabas 

### 📌 Objective
- Learn core cryptographic operations using Python.
- Practice symmetric (AES) and asymmetric (RSA) encryption.
- Understand hashing and digital signatures.
- Verify data integrity and authenticity through hands-on coding.

---

### 🐍 Python Installation
Make sure you have:
1. Install Python (3.8+ recommended).
2. Install necessary libraries:
```bash
pip install cryptography pycryptodome
```

![alt text](<Screenshots/python_installation.png>)

---

## 🔹 Task 1: Symmetric Encryption using AES-256-CBC (Kiel ↔ Aabas)

- Here is the [AES_encrypt.py](Python_Source/AES_encrypt.py) python code.
- Here is the [AES_decrypt.py](Python_Source/AES_decrypt.py) python code.

---

### 🛠️ Steps:

### 👦🏾 Ezekiel 

1. Run `AES_encrypt.py`:

![task1](Screenshots/task1_code1.png) 

2. Enter the **plaintext** and a strong **password**:

![task1](Screenshots/task1_encrypt1.png) 

3. Copy the **Base64 Encrypted Output**:

![task1](Screenshots/task1_encrypt2.png) 

4. Send the **Encrypted (Base64)** to Aabas (Example: via Email/WhatsApp):

### 👦🏾 Aabas 

1. Run `AES_decrypt.py`:

![task1](Screenshots/task1_code2.png) 

2. Paste the **Base64 Encrypted Message** and enter the same **password**:

![task1](Screenshots/task1_decrypt1.png)

3. View the decrypted output to verify successful communication:

![task1](Screenshots/task1_decrypt2.png) 

---

## 🔹 Task 2: Asymmetric Encryption using RSA (Kiel ↔ Aabas)

- Here is the [RSA_key_pair.py](Python_Source/RSA_key_pair.py) code.
- Here is the [RSA_encrypt.py](Python_Source/RSA_encrypt.py) code.
- Here is the [RSA_decrypt.py](Python_Source/RSA_decrypt.py) code.

---

### 🛠️ Steps:

### 👦🏾 Aabas 

1. Run `RSA_key_pair.py` to generate **public** and **private keys**:

![task2](Screenshots/task2_code1.png) 

2. Share the **public key** with Ezekiel.

### 👦🏾 Ezekiel 

1. Run `RSA_encrypt.py`:

![task2](Screenshots/task2_code2.png) 

2. Enter the **plaintext** and Aabas's **public key**:

![task2](Screenshots/task2_encrypt1.png) 

3. Send the **Encrypted (Base64)** to Aabas (Example: via Email/WhatsApp):

![task2](Screenshots/task2_encrypt2.png) 

### 👦🏾 Aabas 

1. Run `RSA_decrypt.py`:

![task2](Screenshots/task2_code3.png) 

2. Enter the **encrypted message** and use your **private key**:

![task2](Screenshots/task2_decrypt1.png) 

3. View the decrypted message:

![task2](Screenshots/task2_decrypt2.png) 

---

## 🔹 Task 3: Hashing and Message Integrity using SHA-256

- Here is the [Hashing_SHA-256.py](Python_Source/Hashing_SHA-256.py) code.

---

### 🛠️ Steps

1. Run the script:
Run the Python script `Hashing_SHA-256.py` to start the hashing program.
![task3](Screenshots/task3_code.png) 

2. Enter your message:
Type your **original plaintext message**.
Example used:
```bash
Cryptography Lab by Ezekiel, DNWS23010066 !
```

📷 Screenshot:

![task3](Screenshots/task3_hash1.png) 

🔑 SHA-256 Output:
```output
3343fe8541a33a630a151b45f5375008d1e020759847b630711d0fdd6c9f3e30
```

3. Modify the Message Slightly:
Now change a single character in the original input.
Example change: Replace `0066` ➜ `0046`
```bash
Cryptography Lab by Ezekiel, DNWS23010046 !
```

📷 Screenshot:

![task3](Screenshots/task3_hash2.png) 

🔑 SHA-256 Output:
```output
d7ec10033d0d9e160e00fe31bc1fad1ce7c77d8c5101ad6b960f622849b12a0b
```

4. Compare the output:
- 1st hash: `Cryptography Lab by Ezekiel, DNWS23010066 !`
```output
3343fe8541a33a630a151b45f5375008d1e020759847b630711d0fdd6c9f3e30
```

- 2nd hash: `Cryptography Lab by Ezekiel, DNWS23010046 !`
```output
d7ec10033d0d9e160e00fe31bc1fad1ce7c77d8c5101ad6b960f622849b12a0b
```

### 🌪️ Avalanche Effect Explained

#### 🔍 What just happened?
Although only two digits were changed (66 ➜ 46), the entire SHA-256 hash changed drastically. This is known as the Avalanche Effect — a key property of cryptographic hash functions.

### ✅ Why It Matters
✔️ Ensures file/data integrity with even tiny changes detected.

---

## 🔹 Task 4: Task 4: Digital Signatures using RSA & SHA-256 (Kiel ↔ Aabas)

- Here is the [RSA_key_pair.py](Python_Source/RSA_key_pair.py) code.
- Here is the [Digital_Signature_signing.py](Python_Source/Digital_Signature_signing.py) code.
- Here is the [Digital_Signatures_verification.py](Python_Source/Digital_Signatures_verification.py) code.

---

### 🛠️ Steps

### 👦🏾 Aabas (Signing)

1. Run `Digital_Signatures_signing.py`:

![task4](Screenshots/task4_code1.png) 

2. Input the **plaintext** and your **private key**:

![task4](Screenshots/task4_ds1.png)  

3. Share the **digital signature (Base64)** and the **plaintext** with Kiel.

![task4](Screenshots/task4_ds2.png) 

### 👦🏾 Ezekiel (Verification)

1. Run `Digital_Signatures_verification.py`:

![task4](Screenshots/task4_code2.png) 

2. Enter Aabas’s **original message, digital signature (Base64)** and **public key** to verify the signature:

![task4](Screenshots/task4_ds3.png) 

3. Confirm if the message is authentic and untampered:
- The message is **valid.** ✅

![task4](Screenshots/task4_valid.png)

- The message is **.** ❌

![task4](Screenshots/task4_invalid.png)

---

