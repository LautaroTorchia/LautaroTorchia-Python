import csv
import requests

def incisos(reader):
    lista_calificaciones=[]
    for info_app in reader:
        if "ES" in info_app[12].split(", ") and "0"==info_app[7]: #Disponibles En Español y son gratuitos
            print("El siguiente juego se encuentra gratis en español: ",info_app[2])
        #Comienza Inciso2
        try:
            lista_calificaciones.append((int(info_app[6]),info_app[4],info_app[2]))
        except ValueError:
            pass
            
    lista_calificaciones.sort(reverse=True,key=lambda x: x[0])
    return(lista_calificaciones[:10])

    
with open('appstore_games.csv','r') as appstore_info:
    print(appstore_info)
    csv_reader=csv.reader(appstore_info,delimiter=",")
    next(csv_reader) #Descarta el encabezado de la busqueda
    lista_para_imprimir_iconos=incisos(csv_reader)
    print()
    for e in lista_para_imprimir_iconos:
        juego = e[2]
        icon_url = e[1]
        icono = requests.get(icon_url)
        try:
            with open(f'{juego}.jpg', 'wb') as f:
                 f.write(icono.content) 
        except FileNotFoundError:
            print(f"No se pudo encontrar el Url para traer la imagen {juego} ")
                 