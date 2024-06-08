from base64 import encode, encodebytes
from cryptography.fernet import Fernet
import os


class encryption:
    def __init__(self):
        key = Fernet.generate_key()
        input_text = input("Enter the text you want to encrypt: ")
        input_text = input_text.encode()
        f = Fernet(key)
        encrypted_text = f.encrypt(input_text)
        print("The encrypted text is: ", encrypted_text)


class decryption:
    def __init__(self):
        key = Fernet.generate_key()
        input_text = input("Enter the text you want to decrypt: ")
        input_text = input_text.encode()
        f = Fernet(key)
        decrypted_text = f.decrypt(input_text)
        print("The decrypted text is: ", decrypted_text.decode())
    

class tool:
    choice = input("Do you want to encrypt or decrypt? ")
    if choice == "encrypt":
        encryption()
    elif choice == "decrypt":
        decryption()
    else:
        print("Invalid choice.")

while True:
    tool()
    break
