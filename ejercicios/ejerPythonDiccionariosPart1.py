"""
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February"
    }
    print switcher.get(argument, "Invalid month")
"""
def normalize(s):
	#Quitar tildes
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

lista = [{"TECLADO" : 13, "RATON" : 9, "IMPRESORA" : 35, "ESCANER" : 25}]

def switch_lista(index):
	switcher = {
		1: "TECLADO",
        2: "RATON",
        3: "IMPRESORA",
        4: "ESCANER"
	}
	return switcher.get(index, "Invalid index")

def ejer1(nombre = ""):
	"""
	1. Escribir un programa que guarde en un diccionario los precios de periféricos de la siguiente
	tabla. Debe preguntar al usuario por un periférico y el programa mostrará el precio
	correspondiente. En caso de que no se encuentre en el diccionario, debe informar sobre ello
	Periférico Precio
	Teclado 13
	Ratón 9
	Impresora 35
	Escáner 25
	"""
	try:

		print(lista[0][normalize(nombre).upper()], "$")

	except KeyError:

		print("No disponemos de ese producto.")

def ejer2(index = 0):
	"""
	2. Escribe un programa que guarde el mismo diccionario que el del ejercicio 1. Debe mostrar por
	pantalla los nombres de los productos y pedir que el usuario elija uno. El programa mostrará
	después por pantalla el precio correspondiente.
	"""
	for key in lista:
		contador = 0
		for i in key:
			contador += 1
			print(contador, i, ":", key[i], "$")

	try:

		print(lista[0][switch_lista(index)], "$")

	except KeyError:

		print("No disponemos de ese producto.")
	
def ejer3(index = 0, descuento = 0):
	"""
	3. Escribe un programa que use el diccionario anterior. Realiza un descuento a los periféricos
	guardados. El usuario debe indicar por pantalla el descuento que se va a realizar. Después de
	introducirlo, el programa guardará los nuevos precios y mostrará por pantalla el nombre del
	periférico, el precio “viejo” y el nuevo precio.
	Ejemplo:
	Se ha aplicado un descuento de 10%
	Teclado → Antes: 13€ -- Ahora: 11,7€
	"""
	for key in lista:
		contador = 0
		for i in key:
			contador += 1
			print(contador, i, ":", key[i], "$")

	try:

		nombreK = ""
		contador = 0
		for key in lista[0].keys():
			contador += 1
			if contador == index:
				nombreK = key

		precioV = lista[0][switch_lista(index)]

		lista[0][switch_lista(index)] = lista[0][switch_lista(index)]-(lista[0][switch_lista(index)] / descuento)

		print("Se aplicara un descuento de", str(descuento)+"%\n"
			+nombreK, "->", "Antes:", str(precioV)+"$", "Ahora:", str(lista[0][switch_lista(index)])+"$")

	except KeyError:

		print("No disponemos de ese producto.")

def ejer4():
	"""
	4. Escribe un programa que primero cree un diccionario vacío y después lo vaya llenado con
	información sobre una persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico,
	etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
	contenido del diccionario.
	"""
	class Persona:
		nombre = ""
		edad = 0
		sexo = ""
		telefono = 0
		email = ""

		def __init__(self, nombre, edad, telefono, email):
			self.nombre = nombre
			self.edad = edad
			self.telefono = telefono
			self.email = email

	p1 = Persona("Pepe", 21, 619283821, "pepe@gmail.com")
	p2 = Persona("Alex", 20, 945827382, "alex@gmail.com")

	lista.append(p1)
	lista.append(p2)

	print(lista[1].nombre)

def ejer5():
	"""
	5. Crear una “lista de la compra”. Escribe un programa que pida al usuario por pantalla los
	artículos y sus precios correspondientes (clave:valor) que quiera añadir a su lista de la compra.
	Una vez acabe de añadir, mostrará todos los artículos y el precio total.
	"""
	class Producto:
		nombre = ""
		cantidad = 0
		precio = 0

		def __init__(self, nombre, cantidad, precio):
			self.nombre = nombre
			self.cantidad = cantidad
			self.precio = precio

	p1 = Producto("Arroz", 2, 2.5)
	p2 = Producto("Leche", 6, 1.4)
	p3 = Producto("Queso", 1, 2.8)

	listaCompra = [p1,p2,p3]

	precioTotal = 0

	for i in range(len(listaCompra)):
		precioTotal += listaCompra[i].cantidad * listaCompra[i].precio

	print("Precio total de carrito:", str(precioTotal)+"$")

def ejer6(n = 0):
	"""
	6. Crea un programa que pida un número al usuario. Este número corresponderá al número de
	elementos del diccionario. Debe devolver un diccionario cuya clave será 1, 2, …n (n será el
	número que el usuario ha introducido) y el valor será el valor al cuadrado de la clave.
	Ejemplo:
	mi_diccionario = {'1' : 1, '2' : 4, '3' : 9 , '4' : 16}
	"""
	mi_diccionario = []

	for i in range(1, n+2):
		mi_diccionario.append(i**2)

	for i in range(len(mi_diccionario)):
		print(i, ":", mi_diccionario[i])

def ejer7(cadena = ""):
	"""
	7. Escribe un programa que cree un diccionario de traducción castellano-inglés. El usuario debe
	añadir las palabras (claves y valores) por pantalla del siguiente modo:
	• Separadas por un :
	• Cada par <palabra>:<traducción> separados por comas.
	El programa debe crear un diccionario con las palabras y sus traducciones.
	Después de crear el diccionario pedirá una frase en castellano y utilizará el diccionario para
	traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
	Nota: utiliza el método Split para poder separar las palabras junto a sus traducciones (por la
	coma) y también la palabra original y su traducción (por los dos puntos).
	Ejemplo de salida:
	Introduce la lista de palabras y traducciones: Hola:Hello,mi:my,nombre:name,es:is
	Escribe la frase a traducir: Hola, mi nombre es Ekaitz
	Hello, my name is Ekaitz
	"""
	class Traductor:
		es = ""
		en = ""
		eu = ""
		jp = ""

		def __init__(self, es, en, eu, jp):
			self.es = es
			self.en = en
			self.eu = eu
			self.jp = jp

	traductor = [Traductor("HOLA", "hello", "kaixo", "こんにちは"), Traductor("MI", "my", "nire", "私の"), Traductor("NOMBRE", "name", "izen", "お名前"), Traductor("ES", "is", "hau da", "は")]

	cadenaS = cadena.replace(",", "").split()

	cadenaEn = ""

	for i in range(len(traductor)):
		for x in cadenaS:
			if x.upper() == traductor[i].es:
				cadenaEn += traductor[i].en + " "
				cadenaS.remove(x)

	for z in cadenaS:
		cadenaEn += z + " "

	print(cadena + "\n" + cadenaEn)
