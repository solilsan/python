def ejer1():

    class Alumno:

        nombre = ""
        apellido = ""
        nota = 0.0

        def __init__(self, nombre, apellido, nota):
            self.nombre = nombre
            self.apellido = apellido
            self.nota = nota

        def setNombre(self, nombre):
            self.nombre = nombre

        def setApellido(self, apellido):
            self.apellido = apellido

        def setNota(self, nota):
            self.nota = nota

        def getNombre(self):
            return self.nombre

        def getApellido(self):
            return self.apellido

        def getNota(self):
            return self.nota

        def getAprobado(self):

            if self.nota >= 5:
                return True
            else:
                return False

    alumno = Alumno("Alex","Ruiz", 8.5)

    print(alumno.getAprobado())

def ejer2():

    class Triangulo:

        vertice1 = 0.0
        vertice2 = 0.0
        vertice3 = 0.0

        def __init__(self, vertice1, vertice2, vertice3):

            self.vertice1 = vertice1
            self.vertice2 = vertice2
            self.vertice3 = vertice3


        def getTipoTriangulo(self):

            if self.vertice1 == self.vertice2 and self.vertice2 == self.vertice3:

                return "Equilátero"

            elif self.vertice1 != self.vertice2 and self.vertice2 != self.vertice3:

                return "Escaleno"

            else:

                return "Isóceles"


        def getPerimetro(self):

            return self.vertice1+self.vertice2+self.vertice3


        def getArea(self):

            return (self.vertice1+self.vertice2+self.vertice3) / 2


    triangulo = Triangulo(11, 11, 11)

    print(triangulo.getTipoTriangulo(), end="\n")
    print(triangulo.getPerimetro(), end="\n")
    print(triangulo.getArea())


def ejer3():

    class Calculadora:

        digito1 = 0.0
        digito2 = 0.0


        def __init__(self, digito1, digito2):

            self.digito1 = float(digito1)
            self.digito2 = float(digito2)


        def getSuma(self):

            return self.digito1 + self.digito2


        def getResta(self):

            return self.digito1 - self.digito2


        def getMultiplicacion(self):

            return self.digito1 * self.digito2


        def getDivision(self):

            if self.digito2 == 0:

                return "No se puede dividir entre 0"

            else:

                return self.digito1 / self.digito2


        def __str__(self):

            print(str(self.digito1), " + ", str(self.digito2), "=", str(self.getSuma()), "\n"
                  + str(self.digito1), " - ", str(self.digito2), "=", str(self.getResta()), "\n"
                  + str(self.digito1), " x ", str(self.digito2), "=", str(self.getMultiplicacion()), "\n"
                  + str(self.digito1), " / ", str(self.digito2) + "=", str(self.getDivision()))

    digito1 = input("Primer digito.\n")
    digito2 = input("Segundo digito.\n")

    calculadora = Calculadora(digito1, digito2)

    calculadora.__str__()

ejer3()