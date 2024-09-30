from Modos import *
import os

Accion = 0
while Accion != 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    Accion = 0
    try:
        print("""
                CALABOZOS Y RUINAS
(1) Campaña    
(2) Editor    
(3) Salir
                                Alpha 0.1
        """)
        Accion = int(input('> '))
        if Accion == 1:
            Campaña()
        elif Accion == 2:
            Editor()
        elif Accion == 3:
            input('Gracias por jugar')
        else:
            print('Accion erronea') 
    except:
        print('Accion erronea')
