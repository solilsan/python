import base64
import os

try:

	cwd = os.getcwd()
	
	with open(cwd+"/pp.jpg", "rb") as f:
	    encode = base64.b64encode(f.read())
	    print(encode.decode())

except FileNotFoundError:
	
	print("Archivo no encontrado.")