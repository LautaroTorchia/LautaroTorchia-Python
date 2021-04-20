y = 9 #Variable Global

def prueba1():
	def prueba2():
		y = y + 1 #Encontramos el error nonvalue+1=?
		print (y)
	y = 5
	prueba2()
 
 
prueba1()
