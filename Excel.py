from pyexcel_ods import get_data, save_data

class Excel:
	def __init__(self):
		self.fileName = ""
		self.rows = []
		self.customers = []
		self.cleanRows = []

	def readFile(self, fileName):
		try:
			rows = get_data(fileName)["Sheet1"]
			for i in range(0,len(rows)):
				if len(rows[i]) > 1:
					rows[i][2] = rows[i][2].upper()
					rows[i][3] = rows[i][3].upper()
					self.rows.append(rows[i])
			return True

		except Exception as e:
			print("\n\nNo es posible leer el archivo, asegurese de que el nombre del archivo sea correcto\n")
			return False

	def cleanFile(self):
		rows = self.rows
		for i in range(0, len(rows)):
			if len(rows[i][3]) != 0:
				self.cleanRows.append(rows[i])


	def setCustomers(self):
		rows = self.rows
		del rows[0]
		self.customers = rows[2]

	def getHeader(self):
		return self.rows[0]

	def writeFile(self, data):
		self.fileName = "Resultado.ods"
		outFile = dict()
		outFile.update({"Sheet 1": data})
		save_data(self.fileName, outFile)
