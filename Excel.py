class Excel:
	def __init__(self, fileName):
        self.rows = get_rows(fileName)["Sheet1"]
        self.customers = []

    def setCustomers():
    	rows = self.rows
    	del rows[0]
    	self.customers = rows[2]

    def getHeader():
    	return self.rows[0]
