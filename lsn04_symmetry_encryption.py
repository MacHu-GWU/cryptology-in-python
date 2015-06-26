##encoding=utf-8

"""
cryptography is the best python cryptography package ever, which beats pycrypto.

Pypi homepage: 
    https://pypi.python.org/pypi/cryptography

Documentation: 
    https://cryptography.io/en/latest/
"""

from __future__ import print_function
from cryptography.fernet import Fernet

# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print("encrypted: [%s]" % token)
print("decrypted: [%s]" % f.decrypt(token))