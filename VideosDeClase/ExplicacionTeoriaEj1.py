y=9

def prueba1():
    
    def prueba2():
        nonlocal y #Al referenciarla como nonlocal, permite que la variable y=5 sea accedida
        y= y+1
        print(y)
    y=5 
    prueba2()


prueba1()