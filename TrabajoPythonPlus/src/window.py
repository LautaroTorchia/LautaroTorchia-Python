import PySimpleGUI as sg

def build():
    SIZE=(30,5)
    "Esta funcion diseña el layout de la pantalla para el ejercicio"
    
    layout=[
        [sg.Text("Que datos analizamos?",font=("Helvetica", 30),justification="center",text_color="blue")],
        [sg.Button("Paises por Poblacion",key="-CHOOSE DATASET1-",size=SIZE,pad=(1,10))],
        [sg.Button("Paises por Costa",key="-CHOOSE DATASET1 VERSION2-",size=SIZE,pad=(1,10))],
        [sg.Button("Dataset2",key="-CHOOSE DATASET2-",size=SIZE)],
        [sg.Button("Salir",key="-EXIT-",size=SIZE,pad=(1,60))]
    ]

    window = sg.Window("Analsis de Datasets",
                                layout,
                                finalize="true",
                                size=(500, 700),
                                element_justification='center',
                                margins=(10,10))
    
    return window