##encoding=utf-8

"""
Pypi homepage: 
    https://pypi.python.org/pypi/pycrypto

Documentation: 
    http://pythonhosted.org/pycrypto/

Personal opinion:
    Most of pycrypto's features can be replaced by cryptography, and better to.
"""

from __future__ import print_function
from __future__ import unicode_literals
from hashlib import sha1, md5
from Crypto.Hash import SHA, MD5
import time

def basic_usage():
    message = "Attack at dawn"*(1000*1000)
    message_in_bytes = message.encode("utf-8")
    
    st = time.clock()
    print(sha1(message_in_bytes).hexdigest(), time.clock() - st)
    
    st = time.clock()
    print(SHA.new(message_in_bytes).hexdigest(), time.clock() - st)
    
    st = time.clock()
    print(md5(message_in_bytes).hexdigest(), time.clock() - st)
    
    st = time.clock()
    print(MD5.new(message_in_bytes).hexdigest(), time.clock() - st)

if __name__ == "__main__":
    basic_usage()