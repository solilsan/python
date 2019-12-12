from subprocess import call
import os
import re

def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls') 

def verificarEmail(email = ""):

    pattern = re.compile('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
    result = pattern.match(email)

    if result:

        return True

    else:

        return False

def email(email = ""):

    while True:
    
            if(verificarEmail(email)):
    
                return email
                break
    
            else:
                
                email = str(input("Introduce un email.\n"))
                clear()

def validarNombre(nombre = ""):

    if nombre.isalpha():

        if len(nombre) <= 6:
            print("Mínimo 6 carácteres.\n")
            valido = False
        elif len(nombre) > 12:
            print("Máximo 12 carácteres.\n")
            valido = False
        else:
            valido = True

    else:
        print("Solo puede contener letras.\n")
        valido = False

    return valido

def nombre(nombre = ""):

    while True:

        if(validarNombre(nombre)):

            return nombre
            break

        else:
            
            nombre = str(input("Introduce un nombre.\n"))
            clear()

def generardorPassword(rango = 0, mi = False, ma = False, num = False, sib = False):

    if mi or ma or num or sib:
    
        if rango >= 4 and rango < 26:
    
            import random
    
            password = ""
    
            while rango > 0:
    
                if mi and rango > 0:
                    abcMinus = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
                    password += abcMinus[random.randrange(0, 26)]
                    rango -= 1
                
                if ma and rango > 0:
                    abcMayus = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
                    password += abcMayus[random.randrange(0, 26)]
                    rango -= 1
                
                if num and rango > 0:
                    nums = ['1','2','3','4','5','6','7','8','9','0']
                    password += nums[random.randrange(0, 9)]
                    rango -= 1
        
                if sib and rango > 0:
                    simbs = ['*','+','-','_',';','¿','?','¡','!','º','ª']
                    password += simbs[random.randrange(0, 10)]
                    rango -= 1
        
            return password
    
        else:
            print("Mínimo 4 y máximo 25 de longitud\n")
            return False

    else:
        print("Elige por lo menos una opción.\n")
        return False

def password(longitud, minus, mayus, nums, sibs):

    password = generardorPassword(longitud, minus, mayus, nums, sibs)

    while True:

        if(password != False):

            return password
            break

        else:

            longitud = int(input("1-Longitud de contraseña (número).\n"))

            minus = False
            if str(input("¿Quiéres minúsculas (si o no)?\n")).upper() == "SI":
                minus = True
            
            mayus = False
            if str(input("¿Quiéres mayúsculas (si o no)?\n")).upper() == "SI":
                mayus = True
            
            nums = False
            if str(input("¿Quiéres números (si o no)?\n")).upper() == "SI":
                nums = True
            
            sibs = False
            if str(input("¿Quiéres símbolos (si o no)?\n")).upper() == "SI":
                sibs = True
                
            #clear()

            password = generardorPassword(longitud, minus, mayus, nums, sibs)

def nivelPassword(password = ""):

    nvl = 0

    longi = len(password)

    if longi >= 4 and longi < 10:
        nvl += 1

    elif longi >= 10 and longi < 20:
        nvl += 2

    elif longi >= 20:
        nvl += 3

    for i in password:
        if i.isupper():
            nvl += 1
            break

    for i in password:
        if i.isdecimal():
            nvl += 1
            break

    for i in password:
        if i.isalpha():
            nvl = nvl
        else:
            nvl += 1
            break

    nivel = ""

    if nvl >= 1 and nvl < 3:
        nivel = "Débil"

    elif nvl >= 3 and nvl < 5:
        nivel = "Media"

    elif nvl >= 5:
        nivel = "Fuerte"

    return nivel

class Usuario:
    nombre = ""
    password = ""

    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

usuario = Usuario("Alexsan", "SJs3h73")

datos = [usuario]

continuar = True

while continuar:

    print("Nuevo usuario.\n")
    iNombre = str(input("Introduce un nombre.\n"))

    comprobar = False
    for i in datos:
    
        if i.nombre == nombre(iNombre):
            comprobar = True
    
    if comprobar:

        #clear()
        print("Ya exite ese nombre.\n")

    else:

        #clear()

        print("Generador de contraseña.\n")

        longitud = int(input("1-Longitud de contraseña (número).\n"))

        minus = False
        if str(input("¿Quiéres minúsculas (si o no)?\n"))   .upper() == "SI":
            minus = True

        mayus = False
        if str(input("¿Quiéres mayúsculas (si o no)?\n"))   .upper() == "SI":
            mayus = True

        nums = False
        if str(input("¿Quiéres números (si o no)?\n")).upper    () == "SI":
            nums = True

        sibs = False
        if str(input("¿Quiéres símbolos (si o no)?\n"))   .upper() == "SI":
            sibs = True

        #clear()

        password = password(longitud, minus, mayus, nums, sibs)

        print("Contraseña: " + password + "\n" + "Nivel de contraseña: " + nivelPassword(password) + "\n")

        iEmail = str(input("Introduce un email.\n"))

        iEmail = email(iEmail)

        #clear()

        usu = Usuario(nombre(iNombre), password)

        datos.append(usu)

        if str(input("¿Quiéres introducir otro usuario (si o no)?\n")).upper() == "SI":

          #clear()
          continuar = True

        else:

          #clear()
          continuar = False

for i in datos:
  print(i.nombre)