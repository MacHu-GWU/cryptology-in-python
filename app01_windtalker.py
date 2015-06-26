##encoding=utf-8

"""
This is an application to can encrypt any files with a password only you know.
Don't put the password anywhere, only in your brain.

Prerequisite
------------
    cryptography
    
Compatibility
-------------
    python27: True
    python33: True
"""

from cryptography.fernet import Fernet
import hashlib
import base64
import os
import sys

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    input = raw_input

class WindTalker():
	"""An application class to encrypt any files.
	"""
	def pre_exam(self, src, dst):
		"""check:
		1. if source file exists
		2. if source file too big ( > 1GB)
		3. if source file == output file (to avoid overwrite self)
		4. if output file exists (to avoid overwrite other files)
		"""
		if not os.path.exists(src):
			raise Exception("Error, Source file '%s' doesn't exists!" % src)
		if os.path.getsize(src) >= 1024*1024*1024:
			raise Exception("Error, you can not encrypt a file larger than 1GB.")
		if src == dst:
			raise Exception("Error, output file's path is same as source file.")
		if os.path.exists(dst):
			decision = input("Are you gonna overwrite '%s'? [Y/N]: " % dst)
			if decision.upper() != "Y":
				raise Exception("Output file already exists. Process canceled.")
		
	def any_text_to_fernet_key(self, text):
		"""generate url_safe base64 encoded key for fernet symmetric encryption
		"""
		m = hashlib.md5()
		m.update(text.encode("utf-8"))
		fernet_key = base64.b64encode(m.hexdigest().encode("utf-8"))
		return fernet_key
	
	def encrypt_file(self, src, dst):
		try:
			self.pre_exam(src, dst)
			text = input("For encryption, enter your secret key: ")
			fernet_key = self.any_text_to_fernet_key(text)
			fernet = Fernet(fernet_key)
			
			with open(src, "rb") as f:
				token = fernet.encrypt(f.read()) # encrypted token
				with open(dst, "wb") as f1:
					f1.write(token)
					
			print("successfully encrypt '%s'." % src)
		except Exception as e:
			print(e)
			
	def decrypt_file(self, src, dst):
		try:
			self.pre_exam(src, dst)
			text = input("For decryption, say your magic words: ")
			fernet_key = self.any_text_to_fernet_key(text)
			fernet = Fernet(fernet_key)
			
			with open(src, "rb") as f:
				try:
					token = fernet.decrypt(f.read()) # decrypted token
				except:
					raise Exception("Opps, wrong magic words!")
				with open(dst, "wb") as f1:
					f1.write(token)
			
			print("successfully decrypt '%s'." % src)
		except Exception as e:
			print(e)

windtalker = WindTalker()
	
if __name__ == "__main__":
    windtalker.encrypt_file("app01_windtalker.py", "app02.py")
    windtalker.decrypt_file("app02.py", "app03.py")