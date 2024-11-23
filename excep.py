class NuestraExcepcion(Exception):
	def __init__(self, message):
		super().__init__(message)
class NumeroFormatoExcepcion(Exception):
	def __init__(self, message, value):
		message = f'{value} no es un número'
		super().__init__(message)
message = "Se ha generado una excepción."

def division_entera(x,y):
	if type(x) != int:
		raise NumeroFormatoExcepcion(message, x)
	elif type(y) != int:
		raise NumeroFormatoExcepcion(message, y)
	elif y == 0:
		raise NuestraExcepcion(message)
	else:
		dividendo = int(x)
		divisor = int(y)
		return dividendo/divisor
try:
	resultado = division_entera(11, 'q')
	print(resultado)
except NuestraExcepcion:
	print('Error en división por 0')

except NumeroFormatoExcepcion as e:
	print(e)