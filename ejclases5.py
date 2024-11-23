# Ejercicio 5: Cálculo de Promedio
# Escribe un programa que solicite al usuario ingresar una lista de números separados
# por comas y luego calcule el promedio. El programa debe manejar entradas no válidas.
# Instrucciones:
# 1. Usa try y except para manejar errores si el usuario no ingresa números
# válidos.
# 2. El programa debe seguir solicitando la lista hasta que el usuario ingrese
# números correctamente.

print("SUPER CALCULADOR DE PROMEDIO")
sumatoria=0
while True:
	try:
		numeros=input("Ingrese las notas separadas por comas(,), los decimales se indican con punto: ")

		numeros=numeros.split(",")
		for i in range(len(numeros)):
			numeros[i]=float(numeros[i])
		break
	except ValueError:
		print("Sólo se debe ingresar números")

for i in numeros:
	sumatoria+=i

promedio=sumatoria/(len(numeros))

print(f "El promedio es {promedio}")