class Persona():
	def __init__(self,nombre):
		self.nombre=nombre

	def Movimiento(self):
		self.estado="Caminando"
		print(f"La persona {self.nombre} está {self.estado}")

class Maratonista(Persona):
	def Movimiento(self):
		self.estado="Trotando"
		print(f"El Maratonista {self.nombre} está {self.estado}")

class Ciclista(Persona):
	def Movimiento(self):
		self.estado="Rodando"
		print(f"La ciclista {self.nombre} está {self.estado}")

Persona1=Persona("Canelita")
Maratonista1=Maratonista("Ramón")
Ciclista1=Ciclista("Pascuala")

def Move(instancia):
	instancia.Movimiento()

Move(Persona1)
Move(Maratonista1)
Move(Ciclista1)
