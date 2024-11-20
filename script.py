import hashlib
import os
import re

# Validate SHA-256 hash format (64 hex characters).
def is_valid_sha256(hash):
    return bool(re.match(r'^[a-fA-F0-9]{64}$', hash))

hash = input("Enter the hash to crack: ").strip()

# Validate hash input.
if not hash:
    print("Error: No hash provided. Exiting.")
    exit()
elif not is_valid_sha256(hash):
    print("Error: Invalid hash format. Please provide a valid SHA-256 hash.")
    exit()

dictionary_path = input("Enter the dictionary directory (default: ./dictionary.txt): ").strip()

# Use default dictionary path if no input is given.
if not dictionary_path:
    dictionary_path = "./dictionary.txt"

# Check if dictionary file exsists.
if not os.path.exists(dictionary_path):
    print(f"Error: The dictionary file '{dictionary_path}' does not exist.")
    exit()

# Check if the dictionary file is empty.
if os.path.getsize(dictionary_path) == 0:
    print(f"Error: The dictionary file '{dictionary_path}' is empty.")
    exit()

# Read the dictionary file 
# Use 'with' to automatically close the file when the block is finished.
try:
    with open(dictionary_path, 'r') as file:
        # Clear the input of spaces in every line of the file.
        dictionary = [line.strip() for line in file]

        # Flag to show process message.
        process_started = False

        for password in dictionary:
            # Calculate the hash of the current password using SHA-256.
            calculated_hash = hashlib.sha256(password.encode()).hexdigest()

            if not process_started:
                print("Cracking...")
                process_started = True

            if calculated_hash == hash:
                print(f"Cracked! The password is: {password}")
                break
        else:
            # If loop was completed without breaking, no match was found.
            print("Password not found in dictionary.")

except IOError as error:
    print(f"Error: Failed to read the dictionary file. {error}")
