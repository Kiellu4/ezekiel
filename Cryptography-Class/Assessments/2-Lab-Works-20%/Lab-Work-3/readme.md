# Lab 3: Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures

**Instructor:** Adli Jaafar  
**Date:** Apr 20  
**Total Points:** 100  
**Due Date:** No due date  
**Time Allocation:** 3 Hours  
**Total Marks:** 15  
**Lab Type:** Hands-On + Report + Demo/Debrief

---

## A. Lab Objectives

This lab introduces students to OpenSSL, a widely used cryptography toolkit, for performing essential cryptographic operations such as:

1. Symmetric encryption (AES)
2. Asymmetric encryption (RSA)
3. Hashing (SHA-256)
4. Digital signatures (RSA with SHA-256)

By the end of this lab, students will be able to:

1. Encrypt and decrypt files using symmetric and asymmetric encryption.
2. Generate and verify hashes for data integrity.
3. Create and verify digital signatures.

---

## B. Lab Tasks

### Task 1: Symmetric Encryption using AES (3 marks)

**Objective:** Encrypt and decrypt a file using AES-256 in CBC mode.

**Steps:**
1. Create a sample text file, `rahsia.txt`  
   `echo "Mesej rahsia guna AES encryption oleh <Tulis Nama Sendiri>" > rahsia.txt`
2. Encrypt the file using AES-256-CBC.
3. Decrypt the file.
4. Verify the decrypted content matches the original.

**Expected Deliverables:**
- Screenshot of encryption & decryption commands.
- Content comparison of original and decrypted files.

---

### Task 2: Asymmetric Encryption using RSA

**Objective:** Generate an RSA key pair, encrypt a message with the public key, and decrypt it with the private key.

**Steps:**
1. Generate an RSA private key (2048-bit).
2. Extract the public key.
3. Encrypt a message using the public key.
4. Decrypt using the private key.
5. Verify the decrypted message matches the original.

**Expected Deliverables:**
- Screenshot of key generation, encryption, and decryption.
- Content comparison of original and decrypted messages.

---

### Task 3: Hashing and Message Integrity using SHA-256 (3 marks)

**Objective:** Generate a hash of a file and verify its integrity.

**Steps:**
1. Create a sample file:  
   `echo "Nama & ID Pelajar" > data.txt`
2. Generate SHA-256 hash.
3. Modify the file slightly and recheck the hash.
4. Observe how the hash changes.

**Expected Deliverables:**
- Screenshot of hash generation before and after modification.
- Explanation of why hashes change.

---

### Task 4: Digital Signatures using RSA & SHA-256 (5 marks)

**Objective:** Sign a file and verify the signature.

**Steps:**
1. Generate a hash and sign it with the private key.
2. Verify the signature using the public key.
3. Tamper with the file and attempt verification again.

**Expected Deliverables:**
- Screenshot of signing and verification.
- Explanation of why verification fails after tampering.

---

## C. Deliverables

1. Walkthrough Document (Markdown file) detailing:
   - Commands used
   - Screenshots of key steps
   - Analysis of results

2. Evidence (Screenshots of outputs).

3. GitHub Repository (Public repo with all files).

4. Live Demo (5-15 min presentation).

---

## D. Demo and Debrief

1. Explain OpenSSL commands used.
2. Show encryption/decryption, hashing, and signing.
3. Discuss real-world applications (e.g., TLS, file integrity).

---

## E. Submission Instructions

1. Push all files to a public GitHub repository.
2. Submit the repository link to the instructor.
3. Be ready for a live demo in the lab session.
