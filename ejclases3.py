# Ejercicio 3: Índices en Listas
# Dada una lista de colores, crea un programa que permita al usuario ingresar un índice
# para acceder a un color en la lista. El programa debe manejar errores cuando el índice
# no es válido o está fuera de rango.
# Instrucciones:
# 1. Usa try y except para manejar entradas no válidas y errores de índice.
# 2. El programa debe continuar solicitando un índice hasta que se ingrese uno
# válido.

colores=["Rojo","Azul","Amarillo","Verde","Calipso","Burdeo","Blanco","Negro"]
print("Los colores de la lista son")
for i in colores:
	print(i)

try:
	sel=int(input("Seleccione el color según su orden numerico: "))
	sel=sel-1
	if sel<0:
		print("Ingrese un número positivo")
	else:
		print(f"El color seleccionado es: {colores[sel]}")
except IndexError:
	print("El color seleccionado no existe en la lista, fuera de rango")
	
