from dataclasses import dataclass

try:
	with open("pruebas.txt", "x", encoding="utf-8") as Archivo:
		pass
except FileExistsError:
	print("Archivo Encontrado.")

lista=["a","b","c","d"]

@dataclass
class Producto():
	codigo: str
	nombre: str
	precio: float
	cantidad: int

	def __str__(self):
		return f"El código del producto es {self.codigo}, nombre {self.nombre},\
	precio ${self.precio}.\nCantidad disponible:{self.cantidad}"

@dataclass
class Libro(Producto):
	pass
# with open("pruebas.txt","a",encoding="utf-8") as Archivo:
# 	pass

producto=Producto("XD","XD",34.3,2)
producto1=Libro("XD","XD",34.3,2)

lista1=[producto,producto1]

with open("pruebas.txt", "w", encoding="utf-8") as Archivo:
	Archivo.write("")
for i in lista1:
	if i.__class__.__name__=="Producto":
		string=(f"PRODUCTO;{i.codigo};{i.nombre};{i.precio};{i.cantidad};\n")

	elif i.__class__.__name__=="Libro":
		string=(f"LIBRO;{i.codigo};{i.nombre};{i.precio};{i.cantidad};\n")
	with open("pruebas.txt", "a", encoding="utf-8") as Archivo:
		Archivo.write(string)

lista3=[]
with open("pruebas.txt","r", encoding="utf-8") as Archivo:
	lineas=Archivo.readlines()
	for i in lineas:
		elementos=i.split(";")
		if elementos[0]=="PRODUCTO":
			producto=Producto(elementos[1],elementos[2],elementos[3],elementos[4])
			lista3.append(producto)
		elif elementos[0]=="LIBRO":
			libro=Libro(elementos[1],elementos[2],elementos[3],elementos[4])
			lista3.append(libro)
		else:
			pass

print(lista3)




