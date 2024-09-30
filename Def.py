import os
import random
from Class import *
from MobsItems import *

def Adjustment(Char):
    if Char.Lv > 1:
        for i in range(2,Char.Lv+1):
            Char.MaxHealth += i
            Char.Attack += 1
        if Char.Xp <= (2**(Char.Lv-1))*4:
            Char.Xp = (2**(Char.Lv-1))*4
    else:
        Char.Lv = 1
    while Char.Xp >= (2**Char.Lv)*4:
        Char.Lv += 1
        Char.MaxHealth += Char.Lv
        Char.Attack += 1
    Char = Equip(Char)
    Char.Health = Char.MaxHealth
    return Char

def Experience(Char):
    while Char.Xp >= (2**Char.Lv)*4:
        os.system('cls' if os.name == 'nt' else 'clear')
        Char.Lv += 1
        print(' Has subido de Nivel')
        print(f'Tu Vida Maxima a aumentado en {Char.Lv}')
        print(f'Tu Ataque a aumentado en 1')
        Char.MaxHealth += Char.Lv
        Char.Attack += 1
        input('Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
    if Char.Xp < (2**Char.Lv)*4:
        print(f'Has conseguido {Char.Xp}/{(2**Char.Lv)*4} de experiencia')
        input('Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
    return Char

def Pocion_hp(Char,Pot):
    os.system('cls' if os.name == 'nt' else 'clear')
    if Char.Health <= (Char.MaxHealth-Pot) :
        Char.Health += Pot
    else:
        Char.Health = Char.MaxHealth
    print('Se ha usado Vida menor')
    print(f'+{Pot} de Vida ')
    return Char

def Dano(Attacker,Target):
    Is_Crit = random.random() < Attacker.ProbCrit
    Att = Attacker.Attack + Attacker.Weapon.Damage
    if Is_Crit:
        Att *= 1.5
    if Att <= Target.Defence:
        print(f'{Target.Name} ha absorvido todo el daño')
    else:
        Att -= Target.Defence
        Target.Health -= Att
        if Is_Crit:
            print(f'¡Golpe crítico! {Target.Name} ha recibido {Att} de daño.')
        else:
            print(f'{Target.Name} ha recibido {Att} de daño')
    return Target

def Item_use(Char):
    '''Items'''
    Pocion00 = 15
    Pocion01 = 30
    ''''''
    Accion = 0
    if not Char.Items:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('No tienes objetos')
    else:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            for i, objeto in enumerate(Char.Items, 1):
                print(f'({i}){objeto}')
            print(f'({len(Char.Items)+1})Salir')
            SubAccion = int(input('>'))
            SubAccion -= 1
            if Char.Items[SubAccion] == 'Pocion Vida Menor':
                Char = Pocion_hp(Char,Pocion00)
                del Char.Items[SubAccion]
            elif Char.Items[SubAccion] == 'Pocion Vida':
                Char = Pocion_hp(Char,Pocion01)
                del Char.Items[SubAccion]
            if 0 >= SubAccion and SubAccion <= len(Char.Items):
                Accion = 1
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No se puede hacer nada')
    return Char, Accion

def Rest(Char):
    Next = False
    while not Next :
        try:
            print('(1)Continuar | (2)objetos | (3)Stats')
            Accion = int(input('>'))
            if Accion == 1:
                Next = True
            elif Accion == 2:
                Char, Accion = Item_use(Char)
            elif Accion == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f' {Char.Name} Lv: {Char.Lv}')
                print(f'Xp: {Char.Xp}/{(2**Char.Lv)*4}')
                print(f'Ataque: {Char.Attack+Char.Weapon.Damage}')
                print(f'Vida: {Char.Health}/{Char.MaxHealth}')
                print(f'Defenza: {Char.Defence}')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Accion erronea.')
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('accion erronea')
    return Char

def Fight(Enemy00,Enemy01,Enemy02,Char):
    Ms0 = Enemy(Enemy00)
    Ms1 = Enemy(Enemy01)
    Ms2 = Enemy(Enemy02)
    Ms0.Health = Ms0.MaxHealth
    Ms1.Health = Ms1.MaxHealth
    Ms2.Health = Ms2.MaxHealth
    Accion = 0
    while (Ms0.Alive) or (Ms1.Alive) or (Ms2.Alive):
        input('Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f' Turno de {Char.Name}')
        while Accion != 1:
            try:
                print(f'Vida: {Char.Health}/{Char.MaxHealth}Hp')
                print('(1)Atacar | (2)objetos | (3)Nada')
                Accion = int(input('>'))
                os.system('cls' if os.name == 'nt' else 'clear')
                if Accion == 1:
                    if Ms0.Alive:
                        print(f'(1){Ms0.Name} {Ms0.Health}/{Ms0.MaxHealth}Hp |', end=" ")
                    if Ms1.Alive:
                        print(f'(2){Ms1.Name} {Ms1.Health}/{Ms1.MaxHealth}Hp |', end=" ")
                    if Ms2.Alive:
                        print(f'(3){Ms2.Name} {Ms2.Health}/{Ms2.MaxHealth}Hp |')
                    SubAccion = int(input('>'))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'  Turno de {Char.Name}')
                    if SubAccion == 1 and Ms0.Alive:
                        print(f'{Char.Name} usa {Char.Weapon.Name}')
                        Ms0 = Dano(Char,Ms0)
                        print('')
                    elif SubAccion == 2 and Ms1.Alive:
                        print(f'{Char.Name} usa {Char.Weapon.Name}')
                        Ms1 = Dano(Char,Ms1)
                        print('')
                    elif SubAccion == 3 and Ms2.Alive:
                        print(f'{Char.Name} usa {Char.Weapon.Name}')
                        Ms2 = Dano(Char,Ms2)
                        print('')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Accion erronea.')
                        Accion = 0
                elif Accion == 2:
                    Char, Accion = Item_use(Char)
                elif Accion == 3:
                    Accion = 1
                    print('No haces nada')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Accion erronea.')
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Accion erronea.')
                Accion = 0
        Accion = 0
        if Ms0.Alive and Ms0.Health <= 0:
            print(f'{Ms0.Name} derrotado')
            Char.Xp += Ms0.MsXp
            Ms0.Alive = False
            print('')
        if Ms1.Alive and Ms1.Health <= 0:
            print(f'{Ms1.Name} derrotado')
            Char.Xp += Ms1.MsXp
            Ms1.Alive = False
            print('')
        if Ms2.Alive and Ms2.Health <= 0:
            print(f'{Ms2.Name} derrotado')
            Char.Xp += Ms2.MsXp
            Ms2.Alive = False
            print('')
        input('Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
        if Ms0.Alive:
            print(f'  Turno de {Ms0.Name}')
            print(f'{Ms0.Name} usa {Ms0.MsAtName}')
            Char = Dano(Ms0,Char)
            print('')
        if Ms1.Alive:
            print(f'  Turno de {Ms1.Name}')
            print(f'{Ms1.Name} usa {Ms1.MsAtName}')
            Char = Dano(Ms1,Char)
            print('')
        if Ms2.Alive:
            print(f'  Turno de {Ms2.Name}')
            print(f'{Ms2.Name} usa {Ms2.MsAtName}')
            Char = Dano(Ms2,Char)
            print('')
        if Char.Health <= 0:
            Char.Alive = False
            print(f'{Char.Name} ha muerto')
            break
    if Char.Health > 0:
        Char = Experience(Char)
    return Char
