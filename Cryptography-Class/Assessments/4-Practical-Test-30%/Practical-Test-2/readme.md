# 🧪 Practical Test 2

---

## ✅ Preparation (Before Running Anything)

1. Create a Safe Analysis Environment:

- Install a fresh Windows 10 VM and disable networking (for safety).

- Install tools inside the VM.

2. Install Required Tools:

- 🛠️ Static & Dynamic Analysis:
   
    - Detect It Easy (DIE) – To identify compiler and packer.

    - pyinstxtractor-ng – To reverse it from executable(.exe) to .pyc etc.

    - uncompyle6 – To decompile .pyc to .py.

- 🔐 Python Environment for Decryption:

    - Install Python 3.8

3. Unpack the Archive:

- Extract simulated_ransomware.7z using 7-Zip (password: semogaberjaya)

- Check hash with:
 ```powershell
CertUtil -hashfile simulated_ransomware.exe SHA256
 ```

## 🧪 Part 1: Static Analysis & Reverse Engineering

### 🔧 Steps:

1. Download the file

- search the file on the web and download it.
https://tinyurl.com/bagicontoh

📷 Screenshot:

![alt text](<Screenshots/task1_download.png>)  

2. Identify Programming Language or Packing Tool

- Use DIE to inspect the .exe.

📷 Screenshot:

![alt text](<Screenshots/task1_die.png>)  

