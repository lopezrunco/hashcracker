import hashlib
import os

hash = input("Enter the hash to crack: ").strip()

dictionary_path = input("Enter the dictionary directory (default: ./dictionary.txt): ").strip()

# Use default dictionary path if no input is given.
if not dictionary_path:
    dictionary_path = "./dictionary.txt"

# Check if dictionary file exsists.
if not os.path.exists(dictionary_path):
    print(f"Error: The dictionary file '{dictionary_path}' does not exist.")

# Read the dictionary file 
# Use 'with' to automatically close the file when the block is finished.
with open(dictionary_path, 'r') as file:
    # Clear the input of spaces in every line of the file.
    dictionary = [line.strip() for line in file]

    for password in dictionary:
        # Calculate the hash of the current password using SHA-256.
        calculated_hash = hashlib.sha256(password.encode()).hexdigest()

        if calculated_hash == hash:
            print(f"Cracked! The password is: {password}")
            break
        else:
            print("Password not found in dictionary.")
