print("SCRIPT EJERCICIO M4 S8 EC")
try:

	with open("informacion.dat","x",encoding="utf-8",newline="") as Info:
		print("Archivo creado.")
		for i in range(1,6):
			Info.write(f"Datos de información en la linea {i}\n")
except FileExistsError:
	print("Archivo ya existe.")
