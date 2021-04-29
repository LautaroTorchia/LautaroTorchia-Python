from src.window import build
from src.event_handler import *
import PySimpleGUI as sg

def loop(window):
    "Mantiene la pantalla abierta y captura todos los eventos que ocurren en ella"
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="-EXIT-":
            break
        boton_paises_criterio_1(event)  #Utiliza dataset1(rank por poblacion)
        boton_paises_criterio_2(event)  #Utiliza dataset1(rank por mortalidad)
        boton_3_criterio_1(event)  #Utiliza dataset2(rank por cantidad de descargas)

def start():
    "Inicia la pantalla"
    window=build()
    loop(window)
    window.close()