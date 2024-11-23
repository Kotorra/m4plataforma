print("SCRIPT EJERCICIO M4 S9 EC")
try:

	with open("informacion.dat","x",encoding="utf-8") as Info:
		print("Archivo creado.")
		for i in range(1,6):
			Info.write(f"Datos de información en la linea {i}\n")
except FileExistsError:
	print("Archivo ya existe.")

print("\n***PARTE 2***\n")

try:

	with open("informacion.dat","x",encoding="utf-8") as Info:
		print("Archivo creado nuevamente.")

except FileExistsError:

	print("El archivo informacion.dat ya existe, ha sido creado previamente")
	with open("informacion.dat","r",encoding="utf-8") as Info:
		datos=Info.read()
	print(datos)


