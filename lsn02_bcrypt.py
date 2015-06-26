##encoding=utf-8

"""bcrypt is a python extension to do password encryption and authentication
This script is to show you how to use bcrypt to verify users' login request

Pypi homepage: 
    https://pypi.python.org/pypi/bcrypt/2.0.0
    
Inside of cryptography algorithm: 
    https://cryptography.io/en/latest/security/
"""

from __future__ import print_function
from __future__ import unicode_literals
import bcrypt

def veryfi_password():
	"""A standard user login process is:
	1. use SSH connection send entered password from browser to server (RSA encrypted)
	2. decrypt the password, hash it, and use bcrypt.hashpw(decrypted, correct_hashed)
		to verify it.
	"""
    password = "super secret password".encode("utf-8") # send password to server using rsa encryption
    hashed = bcrypt.hashpw(password, bcrypt.gensalt()) # you can use bcrypt.gensalt(rounds=14)
    print(hashed)
    print(bcrypt.hashpw(password, hashed))
    
veryfi_password()