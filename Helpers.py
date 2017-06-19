FECHA = 0
RUT = 2
PRODUCTO = 3
ESTADO_USER = 5
ESTADO_BOSS = 4

def findChange(bossRow, userRows):
	for row in userRows:
		if row[RUT] == bossRow[RUT]:
			if row[PRODUCTO] == bossRow[PRODUCTO] and row[ESTADO_USER] == bossRow[ESTADO_BOSS]:
				return False
	return True

def getChange(bossRow, userRows):
	for row in userRows:
		if row[RUT] == bossRow[RUT]:
			if row[PRODUCTO] == bossRow[PRODUCTO] and row[ESTADO_USER] != bossRow[ESTADO_BOSS]:
				return row

def isNew(userRow, bossRows):
	for row in bossRows:
		if row[RUT] == userRow[RUT]:
			if row[PRODUCTO] == userRow[PRODUCTO]:
				return False
	return True			