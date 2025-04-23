# Lab 4: Implementing Cryptography with Python

**Author:** Adli Jaafar  
**Date:** Apr 20 (Edited Apr 20)  
**Time Allocated:** 3 Hours  
**Total Marks:** 15  
**Lab Type:** Hands-On + Report + Demo/Debrief  

---

## A. Objective

The objective of this lab is to implement fundamental cryptographic algorithms in Python, analyze their security properties, and understand real-world applications. Students will:

1. Implement symmetric encryption using **AES**.
2. Implement asymmetric encryption using **RSA**.
3. Explore hashing using **SHA-256**.
4. Implement digital signatures using **RSA**.

---

## B. Lab Tasks

### Task 1: Symmetric Encryption (AES)

- Implement AES encryption and decryption in Python.
- Encrypt a sample message (e.g., `"Cryptography Lab by <Your Name, Student ID>!"`) using a secret key.
- Decrypt the ciphertext back to the original message.

---

### Task 2: Asymmetric Encryption (RSA)

- Generate an RSA key pair (public and private keys).
- Encrypt a short message using the public key.
- Decrypt it using the private key.

---

### Task 3: Hashing (SHA-256)

- Compute the SHA-256 hash of a file or message.
- **Evidence Required:**  
  - Screenshot of hashing outputs for different inputs.

---

### Task 4: Digital Signatures (RSA) (4 Marks)

- Sign a message using the RSA private key.
- Verify the signature using the corresponding public key.
- **Evidence Required:**  
  - Screenshot of the signing and verification process.

---

## C. Deliverables

1. **Walkthrough Document (Markdown File)**  
   - Commands used  
   - Screenshots of key steps  
   - Analysis of results  

2. **Evidence Folder**  
   - Screenshots of AES, RSA, SHA-256, and Digital Signature outputs.

3. **GitHub Repository**  
   - Public repo with all code, documentation, and evidence.

### 📁 Example Repository Structure

```bash
Lab 4/
├── README.md
├── evidence/
│   ├── aes_encryption_output.png
│   ├── rsa_encryption_output.png
│   ├── hashing_output.png
│   └── digital_signature_output.png
└── src/
    ├── aes_encryption.py
    ├── rsa_encryption.py
    ├── hashing.py
    └── digital_signature.py
```

4. **Live Demo (5-15 min presentation).**

---

## D. Demo and Debrief

1. **Explain OpenSSL commands used.**
2. **Show encryption/decryption, hashing, and signing.**
3. **Discuss real-world applications (e.g., TLS, file integrity).**

---
## E. Submission Instructions

1. **Push your walkthrough (in Markdown format) and evidence (screenshots) to your GitHub repository.**
2. **Write your repository link in the comment section below.**
3. **Be prepared to deliver a live demo and debrief during the lab session.**
4. **The order of presentation will be based on the last submission/comment, followed by previous ones.**
5. **Attendance is compulsory; no marks will be awarded for no-shows.**
6. **Marks will be deducted if the tasks are not completed.**
