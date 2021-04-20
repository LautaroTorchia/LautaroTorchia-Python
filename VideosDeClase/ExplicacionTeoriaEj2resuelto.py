def actualizando(burbuja):
	cant = int(input('Ingrese cantidad estudiantes '))
	for integrante in range(cant):
		nombre = input('Ingrese nombre del estudiante ')
		burbuja.append(nombre.capitalize())
 
burbuja = ['Ana','María','Juan','Elena']
resp = input('Desea sumar integrantes a la burbuja?. S/N ')
if resp.upper() == 'S':
	actualizando(burbuja) #Solucion simple burbuja(parametro)=burbuja
print(f'La burbuja actualizada quedó integrada por: {burbuja}')