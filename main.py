from Excel import Excel
from Helpers import findChange, isNew, getChange

done = False

while not done:
	diferentes = []
	faltantes = []

	bossFileName = raw_input("\nIngrese el nombre del archivo del supervisor: \n")
	bossFile = Excel()
	done = bossFile.readFile(bossFileName)


	if  done:
		# bossFile = Excel()
		# bossFile.readFile("jefa.ods")

		userFileName = raw_input("\nIngrese el nombre de su archivo: \n")
		userFile = Excel()
		done = userFile.readFile(userFileName)
		# userFile = Excel()
		# userFile.readFile("taly.ods")
		userFile.cleanFile()

header = ["FECHA","USUARIO","RUT","PRODUCTO","ESTADO"]
faltantes.append(["Faltantes"])
faltantes.append(header)
diferentes.append(["Diferentes"])
diferentes.append(header)

for bossRow in bossFile.rows:
	if getChange(bossRow, userFile.cleanRows) is not None:
		aux = getChange(bossRow, userFile.cleanRows)
		aux[0] = str(aux[0])
		diferentes.append([aux[0],aux[1],aux[2],aux[3],aux[5]])

for userRow in userFile.cleanRows:
	if isNew(userRow, bossFile.rows):
		aux = userRow
		aux[0] = str(aux[0])
		faltantes.append([aux[0],aux[1],aux[2],aux[3],aux[5]])
faltantes.append([])

outFile = Excel()
outFile.writeFile(faltantes+diferentes)
