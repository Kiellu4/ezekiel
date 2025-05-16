# 🧪 Practical Test 1

---

## ✅ Task 1: Generate Your GPG Key Pair

**Objective:** Use `gpg` to generate an RSA key pair tied to your identity.

### 🔧 Steps:
1. Generate key:
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

```bash
gpg --list-keys
```

📷 Screenshot:

![alt text](Screenshots/task1_output2.png)

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

![alt text](<Screenshots/task2_decrypt1.png>) 

![alt text](<Screenshots/task2_decrypt2.png>) 

4. Verify the output:
```bash
cat decrypted.txt
```

📷 Screenshot:

![alt text](<Screenshots/task2_output.png>) 

---

## ✅ Task 3: Sign and Verify a Message

**Objective:** Digitally sign a message and verify authenticity.

### 🔧 Steps:

1. Create the message:
```bash
echo "I, Ezekiel Mukhriz, declare this is my work." > signed_message.txt
```

📷 Screenshot:

![alt text](<Screenshots/task3_message.png>)  

2. Sign the file:
```bash
gpg --clearsign signed_message.txt
```

📷 Screenshot:

![alt text](<Screenshots/task3_sign.png>) 

3. Verify the signature:
```bash
gpg --verify signed_message.txt.asc
```

📷 Screenshot:

![alt text](<Screenshots/task3_verify.png>) 

---

## ✅ Task 4: Configure Passwordless SSH Authentication

**Objective:** Set up SSH key-based login to localhost or a test VM.

### 🔧 Steps:

1. Run the following command in Windows Powershell:
```bash
ssh-keygen -t rsa
```

📷 Screenshot:

![alt text](<Screenshots/task4_1.png>) 

- just press enter to save it in the default path
- leave the passphrase empty for passwordless authentication

2. Go to `.ssh` and check the ssh-key file that has been generate:
```bash
ls
cd .ssh
```
📷 Screenshot:

![alt text](<Screenshots/task4_2.png>)  

3. See the content of the `id_rsa.pub`:
```bash
cat id_rsa.pub
```

📷 Screenshot:

![alt text](<Screenshots/task4_3.png>)

- copy it to `authorized_keys` in **Kali Linux**

4. Run the following command in **Kali Linux terminal**:
```bash
cd .ssh
vim authorized_keys
```

📷 Screenshot:

![alt text](<Screenshots/task4_4-1.png>) 
![alt text](<Screenshots/task4_4-2.png>) 

5. Make sure set the permission as below in Kali Linux:
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

📷 Screenshot:

![alt text](<Screenshots/task4_5.png>) 