def ejer1():
    print("Hola Mundo.")

def ejer2():
    miNombre = "Alexsandro"
    print(miNombre)

def ejer3():
    tuNombre = input("Dime tú nombre.\n")
    print("Hola", tuNombre)

def ejer4():
    tuNombre = input("Dime tú nombre.\n")
    tuEdad = int(input("Dime tú edad.\n"))
    print("Hola", tuNombre + ", tienes", tuEdad, "años.")

def ejer5(num1=0, num2=0):
    if num1 > num2:
        print(num1, "es el mas grande.")
    elif num1 == num2:
        print("Son iguales.")
    else:
        print(num2, "es el mas grande.")

def ejer6(num1=0):
    esta = False

    for x in range(0, 11):
        if num1 == x:
            esta = True

    if esta:
        print(num1, "esta entre 0 y 10.")
    else:
        print(num1, "no esta entre 0 y 10.")

def ejer7(num1=0):
    primo = False

    for x in range(3, num1):
        if num1 % x == 0:
            primo = True

    if primo:
        print(num1, "es primo.")
    else:
        print(num1, "no es primo.")

def ejer8(num1=0):
    par = False
    for i in range(0, num1, 2):
        if i==num1:
            par = True

    if par:
        print(num1, "es par.")
    else:
        print(num1, "no es par.")

    ejer7(num1)

def ejer9(count=0):
    i = 2
    while i <= count:
        print(i)
        i += 2

def ejer10(count=0):
    for i in range(1, count, 2):
        print(i)

def ejer11():
    # switch
    def switch_demo(argument):
        switcher = {
            "a": "París",
            "b": "Nimes",
            "c": "Montpellier",
            "d": "Lyon"
        }
        return switcher.get(argument, "Invalid")

    res = input("¿Cuál es la capital de Francia?\n" + "a) París\n" + "b) Nimes\n" + "c) Montpellier\n" + "d) Lyon\n")

    if switch_demo(res) == "París":
        print("!Has acertado¡")
    else:
        print("Has fallado")

def ejer12(palabra=""):
    rPalabra = ""
    for i in reversed(palabra):
        rPalabra += i

    if palabra == rPalabra:
        print(palabra, "es un políndromo.")
    else:
        print(palabra, "no es un políndromo.")

def ejer13(n = 0):
     """
     13. Crea un programe que muestre X números de la secuencia de Fibonacci.
     """
     a, b = 0,1
     for i in range(n):
          print(a, end=' ')
          a, b = b, a + b

def ejer14():
     """
     14. Crea un programa que pida por pantalla tu nombre y tu edad. El programa mostrará por
     pantalla “Hola NOMBRE, naciste en el año XXXX”. → import datetime
     """
     import datetime
     nombre = "Alex" #input("¿Cuál es tú nombre?\n")
     edad = 21 #input("¿Cuál es tú edad?\n")
     print("Hola", nombre, "naciste en el año", datetime.datetime.now().year-edad)

def ejer15():
     """
     15. Crea un programa llamado “Dados”, que simule una tirada de dos dados de 6 caras. Debe
     mostrar el resultado de los dos dados. → import random
     """
     import random
     dado1 = random.randrange(1, 7, 1)
     dado2 = random.randrange(1, 7, 1)
     print(dado1, dado2)
