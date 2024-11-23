
class RangoSalarioError(Exception):
	def __init__(self):
		super().__init__("Salario no está definido en el rango (1000 a 2000)")

salario=int(input("Ingrese el salario: "))

if salario<1000 or salario>2000:
	raise RangoSalarioError()
else:
	print("Salario correcto")