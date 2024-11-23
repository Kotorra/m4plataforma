usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
id_usuario = '004'

try:
	print(usuarios[id_usuario])

except KeyError:

	print(f"La clave {id_usuario} no está en el diccionario. Agregando clave...")
	usuarios[id_usuario]="Ninguno"
	print(usuarios)