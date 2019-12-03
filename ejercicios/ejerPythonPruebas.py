class Persona:
	id = 0
	name = ""
	age = 0
	email = ""
	password = ""
	juegos = []

	def __init__(self, id, name, age, email, password):
		self.id = id
		self.name = name
		self.age = age
		self.email = email
		self.password = password

	def setJuegos(self, juegos):
			self.juegos = juegos

class Juego:
	name = ""
	price = 0
	persona = []

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def setPersona(self, persona):
		self.persona = persona

p1 = Persona(1, "Alex", 21, "alex@gmail.com", "admin")
p2 = Persona(3, "Pepe", 25, "pepe@gmail.com", "pepe")
juegos = [Juego("LOL", 0), Juego("Forza Horizon 4", 39.99)]
p1.setJuegos(juegos)
personas = [p1, p2]

def login(email = "", password = ""):

	idLogin = 0

	for i in personas:

		if email == i.email and password == i.password:

			idLogin = i.id

	return idLogin

idLogin = login("pepe@gmail.com", "pepe")

for i in personas:
	if i.id == idLogin:
		print("Tienes:", len(i.juegos), "juegos.")