# 🧪 Practical Test 1

---

## ✅ Task 1: Generate Your GPG Key Pair

**Objective:** Use `gpg` to generate an RSA key pair tied to your identity.

### 🔧 Steps:

```bash
sudo gpg --full-generate-key
```

Insert all of this:
- Key type: RSA and RSA
- Key size: 4096 bits
- Expiration: 1y
- Name: Ezekiel Mukhriz
- Email: mukhrizfitry@gmail.com

📷 Screenshot:

![alt text](<Screenshots/task1_input.png>)  

### 🔍 Output

📷 Screenshot:

![alt text](<Screenshots/task1_output.png>) 

---

## ✅ Task 2: Encrypt and Decrypt a File

**Objective:** Perform GPG encryption and decryption.

### 🔧 Steps:

1. Create the message:
```bash
echo "This file was encrypted by Ezekiel MUkhriz NWS23010066" > message.txt
```

📷 Screenshot:

![alt text](<Screenshots/task2_message.png>) 

2. Encrypt with your own public key:
```bash
gpg -e -r "Ezekiel Mukhriz" message.txt

```

📷 Screenshot:

![alt text](<Screenshots/task2_encrypt.png>) 

3. Decrypt the file:
```bash
gpg -d message.txt.gpg > decrypted.txt

```

📷 Screenshot:

![alt text](<Screenshots/task2_decrypt.png>) 

4. Verify the output:
```bash
cat decrypted.txt

```

📷 Screenshot:

![alt text](<Screenshots/task2_output.png>) 



