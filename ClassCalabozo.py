class Character:
    __slots__ = ('Alive','Name','Attack','ProbCrit','Health','MaxHealth','Defence','Xp','Lv','Items','Armor','Weapon')
    def __init__(self,Alive,Name,Attack,ProbCrit,Health,MaxHealth,Defence,Xp,Lv,Items):
        self.Alive      = Alive
        self.Name       = Name
        self.Attack     = Attack
        self.ProbCrit   = ProbCrit
        self.Health     = Health
        self.MaxHealth  = MaxHealth
        self.Defence    = Defence
        self.Xp         = Xp
        self.Lv         = Lv
        self.Items      = Items
        self.Armor      = Equipment('',0,0)
        self.Weapon     = Equipment('',0,0)
    
class Monster:
    __slots__ = ('Alive','Name','Health','MaxHealth','Attack','ProbCrit','Defence','MsAtName','MsXp','Armor','Weapon')
    def __init__(self,Alive,Name,Health,MaxHealth,Attack,ProbCrit,Defence,MsAtName,MsXp,ArmorName,WeaponName):
        self.Alive      = Alive
        self.Name       = Name 
        self.Health     = Health
        self.MaxHealth  = MaxHealth
        self.Attack     = Attack
        self.ProbCrit   = ProbCrit
        self.Defence    = Defence
        self.MsAtName   = MsAtName
        self.MsXp       = MsXp
        self.Armor      = Equipment(ArmorName,0,0)
        self.Weapon     = Equipment(WeaponName,0,0)
class Equipment:
        __slots__ = ('Name','Damage','Armor')
        def __init__(self,Name,Damage,Armor):
            self.Name       = Name
            self.Damage     = Damage
            self.Armor      = Armor