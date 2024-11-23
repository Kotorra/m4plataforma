suma = 3000
contador = 0
resultado=None

try:
	resultado=suma/contador
	print("El resultado es",resultado,".")

except ZeroDivisionError:
	print("División por cero.")
