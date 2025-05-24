@ -1,167 +0,0 @@
# 🧪 Practical Test 2

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

8. Change the path format in windows  10
- many people have problem need to call the location of the file to use the tools. So, I'm using `system environment variables`, you can search at search bar below from windows10. Then, you need to call the location of the tool and paste it on the path.

### Steps
- search `system environment variables`
- click the `environment variables` button
- click the Variable `path`
- paste the location of the tool in the `edit environment variable`. example:(`C:\Users\mukhr\Downloads`)

📷 Screenshot:

![alt text](<Screenshots/task1_path.png>) 