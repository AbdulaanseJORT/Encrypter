from base64 import encode, encodebytes
from cryptography.fernet import Fernet
import os


class encryption:
    def __init__(self):
        key = Fernet.generate_key()
        os.system("cls")
        input_text = input("Enter the text you want to encrypt: ")
        input_text = input_text.encode()
        f = Fernet(key)
        encrypted_text = f.encrypt(input_text)
        print("Here is your encrypted text: ", encrypted_text)

class tool:
    input("Welcome to the tool! Please press enter to continue.")
    encryption()

while True:
    tool()
    break
