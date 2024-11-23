# Ejercicio 6: Raíces Cuadradas de una Lista
# Crea un programa que solicite al usuario ingresar una lista de números separados por
# comas y calcule la raíz cuadrada de cada número. El programa debe manejar entradas no
# válidas y también debe manejar números negativos (dado que no se puede calcular la
# raíz cuadrada de un número negativo sin complejos).
# Instrucciones:
# 1. Usa try y except para manejar números no válidos o negativos.
# 2. Si el usuario ingresa un número negativo, se debe imprimir un mensaje de error.
from math import sqrt
print("SUPER CALCULADORA DE RAÍCES CUADRADAS.")

numeros=input("Ingrese una lista de números separadas por comas: ")

numeros=numeros.split(",")

for i in numeros:
	try:
		i=float(i)
		print(f"La raíz cuadrada de {i} es {sqrt(i)}")
	except ValueError:
		print("Entrada incorrecta, el programa continuará con el siguiente elemento.")