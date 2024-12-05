import hashlib
import os
import re

# Validate hash format.
def is_valid_hash(hash, algorithm):
    if algorithm == 'sha256':
        return bool(re.match(r'^[a-fA-F0-9]{64}$', hash))
    elif algorithm == 'md5':
        return bool(re.match(r'^[a-fA-F0-9]{32}$', hash))
    elif algorithm == 'sha1':
        return bool(re.match(r'^[a-fA-F0-9]{40}$', hash))
    elif algorithm == 'sha512':
        return bool(re.match(r'^[a-fA-F0-9]{128}$', hash))
    else:
        return False
    
# Select hashing algorithm.
def get_hash_function(algorithm):
    if algorithm == 'sha256':
        return hashlib.sha256
    elif algorithm == 'md5':
        return hashlib.md5
    elif algorithm == 'sha1':
        return hashlib.sha1
    elif algorithm == 'sha512':
        return hashlib.sha512
    else:
        return ValueError("The algorithm is not supported.")

hash_input = input("Enter the hash to crack: ").strip()

if not hash_input:
    print("Error: No hash provided. Exiting.")
    exit()

# Ask user to select the hashing algoritm.
algorithm = input("Enter the hashing algorithm (md5, sha1, sha256, sha512): ").strip().lower()

if not algorithm in ['md5', 'sha1', 'sha256', 'sha512']:
    print("Error: The hashing algorithm is not supported. Exiting.")
    exit()

# Validate hash input format based on selected algorithm.
if not is_valid_hash(hash_input, algorithm):
    print(f"Error: Invalid {algorithm} hash format. Please provide a valid {algorithm} hash.")
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

# Read the dictionary file & attempt to crack the hash.
# Use 'with' to automatically close the file when the block is finished.
try:
    with open(dictionary_path, 'r') as file:
        # Clear the input of spaces in every line of the file.
        dictionary = [line.strip() for line in file]

        # Flag to show process message.
        process_started = False

        # Get the hash function for the selected algorithm.
        hash_function = get_hash_function(algorithm)

        for password in dictionary:
            # Calculate the hash of the current password using the selected algorithm.
            calculated_hash = hash_function(password.encode()).hexdigest()

            if not process_started:
                print("Cracking...")
                process_started = True

            if calculated_hash == hash_input:
                print(f"Cracked! The password is: {password}")
                break
        else:
            # If loop was completed without breaking, no match was found.
            print("Password not found in dictionary.")

except IOError as error:
    print(f"Error: Failed to read the dictionary file. {error}")
