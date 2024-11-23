
while True:
	try:
		edad=int(input("Ingrese edad en años: "))
		if edad>=18:
			print("Adulto")
		else:
			print("No adulto")
		break
	except ValueError:
		print("Ingrese un número válido.")
