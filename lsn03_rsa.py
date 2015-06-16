##encoding=utf-8

"""
rsa is a RSA encryption algorithm implementation in python.
This script is to teach you how to use rsa to protect your message and file

Pypi homepage: 
    https://pypi.python.org/pypi/rsa
    
rsa python documentation: 
    http://stuvel.eu/rsa#header1
"""

import rsa
from rsa.bigfile import *

def send_message():
    """encrypt, sign and verification example usage
    """
    (pubkey, privkey) = rsa.newkeys(512, poolsize=1) # generate public, private key
    message = "Go left at the blue tree".encode("utf-8")
    crypto = rsa.encrypt(message, pubkey) # encrypt it
    signature = rsa.sign(message, privkey, 'SHA-1') # sign it
    # send crypto and signature to receiver
    received = rsa.decrypt(crypto, privkey).decode("utf-8") # decrypt message
    print(rsa.verify(received.encode("utf-8"), signature, pubkey)) # verify the signature
    print(received) # print received message
    
send_message()

def work_with_big_file():
    (pubkey, privkey) = rsa.newkeys(512, poolsize=1)
    with open(r"testdata\message.txt", "rb") as infile, open(r"testdata\received.txt", 'wb') as outfile:
        encrypt_bigfile(infile, outfile, pubkey)
    with open(r"testdata\received.txt", "rb") as infile, open(r"testdata\decrypted.txt", 'wb') as outfile:
        decrypt_bigfile(infile, outfile, privkey)
        
work_with_big_file()