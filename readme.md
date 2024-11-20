# Python Hash Cracker

A simple Python-based hash cracker that allows you to crack a hash by using a dictionary file. The script compares the hash of each word in the dictionary file against the target hash and reports if a match is found.

## Features

- [X] **Hash Format Validation**: Ensures that the provided hash is a valid SHA-256 hash (64 hexadecimal characters).

- [X] **Dictionary File Validation**: Checks if the dictionary file exists and is not empty before attempting to use it.

- [X] **Password Cracking**: Attempts to find the original password by comparing the hash of each word in the dictionary against the provided hash.

- [X] **Error Handling**: Handles errors such as invalid hash format, missing or empty dictionary file, and file read errors.

- [ ] **Performance Improvement**:
  - A more efficient search could involve parallelizing the hash cracking process using threads or multiprocessing to speed up the operation.

- [ ] **Allow for Multiple Hash Types**:
  - Currently, the script only works with SHA-256. It would be good to allow the user to choose a hashing algorithm (e.g., MD5, SHA-1, SHA-512) through a command-line option.

- [ ] **Add Exception Handling**:
  - File reading might fail for various reasons (permissions, corrupted files, etc.). Use try-except blocks to handle unexpected errors gracefully and ensure that the program doesn't crash abruptly.

- [ ] **Show Progress or Estimated Time**:
  - If you have a large dictionary, it could be helpful to show the progress or estimated time remaining to give the user feedback on the cracking process.

## Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hashlib](https://img.shields.io/badge/Hashlib-000000?style=for-the-badge&logo=python&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-000000?style=for-the-badge&logo=python&logoColor=white)
![OS](https://img.shields.io/badge/OS-000000?style=for-the-badge&logo=python&logoColor=white)

## Installation:

Ensure you have Python 3.x installed on your system. This script does not require any external libraries, as it only uses Python's built-in `hashlib`, `os`, and `re` modules.

1. Clone the repository.

```sh
git clone https://github.com/lopezrunco/hashcracker.git
cd hashcracker
```

Alternatively, you can directly download the Python script from the repository and place it in your desired directory.

## Usage:

1. Run the script:

    Execute the script in your terminal/command prompt:

    ```sh
    python script.py
    ```

2. Enter the target hash:

    The script will prompt you to enter the hash you want to crack. Example:

    ```sh
    Enter the hash to crack: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
    ```

3. Enter the dictionary file path:

    The script will then prompt you for the path to your dictionary file. If you leave the input blank, it will default to ./dictionary.txt:

    ```sh
    Enter the dictionary directory (default: ./dictionary.txt): ./dictionary.txt
    ```

4. Results:

    The script will try each password from the dictionary and calculate the hash of each word. If the calculated hash matches the input hash, it will display the cracked password:

    ```sh
    Cracked! The password is: password123
    ```

    If no match is found, it will print:

    ```sh
    Password not found in dictionary.
    ```

#### Example Output:

```sh
    Enter the hash to crack: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
    Enter the dictionary directory (default: ./dictionary.txt): ./dictionary.txt
    Cracked! The password is: password123
```

## Error Handling

- **Invalid Hash Format**:  
  The script checks if the provided hash is a valid SHA-256 hash. If it is not, the script will print an error and exit.

- **Missing or Empty Dictionary File**:  
  If the dictionary file is missing or empty, the script will alert you and exit.

- **File Read Errors**:  
  If there is an issue reading the dictionary file (e.g., permission issues), the script will display an error message.

## Disclaimer:

This tool is for educational and personal use only. Cracking passwords or attempting to break into systems without authorization is illegal and unethical. Always ensure you have proper authorization before using password cracking tools.