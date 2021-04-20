def actualizando(burbuja):
    cant = int(input('Ingrese cantidad estudiantes '))
    for integrante in range(cant):
        nombre = input('Ingrese nombre del estudiante ')
        burbuja.append(nombre)
    print(burbuja)
 
burbuja = ['Ana','María','Juan','Elena']
resp = input('Desea sumar integrantes a la burbuja?. S/N ')
if resp.upper() == 'S':
	actualizando(burbuja[:])  #Error burbuja.copy() burbuja2=burbuja
print(f'La burbuja actualizada quedó integrada por: {burbuja}')


