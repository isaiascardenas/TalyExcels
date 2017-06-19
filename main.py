from Excel import Excel
from Helpers import findChange, isNew, getChange

diferentes = []
faltantes = []

# print("\nIngrese en nombre del archivo del supervisor: \n")
bossFileName = raw_input("\nIngrese en nombre del archivo del supervisor: \n")
# print(bossFileName)
bossFile = Excel()
bossFile.readFile(bossFileName)
# bossFile = Excel()
# bossFile.readFile("planillaJefa.ods")

# print("\nIngrese en nombre de su archivo: \n")
userFileName = raw_input("\nIngrese en nombre de su archivo: \n")
userFile = Excel()
userFile.readFile(userFileName)
# userFile = Excel()
# userFile.readFile("ACARAA Junioo.ods")
userFile.cleanFile()

header = ["FECHA","USUARIO","RUT","PRODUCTO","ESTADO"]
faltantes.append(["Faltantes"])
faltantes.append(header)
diferentes.append(["Diferentes"])
diferentes.append(header)

for bossRow in bossFile.rows:
	if getChange(bossRow, userFile.cleanRows) is not None:
		aux = getChange(bossRow, userFile.cleanRows)
		diferentes.append([aux[0],aux[1],aux[2],aux[3],aux[5]])

for userRow in userFile.cleanRows:
	if isNew(userRow, bossFile.rows):
		aux = userRow
		faltantes.append([aux[0],aux[1],aux[2],aux[3],aux[5]])
faltantes.append([])

outFile = Excel()
outFile.writeFile(faltantes+diferentes)
