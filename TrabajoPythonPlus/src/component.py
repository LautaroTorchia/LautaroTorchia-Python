from src.window import build
from src.event_handler import *
import PySimpleGUI as sg

def loop(window):
    "Mantiene la pantalla abierta y captura todos los eventos que ocurren en ella"
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        verDatos()

def start():
    "Inicia la pantalla"
    window=build()
    loop(window)
    window.close()