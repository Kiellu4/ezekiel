# 🧪 Practical Test 2

## ✅ Summary of Analysis

This test involved performing **static analysis and reverse engineering** on a simulated ransomware binary. The analysis was conducted in a secure Windows 10 virtual environment with networking disabled.

---

## ✅ Preparation (Before Running Anything)

1. Create a Safe Analysis Environment:

- Install a fresh Windows 10 VM and disable networking (for safety).

- Install tools inside the VM.

2. Install Required Tools:

- 🛠️ Static & Dynamic Analysis:
   
    - Detect It Easy (DIE) – To identify compiler and packer.

    - pyinstxtractor-ng – To decompile it from executable(.exe) to .pyc etc.

    - uncompyle6 – To decompile .pyc to .py.

- 🔐 Python Environment for Decryption:

    - Install Python 3.8

3. Unpack the Archive:

- Extract simulated_ransomware.7z using 7-Zip (password: semogaberjaya)

- Check hash with:
 ```powershell
Get-FileHash simulated_ransomware.7z 
 ```

📷 Screenshot:

![alt text](<Screenshots/hash.png>) 

## 🧪 Static Analysis & Reverse Engineering

### 🔧 Steps:

1. Download the file

- search the file on the web and download it. https://tinyurl.com/bagicontoh

📷 Screenshot:

![alt text](<Screenshots/task1_download1.png>)  

### Output:

📷 Screenshot:

- the file is downloaded and saved in the folder `C:\Users\user\Downloads`
- I cut and paste it on anoteher directory `C:\Users\mukhr\Downloads\practical-test-2` 

📷 Screenshot:

![alt text](<Screenshots/task1_download2.png>) 

2. Extract the file using 7-Zip and fill the password

- extract the file `simulated_ransomware.7z` using 7-Zip
- the password use `semogaberjaya`

📷 Screenshot:

![alt text](<Screenshots/task1_download3.png>) 

3. Identify Programming Language or Packing Tool

- use DIE to inspect the .exe.

📷 Screenshot:

![alt text](<Screenshots/task1_die.png>)  

4. Change the path format in windows  10
- many people have problem need to call the location of the file to use the tools. So, I'm using `system environment variables`, you can search at search bar below from windows10. Then, you need to call the location of the tool and paste it on the path.

### Steps
- search `system environment variables`
- click the `environment variables` button
- click the Variable `path`
- paste the location of the tool in the `edit environment variable`. example:(`C:\Users\mukhr\Downloads`)

📷 Screenshot:

![alt text](<Screenshots/task1_path.png>)

### 🔍 DIE Output

| Field | Meaning |
|-------|--------|
| **PE64** | 64-bit Windows executable file. |
| **OS: Windows Vista+** | Made for modern Windows (64-bit). |
| **Linker: Microsoft Linker** | Built with Microsoft compiler tools. |
| **Compiler: MSVC C/C++** | Has C/C++ parts, probably native code used. |
| **Language: Python** | The main logic is written in Python. |
| **Tool: Visual Studio 2022** | Built or packaged using Visual Studio. |
| **Packer: PyInstaller (modified)** | Python script bundled as EXE using PyInstaller. |
| **Compressed or Packed** | The real code is hidden in compressed sections. |
| **Overlay: ZLIB data** | Compressed Python files are hidden inside the EXE. |

4. Identify the Type of Malware using Online Resources 

- search **VirusTotal** on the web
- copy the hash `simulated_ransomware.7z` and paste it on **VirusTotal**
    - Hash: `4BF1DA4E96EE6DD0306284C7F9CFE30F93113106843F2360052F8FEAF7B5578F`

📷 Screenshot:

![alt text](<Screenshots/task1_virustotal.png>)  

- the result shows `No security vendors flagged this file as malicious` means not malicious.

5. Convert .exe to .pyc using pyinstxtractor

- use **pyinstxtractor** to extract the Python code from the .exe file

``` powershell
pyinstxtractor-ng.exe .\simulated_ransomware.exe
```

📷 Screenshot:

![alt text](<Screenshots/task1_pyinstxtractor.png>) 

### 🧵 PyInstaller Extraction Output

| Output | Meaning |
|--------|--------|
| **PyInstaller version: 2.1+** | The EXE was packed using PyInstaller v2.1 or later. |
| **Python version: 3.8** | The embedded ransomware script was written in Python 3.8. |
| **Length of package: 8766261 bytes** | Size of the internal PyInstaller archive inside the EXE. |
| **Found 91 files in CArchive** | CArchive is the container for bundled files like modules and scripts. |
| **Entry points (e.g. `pyi_rth_*`)** | These are runtime hooks that PyInstaller uses during execution. |
| **Main script: `simulated_ransomware.pyc`** | This is the compiled Python file containing the ransomware logic. |
| **Found 526 files in PYZ archive** | The PYZ archive includes compressed Python modules. |
| **Successfully extracted archive** | All files are extracted and ready for decompilation. |

6. Go to the extracted directory and find the ransomware script
```bash
ls
cd simulated_ransomware.exe_extracted
ls
```

📷 Screenshot:

![alt text](<Screenshots/task1_extracted1.png>) 

![alt text](<Screenshots/task1_extracted2.png>) 

7. Read the file `simulated_ransomware.pyc`
```bash
ls simulated*
Get-Content simulated_ransomware.pyc
```

📷 Screenshot:

![alt text](<Screenshots/task1_read.png>) 

- you can see the file is in .pyc format, which is unreadable. So, we can use tools like **uncompyle6** to change it to .py format to read.

8. use uncompyle6 to convert the .pyc file to .py format
```powershell
uncompyle6.exe -o . .\simulated_ransomware.pyc
```

📷 Screenshot:

![alt text](<Screenshots/task1_uncompyle6.png>)  

- now you can read the ransomware script in .py format.

```bash
# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: simulated_ransomware.py
from Crypto.Cipher import AES
import os
from hashlib import sha256
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[None[:16]]

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len


def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        plaintext = f.read()
    padded = pad(plaintext)
    cipher = AES.new(KEY, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    with open(filepath + ".enc", "wb") as f:
        f.write(ciphertext)
    os.remove(filepath)


if __name__ == "__main__":
    folder = "locked_files/"
    os.makedirs(folder, exist_ok=True)
    sample_files = [
     "maklumat1.txt", "maklumat2.txt", "maklumat3.txt"]
    contents = [
     "Assalamualaikum semua, pelajar kursus Cryptography semester 5.\nKeselamatan siber bergantung kepada kebijaksanaan anda dalam memahami kriptografi.\nGunakan ilmu ini untuk melindungi data, sistem, dan masa depan teknologi.\nJadilah perisai digital yang berintegriti dan berkemahiran.",
     "Setiap algoritma yang anda pelajari hari ini adalah benteng pertahanan esok.\nKuasa penyulitan (encryption) bukan hanya tentang kod, tetapi amanah dalam menjaga maklumat.\nTeruskan usaha, dunia digital menanti kepakaran anda!",
     "Semoga ilmu yang dipelajari menjadi manfaat kepada semua.\nGunakan kepakaran anda untuk kebaikan, bukan kemudaratan.\nSemoga berjaya di dunia dan akhirat!\n\nAdli, Lecturer Part Time, Feb-Mei 2025"]
    for name, content in zip(sample_files, contents):
        path = os.path.join(folder, name)
        with open(path, "w") as f:
            f.write(content)
        encrypt_file(path)

```

9. build decrypt file using python

- I named as decrypt_ransomware.py and put this code

```bash
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
    folder = "locked_files/"
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            decrypt_file(os.path.join(folder, filename))

```

- after all of this, run it use commnad at terminal
```bash
python decrypt_ransomware.py
```

10. Open the file with the decrypted content and verify that the content is correct.

📷 Screenshot:

![alt text](<Screenshots/task1_dec1.png>)  

### 🧵 Final Output

- dec 1
```bash
Assalamualaikum semua, pelajar kursus Cryptography semester 5.
Keselamatan siber bergantung kepada kebijaksanaan anda dalam memahami kriptografi.
Gunakan ilmu ini untuk melindungi data, sistem, dan masa depan teknologi.
Jadilah perisai digital yang berintegriti dan berkemahiran.
```

📷 Screenshot:

![alt text](Screenshots/image.png)

- dec 2
```bash
Assalamualaikum semua, pelajar kursus Cryptography semester 5.
Keselamatan siber bergantung kepada kebijaksanaan anda dalam memahami kriptografi.
Gunakan ilmu ini untuk melindungi data, sistem, dan masa depan teknologi.
Jadilah perisai digital yang berintegriti dan berkemahiran.
```

📷 Screenshot:

![alt text](Screenshots/image-1.png)

- dec 3
```bash
Semoga ilmu yang dipelajari menjadi manfaat kepada semua.
Gunakan kepakaran anda untuk kebaikan, bukan kemudaratan.
Semoga berjaya di dunia dan akhirat!

Adli, Lecturer Part Time, Feb-Mei 2025
```

📷 Screenshot:

![alt text](Screenshots/image-2.png)

# 🔐 Cryptography Analysis of Simulated Ransomware

## 📌 Summary of Learning

In this practical test, we performed **static analysis and reverse engineering** on a simulated ransomware binary. The executable was found to be a Python script packaged using **PyInstaller**. After extraction and decompilation, we discovered it used **AES encryption in ECB mode** with a **hardcoded key** to encrypt files. We then wrote a Python script to **decrypt the files** successfully, confirming our analysis.

---

## ❌ 1. Flaws in the Ransomware's Cryptography

The ransomware implementation demonstrates several critical cryptographic flaws:

### 🔑 Hardcoded Key
- **Issue**: The encryption key is hardcoded in the source code:
  ```python
  KEY_SUFFIX = "RahsiaLagi"
  KEY_STR = f"Bukan{KEY_SUFFIX}"
  KEY = sha256(KEY_STR.encode()).digest()[:16]

### 🧱 ECB Mode (Electronic Codebook)

```python
cipher = AES.new(KEY, AES.MODE_ECB)
```

### ✅ 2. A More Secure Encryption Approach
A better implementation of file encryption using AES would include:

### ✅ Use AES in a Secure Mode (e.g., GCM or CBC + HMAC)
Replace ECB with AES-GCM, which provides confidentiality and integrity.
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)  # 256-bit key
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
```

### ✅ Use a Random IV/Nonce Per File
- Always generate a new random IV or nonce for each encryption session:
```python
nonce = cipher.nonce
```

### ✅ Store Key Securely or Use Public-Key Cryptography
- Do not hardcode keys in code.

- Instead, use asymmetric encryption (e.g., RSA) to encrypt a symmetric AES key.

- The ransomware holds the private key.

- Victims cannot decrypt without paying (still unethical but technically stronger).

### ✅ Add File Integrity Checks
- Use HMAC or authenticated encryption (like AES-GCM) to ensure that tampered files are detected and rejected.