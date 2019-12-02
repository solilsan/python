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
	lista = [{"TECLADO" : 13, "RATON" : 9, "IMPRESORA" : 35, "ESCANER" : 25}]

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
	lista = [{"TECLADO" : 13, "RATON" : 9, "IMPRESORA" : 35, "ESCANER" : 25}]

	def switch_lista(index):
		switcher = {
			1: "TECLADO",
    	    2: "RATON",
    	    3: "IMPRESORA",
    	    4: "ESCANER"
		}
		return switcher.get(index, "Invalid index")

	for key in lista:
		contador = 0
		for i in key:
			contador += 1
			print(contador, i, ":", key[i], "$")

	try:

		print(lista[0][switch_lista(index)], "$")

	except KeyError:

		print("No disponemos de ese producto.")
	

ejer2(3)