# Ejercicio 1: Calculadora de Operaciones Básicas
# Crea un programa que permita al usuario ingresar dos números y una operación (suma,
# resta, multiplicación, división). El programa debe manejar los casos en los que el
# usuario ingresa valores no numéricos o intenta dividir por cero.
# Instrucciones:
# 1. El programa debe solicitar dos números y una operación.
# 2. Usa try y except para manejar la entrada de datos y posibles errores de
# división por cero.

def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def mult(a,b):
	return a*b

def div(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		print("La división por cero tiene por resultado 'Indeterminado'")

print("Ingresa que operacion quieres hacer.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.División")
opcion=input("Opción elegida: ")

while True:
	try:
		a=int(input("Ingresa el primer numero: "))
		b=int(input("Ingresa el segundo numero: "))
		break
	except ValueError:
		print("Ingresa números válidos")

if opcion=="1":
	print(f"El resultado de la suma es {suma(a,b)}")
if opcion=="2":
	print(f"El resultado de la resta es {resta(a,b)}")
if opcion=="3":
	print(f"El resultado de la Multiplicacion es {mult(a,b)}")
if opcion=="4":
	print(f"El resultado de la división es {div(a,b)}")
else:
	print("CUEK")
