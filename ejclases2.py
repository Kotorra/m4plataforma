# Ejercicio 2: Validación de Edad
# Escribe un programa que solicite al usuario ingresar su edad. El programa debe
# verificar que el usuario ingrese un número entero válido y que este número sea
# positivo.
# Instrucciones:
# 1. Usa try y except para manejar entradas no válidas.
# 2. Si la edad ingresada no es válida o es menor que 0, el programa debe imprimir
# un mensaje de error.

print("SUPER VERIFICADOR DE EDAD")
try:
	edad=int(input("Ingrese su edad: "))
	if edad<0:
		print("Edad no valida.")
	print("Su edad es correcta")
except ValueError:
	print("Debe ingresar números enteros")