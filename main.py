from pyexcel_ods import get_data
import datetime
import json

import Excel

# print("\nIngrese en nombre del archivo del supervisor: \n")
# nombreArchivoSupervisor = input()
# archivoSupervisor = get_data(nombreArchivoSupervisor)["Sheet1"]
archivoSupervisor = get_data("planillaJefa.ods")["Sheet1"]
del archivoSupervisor[0]

# print("\nIngrese en nombre de su archivo: \n")
# nombreArchivoUsuario = input()
# archivoUsuario = get_data(nombreArchivoUsuario)["Sheet1"]
archivoUsuario = get_data("ACARAA Junioo.ods")["Sheet1"]
encabezado = archivoUsuario[0]
del archivoUsuario[0]

archivoSalida = []

for filaUsuario in archivoUsuario:
	for filaSupervisor in archivoSupervisor:
		if len(filaUsuario) > 1 and len(filaSupervisor) > 1:
			print(row[2].upper()) #rut


# print(json.dumps(data, default=datetime_handler))