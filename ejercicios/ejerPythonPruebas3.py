#https://www.w3schools.com/python/python_mysql_insert.asp
def cnn():
	import pymysql

	cnn = pymysql.connect("db4free.net","solilnone","ALEXsandro100","solilnone" )

	return cnn

def idRandom(rango = 0):
	import random

	abcDario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','1','2','3','4','5','6','7','8','9','0']
	
	idRandom = ""

	i = rango
	while i > 0:
		idRandom += abcDario[random.randrange(0, 35)]
		i -= 1

	return idRandom

"""
cnn = cnn()
select = cnn.cursor()
select.execute("SELECT VERSION()")
data = select.fetchone()
cnn.close()
"""

cnn = cnn()

sql = "INSERT INTO PRUEBAS(id, nick) VALUES(%s, %s);"
val = [
	(idRandom(20), "Solil"),
	(idRandom(20), "Ivanox556"),
	(idRandom(20), "LaPechaNegra"),
	(idRandom(20), "ReyDelfin"),
	(idRandom(20), "CarlosX97")
	]

cnn.cursor().executemany(sql, val)
cnn.commit()
cnn.close()