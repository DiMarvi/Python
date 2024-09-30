from Class import *

# Players

def Player(Char):
    if Char == 'Diana':
        return Character(True,'Diana',0,0.1,0,50,0,0,1,['Pocion Vida Menor'],'Armadura de Cuero','Arco',)
    elif Char == 'Mark':
        return Character(True,'Mark',0,0.1,0,50,0,0,1,['Pocion Vida Menor'],'Armadura de maya','Espada Larga',)
    else:
        return Character(False,'',0,0,0,0,0,0,0,[],'','')

# Armors and Weapons

def Equip(Char):
    if 'Arco' == Char.Weapon.Name:
        Char.Weapon.Damage = 5
    elif 'Espada Larga' == Char.Weapon.Name:
        Char.Weapon.Damage = 8
    else:
        Char.Weapon.Damage = 1
    if 'Armadura de Cuero' == Char.Armor.Name:
        Char.Defence = 5
    elif 'Armadura de maya' == Char.Armor.Name:
        Char.Defence = 7
    else:
        Char.Defence = 0
    return Char

# Enemies

def Enemy(Enemy):
    if Enemy == 'Slime':
        return Monster(True,'Slime',         0, 10, 7, 0.01, 0, 'Baba', 2,'','')
    elif Enemy == 'Snake':
        return Monster(True,'Serpiente',     0, 6, 8, 0.1, 0, 'Picar', 1,'','')
    elif Enemy == 'Wolf':
        return Monster(True,'Lobo',          0, 15, 8, 0.02, 1, 'Morder', 4,'','')
    elif Enemy == 'Gigant wolf':
        return Monster(True,'Lobo Gigante',  0, 30, 10, 0.05, 2, 'Morder', 10,'','')
    elif Enemy == 'Diana':
        return Monster(True,'Diana (Lv5)',   0, 64, 9, 0.1, 5, 'Arco', 25,'','')
    else:
        return Monster(False,'NoName',       0, 0, 0, 0, 0, 'NoAttack', 0,'','')