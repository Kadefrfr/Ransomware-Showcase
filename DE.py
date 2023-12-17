#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_decrypted)

files = []

for root, _, filenames in os.walk('.'):
    for filename in filenames:
        if filename in ["EN.py", "thekey.key", "DE.py"]:
            continue
        file_path = os.path.join(root, filename)
        files.append(file_path)

with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

secret_phrase = "Owen"

user_phrase = input("Enter the phrase\n")

if user_phrase == secret_phrase:
    for file_path in files:
        decrypt_file(file_path, secret_key)
    print("Files decrypted successfully.")
else:
    print("Incorrect phrase. Unable to decrypt files.")
