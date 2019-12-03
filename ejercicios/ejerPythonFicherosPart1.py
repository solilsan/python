def ejer1(n = 0):
	"""
	Escribir una función que pida un número entero entre 1 y 10
	y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
	done n es el número introducido.
	"""
	import os
	cwd = os.getcwd()

	directorio = cwd+"/tabla-de-multiplicar"

	try:
	  os.stat(directorio)
	except:
	  os.mkdir(directorio)

	file = open(cwd+"/tabla-de-multiplicar/tabla-" + str(n) + ".txt", "w")

	cadena = ""

	for i in range(1, 11):
		cadena += str(n) + "x" + str(i) + "=" + str(n*i) + "\n"

	file.write(cadena)
	file.close()

def ejer2(n = 0):
	"""
	Escribir una función que pida un número entero entre 1 y 10,
	lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
	done n es el número introducido, y la muestre por pantalla.
	Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
	"""
	import os
	cwd = os.getcwd()

	try:

		file = open(cwd+"/tabla-de-multiplicar/tabla-" + str(n) + ".txt", "r")
	
		print(file.read())
	
		file.close()

	except FileNotFoundError:

		print("El fichero no existe.")

def ejer3(n = 0, m = 0):
	"""
	Escribir una función que pida dos números n y m entre 1 y 10,
	lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
	y muestre por pantalla la línea m del fichero.
	Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
	"""
	import os
	cwd = os.getcwd()

	try:

		file = open(cwd+"/tabla-de-multiplicar/tabla-" + str(n) + ".txt", "r")
	
		lines = file.readlines()
		for i in range(len(lines)):
			if m-1 == i:
				print(lines[i])
	
		file.close()

	except FileNotFoundError:

		print("El fichero no existe.")

def ejer4(n = 0):
	"""
	Escribir un programa que acceda a un fichero de internet mediante su url
	y muestre por pantalla el número de palabras que contiene.
	"""
	import urllib.request
	url = "https://opendata.euskadi.eus/contenidos/ds_recursos_turisticos/empresas_transporte_euskadi/opendata/transporte.json"

	try:

		file = urllib.request.urlopen(url)
	
		nPalabras = len(file.read())

		print(nPalabras)
	
		file.close()

	except urllib.error.URLError:

		print("El fichero no existe.")
