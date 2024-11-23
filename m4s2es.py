class Persona():
	def __init__(self,nombre,apellido,genero,edad,estatura,peso):
		self.__nombre=nombre
		self.__apellido=apellido
		self.__genero=genero
		self.__edad=edad
		self.__estatura=estatura
		self.__peso=peso

	def get_nombre(self):
		return self.__nombre

	def get_apellido(self):
		return self.__apellido

	def get_genero(self):
		return self.__genero

	def get_edad(self):
		return self.__edad

	def get_estatura(self):
		return self.__estatura

	def get_peso(self):
		return self.__peso

	def set_nombre(self,nombre):
		aux=self.get_nombre()
		self.__nombre=nombre
		print(f"El nombre cambio de {aux} a {nombre}")

	def set_apellido(self,apellido):
		aux=self.get_apellido()
		self.__apellido=apellido
		print(f"El apellido de {self.get_nombre()} cambio de {aux} a {apellido}")

	def set_genero(self,genero):
		aux=self.get_genero()
		self.__genero=genero
		print(f"El género de {self.get_nombre()} cambio de {aux} a {genero}")

	def set_edad(self,edad):
		aux=self.get_edad()
		self.__edad=edad
		print(f"La edad de {self.get_nombre()} cambio de {aux} a {edad}")

	def set_estatura(self,estatura):
		aux=self.get_estatura()
		self.__estatura=estatura
		print(f"La estatura de {self.get_nombre()} cambio de {aux} a {estatura}")

	def set_peso(self,peso):
		aux=self.get_peso()
		self.__peso=peso
		print(f"El peso de {self.get_nombre()} cambio de {aux} a {nombre}")

Persona_1=Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg")
Persona_2=Persona("Juan", "Camargo", "Masculino","18 años", "1.8 mts", "75 Kg")

Persona_1.set_edad("21 años")
Persona_2.set_apellido("Santiago")
