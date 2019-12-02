def capicuaOpalindromo(n = "0"):
	#comprobar si es capicúa o palíndromo, si es capicua o palíndromo devuelve true
	a = str(n)[::-1]
	if str(n) == a:
		return True
	else:
		return False

def primo(n = 0):
	#Comprobar si un número es primo, si es primo me devuelve true
	if n == 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
			else:
				return True

def parImpar(n = 0):
	#Comprobar si un número es par si es par me devuelve true
	comprobar = False

	for i in range(2, n+2, 2):
		if i == n:
			comprobar = True
		else:
			comprobar = False

	return comprobar

def ejer1(n = 0):
	"""
	1. Crea un programa que pida al usuario un número y muestre por pantalla todos los números
	capicúas desde 1 hasta ese número separados por dos guiones. Crea una función llamada
	capicúa en otro archivo de Python.
	Ejemplo de salida: 11--22--33--44--55--………111--………--2222--………
	"""
	for i in range(1, n+1):
		if capicuaOpalindromo(i):
			print(i, end="--")

def ejer2(cantidad = 0, plazos = 0):
	"""
	2. Crea un programa en el que pida una cantidad de dinero (préstamo). Por otro lado, que
	pida también el número de plazos en el que se tiene que devolver ese dinero prestado.
	Muestra por pantalla, en cada fila, el número del plazo y la cantidad que queda por devolver
	al final de este.
	Ejemplo:
	Ingresa una cantidad: 12000
	Ingresa el número de plazos en el que devolverlo: 12
	Plazo 1 : 11000.0
	…
	Plazo 11 : 1000.0
	Plazo 12 : 0.0
	"""
	for i in range(plazos):
		cantidad-=(cantidad/plazos)
		plazos-=1
		print("Plazo", i+1, ":", cantidad)

def ejer3(n = 0):
	"""
	3. Escribir un programa que pida al usuario un número entero y muestre por pantalla una
	forma como la de abajo, de altura el número introducido.
	*
	**
	***
	****
	*****
	"""
	carac = "*"
	stric = ""
	for i in range(n):
		stric += carac+"\n"
		carac += "*"

	print(stric)

def ejer4(n = 0):
	"""
	4. Crea un programa que pida al usuario un número entero y muestre por pantalla una forma
	como la siguiente:
	2
	4 2
	6 4 2
	8 6 4 2
	10 8 6 4 2
	"""
	cadena = ""
	for x in range(0, n, 2):
		for i in range(x+2, 0, -2):
			cadena += str(i)+" "
		cadena += "\n"

	print(cadena)

def ejer5(n = 0):
	"""
	5. Crea un programa en el que por pantalla se pida un número del 1 al 10 y que muestre por
	pantalla su tabla de multiplicar.
	"""
	for i in range(1, 11):
		print(n, "x", i, "=", n*i)

def ejer6(n = 0):
	"""
	6. Crea un programa en el que se pida un número por pantalla. Mostrará la siguiente
	información de los números anteriores:
	- Es capicúa
	- Es par o impar
	- Es número primo
	Ejemplo:
	Introduce un número: 10
	1: capicúa, impar
	2: capicúa, par, primo
	…
	10: par
	…
	22: capicúa, par
	"""
	cadena = str(n)+": "
	if capicuaOpalindromo(n):
		cadena += "capicúa, "
	if primo(n):
		cadena += "primo, "
	if parImpar(n):
		cadena += "par"
	else:
		cadena += "impar"

	print(cadena)

def ejer7(n = 0):
	"""
	7. Escribe otro programa similar al 3, pero que muestre por pantalla lo siguiente:
	    *
	   ***
	  *****
	 *******
	*********
	"""
	carac = "*"
	espac = ""
	stric = ""
	for i in range(n):
		espac += " "
	for i in range(n):
		stric += espac+carac+"\n"
		espac = espac[1:]
		carac += "**"

	print(stric)

def ejer8():
	"""
	8. Guarda los valores del 1 al 100 en una lista y saca por pantalla sólo los pares.
	"""
	lista = {}
	for i in range(1, 101):
		lista[i] = i
	for x in lista:
		if parImpar(x):
			print(x)

def ejer9():
	"""
	9. Guarda los valores del 1 al 100 en una lista y guarda en otras dos listas lo siguiente:
	• Lista de pares: los números pares
	• Lista de impares: los elementos impares
	Saca las dos listas por pantalla.
	"""
	lista = {}

	for i in range(1, 101):
		lista[i] = i

	listaPares = {}
	listaImpares = {}
	
	for i in lista:
		if parImpar(i):
			listaPares[i] = i
		else:
			listaImpares[i] = i

	for p in listaPares:
		print(p)

	for z in listaImpares:
		print(z)

def ejer10(s = ""):
	"""
	10. Crea un programa en el que pida una palabra por pantalla y devuelva si es palíndromo.
	"""
	if capicuaOpalindromo(s.upper()):
		print(s, "es un palíndromo")
	else:
		print(s, "no es un palíndromo")

def ejer11():
	"""
	11. Crea un programa que almacene las asignaturas de un curso (SGE, DI, SI…) en una lista y la
	muestre por pantalla el mensaje El curso 2º de DAM tiene las siguientes
	asignaturas: <asignatura>, donde <asignatura> es cada una de las asignaturas de la
	lista.
	"""
	class Asignatura:
		nombre = ""

		def __init__(self, n):
			self.nombre = n

		def print_name(self):
			print(self.nombre)

	sge = Asignatura("SGE")

	di = Asignatura("")
	di.nombre = "DI"

	si = Asignatura("")
	si.nombre = "SI"

	dam = {}
	dam[0] = sge
	dam[1] = di
	dam[2] = si

	cadena = "El curso 2º de DAM tiene las siguientes asignaturas:\n"
	for i in dam:
		cadena += dam[i].nombre +"\n"

	print(cadena)

def ejer12():
	"""
	12. Crea un programa que tenga una lista desordenada y que la muestre por pantalla ordenada
	de menor a mayor. Nota: la lista debe contener números solamente.
	https://devcode.la/tutoriales/listas-python/
	"""
	import random
	lista = []
	
	for i in range(100):
		lista.append(random.randrange(1, 1001, 1))

	listaOrdenada = sorted(lista)
	
	print(listaOrdenada)
