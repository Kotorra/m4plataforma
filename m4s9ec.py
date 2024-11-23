print("SCRIPT EJERCICIO M4 S9 EC")
try:

	with open("informacion.dat","w",encoding="utf-8") as Info:
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


print("\n***Parte3***")

with open("informacion.dat","a",encoding="utf-8") as Info:
	Info.write("Hola Mundo\n")
	Info.write("Este en una nueva línea en el archivo\n")
	Info.write("agregando la segunda línea del archivo\n")
	Info.write("finalizando la línea agregada\n")

with open("informacion.dat","r",encoding="utf-8") as Info:
	print(Info.read())

print("\n***Parte 4***")

contador=0
nuevo=""
with open("informacion.dat","r",encoding="utf-8") as Info:
	for linea in Info:
		if "información" in linea:
			contador+=1
		linea=linea.strip()
		linea=linea.replace("información","Procesamiento")
		nuevo+=linea+"\n"

with open("informacion.dat","w",encoding="utf-8") as Info:
	Info.write(nuevo)

print(f"Se realizaron {contador} reemplazos.")

with open("informacion.dat","r",encoding="utf-8") as Info:
	print(Info.read())

