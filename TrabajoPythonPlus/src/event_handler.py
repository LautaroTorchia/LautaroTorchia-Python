import os
import csv
import json

#Funcion que manda al JSON
def mandar_a_json(iterator):
    """Esta funcion, toma la lista de entrada(cualquiera sea el boton que fue seleccionado) y la convierte a un objeto
    en formato JSON, para luego depositarla en un archivo.json(el cual tiene el nombre puesto dinamicamente con las keys
    con formato: key1_key2.json"""
    item=iterator[0]
    key_list=list(item.keys()) #Consigo las keys para poder generalizar el metodo para todos los archivos y asi no tener que reescribir codigo
    print(key_list)
    
    with open(f"{key_list[0]}_{key_list[1]}.json","w") as info_json:
        json_list=[]
        for item in iterator:
            json_list.append({key:item[key]
                for key in key_list
                    })
        json.dump(json_list, info_json, indent=4)
        print("Se ha realizado el json con exito!")
   
   
   
        
#Funciones para el boton1
def boton_paises_criterio_1(event):
    """ Esta funcion itera el archivo CSV de paises y lo lleva a una lista con los datos en los cuales se interesa hacer el analisis, que en
    este caso son los nombres de los paises(para devolver un valor) y la poblacion de ellos,todo esto con 
    la funcion map de Python, luego se manda a la funcion que los transforma en un json esta misma lista 
    ordenada de mayor a menor por Poblacion(cortando los 20 elementos con mayor poblacion asi nos queda acotada a
    ese rango"""
    
    if event=="-CHOOSE DATASET1-":
        with open(os.path.join(os.getcwd(),f'TrabajoPythonPlus{os.sep}datasets{os.sep}countries.csv')) as info_paises:
            csv_reader=csv.reader(info_paises,delimiter=",")
            next(csv_reader) #Salteamos el encabezado
            lista_paises=(list(map(lambda x:{"Country":x[0],"Population":int(x[2])},csv_reader))) #Conseguimos los datos que nos interesan( poblacion y nombre del pais)
            
            mandar_a_json((sorted(lista_paises,key=lambda x:x["Population"],reverse=True))[:20]) #Mandamos los 20 paises mas grandes
            




#Funciones para el boton2
def chequear_mortalidad(x):
    """ Esta funcion chequea que el dato de la mortalidad cada 1000 nacimientos este escrita correctamente, ya que en el csv muchos datos
    contienen el numero flotante con , cuando python permite solo con .  por lo cual realizo el cambio para que el dato quede correcto,
    luego esta funcion es llevada a la siguiente funcion en el metodo map"""
    
    try:
        return {"Country":x[0],"Mortality":float(x[7].replace(",","."))}
    except ValueError:
        return {"Country":x[0],"Mortality":0}

def boton_paises_criterio_2(event):
    """Esta funcion permite en el caso de tocar el segundo boton de la aplicacion iterar de nuevo el archivo csv de paises y luego
    mandar a una lista con la funcion map todos los elementos, con sus campos nombre(country) y su campo(Mortality) o mortalidad,
    luego mando a la funcion que los deposita en un json ordenandolos de mayor a menor mortalidad, dejando solo los 20 paises con mayor
    mortalidad"""
    
    if event=="-CHOOSE DATASET1 VERSION2-":
        with open(os.path.join(os.getcwd(),f'TrabajoPythonPlus{os.sep}datasets{os.sep}countries.csv')) as info_paises:
            csv_reader=csv.reader(info_paises,delimiter=",")
            next(csv_reader) #Salteamos el encabezado
            lista_paises=(list(map(chequear_mortalidad,csv_reader)))
            
            mandar_a_json((sorted(lista_paises,key=lambda x:x["Mortality"],reverse=True))[:20]) #Mandamos los 20 paises con mayor mortalidad


def boton_3_criterio_1(event):
    """Esta funcion permite que en el caso de que se utilice el boton 3, se itere el archivo csv de felicidad y consiga una lista con
    2 items especificos que son el nombre del pais y su score de felicidad para luego mandarlo a un archivo json cortando los 10 
    paises con mayor felicidad del mundo"""
    
    if event=="-CHOOSE DATASET2-":
        with open(os.path.join(os.getcwd(),f'TrabajoPythonPlus{os.sep}datasets{os.sep}world-happiness-report.csv')) as info_Happiness:
            csv_reader=csv.reader(info_Happiness,delimiter=",")
            next(csv_reader) #Salteamos el encabezado
            lista_happiness=(list(map(lambda x:{"Country":x[0],"Happines score":float(x[4])},csv_reader)))
            
            mandar_a_json((sorted(lista_happiness,key=lambda x:x["Happines score"],reverse=True))[:10]) #Mandamos los 10 paises mas felices