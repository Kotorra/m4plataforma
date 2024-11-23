from datetime import datetime
fechaSalida="01/01/2025"


fechaSalida = datetime.strptime(fechaSalida, "%d/%m/%Y")
fechaValidar=fechaSalida.strftime("%Y%m%d")
fechaValidar=int(fechaValidar)
fechaHoy=datetime.today().strftime("%Y%m%d")
fechaHoy=int(fechaHoy)

print(fechaValidar)
print(fechaHoy)