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
Get-FileHash simulated_ransomware.7z 
 ```

📷 Screenshot:

![alt text](<Screenshots/hash.png>) 

## 🧪 Part 1: Static Analysis & Reverse Engineering

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

- Use DIE to inspect the .exe.

📷 Screenshot:

![alt text](<Screenshots/task1_die.png>)  

- the output shows:
 explain chatgpt

4. Identify the Type of Malware using Online Resources 

- search **VirusTotal** on the web
- copy the hash `simulated_ransomware.7z` and paste it on **VirusTotal**
    - Hash: `4BF1DA4E96EE6DD0306284C7F9CFE30F93113106843F2360052F8FEAF7B5578F`

📷 Screenshot:

![alt text](<Screenshots/task1_virustotal.png>)  

- the result 