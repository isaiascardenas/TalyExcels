from Excel import Excel

FECHA = 0
RUT = 2
PRODUCTO = 3
ESTADO = 5

# print("\nIngrese en nombre del archivo del supervisor: \n")
# bossFileName = input()
# bossFile = Excel()
# userFile.readFile(bossFileName)
bossFile = Excel()
bossFile.readFile("planillaJefa.ods")

# print("\nIngrese en nombre de su archivo: \n")
# userFileName = input()
# userFile = Excel()
# userFile.readFile(userFileName)
userFile = Excel()
userFile.readFile("ACARAA Junioo.ods")

# data = [["mako", "taly", "pistola","made"],[1,2,3,4],["a","b","c","d"],[0,9,8,7]]
# outFile = Excel()
# outFile.writeFile(data)

for userRow in userFile.rows:
	for bossRow in bossFile.rows:
		if bossRow[RUT] == userRow[RUT]:
			print(bossRow[RUT]) #rut


# print(json.dumps(data, default=datetime_handler))