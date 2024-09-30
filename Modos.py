import os
from Def import *
from Class import *
from MobsItems import *

'''Monstros'''
Mos = ['Nada','Slime','Snake','Wolf','Gigant wolf','Diana']
''''''



input()
def Campaña():
    os.system('cls' if os.name == 'nt' else 'clear')
    Char = Player('Diana')
    Char = Adjustment(Char)
    Accion = 0
    while Char.Alive:
        # Introducción
        print("""
        Calabozos y Ruinas
        ______________________________________________________________
        Diana, una aventurera se adentra a una mazmorra de estilo
        templo en una montaña al norte de New Harld donde ella afirma
        que hay un tesoro de gran valor, con la misión de saquear el
        tesoro y así lograr obtener el respeto de los pueblerinos y
        aventureros de su pueblo de nacimiento, Gangia, que se
        encontraba al norte de New Harld.
        ______________________________________________________________

        """)
        input('Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

        # Sala uno
        print("""
        SALA 1
        ______________________________________________________________
        Entras a la primera sala, iluminada por tu antorcha y la luz
        del día que entra por la puerta grande del exterior, notas
        rápidamente que no hay nada de valor, solamente antorchas en
        las paredes.
        ______________________________________________________________

        """)
        Char = Rest(Char)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Sala dos
        print("""
        SALA 2
        ______________________________________________________________
        En cuanto pasas a la siguiente sala con la antorcha
        encendida, te percatas de que un slime amenazador está en el
        centro de la habitación. No te queda de otra que acabar con él
        antes de que se convierta en un problema pronto.
        ______________________________________________________________

        """)
        Enemy00,Enemy01,Enemy02 = Mos[1],Mos[0],Mos[0]
        Char = Fight(Enemy00,Enemy01,Enemy02,Char)
        if not Char.Alive:
            break
        print("""
        ______________________________________________________________
        La baba del Slime quedó derramada en el centro de la sala.
        Observas con precaución a tu alrededor y no ves nada más
        que antorchas en las paredes, y dos huecos de puerta grandes.
        ______________________________________________________________
        
        """)
        Char = Rest(Char)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Decisión
        print("""
        DECISIÓN
        ______________________________________________________________
        La sala se divide en dos salas, una a la izquierda y otra a
        la derecha. Ambas salas están muy oscuras como para ver los
        posibles peligros.
        ______________________________________________________________
        
        """)
        while Accion != 1 and Accion != 2:
            try:
                print('(1)Izquierda | (2)Derecha')
                Accion = int(input('>'))
                if Accion != 1 and Accion !=2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(print('Accion erronea.'))
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Accion erronea.')
        os.system('cls' if os.name == 'nt' else 'clear')
        if Accion == 1: 

            # Sala tres izq
            print("""
            SALA 3
            ______________________________________________________________
            Entras en la sala de la izquierda, atenta y te percatas de
            dos slimes: uno en el centro y otro en la esquina en el fondo a la
            derecha. Tienes que luchar contra ellos.
            ______________________________________________________________
            
            """)
            Enemy00,Enemy01,Enemy02 = Mos[1],Mos[1],Mos[0]
            Char = Fight(Enemy00,Enemy01,Enemy02,Char)
            if not Char.Alive:
                break
            print("""
            ____________________________________________________________
            Tan pronto como bajas la guardia, sientes que el frío te abraza,
            cides encender las antorchas de las paredes y revisar unas
            sas de piedra de la sala, pero no encuentras nada de utilidad.
            ____________________________________________________________
            
            """)
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Sala cuarta izq
            print("""
            SALA 4
            ______________________________________________________________
            Desde el hueco de la puerta de la siguiente sala logras ver
            un slime y una serpiente rondando por la sala. También ves unas
            estanterías que parecen vacías, pero primero tienes que matar
            a los monstruos de la sala.
            ______________________________________________________________
            
            """)
            Enemy00,Enemy01,Enemy02 = Mos[1],Mos[2],Mos[0]
            Char = Fight(Enemy00,Enemy01,Enemy02,Char)
            if not Char.Alive:
                break
            print("""
            ______________________________________________________________
            Una vez que acabas con los monstruos, enciendes las antorchas de
            la pared de nuevo y decides ver las estanterías. Otra vez la
            mala suerte sigue y no encuentras nada.
            ______________________________________________________________
            
            """)
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Sala quinta izq
            print("""
            SALA 5
            ______________________________________________________________
            Miras adentro de la sala pero no ves ningún monstruo, así que
            te diriges a encender las antorchas, pero de repente una
            serpiente intenta picarte. Logras evadirla y te percatas de
            un slime muy agresivo en la sala.
            ______________________________________________________________
            
            """)
            Enemy00,Enemy01,Enemy02 = Mos[1],Mos[2],Mos[0]
            Char = Fight(Enemy00,Enemy01,Enemy02,Char)
            if not Char.Alive:
                break
            print("""
            ______________________________________________________________
            Ahora sí, logras encender las antorchas y te calientas en una
            de ellas, ya que el frío de la sala cada vez es más abrazador.
            ______________________________________________________________')

            """)
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            # Sala tres Der
            print("""
            SALA 3
            ______________________________________________________________
            Al entrar por la sala de la derecha, ves a un lobo durmiendo.
            El lobo se despierta y te empieza a gruñir. Decides
            dispararle primero antes de que te ataque.
            ______________________________________________________________
            
            """)
            Enemy00,Enemy01,Enemy02 = Mos[3],Mos[0],Mos[0]
            Char = Fight(Enemy00,Enemy01,Enemy02,Char)
            if not Char.Alive:
                break
            print("""
            ______________________________________________________________
            Tan pronto como bajas la guardia, sientes que el frío te abraza,
            decides encender las antorchas de las paredes y revisar unas
            mesas de piedra de la sala, pero no encuentras nada de utilidad.
            ______________________________________________________________
            
            """)
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')
            # Sala cuarta Der
            print("""
            SALA 4
            ______________________________________________________________
            Desde la puerta, observas dos lobos encima de una mesa en una
            esquina, alertados por la lucha contra el otro lobo.
            Percatándose de tu presencia, decides atacar primero.
            ______________________________________________________________
            
            """)
            Enemy00,Enemy01,Enemy02 = Mos[3],Mos[3],Mos[0]
            Char = Fight(Enemy00,Enemy01,Enemy02,Char)
            if not Char.Alive:
                break
            print("""
            ______________________________________________________________
            Los lobos ya parecen haber muerto y ves que en la sala
            hay mucho pelo de lobo. Piensas que podría ser una
            guarida de lobos. Enciendes las antorchas de la pared y sigues.
            ______________________________________________________________
            
            """)
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Sala quinta Der
            print("""
            SALA 5
            ______________________________________________________________
            Entras en la quinta sala y, tras observar, no ves ningún
            lobo. Emocionadamente corres al otro lado de la sala para
            abrir un cofre. Encuentras una Poción de Vida Menor.
            ______________________________________________________________
            
            """)
            Char.Items.append('Pocion Vida Menor')
            Char = Rest(Char)
            os.system('cls' if os.name == 'nt' else 'clear')

        # Sala Sexta
        print("""
        SALA 6
        ______________________________________________________________
        Entras a la sala que parece ser la unión del otro pasillo,
        pero no tienes mucho tiempo para quedarte mirando porque
        dos lobos y un slime vienen a acabar contigo.
        ______________________________________________________________
        
        """)
        Enemy00,Enemy01,Enemy02 = Mos[3],Mos[3],Mos[1]
        Char = Fight(Enemy00,Enemy01,Enemy02,Char)
        if not Char.Alive:
            break
        print("""
        ______________________________________________________________
        Ya exhausta, decides encender las antorchas y revisar 3 baúles
        que hay en la sala. El primero contenía una Poción de Vida,
        el segundo estaba vacío y el tercero tenía 7 monedas de oro.
        Esto ya empieza a levantar tu ánimo.
        ______________________________________________________________
        
        """)
        Char.Items.append('Pocion Vida')
        Char = Rest(Char)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Sala séptima
        print("""
        SALA 7
        ______________________________________________________________
        Antes de entrar a la sala, escuchas un aullido de lobo muy fuerte.
        Aun así, entras y enseguida un lobo enorme de piel blanca se te
        abalanza.
        ______________________________________________________________
        
        """)
        Enemy00,Enemy01,Enemy02 = Mos[4],Mos[0],Mos[0]
        Char = Fight(Enemy00,Enemy01,Enemy02,Char)
        if not Char.Alive:
            break
        print("""
        ______________________________________________________________
        Acabas con el gran lobo de piel blanca y decides quitarle un
        colmillo para mostrárselo a los demás. Mientras le sacas el 
        colmillo, te das cuenta de que esta es la última sala, así que 
        terminas de sacar el colmillo y decides revisar la sala.
        Revisas estanterías, librerías, una mesa grande en el centro y
        unos baúles, encontrando muchos tesoros valuados en 125 monedas
        de oro, lo cual es mucho para esa época. Estabas tan emocionada que
        no te das cuenta hasta ahora del horrible olor de la sala,
        debido a los cadáveres muertos por el Gran Lobo Blanco. Por lo
        cual decides irte victoriosa.
        ______________________________________________________________
        
        """)
        Char = Rest(Char)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("¡Victoria! La aventura ha llegado a su fin con gloria y tesoros.")
        print('Creado por DiMarvi')
        print('')
        input
        break
    print("Fin de la aventura")
    input()

def Editor():
    os.system('cls' if os.name == 'nt' else 'clear')
    Enemies = ['','','']
    Accion = 0
    # Personaje
    while Accion != 1 and Accion !=2:
        try:
            print("""
        Elige el personaje
        (1)Diana | (2) Mark
            """)
            Accion = int(input('> '))
            if Accion == 1:
                Char = Player('Diana')
                Char.Lv = int(input('Nivel: '))
            elif Accion == 2:
                Char = Player('Mark')
                Char.Lv = int(input('Nivel: '))
            else:
                print('Accion erronea')
        except:
            print('Accion erronea')
    Char = Adjustment(Char)
    # Mostruos
    for i in range(3):
        Accion = -1
        while Accion < 0 or Accion > len(Mos)-1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Seleccione su monstruo numero {i+1}/3')
            for j,Mo in enumerate(Mos):
                print(f'({j}) {Mo}', end=" ")
            try:
                Accion = int(input('>'))
                
            except:
                print('Accion erronea')
        Enemies[i] = Mos[Accion]
    Enemy00,Enemy01,Enemy02 = Enemies[0],Enemies[1],Enemies[2]
    # Pelea
    Char = Fight(Enemy00,Enemy01,Enemy02,Char)
    print("Fin de la pelea")
    input()
